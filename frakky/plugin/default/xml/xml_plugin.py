from jinja2 import Environment as JinjaEnvironment
from jinja2 import PackageLoader as JinjaPackageLoader

from ...plugin import Plugin


class XmlPlugin(Plugin):
    @staticmethod
    def get_name():
        return 'xml'

    @staticmethod
    def get_output_file_extension():
        return 'xml'

    def __init__(self):
        super().__init__()
        self._environment = JinjaEnvironment(
            loader=JinjaPackageLoader(__package__, "templates"),
            trim_blocks=True,
            keep_trailing_newline=True
        )
        self._template = self._environment.get_template("root.xml")

    def execute(self, root, context):
        render = self._template.render(
            root=root
        )
        return render
