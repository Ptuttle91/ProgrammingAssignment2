# The purpose of this module is to store a list of LogEntry objects and export them into a .txt file.
# See ReadMe.md for references used.

from pathlib import Path
from .logging_module import LogEntry

class History:
    def __init__(self) -> None:
        self.entries: list[LogEntry] = []

    def add(self, entry: LogEntry) -> None:
        self.entries.append(entry)

    def clear(self) -> None:
        self.entries.clear()

    def toText(self,title: str = "Project 2 Run Log") -> str:
        lines = []
        lines.append(title)
        lines.append("="*len(title))
        lines.append("")

        if not self.entries:
            lines.append("No entries found")
            return ("\n".join(lines))

        for e in self.entries:
            lines.append(f"[{e.timestamp}] {e.task_name}")
            lines.append(f"Inputs: {e.inputs}")
            lines.append(f"Outputs: {e.outputs}")
            lines.append("-*" * 30)
            
        return ("\n".join(lines))
    
    def export_text(self, filepath: str) -> None:
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.toText()), encoding="utf-8"
