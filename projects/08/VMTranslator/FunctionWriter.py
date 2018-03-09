# Writes assembly code for function calls
from WritingHelpers import push, pop, at
from StackArithmeticWriter import write_sub


def write_function(func_name, num_vars, ftitle):
    output = ["({0}.{1})".format(ftitle, func_name)]
    for i in range(int(num_vars)):
        output += ["D=0"] + push()
    return output


def write_return():
    # endFrame = LCL
    # retAddr = *(endFrame-5)
    # *ARG = pop(), sets return value to arg[0]
    # SP = ARG+1
    # endFrame -=1, THAT = *(endFrame)
    # endFrame -=1, THIS = *(endFrame)
    # endFrame -=1, ARG = *(endFrame)
    # endFrame -=1, LCL = *(endFrame)
    # goto retAddr

    # ---- implementation ----
    # endFrame = LCL
    output = [at("LCL"), "D=M", at("endFrame"), "M=D"]
    # retAddr = *(endFrame-5)
    output += __write_save_retAddr()
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
    # endFrame -=1, segm_var = *(endFrame)
    output += __write_restore("THAT")
    output += __write_restore("THIS")
    output += __write_restore("ARG")
    output += __write_restore("LCL")
    # goto retAddr
    output += ["// goto retAddr",
               "@retAddr",
               "A=M",
               "0;JMP"]
    return output


def write_call(func_name, num_args, curr_func, num_calls):
    return_label = "{0}$ret.{1}".format(curr_func, num_calls)
    # push returnLabel
    output = [at(return_label), "D=A"] + push()
    # push LCL
    output += [at("LCL"), "D=M"] + push()
    # push ARG
    output += [at("ARG"), "D=M"] + push()
    # push THIS
    output += [at("THIS"), "D=M"] + push()
    # push THAT
    output += [at("THAT"), "D=M"] + push()
    # ARG=SP-5-nArgs
    output += [at("SP"), "D=M-1"]
    for i in range(3+int(num_args)):
        output.append("D=D-1")
    output += [at("ARG"), "M=D-1"]
    # LCL=SP
    output += [at("SP"), "D=M", at("LCL"), "M=D"]
    # goto functionName
    output += [at(func_name), "0;JMP"]
    # (returnLabel)
    output.append("({0})".format(return_label))
    return output

# ---- helpers ----


def __write_save_retAddr():
    """Saves the return address in a local variable. """
    return (["// retAddr = *(endFrame - 5)",
             at("endFrame"),
             "D=M"] +
            push() +
            [at(5),
             "D=A", "// push"] +
            push() + ["// write_sub"] +
            write_sub() + ["// pop"] +
            pop() +
            ["A=M",
             "D=M",
             at("retAddr"),
             "M=D"])


def __write_restore(var):
    """Decrement endframe by 1, then set var to that value"""
    return (["// endFrame-=1, {0} = *(endFrame)".format(var),
             at("endFrame"),
             "M=M-1"] +
            ["A=M",
             "D=M",
             at(var),
             "M=D"])
