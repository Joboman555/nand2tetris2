# Writes assembly code for stack arithmetic operations
from WritingHelpers import push, pop, unique, at


def write_add():
    """Pop 2 items off the stack, add them, push the result back on"""
    return __write_bitwise('+')


def write_sub():
    """Pop 2 items off the stack, sub bot from top, push the result back on"""
    return __write_bitwise('-')


def write_and():
    """Pop 2 items off the stack, and them, push the result back on"""
    return __write_bitwise('&')


def write_or():
    """Pop 2 items off the stack, or them, push the result back on"""
    return __write_bitwise('|')


def write_neg():
    """Pop 1 item off the stack, negate it, push the result back on"""
    return pop() + ['D=-M'] + push()


def write_not():
    """Pop 1 item off the stack, negate it, push the result back on"""
    return pop() + ['D=!M'] + push()


def write_eq():
    """Pop 2 items off the stack, push value of (bottomval==topval) back on"""
    return __write_cmp('EQ')


def write_gt():
    """Pop 2 items off the stack, push value of (bottomval>topval) back on"""
    return __write_cmp('GT')


def write_lt():
    """Pop 2 items off the stack, push value of (bottomval<topval) back on"""
    return __write_cmp('LT')


# ---- Private helper methods ----


def __write_bitwise(op):
    """Pop 2 items off the stack, do a bitwise operation, push result back on
       this is only used for operations which do not need a jump"""
    if op not in ['|', '&', '+', '-']:
        raise Exception("Unexpected Bitwise Operation: {0}".format(op))
    return pop() + ['D=M'] + pop() + ['D=M{0}D'.format(op)] + push()


def __write_cmp(jump_type):
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
        raise Exception("Unexpected Jump Type: {0}".format(jump_type))
    true_label = unique("TRUE")
    false_label = unique("FALSE")
    end_label = unique("END")
    return (pop() +
            ['D=M'] +
            pop() +
            ['D=M-D',
             at(true_label),
             'D;J{0}'.format(jump_type),
             '({0})'.format(false_label),
             'D=0',
             at(end_label),
             '0;JMP',
             '({0})'.format(true_label),
             'D=-1',  # -1 == 11111...11 in 2's complement
             '({0})'.format(end_label)] +
            push())
