grammar CalC;

program : declaration* EOF;

declaration : (var_declaration | func_declaration) ;

var_declaration : symbol_type (ID | assignment) ';' ;

symbol_type : ID | PTR ;

lit : INT_LIT | FLOAT_LIT | CHAR_LIT | BOOL_LIT ;

func_declaration : symbol_type ID '(' parameter* ')' (func_definition | ';') ;

parameter : symbol_type ID ','? ;

func_definition : statement | block ;

block : '{' statement* '}' ;

statement
    : binary_op ';'
    | assignment ';'
    | var_declaration
    | if_statement
    | while_statement
    ;
    
binary_op
    : add_op
    ;

add_op
    : mult_op
    | add_op ADD_OP mult_op
    ;

mult_op
    : operand
    | mult_op MULT_OP binary_op
    ;

operand
    : lit
    | ID
    | func_call
    ;
    
assignment : ID '=' (binary_op | assignment) ;

if_statement : 'if' '(' binary_op ')' (statement | block) ;

while_statement : 'while' '(' binary_op ')' (statement | block) ;

func_call : ID '(' arg* ')' ;

arg : (lit | ID) ','? ;

KEYWORD : 'if' | 'while' ;

INT_LIT : [_0-9]+ ;
FLOAT_LIT : [_0-9]+ '.' [_0-9]+ ;
CHAR_LIT : '\'' [a-zA-Z] '\'' ;
BOOL_LIT : 'true' | 'false' ;

PTR : ID '*'+ ;

MULT_OP : '*' | '/' ;

ADD_OP : '+' | '-' ;

ID : [_a-zA-Z][_a-zA-Z0-9]* ;

WS : [ \t\r\n]+ -> skip;