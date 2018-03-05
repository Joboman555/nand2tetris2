# Writes assembly code for control flow operations
from WritingHelpers import pop, at


def write_label(label):
    return ["({0})".format(label)]


def write_goto(label):
    return [at(label), "0; JMP"]


def write_if_goto(label):
    return pop() + ["D=M", at(label), "D; JNE"]
