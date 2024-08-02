from CalCListener import CalCListener
from CalCParser import CalCParser
from Stack import Stack
from Symbol import Symbol
from CalCUtils import *

class CalCWalker(CalCListener):

    scope = Stack()
    scope.push(SymbolTable()) # the global symbol table

    entry_point_seen: bool = False # keep track of if an entry point (main()) has been seen

    def __init__(self, source: str) -> None:
        super().__init__()
        self.out = open(source.removesuffix(".c") + ".asm", "w")
        self.out.write("__main: start\n")

    def exit(self):
        if not self.entry_point_seen:
            raise SymbolError("No entry point found. Please include int main() somewhere in your program's global scope.")

        # take care of all global definitions at this point
        data_definitions = ""
        data_byte_count = 0
        for name, symbol in self.scope.top.items():
            if not symbol.is_function:
                data_definitions += f"{name}: db {symbol.value}\n"
                data_byte_count += 1

        self.out.write(f"__data: {data_byte_count}\n")
        self.out.write(data_definitions)

        # close assembly file
        self.out.close()

    def enterFunc_declaration(self, ctx: CalCParser.Func_declarationContext):
        name = ctx.ID().getText()
        type = ctx.symbol_type().getText()
        params = ctx.parameter() # list of parameters

        # add to the sym table of which this function is a part
        self.scope.top[name] = Symbol(
            name, Symbol.string2type(type),
            function = True, params = [] # TODO: fix the params (processParams)
        )

        # if the function is main and has a following definition
        # mark it as the entry point
        if ctx.func_definition() and name == "main":
            self.entry_point_seen = True
            
        self.scope.push(SymbolTable()) # start table for this function

    def exitFunc_declaration(self, ctx: CalCParser.Func_declarationContext):
        pass

    def enterFunc_definition(self, ctx: CalCParser.Func_definitionContext):
        
        # figure out what kind of a definition
        if ctx.statement():
            self.process_statement(ctx.statement())
        elif ctx.block():
            for statement in ctx.block().statement():
                self.process_statement(statement)

    def exitFunc_definition(self, ctx: CalCParser.Func_definitionContext):
        # go up to the previous scope
        self.pop_scope()

    # utility functions, not bound to any parse tree node

    current_base_offset = 0
    def next_base_offset(self) -> int:
        self.current_base_offset += 1
        return self.current_base_offset
    
    def pop_scope(self) -> None:
        symbol_table = self.scope.pop()
        for symbol in symbol_table.values():
            if not symbol.is_function:
                self.current_base_offset -= 1        

    def get_symbol(self, symbol_name: str) -> Symbol:
        try:
            symbol: Symbol = self.scope.top[symbol_name]
        except:
            raise SymbolError(f'Symbol "{symbol_name}" not found')
        
        return symbol
    
    def process_statement(self, statement: CalCParser.StatementContext):
        if statement.binary_op():
            pass # don't care about random binary operation

        elif assignment_statement := statement.assignment():
            self.process_assignment(assignment_statement)

        elif declaration := statement.var_declaration():
            id = self.process_var_declaration(declaration)
            if declaration.assignment():
                value = self.process_assignment(declaration.assignment())
                self.assign_sym_value(id, value)

        elif statement.if_statement():
            print("ifst")

        elif statement.while_statement():
            print("wlst")

    def process_assignment(self, assignment_statement: CalCParser.AssignmentContext):
        if inner_assignment := assignment_statement.assignment():
            value = self.process_assignment(inner_assignment)
        else:
            # binary operation on right of =
            value = CalCOperations.process_binary_operation(
                assignment_statement.binary_op()
            )

        self.assign_sym_value(assignment_statement.ID().getText(), value)

        return value
    
    def assign_sym_value(self, sym_name: str, value):
        # if the variable is in scope
        # assign it the value
        if sym := self.scope.top.get(sym_name):
            sym.value = value
        else:
            raise SymbolError(f"Symbol {sym_name} not recognized")
    
    def process_var_declaration(self, declaration: CalCParser.Var_declarationContext):
        # get the id to know which symbol is being declared
        if declaration.assignment():
            id = declaration.assignment().ID().getText()
        else:
            id = declaration.ID().getText()
        
        # create the symbol as assign it to the symbol table
        sym = Symbol(
            id, Symbol.string2type(declaration.symbol_type().getText())
        )
        sym.base_offset = self.next_base_offset()
        self.scope.top[id] = sym

        return id