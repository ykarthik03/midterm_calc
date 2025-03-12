from threading import Lock
import pandas as pd
from datetime import datetime

class HistoryManager:
    _instance = None
    _lock = Lock()

    def __init__(self):
        # Initialize the DataFrame with explicit columns and types.
        self.history = pd.DataFrame({
            "command": pd.Series(dtype="str"),
            "arguments": pd.Series(dtype="str"),
            "result": pd.Series(dtype="float"),
            "timestamp": pd.Series(dtype="str")
        })

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = HistoryManager()
            return cls._instance

    def add_record(self, command, arguments, result):
        # Use microsecond precision to ensure unique timestamps.
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        new_record = {
            "command": command,
            "arguments": str(arguments),
            "result": result,
            "timestamp": timestamp
        }
        new_record_df = pd.DataFrame([new_record])
        self.history = pd.concat([self.history, new_record_df], ignore_index=True)

    def get_history(self):
        if self.history.empty:
            return "No history available."
        return self.history.to_string(index=True)

    def clear_history(self):
        self.history = self.history.iloc[0:0]

    def save_history(self, filepath):
        self.history.to_csv(filepath, index=False)

    def load_history(self, filepath):
        self.history = pd.read_csv(filepath)

    def edit_record(self, index, new_command=None, new_arguments=None, new_result=None):
        """
        Edit an existing history record at the given index and update the timestamp.
        Raises IndexError if the index is out of range.
        """
        if index < 0 or index >= len(self.history):
            raise IndexError("History record index out of range")
        if new_command is not None:
            self.history.at[index, "command"] = new_command
        if new_arguments is not None:
            self.history.at[index, "arguments"] = str(new_arguments)
        if new_result is not None:
            self.history.at[index, "result"] = new_result
        # Update the timestamp (with microseconds) so even rapid edits yield a new value.
        self.history.at[index, "timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
