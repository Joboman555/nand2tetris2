// Multiply 2 numbers located at R0 and R1. Store in R2

// High level
// sum = 0
// i = 0
// x = RAM[R0]
// y = RAM[R1]
// for(i=0; i++ i<y) {
//    sum = sum + x
// }

// Medium Level
// sum = 0
// i = 0
// x = RAM[R0]
// y = RAM[R1]
// LOOP:
//  if i==y GOTO END
//  sum = sum + x
//  i = i + 1
// END
//  goto END

// Actual Program ----------------
// Initialization
@R2
M = 0
@i
M = 0
@R0
D = M
@x
M = D
@R1
D = M
@y
M = D

(LOOP)
    // if i==y GOTO END
    @i
    D = M
    @y
    D = D - M
    @END
    D; JEQ

    //sum = sum + x
    @x
    D = M
    @R2
    M = M+D
    // i = i + 1
    @i
    M = M+1

    @LOOP
    0; JMP

(END)
    @END
    0; JMP
