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
// endFrame-=1, THAT = *(endFrame)
@endFrame
M=M-1
A=M
D=M
@THAT
M=D
// endFrame-=1, THIS = *(endFrame)
@endFrame
M=M-1
A=M
D=M
@THIS
M=D
// endFrame-=1, ARG = *(endFrame)
@endFrame
M=M-1
A=M
D=M
@ARG
M=D
// endFrame-=1, LCL = *(endFrame)
@endFrame
M=M-1
A=M
D=M
@LCL
M=D
// endFrame-=1, goto endFrame
@endFrame
M=M-1
A=M
0; JMP

