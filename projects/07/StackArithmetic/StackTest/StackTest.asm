// push constant 17
// push constant 17
// eq
// push constant 17
// push constant 16
// eq
// push constant 16
// push constant 17
// eq
// push constant 892
// push constant 891
// lt
// push constant 891
// push constant 892
// lt
// push constant 891
// push constant 891
// lt
// push constant 32767
// push constant 32766
// gt
// push constant 32766
// push constant 32767
// gt
// push constant 32766
// push constant 32766
// gt
// push constant 57
// push constant 31
// push constant 53
// add
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D+M
@SP
A=M
M=D
@SP
M=M+1

// push constant 112
// sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D-M
@SP
A=M
M=D
@SP
M=M+1

// neg
@SP
M=M-1
A=M
D=-M
@SP
A=M
M=D
@SP
M=M+1

// and
// push constant 82
// or
// not
