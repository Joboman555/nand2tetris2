# Writes assembly code given a list of parsed commands
from os.path import splitext
from StackArithmeticWriter import (write_add, write_sub, write_and, write_or,
                                   write_neg, write_not, write_eq, write_gt,
                                   write_lt)
from WritingHelpers import push

# command_types = {
#     "add": "C_ADD",
#     "sub": "C_SUB",
#     "neg": "C_NEG",
#     "eq": "C_EQ",
#     "gt": "C_GT",
#     "lt": "C_LT",
#     "and": "C_AND",
#     "or": "C_OR",
#     "not": "C_NOT",
#     "pop": "C_POP",
#     "push": "C_PUSH"
# }


def writeline(file, line):
    """Writes a new line to a file"""
    file.write(line + '\n')


def write_code(fname, parsed_commands):
    output_fname = splitext(fname)[0] + '.asm'
    print "Writing assembly code to {0} ...".format(output_fname)
    with open(output_fname, 'w') as f:
        for command in parsed_commands:
            # Display the original line as a comment
            writeline(f, "// " + command.original_line)
            # ---- Stack Arithmetic Commands ----
            if command.command_type == 'C_ADD':
                for l in write_add():
                    writeline(f, l)
                writeline(f, '')
            elif command.command_type == 'C_SUB':
                for l in write_sub():
                    writeline(f, l)
                writeline(f, '')
            elif command.command_type == 'C_AND':
                for l in write_and():
                    writeline(f, l)
                writeline(f, '')
            elif command.command_type == 'C_OR':
                for l in write_or():
                    writeline(f, l)
                writeline(f, '')
            elif command.command_type == 'C_NEG':
                for l in write_neg():
                    writeline(f, l)
                writeline(f, '')
            elif command.command_type == 'C_NOT':
                for l in write_not():
                    writeline(f, l)
                writeline(f, '')
            elif command.command_type == 'C_EQ':
                for l in write_eq():
                    writeline(f, l)
                writeline(f, '')
            elif command.command_type == 'C_GT':
                for l in write_gt():
                    writeline(f, l)
                writeline(f, '')
            elif command.command_type == 'C_LT':
                for l in write_lt():
                    writeline(f, l)
                writeline(f, '')
            # ---- Virtual Memory Commands ----
            elif command.command_type == 'C_PUSH':
                for l in write_push(command.arg1, command.arg2):
                    writeline(f, l)
                writeline(f, '')
            else:
                raise Exception('Invalid Command Type: ' + command_type)

# ---- Virtual Memory Helpers ----


def write_push(segment, i):
    """Push value i from a segment onto the stack"""
    if segment == "constant":
        return ["@{0}".format(i), "D=A"] + push()
    raise Exception("{0} segment type not implemented yet".format(segment))

# ---- Helpers ----
