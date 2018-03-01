# Writes assembly code given a list of parsed commands
from os.path import splitext

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
            elif command.command_type == 'C_NEG':
                for l in write_neg():
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

# ---- Stack Arithmetic Helpers ----


def write_add():
    """Pop 2 items off the stack, add them, push the result back on"""
    return pop() + ['D=M'] + pop() + ['D=D+M'] + push()


def write_sub():
    """Pop 2 items off the stack, subtract them, push the result back on"""
    return pop() + ['D=M'] + pop() + ['D=D-M'] + push()


def write_neg():
    """Pop 1 item off the stack, negate it, push the result back on"""
    return pop() + ['D=-M'] + push()


def write_eq():
    """Pop 2 items off the stack, push value of (topval==bottomval) back on"""
    return write_cmp('EQ')


def write_gt():
    """Pop 2 items off the stack, push value of (topval>bottomval) back on"""
    return write_cmp('GT')


def write_lt():
    """Pop 2 items off the stack, push value of (topval<bottomval) back on"""
    return write_cmp('LT')


def write_cmp(jump_type):
    """Pop 2 items off the stack, compare them, push the result back on"""
    # pop an item off the stack
    # D = M
    # pop another item off the stack
    # D = D - M
    # @TRUE_0
    # D; JEQ
    # (FALSE_0)
    #   D = 0
    #   @END_0
    #   0; jump_type
    # (TRUE_0)
    #   D = 1
    # (END_0)
    #   push()
    if jump_type not in ['EQ', 'GT', 'LT', 'GE', 'LE', 'NE']:
        raise Exception("Unexpected Jump Type: {0}")
    true_label = unique("TRUE")
    false_label = unique("FALSE")
    end_label = unique("END")
    return (pop() +
            ['D=M'] +
            pop() +
            ['D=D-M',
             at(true_label),
             'D;J{0}'.format(jump_type),
             '({0})'.format(false_label),
             'D=0',
             at(end_label),
             '0;JMP',
             '({0})'.format(true_label),
             'D=1',
             '({0})'.format(end_label)] +
            push())

# ---- Virtual Memory Helpers ----


def write_push(segment, i):
    """Push value i from a segment onto the stack"""
    if segment == "constant":
        return ["@{0}".format(i), "D=A"] + push()
    raise Exception("{0} segment type not implemented yet".format(segment))

# ---- Helpers ----


def pop():
    """Pop an item off the stack and leaves value in M"""
    return [
        '@SP',
        'M=M-1',
        'A=M',
    ]


def push():
    """Push a value stored at D onto the stack"""
    return [
        '@SP',
        'A=M',
        'M=D',
        '@SP',
        'M=M+1'
    ]

occurances = {}
def unique(label):
    """creates a unique label from a non-unique label"""
    if label not in occurances:
        occurances[label] = 0
    else:
        occurances[label] = occurances[label] + 1
    return "{0}_{1}".format(label, occurances[label])


def at(label):
    """appends an @ to a label"""
    return "@{0}".format(label)
