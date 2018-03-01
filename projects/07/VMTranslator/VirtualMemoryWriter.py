# Writes assembly code for virtual memory operations
from WritingHelpers import push, pop, at


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
