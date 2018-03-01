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
#     "pop": "C_PUSH",
#     "push": "C_PUSH"
# }


def write_code(fname, parsed_commands):
    output_fname = splitext(fname)[0] + '.asm'
    print "Writing assembly code to {0} ...".format(output_fname)
    with open(output_fname, 'w') as f:
        for command in parsed_commands:
            # Display the original line as a comment
            f.write("// " + command.original_line + '\n')
            if command.command_type == 'C_ADD':
                for l in write_add():
                    f.write(l + '\n')
                f.write('\n')
            elif command.command_type == 'C_SUB':
                for l in write_sub():
                    f.write(l + '\n')
                f.write('\n')
            elif command.command_type == 'C_NEG':
                for l in write_neg():
                    f.write(l + '\n')
                f.write('\n')
            # elif command.command_type == 'C_NEG':
            #     for l in write_eq():
            #         f.write(l + '\n')
            #     f.write('\n')


def write_add():
    """Pop 2 items off the stack, add them, push the result back on"""
    return pop() + ['D=M'] + pop() + ['D=D+M'] + push()


def write_sub():
    """Pop 2 items off the stack, subtract them, push the result back on"""
    return pop() + ['D=M'] + pop() + ['D=D-M'] + push()


def write_neg():
    """Pop 1 item off the stack, negate it, push the result back on"""
    return pop() + ['D=-M'] + push()


# def write_eq():
#     """Pop 2 items off the stack, subtract them, push the result back on"""
#     # pop an item off the stack
#     # D = M
#     # pop another item off the stack
#     # D = D - M
#     # @TRUE_0
#     # 0: JEQ
#     # (TRUE_0)
#     #   D = 1
#     #   @END_0
#     #   0: JMP
#     # (FALSE_0)
#     #   D = 0
#     # (END_0)
#     #   push()
#     return pop() + ['D=M'] + pop() + ['D=D-M', '@0', '0:JEQ', '@1', 'D=A'] + push()


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
