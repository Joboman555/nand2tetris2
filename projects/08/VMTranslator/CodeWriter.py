# Writes assembly code given a list of parsed commands
from os.path import splitext, basename
from StackArithmeticWriter import (write_add, write_sub, write_and, write_or,
                                   write_neg, write_not, write_eq, write_gt,
                                   write_lt)
from VirtualMemoryWriter import write_push, write_pop
from ControlFlowWriter import write_label, write_goto, write_if_goto
from FunctionWriter import write_function, write_return, write_call


def writeline(file, line):
    """Writes a new line to a file"""
    file.write(line + '\n')


def write_code(fname, parsed_commands, outfile=None):
    output_fname = outfile or splitext(fname)[0] + '.asm'
    # title of file will be used for labels
    ftitle = splitext(basename(fname))[0]
    print "Writing assembly code to {0}".format(output_fname)
    # keep track of the current function
    # if no function is currently being used, use just ftitle
    curr_func = ftitle
    num_calls = 0
    with open(output_fname, 'a') as f:
        writeline(f, '// --------- {0} --------'.format(basename(fname)))
        for command in parsed_commands:
            # Display the original line as a comment
            writeline(f, "// " + command.original_line)
            output = []
            # ---- Stack Arithmetic Commands ----
            if command.command_type == 'C_ADD':
                output = write_add()
            elif command.command_type == 'C_SUB':
                output = write_sub()
            elif command.command_type == 'C_AND':
                output = write_and()
            elif command.command_type == 'C_OR':
                output = write_or()
            elif command.command_type == 'C_NEG':
                output = write_neg()
            elif command.command_type == 'C_NOT':
                output = write_not()
            elif command.command_type == 'C_EQ':
                output = write_eq()
            elif command.command_type == 'C_GT':
                output = write_gt()
            elif command.command_type == 'C_LT':
                output = write_lt()
            # ---- Virtual Memory Commands ----
            elif command.command_type == 'C_PUSH':
                output = write_push(command.arg1, command.arg2, ftitle)
            elif command.command_type == 'C_POP':
                output = write_pop(command.arg1, command.arg2, ftitle)
            # ---- Control Flow Commands ----
            elif command.command_type == 'C_LABEL':
                output = write_label(command.arg1, curr_func)
            elif command.command_type == 'C_GOTO':
                output = write_goto(command.arg1, curr_func)
            elif command.command_type == 'C_IF_GOTO':
                output = write_if_goto(command.arg1, curr_func)
            # ---- Function Commands ----
            elif command.command_type == 'C_FUNCTION':
                curr_func = command.arg1
                num_calls = 0
                output = write_function(command.arg1, command.arg2)
            elif command.command_type == 'C_RETURN':
                output = write_return()
            elif command.command_type == 'C_CALL':
                num_calls += 1
                output = write_call(command.arg1, command.arg2, curr_func, num_calls)
            else:
                raise Exception('Invalid Command Type: '+command.command_type)
            for line in output:
                writeline(f, line)
            writeline(f, '')
