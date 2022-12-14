# Author: https://github.com/ecriminal

import sys

class Logger:

    @staticmethod
    def __log(prefix, color, message, file=sys.stdout):
        """ Log message template """
        print(f'[ {color}{prefix} \x1b[0m] {message}\x1b[0m')

    @staticmethod
    def success(message):
        """ Log success message to stdout """
        Logger.__log('OKAY', '\x1b[92m', message)

    @staticmethod
    def info(message):
        """ Log information message to stdout """
        Logger.__log('INFO', '\x1b[94m', message)
        
    @staticmethod
    def warning(message):
        """ Log warning message to stdout """
        Logger.__log('WARN', '\x1b[93m', message)

    @staticmethod
    def error(message, should_exit=True):
        """ Log error message to stderr """
        Logger.__log('FAIL', '\x1b[91m', message, sys.stderr)

        if should_exit:
            sys.exit(-1)

    @staticmethod
    def empty_line():
        """ Log a newline `\n` character to stdout """
        print()
