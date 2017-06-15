# Multiply two numbers, found in locations 0 and 1, leaving the result in location 2.
# Assumes this code is loaded at location 20.
mov 0 2
mov *0 reg2
jez reg2 31
mov *1 reg1
jez reg1 31
mov reg2 reg0
sub 1 reg1
jez reg1 30
add reg0 reg2
jmp 26
mov reg2 2
end
