# Helpers for writing assembly code


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
