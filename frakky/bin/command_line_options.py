# Utility for command line options

import getopt


def parse_command_line_options(argv, out_options):
    input_directory = ""
    output_directory = ""
    verbose = False

    available_options = "vi:o:"
    
    try:
        opts, args = getopt.getopt(argv, available_options, [
            "outputdirectory=",
            "inputdirectory=",
            "verbose",
        ])
    except getopt.GetoptError:
        print("Invalid command line option(s) specified.")
        return False

    for opt, arg in opts:
        if opt in ("-i", "--inputdirectory"):
            input_directory = arg

        if opt in ("-o", "--outputdirectory"):
            output_directory = arg

        if opt in ("-v", "--verbose"):
            verbose = True

    out_options["input_directory"] = input_directory
    out_options["output_directory"] = output_directory
    out_options["verbose"] = verbose

    return True
