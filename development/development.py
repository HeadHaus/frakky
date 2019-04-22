import sys

from frakky.bin import run_command_line
from frakky.plugin import Plugin, PluginManager


class TestPlugin(Plugin):
    @classmethod
    def get_name(cls):
        return 'test'

    @classmethod
    def get_output_file_extension(cls):
        return 'txt'

    def __init__(self):
        super().__init__()

    def execute(self, root, context):
        files = ""
        for file in root.all_files:
            files += file.full_path + "\n"
        return files


PluginManager.get_instance().install_plugin(TestPlugin)


if __name__ == "__main__":
    run_command_line(sys.argv[1:])
