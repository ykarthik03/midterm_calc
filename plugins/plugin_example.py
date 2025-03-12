"""
Sample plugin for the Advanced Python Calculator.
This plugin provides a 'square' command to square a number.
"""

def square(x):
    """Return the square of x."""
    return x * x

def register():
    """
    Register the plugin with the PluginManager.
    Returns a dictionary with the plugin's command name and function.
    """
    return {
        "name": "square",
        "function": square
    }
