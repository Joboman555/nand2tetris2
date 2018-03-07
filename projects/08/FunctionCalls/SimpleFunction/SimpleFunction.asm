// function SimpleFunction.test 2
(SimpleFunction.test)
D=0
@SP
A=M
M=D
@SP
M=M+1
D=0
@SP
A=M
M=D
@SP
M=M+1

// push local 0
@LCL
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 1
@LCL
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M+D
@SP
A=M
M=D
@SP
M=M+1

// not
@SP
M=M-1
A=M
D=!M
@SP
A=M
M=D
@SP
M=M+1

// push argument 0
@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M+D
@SP
A=M
M=D
@SP
M=M+1

// push argument 1
@ARG
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SP
A=M
M=D
@SP
M=M+1

// return
@LCL
D=M
@endFrame
M=D
// retAddr = *(endFrame - 5)
@endFrame
D=M
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
// push
@SP
A=M
M=D
@SP
M=M+1
// write_sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SP
A=M
M=D
@SP
M=M+1
// pop
@SP
M=M-1
A=M
A=M
D=M
@retAddr
M=D
// *ARG = pop()
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
// SP = ARG+1
@ARG
D=M+1
@SP
M=D
// THAT = *(endFrame - 1)
@endFrame
D=M
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
// push
@SP
A=M
M=D
@SP
M=M+1
// write_sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SP
A=M
M=D
@SP
M=M+1
// pop
@SP
M=M-1
A=M
A=M
D=M
@THAT
M=D
// THIS = *(endFrame - 2)
@endFrame
D=M
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
// push
@SP
A=M
M=D
@SP
M=M+1
// write_sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SP
A=M
M=D
@SP
M=M+1
// pop
@SP
M=M-1
A=M
A=M
D=M
@THIS
M=D
// ARG = *(endFrame - 3)
@endFrame
D=M
@SP
A=M
M=D
@SP
M=M+1
@3
D=A
// push
@SP
A=M
M=D
@SP
M=M+1
// write_sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SP
A=M
M=D
@SP
M=M+1
// pop
@SP
M=M-1
A=M
A=M
D=M
@ARG
M=D
// LCL = *(endFrame - 4)
@endFrame
D=M
@SP
A=M
M=D
@SP
M=M+1
@4
D=A
// push
@SP
A=M
M=D
@SP
M=M+1
// write_sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SP
A=M
M=D
@SP
M=M+1
// pop
@SP
M=M-1
A=M
A=M
D=M
@LCL
M=D
@retAddr
A=D
0; JMP

