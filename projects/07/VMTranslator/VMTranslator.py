# Converts a VM bytecode file into Hack assembly
# Input: File.vm
# Output: File.asm

from Parser import parse
from CodeWriter import write_code
import sys

for fname in sys.argv[1:]:
    parsed_commands = parse(fname)
    write_code(fname, parsed_commands)
if len(sys.argv) == 1:
    print "Please specify a .vm file to translate."
