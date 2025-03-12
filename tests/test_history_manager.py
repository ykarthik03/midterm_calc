import time
import pytest
from app.history_manager import HistoryManager

def test_history_manager_singleton():
    hm1 = HistoryManager.get_instance()
    hm2 = HistoryManager.get_instance()
    assert hm1 is hm2

def test_history_add_and_clear():
    hm = HistoryManager.get_instance()
    hm.clear_history()
    hm.add_record("add", [2, 3], 5)
    history_str = hm.get_history()
    assert "add" in history_str
    hm.clear_history()
    assert hm.get_history() == "No history available."

def test_add_record_includes_timestamp():
    hm = HistoryManager.get_instance()
    hm.clear_history()
    hm.add_record("multiply", [4, 5], 20)
    record = hm.history.iloc[0]
    # Verify that the timestamp field is non-empty.
    assert record["timestamp"] != ""

def test_edit_record_success():
    hm = HistoryManager.get_instance()
    hm.clear_history()
    hm.add_record("subtract", [10, 4], 6)
    old_timestamp = hm.history.loc[0, "timestamp"]
    time.sleep(0.001)  # Short sleep to allow timestamp change
    hm.edit_record(0, new_command="divide", new_arguments=[20, 5], new_result=4)
    updated = hm.history.loc[0]
    assert updated["command"] == "divide"
    assert updated["arguments"] == "[20, 5]"
    assert updated["result"] == 4
    assert updated["timestamp"] != old_timestamp

def test_edit_record_only_command():
    hm = HistoryManager.get_instance()
    hm.clear_history()
    hm.add_record("add", [2, 3], 5)
    old = hm.history.iloc[0].copy()
    time.sleep(0.001)
    hm.edit_record(0, new_command="subtract")
    updated = hm.history.iloc[0]
    assert updated["command"] == "subtract"
    # Other fields should remain unchanged.
    assert updated["arguments"] == old["arguments"]
    assert updated["result"] == old["result"]
    assert updated["timestamp"] != old["timestamp"]

def test_edit_record_only_arguments():
    hm = HistoryManager.get_instance()
    hm.clear_history()
    hm.add_record("add", [2, 3], 5)
    old = hm.history.iloc[0].copy()
    time.sleep(0.001)
    hm.edit_record(0, new_arguments=[4, 5])
    updated = hm.history.iloc[0]
    assert updated["command"] == old["command"]
    assert updated["arguments"] == "[4, 5]"
    assert updated["result"] == old["result"]
    assert updated["timestamp"] != old["timestamp"]

def test_edit_record_only_result():
    hm = HistoryManager.get_instance()
    hm.clear_history()
    hm.add_record("add", [2, 3], 5)
    old = hm.history.iloc[0].copy()
    time.sleep(0.001)
    hm.edit_record(0, new_result=100)
    updated = hm.history.iloc[0]
    assert updated["command"] == old["command"]
    assert updated["arguments"] == old["arguments"]
    assert updated["result"] == 100
    assert updated["timestamp"] != old["timestamp"]

def test_edit_record_index_error():
    hm = HistoryManager.get_instance()
    hm.clear_history()
    with pytest.raises(IndexError):
        hm.edit_record(0, new_command="divide", new_arguments=[20, 5], new_result=4)

def test_save_and_load_history(tmp_path):
    hm = HistoryManager.get_instance()
    hm.clear_history()
    hm.add_record("add", [1, 2], 3)
    file_path = tmp_path / "history.csv"
    hm.save_history(file_path)
    hm.clear_history()
    hm.load_history(file_path)
    assert "add" in hm.get_history()
