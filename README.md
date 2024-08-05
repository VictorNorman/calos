# CalOS

## Architecture Description

There are 3 general purpose registers:

* `reg0`
* `reg1`
* `reg2`

A program counter register `pc`

## Core Memory

There are 1024 words of RAM, from addresses 0 to 1023.  The number of bits/bytes in a word is not defined. This attribute means that:

* Any positive or negative number fits in a word.
* Every instruction, including arguments, fits in a word.
* A string of up to 4 characters fits in a word: this is
  indicated by surrounding the string with single quotes.

## Assembly Language Instructions

* `mov <src> <dst>`   move value from `<src>` to `<dst>`
* `add <val> <dst>`   add value to `<dst>`
* `sub <val> <dst>`   subtract value from `<dst>`

Where `<src>` and `<dst>` can be a register name, a `<value>`, or `*<value>`. `<val>` can be a literal value or a register name.

`*<src>` means the contents of RAM at the address `<src>`.
`*<reg>` means the contents of RAM at the location referenced by `<reg>`.

You cannot move values from one RAM location to another.
A value can be given in decimal or hexidecimal.

More instructions:

* `jmp <dst>` means change pc to `<dst>`.
* `jez <reg> <dst>` means change pc to `<dst>` if register `<reg>` is 0.
* `jnz <reg> <dst>` means change pc to `<dst>` if register `<reg>` is not 0.
* `jgz <reg> <dst>` "    " greater than 0.
* `jlz <reg> <dst>` "    " less than 0.
* `end` means end the program

### Sample Program

#### Multiply Values in Addresses 0 and 1, Leaving Result in Location 2

```assembly
mov 0 4          /* put 0 into the destination in case val1 or val2 are 0. */
mov *0 reg2      /* move 1st value to reg2 */
jez reg2 31      /* we are done if val1 is 0 */
mov *1 reg1      /* move 2nd value to reg1 */
jez reg1 31      /* we are done if val2 is 0 */
mov reg2 reg0    /* copy reg2 to reg0 */
sub 1 reg1       /* loop: subtract 1 from val2 */
jez reg1 30      /* if == 0, we are done looping */
add reg0 reg2    /* add reg0 to reg2  where we accumulate result */
jmp 26           /* repeat the loop */
mov reg2 2      /* store result in location 2 */
end
```

> ⓘ Note that CalOS *does* use virutal addressing. The true memory locations used above will be dependent on the address space of the program.
