from abc import ABCMeta
from abc import abstractmethod

import os


class Plugin(metaclass=ABCMeta):
    class Output:
        def __init__(self, directory, file_name, contents):
            self._directory = directory
            self._file_name = file_name
            self._contents = contents

        def write(self):
            if not os.path.exists(self._directory):
                os.makedirs(self._directory)
            file_path = os.path.join(self._directory, self._file_name)
            with open(file_path, 'wb') as file:
                file.write(self._contents.encode('utf-8'))
                file.close()

    @staticmethod
    @abstractmethod
    def get_name():
        ...

    @staticmethod
    @abstractmethod
    def get_output_file_extension():
        ...

    def __init__(self):
        self._roots = []
        self._outputs = []

    def add_output(self, output):
        self._outputs.append(output)

    def generate_output(self, root, context):
        output_directory = os.path.abspath(context.get_output_directory())
        file_name = f'{root.name}.{self.get_output_file_extension()}'
        contents = self.execute(root, context)

        output = Plugin.Output(output_directory, file_name, contents)
        self.add_output(output)

    @abstractmethod
    def execute(self, root, context):
        ...

    def write_output(self):
        for output in self._outputs:
            output.write()
