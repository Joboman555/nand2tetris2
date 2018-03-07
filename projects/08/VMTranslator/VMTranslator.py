# Converts a VM bytecode file into Hack assembly
# Input: File.vm or Directory
# Output: File.asm

from Parser import parse
from os.path import splitext, isdir
from os import listdir
from CodeWriter import write_code
import sys


def write_header(outfile):
    """Writes the header required at the beginnign of each assembly file."""
    print "Creating assembly file: {0}".format(outfile)
    with open(outfile, 'w') as f:
        # f.write('SP=256\n')
        # f.write('call Sys.init\n')
        # f.write('\n')
        pass

if len(sys.argv) == 2:
    path = sys.argv[1]
    if isdir(path):
        # calculate the output filename
        if path[-1] != '/':
            path += '/'
        # last item will be the '/'
        # second to last will  be the dirname
        dirname = path.split('/')[-2]
        outfile = path + dirname + '.asm'
        write_header(outfile)
        for fname in listdir(path):
            if fname.endswith('.vm'):
                parsed_commands = parse(path+fname)
                write_code(path+fname, parsed_commands, outfile)
elif len(sys.argv) == 1:
    print "Please specify a .vm file or directory to translate."
else:
    print "Too many arguments provited"
