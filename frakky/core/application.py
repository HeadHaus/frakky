import os

from frakky.structure import Directory, File
from frakky.plugin import PluginManager


class Application:
    @staticmethod
    def generate_folder_structure(parent):
        full_parent_path = parent.full_path

        for item in os.listdir(full_parent_path):
            item_path = os.path.join(full_parent_path, item)

            if os.path.isdir(item_path):
                subdirectory = Directory(item, item_path)
                parent.add_subdirectory(subdirectory)
                Application.generate_folder_structure(subdirectory)
            else:
                file = File(item, item_path)
                parent.add_file(file)

    def __init__(self):
        self._roots = []
        self._outputs = []

    def gather_root_directories(self, context):
        input_directory = os.path.abspath(context.get_input_directory())
        verbose = context.get_verbose()

        roots = []
        for root_folder in os.listdir(input_directory):
            full_path = os.path.join(input_directory, root_folder)
            if not os.path.isdir(full_path):
                continue
        
            root = Directory(root_folder, full_path)
            Application.generate_folder_structure(root)
            root.find_all_files()
            roots.append(root)

        if verbose:
            for root in roots:
                print(root)

        self._roots = roots

    def execute_plugins(self, context):
        plugin_manager = PluginManager.get_instance()
        verbose = context.get_verbose()

        plugins = plugin_manager.get_installed_plugins()
        for plugin_instance in [plugin() for plugin in plugins]:
            if verbose:
                print("Executing plugin", plugin_instance.get_name(), end='.\n')
            for root in self._roots:
                plugin_instance.generate_output(root, context)

            plugin_instance.write_output()

    def execute(self, context):
        input_directory = os.path.abspath(context.get_input_directory())
        output_directory = os.path.abspath(context.get_output_directory())
        if input_directory == "":
            print("No input directory specified.")
            return
        if output_directory == "":
            print("No output directory specified.")
            return

        verbose = context.get_verbose()
        if verbose:
            print("Input directory:", input_directory)
            print("Output directory:", output_directory)

        self.gather_root_directories(context)
        self.execute_plugins(context)
