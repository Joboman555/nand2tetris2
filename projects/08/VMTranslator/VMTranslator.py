# Converts a VM bytecode file into Hack assembly
# Input: File.vm or Directory
# Output: File.asm

from Parser import parse
from os.path import splitext
from CodeWriter import write_code
import sys


def write_header(output_fname):
    """Writes the header required at the beginnign of each assembly file."""
    print "Creating assembly file: {0}".format(output_fname)
    with open(output_fname, 'w') as f:
        # f.write('// Initialize System\n')
        # f.write('SP=256\n')
        # f.write('call Sys.init\n')
        # f.write('\n')
        pass

path = sys.argv[1]
if len(sys.argv) == 2:
    output_fname = splitext(path)[0] + '.asm'
    write_header(output_fname)
    parsed_commands = parse(path)
    write_code(path, parsed_commands)
elif len(sys.argv) == 1:
    print "Please specify a .vm file or directory to translate."
else:
    print "Too many arguments provited"
