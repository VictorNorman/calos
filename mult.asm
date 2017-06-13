mov 0 4
mov *0 reg2
jez reg2 42
mov *2 reg1
jez reg1 42
mov reg2 reg0
sub 1 reg1
jez reg1 40
add reg0 reg2
jmp 32
mov reg2 4
end
