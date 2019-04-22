class Context:
    """A context represents a single usage of the application
    and stores all the necessary runtime information.
    A context contains the input and output directories,
    and relevant metadata.
    """

    def __init__(self):
        self._input_directory = ''
        self._output_directory = ''
        self._verbose = False

    def get_input_directory(self):
        return self._input_directory

    def set_input_directory(self, value):
        self._input_directory = value

    def get_output_directory(self):
        return self._output_directory

    def set_output_directory(self, value):
        self._output_directory = value

    def get_verbose(self):
        return self._verbose

    def set_verbose(self, value):
        self._verbose = value
