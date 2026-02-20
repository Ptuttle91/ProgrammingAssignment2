# This module serves to define and shape user I/O as it will appear in the history log and exports.
# See ReadMe.md for references used.

from dataclasses import dataclass
from datetime import datetime

@dataclass
class LogEntry:
    timestamp: str
    task_name: str
    inputs: dict
    outputs: str

    @staticmethod
    def create(task_name: str, inputs:dict, outputs) -> "LogEntry":
        return LogEntry(
            timestamp=datetime.now(),
            task_name=task_name,
            inputs=inputs,
            outputs=str(outputs)
        )
