"""
Module: plugin_manager
Manages the dynamic loading and execution of calculator plugins.
Plugins should be placed in the specified directory and implement a register() function.
"""

import os
import importlib.util
import logging

class PluginManager:
    """
    Loads plugins from a given directory. Each plugin must define a register() function
    that returns a dictionary with keys "name" and "function".
    """
    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir
        self.plugins = {}

    def load_plugins(self):
        """
        Load all Python plugins from the plugin directory.
        """
        if not os.path.exists(self.plugin_dir):
            logging.info("Plugin directory '%s' does not exist.", self.plugin_dir)
            return

        for filename in os.listdir(self.plugin_dir):
            if filename.endswith(".py"):
                plugin_path = os.path.join(self.plugin_dir, filename)
                plugin_name = filename[:-3]
                spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
                module = importlib.util.module_from_spec(spec)
                try:
                    spec.loader.exec_module(module)
                    if hasattr(module, "register"):
                        plugin_info = module.register()
                        self.plugins[plugin_info["name"]] = plugin_info["function"]
                        logging.info("Loaded plugin: %s", plugin_info["name"])
                except Exception as e:
                    logging.error("Error loading plugin %s: %s", plugin_name, e)

    def get_plugin_commands(self):
        """Return a list of available plugin command names."""
        return list(self.plugins.keys())

    def execute_plugin(self, name, *args):
        """
        Execute the plugin command identified by 'name' with the provided arguments.
        Raises a ValueError if the plugin is not found.
        """
        if name in self.plugins:
            return self.plugins[name](*args)
        else:
            raise ValueError(f"Plugin '{name}' not found.")
