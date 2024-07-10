grammar CalC;

program : declaration* EOF;

declaration : (var_declaration | func_declaration) ;

var_declaration : symbol_type ID var_definition? ';' ;

symbol_type : ID '*'* ;

var_definition : '=' expression ;

lit : INT_LIT | FLOAT_LIT | CHAR_LIT | BOOL_LIT ;

func_declaration : symbol_type ID '(' parameter* ')' (func_definition | ';') ;

parameter : symbol_type ID ','? ;

func_definition : statement | block ;

block : '{' statement* '}' ;

statement
    : expression ';'
    | declaration
    | if_statement
    | while_statement
    ;

expression
    : lit
    | ID
    | assignment
    | expression OP expression
    | func_call
    | var_declaration
    ;
    
assignment : ID '=' expression ;

if_statement : 'if' '(' expression ')' (statement | block) ;

while_statement : 'while' '(' expression ')' (statement | block) ;

func_call : ID '(' arg* ')' ;

arg : (lit | ID) ','? ;

KEYWORD : 'if' | 'while' ;

INT_LIT : [_0-9]+ ;
FLOAT_LIT : [_0-9]+ '.' [_0-9]+ ;
CHAR_LIT : '\'' [a-zA-Z] '\'' ;
BOOL_LIT : 'true' | 'false' ;

OP : '+' | '-' | '*' | '/' ;

ID : [_a-zA-Z][_a-zA-Z0-9]* ;

WS : [ \t\r\n]+ -> skip;