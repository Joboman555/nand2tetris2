# Parses a .vm file
# Converts each line into its lexical components,
# ignoring whitespace and comments
from collections import namedtuple

ParsedCommand = namedtuple('ParsedCommand', ['command_type', 'arg1', 'arg2', 'original_line'])

command_types = {
    "add": "C_ADD",
    "sub": "C_SUB",
    "neg": "C_NEG",
    "eq": "C_EQ",
    "gt": "C_GT",
    "lt": "C_LT",
    "and": "C_AND",
    "or": "C_OR",
    "not": "C_NOT",
    "pop": "C_POP",
    "push": "C_PUSH",
    "label": "C_LABEL",
    "goto": "C_GOTO",
    "if-goto": "C_IF_GOTO",
}


def parse(fname):
    print "Parsing input file: {0}".format(fname)
    parsed_commands = []
    with open(fname, 'r') as f:
        for line in f.readlines():
            # Remove whitespace and comments
            trimmed_line = str.rsplit(line.strip(), '//')[0]
            if trimmed_line:
                components = trimmed_line.split()
                if components[0] not in command_types:
                    raise Exception('Command Type not recognized')
                else:
                    command = command_types[components[0]]
                    arg1 = components[1] if len(components) > 1 else None
                    arg2 = components[2] if len(components) == 3 else None
                    parsed_command = ParsedCommand(command, arg1, arg2, trimmed_line)
                    parsed_commands.append(parsed_command)
    return parsed_commands
