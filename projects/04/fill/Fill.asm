// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// High-level code
// while(true):
//  if (key != 0):
//      blacken_screen
//  else:
//      whiten_screen:

// blacken_screen:
//  for (i=0; i!=8192; i++) {
//      draw 16 black pixels
//  }
//  goto beginning

// whiten_screen:
//  for (i=0; i!=8192; i++) {
//      draw 16 white pixels
//  }
//  goto beginning

// Medium-Level Code
// n = 8192
// (START)
// key = &Keyboard
// if key == 0:
//      goto white
// else
//      goto black

// (BLACK)
// color = -1
// goto LOOP_START
// (WHITE)
// color = 0
// (LOOP_START)
// addr = SCREEN
// i=0
// (LOOP)
//     if i == n GOTO START
//     RAM[addr] = color // all black
//     addr = addr+32
//     i = i + 1
//     goto LOOP
// goto START

// Low-level Code
// Initialize variables
@8192
D = A
@n
M = D

(START)
// Get current value from keyboard
@KBD
D = M
@WHITE // if key == 0, goto white
D; JEQ
@BLACK // else goto black
0; JMP

(BLACK)
@color
M = -1
@LOOP_START
0; JMP
(WHITE)
@color
M = 0

(LOOP_START)
// These must be reset every time we change the screen's color
@i // i = 0
M = 0
@SCREEN // addr = SCREEN
D = A
@addr
M = D
(LOOP)
    // if i == n GOTO START
    @i
    D = M
    @n
    D = D - M
    @START
    D; JEQ
    // RAM[addr] = color
    @color
    D = M
    @addr
    A = M
    M = D
    // addr = addr + 1
    @addr
    M = M+1
    // i = i + 1
    @i
    M = M + 1
    @LOOP
    0; JMP

// goto START
@START
0; JMP
