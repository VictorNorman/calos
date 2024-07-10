# Generated from CalC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalCParser import CalCParser
else:
    from CalCParser import CalCParser

# This class defines a complete listener for a parse tree produced by CalCParser.
class CalCListener(ParseTreeListener):

    # Enter a parse tree produced by CalCParser#program.
    def enterProgram(self, ctx:CalCParser.ProgramContext):
        pass

    # Exit a parse tree produced by CalCParser#program.
    def exitProgram(self, ctx:CalCParser.ProgramContext):
        pass


    # Enter a parse tree produced by CalCParser#declaration.
    def enterDeclaration(self, ctx:CalCParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CalCParser#declaration.
    def exitDeclaration(self, ctx:CalCParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CalCParser#var_declaration.
    def enterVar_declaration(self, ctx:CalCParser.Var_declarationContext):
        pass

    # Exit a parse tree produced by CalCParser#var_declaration.
    def exitVar_declaration(self, ctx:CalCParser.Var_declarationContext):
        pass


    # Enter a parse tree produced by CalCParser#symbol_type.
    def enterSymbol_type(self, ctx:CalCParser.Symbol_typeContext):
        pass

    # Exit a parse tree produced by CalCParser#symbol_type.
    def exitSymbol_type(self, ctx:CalCParser.Symbol_typeContext):
        pass


    # Enter a parse tree produced by CalCParser#var_definition.
    def enterVar_definition(self, ctx:CalCParser.Var_definitionContext):
        pass

    # Exit a parse tree produced by CalCParser#var_definition.
    def exitVar_definition(self, ctx:CalCParser.Var_definitionContext):
        pass


    # Enter a parse tree produced by CalCParser#lit.
    def enterLit(self, ctx:CalCParser.LitContext):
        pass

    # Exit a parse tree produced by CalCParser#lit.
    def exitLit(self, ctx:CalCParser.LitContext):
        pass


    # Enter a parse tree produced by CalCParser#func_declaration.
    def enterFunc_declaration(self, ctx:CalCParser.Func_declarationContext):
        pass

    # Exit a parse tree produced by CalCParser#func_declaration.
    def exitFunc_declaration(self, ctx:CalCParser.Func_declarationContext):
        pass


    # Enter a parse tree produced by CalCParser#parameter.
    def enterParameter(self, ctx:CalCParser.ParameterContext):
        pass

    # Exit a parse tree produced by CalCParser#parameter.
    def exitParameter(self, ctx:CalCParser.ParameterContext):
        pass


    # Enter a parse tree produced by CalCParser#func_definition.
    def enterFunc_definition(self, ctx:CalCParser.Func_definitionContext):
        pass

    # Exit a parse tree produced by CalCParser#func_definition.
    def exitFunc_definition(self, ctx:CalCParser.Func_definitionContext):
        pass


    # Enter a parse tree produced by CalCParser#block.
    def enterBlock(self, ctx:CalCParser.BlockContext):
        pass

    # Exit a parse tree produced by CalCParser#block.
    def exitBlock(self, ctx:CalCParser.BlockContext):
        pass


    # Enter a parse tree produced by CalCParser#statement.
    def enterStatement(self, ctx:CalCParser.StatementContext):
        pass

    # Exit a parse tree produced by CalCParser#statement.
    def exitStatement(self, ctx:CalCParser.StatementContext):
        pass


    # Enter a parse tree produced by CalCParser#expression.
    def enterExpression(self, ctx:CalCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CalCParser#expression.
    def exitExpression(self, ctx:CalCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CalCParser#assignment.
    def enterAssignment(self, ctx:CalCParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CalCParser#assignment.
    def exitAssignment(self, ctx:CalCParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CalCParser#if_statement.
    def enterIf_statement(self, ctx:CalCParser.If_statementContext):
        pass

    # Exit a parse tree produced by CalCParser#if_statement.
    def exitIf_statement(self, ctx:CalCParser.If_statementContext):
        pass


    # Enter a parse tree produced by CalCParser#while_statement.
    def enterWhile_statement(self, ctx:CalCParser.While_statementContext):
        pass

    # Exit a parse tree produced by CalCParser#while_statement.
    def exitWhile_statement(self, ctx:CalCParser.While_statementContext):
        pass


    # Enter a parse tree produced by CalCParser#func_call.
    def enterFunc_call(self, ctx:CalCParser.Func_callContext):
        pass

    # Exit a parse tree produced by CalCParser#func_call.
    def exitFunc_call(self, ctx:CalCParser.Func_callContext):
        pass


    # Enter a parse tree produced by CalCParser#arg.
    def enterArg(self, ctx:CalCParser.ArgContext):
        pass

    # Exit a parse tree produced by CalCParser#arg.
    def exitArg(self, ctx:CalCParser.ArgContext):
        pass



del CalCParser