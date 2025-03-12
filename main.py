#!/usr/bin/env python3
"""
Main entry point for the Advanced Python Calculator.
Provides a human-friendly REPL interface to perform arithmetic operations,
view and manage calculation history, and execute plugin commands.
"""

import logging
import os
from logger_setup import setup_logging
from app.command import CommandFactory
from app.history_manager import HistoryManager
from plugin_manager import PluginManager

def repl():
    logging.info("Starting the Advanced Python Calculator REPL.")
    command_factory = CommandFactory()
    history_manager = HistoryManager.get_instance()
    plugin_manager = PluginManager(plugin_dir="plugins")
    plugin_manager.load_plugins()

    # Load history if available
    history_file = os.path.join("data", "history.csv")
    if os.path.exists(history_file):
        try:
            history_manager.load_history(history_file)
            logging.info("Loaded history from %s", history_file)
        except Exception as e:
            logging.error("Failed to load history from %s: %s", history_file, e)

    welcome_msg = (
        "\nWelcome to the Advanced Python Calculator!\n"
        "Commands (separate multiple commands with a semicolon ';'):\n"
        "  add, subtract, multiply, divide <arg1> <arg2>\n"
        "  history        -- show calculation history\n"
        "  clear_history  -- clear history\n"
        "  edit_history   -- edit a history record\n"
        "  plugins        -- list plugin commands\n"
        "  help           -- show this message\n"
        "  exit           -- quit (history will be saved)\n"
    )
    print(welcome_msg)
    
    while True:
        try:
            user_input = input("calc> ").strip()
            # Check if the user wants to exit.
            if user_input.lower() in ("exit", "quit"):
                try:
                    history_manager.save_history(history_file)
                    print("History saved.")
                except Exception as e:
                    logging.error("Failed to save history: %s", e)
                print("Thank you for using the calculator. Goodbye!")
                break

            # Split the input into individual commands if semicolons are used.
            commands = [cmd.strip() for cmd in user_input.split(';') if cmd.strip()]
            for cmd_line in commands:
                # Process each command independently
                if cmd_line.lower() == "help":
                    print(welcome_msg)
                    continue
                elif cmd_line.lower() == "history":
                    print(history_manager.get_history())
                    continue
                elif cmd_line.lower() == "clear_history":
                    history_manager.clear_history()
                    print("Calculation history cleared.")
                    continue
                elif cmd_line.lower() == "plugins":
                    print("Available plugin commands:", plugin_manager.get_plugin_commands())
                    continue
                elif cmd_line.lower().startswith("edit_history"):
                    parts = cmd_line.split()
                    if len(parts) < 4:
                        print("Usage: edit_history <record_index> <command> <arg1> <arg2> ...")
                        continue
                    try:
                        record_index = int(parts[1])
                    except ValueError:
                        print("Record index must be an integer.")
                        continue
                    new_command = parts[2]
                    try:
                        new_args = list(map(float, parts[3:]))
                    except ValueError:
                        print("Arguments must be numbers.")
                        continue

                    command = command_factory.create_command(new_command, new_args)
                    if command is None:
                        print("Unknown command for editing.")
                        continue
                    try:
                        new_result = command.execute()
                        history_manager.edit_record(record_index, new_command=new_command, new_arguments=new_args, new_result=new_result)
                        print("Record updated successfully.")
                    except Exception as e:
                        logging.error("Error updating history record: %s", e)
                        print("Error updating record:", e)
                    continue

                # Check if this is a plugin command.
                parts = cmd_line.split()
                command_name = parts[0]
                if command_name in plugin_manager.get_plugin_commands():
                    args = parts[1:]
                    try:
                        args = [float(arg) if arg.replace('.', '', 1).isdigit() else arg for arg in args]
                    except Exception:
                        pass
                    result = plugin_manager.execute_plugin(command_name, *args)
                    print(f"Plugin '{command_name}' result:", result)
                    continue

                # Otherwise, treat as an arithmetic command.
                try:
                    args = list(map(float, parts[1:]))
                except Exception as e:
                    print("Error converting arguments to numbers:", e)
                    continue
                command = command_factory.create_command(command_name, args)
                if command:
                    result = command.execute()
                    history_manager.add_record(command_name, args, result)
                    print("Result:", result)
                else:
                    print("Unknown command. Type 'help' for available commands.")
        except Exception as e:
            logging.error("Error processing command: %s", e)
            print("Oops! There was an error:", e)

if __name__ == "__main__":
    setup_logging()
    repl()
