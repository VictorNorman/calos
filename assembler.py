# assembler.py provdies an assembler (shocker) for the CalOS
# This adds functionality like labels and the ability to evaluate a symbol table
# CalOS supports stringified instructions in core memory,
# so not too much translation needs to be done

import regex as re
import os
from sys import argv

class Assembler:

    # singleton tracker
    instance = None

    # this defines keyword directives as starting with double underscore
    label_pattern = re.compile(r"\s*([^__]\w+):\s*")
    comment_pattern = re.compile(r"(\s*#.*)", re.DOTALL)

    # relates labels to their actual memory locations
    symbol_table = dict()

    def __new__(cls):
        if cls.instance == None:
            cls.instance = super(Assembler, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def assemble(source: str):
        Assembler.__precompile(source)
        Assembler.__compile(source)

    @staticmethod
    def __precompile(source: str):
        '''Builds the symbol table'''
        
        try:
            with open(source, "r") as input:
                line_num = 0
                for line in input.readlines():

                    # if line is just whitespace, skip it
                    if not line.strip(): continue

                    # if line is a keyword directive, skip it
                    elif line.startswith("__"): continue

                    # if line is a comment, skip it
                    elif Assembler.comment_pattern.match(line): continue

                    # see if the line is a label
                    elif match := Assembler.label_pattern.match(line):

                        # remember the label
                        symbol = match.group(1)
                        Assembler.symbol_table[symbol] = line_num

                        # if nothing past label, skip it
                        rest = line.split(":")[1].strip()
                        if not rest: continue

                    line_num += 1 

        except Exception as e:
            print(e)
            exit()

    @staticmethod
    def __compile(source: str):
        '''Builds the program using the built symbol table'''

        with open(source, "r") as input, open(source.removesuffix(".asm"), "w") as output:
            try:
                line_num = 0
                for line in input.readlines():

                    # strip comments if they are present in line
                    if match := Assembler.comment_pattern.search(line):
                        line = line.removesuffix(match.group(1))
                        
                        # if there is nothing left (line was only a comment) throw it away
                        if not match: continue

                    translated_line = Assembler.__line_translate(line)
                    if translated_line:
                        output.write(translated_line.strip() + "\n")

                    line_num += 1 # move to next line

            except Exception as e:
                print(e, "at", line_num)
                os.remove(source.removesuffix(".asm"))
                exit()

    @staticmethod
    def __line_translate(line: str):
        '''Returns the program-ready translation of a line'''
        
        # check if line is just whitespace, if so throw away
        if not line.strip():
            return ""
        
        # check if label, if so throw away the label part
        elif Assembler.label_pattern.match(line):
            line = Assembler.label_pattern.sub("", line)

            # if just whitespace left, leave
            if not line:
                return ""
            
        # if regular instruction, translate any known symbols
        return Assembler.__symbol_translate(line)


    # TODO: parse out all possible symbols to check those that are not valid
    @staticmethod
    def __symbol_translate(content: str):
        '''Translates the symbols present in content'''

        for symbol, value in Assembler.symbol_table.items():
            content = content.replace(symbol, str(value))
        
        return content

if __name__ == "__main__":
    if len(argv) != 2:
        print("\n\tUse is python3 assembler.py <name of file to assemble>\n")
    else:
        Assembler.assemble(argv[1])