''' The PyBasic interpreter.

An implementation of BASIC in Python.

Ambidextrous
Apr 19, 2016
'''

def execute(command):
    ''' Executes any single PyBasic command '''
    if 'PRINT' in command:
        return execute_print(command)

def execute_print(command):
    ''' Handles all print statements '''
    if ';' not in command:
        fragments = command.split('"')
        arguments = fragments[1]
        arguments_trimmed = arguments.replace('"', '')
        return arguments_trimmed
