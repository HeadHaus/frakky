from frakky.plugin.default.json.json_plugin import JsonPlugin
from frakky.plugin.default.xml.xml_plugin import XmlPlugin


class PluginManager:
    _singleton = None

    def __init__(self):
        self._installed_plugins = []
        self._install_default_plugins()

    def _install_default_plugins(self):
        self.install_plugin(JsonPlugin)
        self.install_plugin(XmlPlugin)

    def install_plugin(self, plugin):
        self._installed_plugins.append(plugin)

    def get_installed_plugins(self):
        return self._installed_plugins

    def get_plugin(self, name):
        for installed_plugin in self.get_installed_plugins():
            if installed_plugin.get_name() == name:
                return installed_plugin
        print(f'Requested plugin {name} not installed.')

    @staticmethod
    def get_instance():
        if PluginManager._singleton is None:
            PluginManager._singleton = PluginManager()
        return PluginManager._singleton
