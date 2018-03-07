# Writes assembly code for control flow operations
from WritingHelpers import pop, at


def write_label(label, func):
    return ["({0}.{1})".format(func, label)]


def write_goto(label, func):
    return [at(func+'.'+label), "0; JMP"]


def write_if_goto(label, func):
    return pop() + ["D=M", at(func+'.'+label), "D; JNE"]
