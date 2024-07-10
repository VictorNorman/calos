# For generating lexer, parser, node listener
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.13.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool'

# To generate grammer
antlr4 -Dlanguage=Python3 CalC.g4