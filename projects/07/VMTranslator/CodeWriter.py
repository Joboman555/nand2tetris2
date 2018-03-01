# Writes assembly code given a list of parsed commands
from os.path import splitext, basename
from StackArithmeticWriter import (write_add, write_sub, write_and, write_or,
                                   write_neg, write_not, write_eq, write_gt,
                                   write_lt)
from VirtualMemoryWriter import write_push, write_pop


def writeline(file, line):
    """Writes a new line to a file"""
    file.write(line + '\n')


def write_code(fname, parsed_commands):
    output_fname = splitext(fname)[0] + '.asm'
    # title of file will be used for labels
    ftitle = splitext(basename(fname))[0]
    print "Writing assembly code to {0} ...".format(output_fname)
    with open(output_fname, 'w') as f:
        for command in parsed_commands:
            # Display the original line as a comment
            writeline(f, "// " + command.original_line)
            output = []
            # ---- Stack Arithmetic Commands ----
            if command.command_type == 'C_ADD':
                output = write_add()
            elif command.command_type == 'C_SUB':
                output = write_sub()
            elif command.command_type == 'C_AND':
                output = write_and()
            elif command.command_type == 'C_OR':
                output = write_or()
            elif command.command_type == 'C_NEG':
                output = write_neg()
            elif command.command_type == 'C_NOT':
                output = write_not()
            elif command.command_type == 'C_EQ':
                output = write_eq()
            elif command.command_type == 'C_GT':
                output = write_gt()
            elif command.command_type == 'C_LT':
                output = write_lt()
            # ---- Virtual Memory Commands ----
            elif command.command_type == 'C_PUSH':
                output = write_push(command.arg1, command.arg2, ftitle=ftitle)
            elif command.command_type == 'C_POP':
                output = write_pop(command.arg1, command.arg2, ftitle=ftitle)
            else:
                raise Exception('Invalid Command Type: ' + command.command_type)
            for line in output:
                writeline(f, line)
            writeline(f, '')
