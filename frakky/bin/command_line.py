# Command line entry point defined in setup.py

import sys

from . import command_line_options
from frakky.core import Application, Context


def run_command_line(argv):
    options = {}
    parsed = command_line_options.parse_command_line_options(argv, options)
    if not parsed:
        return

    input_directory = options["input_directory"]
    output_directory = options["output_directory"]
    verbose = options["verbose"]

    context = Context()
    context.set_input_directory(input_directory)
    context.set_output_directory(output_directory)
    context.set_verbose(verbose)

    application = Application()
    application.execute(context)


def main():
    argv = sys.argv[1:]
    run_command_line(argv)
