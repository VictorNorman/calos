from CalCListener import CalCListener
from CalCParser import CalCParser
from enum import Enum
from Stack import Stack

class SymbolType(Enum):
    function = 0
    int = 1
    float = 2
    bool = 3
    char = 4
    defined = 5

    def __str__(self):
        return self.name

def string2type(s):
    match(s):
        case("int"):
            return SymbolType.int
        case("float"):
            return SymbolType.float
        case("bool"):
            return SymbolType.bool
        case("char"):
            return SymbolType.char
        case _:
            return SymbolType.defined
    

class SymbolTableEntry():

    def __init__(self, type, sig = None):
        self.type = type
        self.sig = sig
    
    def __str__(self):
        return f"Type: {self.type}--{self.sig}"
    


class CalCWalker(CalCListener):

    # keep track of symbols and their surrounding information
    # structure
    # {name: {type:<symbol type>, (if function)sig: [<return type>, <p-1>...<p-n>]}}
    symbol_table = dict[SymbolTableEntry]()

    scope = Stack()

    def __init__(self, source: str) -> None:
        super().__init__()
        self.out = open(source.removesuffix(".c") + ".asm", "w")
        self.out.write("__main: start\n")

    def exit(self):
        for k,v in self.symbol_table.items():
            print(k+'\n\t'+str(v))
        self.out.close()

    def enterFunc_declaration(self, ctx: CalCParser.Func_declarationContext):
        name = ctx.ID().getText()
        self.symbol_table[name] = SymbolTableEntry(
            SymbolType.function, [
                string2type(ctx.symbol_type().getText()),
                # TODO: parameter work
            ]
        )

        self.scope.push(name)
        print(self.scope)

    def exitFunc_declaration(self, ctx: CalCParser.Func_declarationContext):
        self.scope.pop()
        print(self.scope)
