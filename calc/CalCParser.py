# Generated from CalC.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,159,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        0,1,0,1,1,1,1,3,1,45,8,1,1,2,1,2,1,2,3,2,50,8,2,1,2,1,2,1,3,1,3,
        5,3,56,8,3,10,3,12,3,59,9,3,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,
        5,6,70,8,6,10,6,12,6,73,9,6,1,6,1,6,1,6,3,6,78,8,6,1,7,1,7,1,7,3,
        7,83,8,7,1,8,1,8,3,8,87,8,8,1,9,1,9,5,9,91,8,9,10,9,12,9,94,9,9,
        1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,104,8,10,1,11,1,11,1,
        11,1,11,1,11,1,11,3,11,112,8,11,1,11,1,11,1,11,5,11,117,8,11,10,
        11,12,11,120,9,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,
        13,3,13,132,8,13,1,14,1,14,1,14,1,14,1,14,1,14,3,14,140,8,14,1,15,
        1,15,1,15,5,15,145,8,15,10,15,12,15,148,9,15,1,15,1,15,1,16,1,16,
        3,16,154,8,16,1,16,3,16,157,8,16,1,16,0,1,22,17,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,0,1,1,0,12,15,163,0,37,1,0,0,0,2,44,
        1,0,0,0,4,46,1,0,0,0,6,53,1,0,0,0,8,60,1,0,0,0,10,63,1,0,0,0,12,
        65,1,0,0,0,14,79,1,0,0,0,16,86,1,0,0,0,18,88,1,0,0,0,20,103,1,0,
        0,0,22,111,1,0,0,0,24,121,1,0,0,0,26,125,1,0,0,0,28,133,1,0,0,0,
        30,141,1,0,0,0,32,153,1,0,0,0,34,36,3,2,1,0,35,34,1,0,0,0,36,39,
        1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,
        40,41,5,0,0,1,41,1,1,0,0,0,42,45,3,4,2,0,43,45,3,12,6,0,44,42,1,
        0,0,0,44,43,1,0,0,0,45,3,1,0,0,0,46,47,3,6,3,0,47,49,5,17,0,0,48,
        50,3,8,4,0,49,48,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,51,52,5,1,0,
        0,52,5,1,0,0,0,53,57,5,17,0,0,54,56,5,2,0,0,55,54,1,0,0,0,56,59,
        1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,7,1,0,0,0,59,57,1,0,0,0,60,
        61,5,3,0,0,61,62,3,22,11,0,62,9,1,0,0,0,63,64,7,0,0,0,64,11,1,0,
        0,0,65,66,3,6,3,0,66,67,5,17,0,0,67,71,5,4,0,0,68,70,3,14,7,0,69,
        68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,
        0,73,71,1,0,0,0,74,77,5,5,0,0,75,78,3,16,8,0,76,78,5,1,0,0,77,75,
        1,0,0,0,77,76,1,0,0,0,78,13,1,0,0,0,79,80,3,6,3,0,80,82,5,17,0,0,
        81,83,5,6,0,0,82,81,1,0,0,0,82,83,1,0,0,0,83,15,1,0,0,0,84,87,3,
        20,10,0,85,87,3,18,9,0,86,84,1,0,0,0,86,85,1,0,0,0,87,17,1,0,0,0,
        88,92,5,7,0,0,89,91,3,20,10,0,90,89,1,0,0,0,91,94,1,0,0,0,92,90,
        1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,92,1,0,0,0,95,96,5,8,0,0,
        96,19,1,0,0,0,97,98,3,22,11,0,98,99,5,1,0,0,99,104,1,0,0,0,100,104,
        3,2,1,0,101,104,3,26,13,0,102,104,3,28,14,0,103,97,1,0,0,0,103,100,
        1,0,0,0,103,101,1,0,0,0,103,102,1,0,0,0,104,21,1,0,0,0,105,106,6,
        11,-1,0,106,112,3,10,5,0,107,112,5,17,0,0,108,112,3,24,12,0,109,
        112,3,30,15,0,110,112,3,4,2,0,111,105,1,0,0,0,111,107,1,0,0,0,111,
        108,1,0,0,0,111,109,1,0,0,0,111,110,1,0,0,0,112,118,1,0,0,0,113,
        114,10,3,0,0,114,115,5,16,0,0,115,117,3,22,11,4,116,113,1,0,0,0,
        117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,23,1,0,0,0,120,
        118,1,0,0,0,121,122,5,17,0,0,122,123,5,3,0,0,123,124,3,22,11,0,124,
        25,1,0,0,0,125,126,5,9,0,0,126,127,5,4,0,0,127,128,3,22,11,0,128,
        131,5,5,0,0,129,132,3,20,10,0,130,132,3,18,9,0,131,129,1,0,0,0,131,
        130,1,0,0,0,132,27,1,0,0,0,133,134,5,10,0,0,134,135,5,4,0,0,135,
        136,3,22,11,0,136,139,5,5,0,0,137,140,3,20,10,0,138,140,3,18,9,0,
        139,137,1,0,0,0,139,138,1,0,0,0,140,29,1,0,0,0,141,142,5,17,0,0,
        142,146,5,4,0,0,143,145,3,32,16,0,144,143,1,0,0,0,145,148,1,0,0,
        0,146,144,1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,146,1,0,0,
        0,149,150,5,5,0,0,150,31,1,0,0,0,151,154,3,10,5,0,152,154,5,17,0,
        0,153,151,1,0,0,0,153,152,1,0,0,0,154,156,1,0,0,0,155,157,5,6,0,
        0,156,155,1,0,0,0,156,157,1,0,0,0,157,33,1,0,0,0,17,37,44,49,57,
        71,77,82,86,92,103,111,118,131,139,146,153,156
    ]

class CalCParser ( Parser ):

    grammarFileName = "CalC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'*'", "'='", "'('", "')'", "','", 
                     "'{'", "'}'", "'if'", "'while'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "KEYWORD", 
                      "INT_LIT", "FLOAT_LIT", "CHAR_LIT", "BOOL_LIT", "OP", 
                      "ID", "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_var_declaration = 2
    RULE_symbol_type = 3
    RULE_var_definition = 4
    RULE_lit = 5
    RULE_func_declaration = 6
    RULE_parameter = 7
    RULE_func_definition = 8
    RULE_block = 9
    RULE_statement = 10
    RULE_expression = 11
    RULE_assignment = 12
    RULE_if_statement = 13
    RULE_while_statement = 14
    RULE_func_call = 15
    RULE_arg = 16

    ruleNames =  [ "program", "declaration", "var_declaration", "symbol_type", 
                   "var_definition", "lit", "func_declaration", "parameter", 
                   "func_definition", "block", "statement", "expression", 
                   "assignment", "if_statement", "while_statement", "func_call", 
                   "arg" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    KEYWORD=11
    INT_LIT=12
    FLOAT_LIT=13
    CHAR_LIT=14
    BOOL_LIT=15
    OP=16
    ID=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CalCParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalCParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(CalCParser.DeclarationContext,i)


        def getRuleIndex(self):
            return CalCParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = CalCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 34
                self.declaration()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(CalCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declaration(self):
            return self.getTypedRuleContext(CalCParser.Var_declarationContext,0)


        def func_declaration(self):
            return self.getTypedRuleContext(CalCParser.Func_declarationContext,0)


        def getRuleIndex(self):
            return CalCParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = CalCParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 42
                self.var_declaration()
                pass

            elif la_ == 2:
                self.state = 43
                self.func_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symbol_type(self):
            return self.getTypedRuleContext(CalCParser.Symbol_typeContext,0)


        def ID(self):
            return self.getToken(CalCParser.ID, 0)

        def var_definition(self):
            return self.getTypedRuleContext(CalCParser.Var_definitionContext,0)


        def getRuleIndex(self):
            return CalCParser.RULE_var_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_declaration" ):
                listener.enterVar_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_declaration" ):
                listener.exitVar_declaration(self)




    def var_declaration(self):

        localctx = CalCParser.Var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.symbol_type()
            self.state = 47
            self.match(CalCParser.ID)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 48
                self.var_definition()


            self.state = 51
            self.match(CalCParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Symbol_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalCParser.ID, 0)

        def getRuleIndex(self):
            return CalCParser.RULE_symbol_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbol_type" ):
                listener.enterSymbol_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbol_type" ):
                listener.exitSymbol_type(self)




    def symbol_type(self):

        localctx = CalCParser.Symbol_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_symbol_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(CalCParser.ID)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 54
                self.match(CalCParser.T__1)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CalCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CalCParser.RULE_var_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_definition" ):
                listener.enterVar_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_definition" ):
                listener.exitVar_definition(self)




    def var_definition(self):

        localctx = CalCParser.Var_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(CalCParser.T__2)
            self.state = 61
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(CalCParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(CalCParser.FLOAT_LIT, 0)

        def CHAR_LIT(self):
            return self.getToken(CalCParser.CHAR_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(CalCParser.BOOL_LIT, 0)

        def getRuleIndex(self):
            return CalCParser.RULE_lit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLit" ):
                listener.enterLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLit" ):
                listener.exitLit(self)




    def lit(self):

        localctx = CalCParser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symbol_type(self):
            return self.getTypedRuleContext(CalCParser.Symbol_typeContext,0)


        def ID(self):
            return self.getToken(CalCParser.ID, 0)

        def func_definition(self):
            return self.getTypedRuleContext(CalCParser.Func_definitionContext,0)


        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalCParser.ParameterContext)
            else:
                return self.getTypedRuleContext(CalCParser.ParameterContext,i)


        def getRuleIndex(self):
            return CalCParser.RULE_func_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_declaration" ):
                listener.enterFunc_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_declaration" ):
                listener.exitFunc_declaration(self)




    def func_declaration(self):

        localctx = CalCParser.Func_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.symbol_type()
            self.state = 66
            self.match(CalCParser.ID)
            self.state = 67
            self.match(CalCParser.T__3)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 68
                self.parameter()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(CalCParser.T__4)
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 9, 10, 12, 13, 14, 15, 17]:
                self.state = 75
                self.func_definition()
                pass
            elif token in [1]:
                self.state = 76
                self.match(CalCParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symbol_type(self):
            return self.getTypedRuleContext(CalCParser.Symbol_typeContext,0)


        def ID(self):
            return self.getToken(CalCParser.ID, 0)

        def getRuleIndex(self):
            return CalCParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = CalCParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.symbol_type()
            self.state = 80
            self.match(CalCParser.ID)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 81
                self.match(CalCParser.T__5)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(CalCParser.StatementContext,0)


        def block(self):
            return self.getTypedRuleContext(CalCParser.BlockContext,0)


        def getRuleIndex(self):
            return CalCParser.RULE_func_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_definition" ):
                listener.enterFunc_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_definition" ):
                listener.exitFunc_definition(self)




    def func_definition(self):

        localctx = CalCParser.Func_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_definition)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 12, 13, 14, 15, 17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.statement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalCParser.StatementContext)
            else:
                return self.getTypedRuleContext(CalCParser.StatementContext,i)


        def getRuleIndex(self):
            return CalCParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = CalCParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(CalCParser.T__6)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 194048) != 0):
                self.state = 89
                self.statement()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self.match(CalCParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CalCParser.ExpressionContext,0)


        def declaration(self):
            return self.getTypedRuleContext(CalCParser.DeclarationContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(CalCParser.If_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(CalCParser.While_statementContext,0)


        def getRuleIndex(self):
            return CalCParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = CalCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_statement)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.expression(0)
                self.state = 98
                self.match(CalCParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                self.while_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lit(self):
            return self.getTypedRuleContext(CalCParser.LitContext,0)


        def ID(self):
            return self.getToken(CalCParser.ID, 0)

        def assignment(self):
            return self.getTypedRuleContext(CalCParser.AssignmentContext,0)


        def func_call(self):
            return self.getTypedRuleContext(CalCParser.Func_callContext,0)


        def var_declaration(self):
            return self.getTypedRuleContext(CalCParser.Var_declarationContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CalCParser.ExpressionContext,i)


        def OP(self):
            return self.getToken(CalCParser.OP, 0)

        def getRuleIndex(self):
            return CalCParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalCParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 106
                self.lit()
                pass

            elif la_ == 2:
                self.state = 107
                self.match(CalCParser.ID)
                pass

            elif la_ == 3:
                self.state = 108
                self.assignment()
                pass

            elif la_ == 4:
                self.state = 109
                self.func_call()
                pass

            elif la_ == 5:
                self.state = 110
                self.var_declaration()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CalCParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 113
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 114
                    self.match(CalCParser.OP)
                    self.state = 115
                    self.expression(4) 
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalCParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(CalCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CalCParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = CalCParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(CalCParser.ID)
            self.state = 122
            self.match(CalCParser.T__2)
            self.state = 123
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CalCParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(CalCParser.StatementContext,0)


        def block(self):
            return self.getTypedRuleContext(CalCParser.BlockContext,0)


        def getRuleIndex(self):
            return CalCParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = CalCParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(CalCParser.T__8)
            self.state = 126
            self.match(CalCParser.T__3)
            self.state = 127
            self.expression(0)
            self.state = 128
            self.match(CalCParser.T__4)
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 12, 13, 14, 15, 17]:
                self.state = 129
                self.statement()
                pass
            elif token in [7]:
                self.state = 130
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CalCParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(CalCParser.StatementContext,0)


        def block(self):
            return self.getTypedRuleContext(CalCParser.BlockContext,0)


        def getRuleIndex(self):
            return CalCParser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)




    def while_statement(self):

        localctx = CalCParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(CalCParser.T__9)
            self.state = 134
            self.match(CalCParser.T__3)
            self.state = 135
            self.expression(0)
            self.state = 136
            self.match(CalCParser.T__4)
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 12, 13, 14, 15, 17]:
                self.state = 137
                self.statement()
                pass
            elif token in [7]:
                self.state = 138
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalCParser.ID, 0)

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalCParser.ArgContext)
            else:
                return self.getTypedRuleContext(CalCParser.ArgContext,i)


        def getRuleIndex(self):
            return CalCParser.RULE_func_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)




    def func_call(self):

        localctx = CalCParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(CalCParser.ID)
            self.state = 142
            self.match(CalCParser.T__3)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 192512) != 0):
                self.state = 143
                self.arg()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
            self.match(CalCParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lit(self):
            return self.getTypedRuleContext(CalCParser.LitContext,0)


        def ID(self):
            return self.getToken(CalCParser.ID, 0)

        def getRuleIndex(self):
            return CalCParser.RULE_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg" ):
                listener.enterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg" ):
                listener.exitArg(self)




    def arg(self):

        localctx = CalCParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 13, 14, 15]:
                self.state = 151
                self.lit()
                pass
            elif token in [17]:
                self.state = 152
                self.match(CalCParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 155
                self.match(CalCParser.T__5)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




