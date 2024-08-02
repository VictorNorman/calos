#!/bin/python3

from antlr4 import *
from CalCLexer import CalCLexer
from CalCParser import CalCParser
from CalCWalker import CalCWalker

from sys import argv

if len(argv) != 2:
    print(f"\n\tUse is {argv[0]} <source code path>\n")
    exit()

source = argv[1]
lexer = CalCLexer(FileStream(source))

stream = CommonTokenStream(lexer)
parser = CalCParser(stream)

# starting position for the tree
tree = parser.program()

walker = ParseTreeWalker()
walker.walk(calc := CalCWalker(source), tree)
calc.exit()
