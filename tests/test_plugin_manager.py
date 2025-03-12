import pytest
from plugin_manager import PluginManager

def test_plugin_manager_nonexistent_dir():
    pm = PluginManager(plugin_dir="nonexistent_dir")
    pm.load_plugins()
    assert not pm.get_plugin_commands()

def test_plugin_missing_register(tmp_path):
    plugin_dir = tmp_path / "plugins"
    plugin_dir.mkdir()
    bad_plugin = plugin_dir / "bad_plugin.py"
    bad_plugin.write_text("def dummy(): pass")
    pm = PluginManager(plugin_dir=str(plugin_dir))
    pm.load_plugins()
    assert not pm.get_plugin_commands()

def test_plugin_register_error(tmp_path):
    plugin_dir = tmp_path / "plugins"
    plugin_dir.mkdir()
    error_plugin = plugin_dir / "error_plugin.py"
    error_plugin.write_text(
        "def register():\n    raise Exception('Plugin error')"
    )
    pm = PluginManager(plugin_dir=str(plugin_dir))
    pm.load_plugins()
    assert not pm.get_plugin_commands()

def test_plugin_success(tmp_path):
    plugin_dir = tmp_path / "plugins"
    plugin_dir.mkdir()
    dummy_plugin = plugin_dir / "dummy_plugin.py"
    dummy_plugin.write_text(
        "def double(x):\n    return x * 2\n\n"
        "def register():\n    return {'name': 'double', 'function': double}\n"
    )
    pm = PluginManager(plugin_dir=str(plugin_dir))
    pm.load_plugins()
    assert 'double' in pm.get_plugin_commands()
    assert pm.execute_plugin('double', 5) == 10

def test_plugin_empty_register(tmp_path):
    plugin_dir = tmp_path / "plugins"
    plugin_dir.mkdir()
    empty_plugin = plugin_dir / "empty_plugin.py"
    empty_plugin.write_text(
        "def register():\n    return {}"
    )
    pm = PluginManager(plugin_dir=str(plugin_dir))
    pm.load_plugins()
    assert not pm.get_plugin_commands()

def test_execute_plugin_not_found(tmp_path):
    plugin_dir = tmp_path / "plugins"
    plugin_dir.mkdir()
    pm = PluginManager(plugin_dir=str(plugin_dir))
    pm.load_plugins()
    with pytest.raises(ValueError):
        pm.execute_plugin("nonexistent", 1)

def test_plugin_ignore_non_py_file(tmp_path):
    # Create a file that does not end with '.py'
    plugin_dir = tmp_path / "plugins"
    plugin_dir.mkdir()
    non_py_file = plugin_dir / "not_a_plugin.txt"
    non_py_file.write_text("This is not a plugin")
    pm = PluginManager(plugin_dir=str(plugin_dir))
    pm.load_plugins()
    # Since the file doesn't end with .py, it should be ignored.
    assert not pm.get_plugin_commands()
