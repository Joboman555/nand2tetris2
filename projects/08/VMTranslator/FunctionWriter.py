# Writes assembly code for function calls
from WritingHelpers import push, pop, at
from StackArithmeticWriter import write_sub


def write_function(func_name, num_vars):
    output = ["({0})".format(func_name)]
    for i in range(int(num_vars)):
        output += ["D=0"] + push()
    return output


def write_return():
    # endFrame = LCL
    # retAddr = *(endFrame-5)
    # *ARG = pop(), sets return value to arg[0]
    # SP = ARG+1
    # THAT = *(endFrame-1)
    # THIS = *(endFrame-2, "THIS")
    # ARG = *(endFrame-3, "ARG")
    # LCL = *(endFrame-4. "LCL")
    # goto retAddr

    # ---- implementation ----
    # endFrame = LCL
    output = [at("LCL"), "D=M", at("endFrame"), "M=D"]
    output += __write_restore(5, "retAddr")
    # *ARG = pop()
    output += (["// *ARG = pop()"] +
               pop() +
               ["D=M",
                "@ARG",
                "A=M",
                "M=D"])
    # SP = ARG+1
    output += ["// SP = ARG+1",
               "@ARG",
               "D=M+1",
               "@SP",
               "M=D"]
    # endFrame -=1,
    output += __write_restore_partial("THAT")
    output += __write_restore_partial("THIS")
    output += __write_restore_partial("ARG")
    output += __write_restore_partial("LCL")
    # goto retAddr
    output += ["@retAddr",
               "A=D",
               "0; JMP"]
    return output


def write_call(func_name, num_args):
    return []


def __write_restore(i, var):
    """Writes code equvialent to var=*(endFrame-5)"""
    return (["// {0} = *(endFrame - {1})".format(var, i),
             at("endFrame"),
             "D=M"] +
            push() +
            [at(i),
             "D=A", "// push"] +
            push() + ["// write_sub"] +
            write_sub() + ["// pop"] +
            pop() +
            ["A=M",
             "D=M",
             at(var),
             "M=D"])


def __write_restore_partial(var):
    """Decrement endframe by 1, then set var to that value"""
    return (["// endFrame-=1, {0} = *(endFrame)".format(var),
             at("endFrame"),
             "M=M-1"] +
            ["A=M",
             "D=M",
             at(var),
             "M=D"])
