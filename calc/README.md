# WIP: CalC (CalOS C Compiler)

## Dev Help

### To generate grammer

CalC uses the Antlr4 lexer and parser generator, so it must be installed to make any changes to the language. With Antlr4 (and respective dependencies) installed, the parser and lexer can be generated with the following two commands, assuing the grammer lives in the file `CalC.g4`.

```bash
$ alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.13.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool'

$ antlr4 -Dlanguage=Python3 CalC.g4
```
