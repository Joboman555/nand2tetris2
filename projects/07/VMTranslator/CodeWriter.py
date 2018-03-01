# Writes assembly code given a list of parsed commands
from os.path import splitext, basename
from StackArithmeticWriter import (write_add, write_sub, write_and, write_or,
                                   write_neg, write_not, write_eq, write_gt,
                                   write_lt)
from WritingHelpers import push, pop, at

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
    # title of file will be used for labels
    ftitle = splitext(basename(fname))[0]
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
                for l in write_push(command.arg1, command.arg2, ftitle=ftitle):
                    writeline(f, l)
                writeline(f, '')
            elif command.command_type == 'C_POP':
                for l in write_pop(command.arg1, command.arg2, ftitle=ftitle):
                    writeline(f, l)
                writeline(f, '')
            else:
                raise Exception('Invalid Command Type: ' + command.command_type)

# ---- Virtual Memory Helpers ----


def write_push(segment, i, ftitle=None):
    """Push value i from a segment onto the stack"""
    # local, argument, this, and that are implemented the same way
    standard_segs = {
        "local": "LCL",
        "argument": "ARG",
        "this": "THIS",
        "that": "THAT",
    }
    if segment in standard_segs:
        segname = standard_segs[segment]
        return ([at(segname),  # addr=segname+i
                 "D=M",
                 at(i),
                 "D=D+A",
                 "A=D",
                 "D=M"] +
                push())
    elif segment == "temp":
        return ([at(5),  # temp base address is 5
                 "D=A",
                 at(i),
                 "D=D+A",
                 "A=D",
                 "D=M"] +
                push())
    elif segment == "static":
        label = "{0}.{1}".format(ftitle, i)
        return [at(label), "D=M"] + push()
    elif segment == "pointer":
        if int(i) not in [0, 1]:
            raise Exception('Invalid i for push pointer: ' + str(i))
        target = "THAT" if int(i) else "THIS"
        return [at(target),  # *SP = THIS/THAT
                "D=M",
                "@SP",
                "A=M",
                "M=D",
                "@SP",  # SP++
                "M=M+1"]
    elif segment == "constant":
        return [at(i), "D=A"] + push()
    raise Exception("{0} segment type not implemented yet".format(segment))


def write_pop(segment, i, ftitle=None):
    """Pop a value from the stack and store it at position i in segment"""
    # local, argument, this, and that are implemented the same way
    standard_segs = {
        "local": "LCL",
        "argument": "ARG",
        "this": "THIS",
        "that": "THAT",
    }
    if segment in standard_segs:
        segname = standard_segs[segment]
        return ([at(segname),  # addr=segname+i
                 "D=M",
                 at(i),
                 "D=D+A",
                 at('addr'),
                 "M=D"] +
                pop() +
                ["D=M",
                 at('addr'),  # *addr=*SP
                 "A=M",
                 "M=D"])
    elif segment == "temp":
        return ([at(5),  # temp base address is 5
                 "D=A",
                 at(i),
                 "D=D+A",
                 at('addr'),
                 "M=D"] +
                pop() +
                ["D=M",
                 at('addr'),  # *addr=*SP
                 "A=M",
                 "M=D"])
    elif segment == "static":
        label = "{0}.{1}".format(ftitle, i)
        return pop() + ["D=M", at(label), "M=D"]
    elif segment == "pointer":
        if int(i) not in [0, 1]:
            raise Exception('Invalid i for pop pointer: ' + str(i))
        target = "THAT" if int(i) else "THIS"
        return ["@SP",  # SP--
                "M=M-1",
                "A=M",  # THIS/THAT = *SP
                "D=M",
                at(target),
                "M=D"]
    raise Exception("{0} segment type not implemented yet".format(segment))
