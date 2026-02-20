# This module contains the GUI that will interface with modules from the core.

import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from core.tasks_registry import (
    get_task_titles,
    resolve_callable,
    get_task_by_title,
    resolve_callable,
)
from core.history import  History
from core.logging_module import Logging

class App:
    def __init__(self): -> None:
        self.root = tk.Tk()
        self.root.title("Cryptography Tasks GUI")
    
        self.history = History()
        self.current_task = None
        self.input_vars: dict[str, tk.StringVar] = {}
    
        self._build_top_controls()
        self._build_input_area()
        self._build_output_area()
        self._build_history_area()
    
        titles = get_task_titles()
        if titles:
            self.task_combo.set(titles[0])
            self._on_task_change()
            
        def run(self) -> None:
            self.root.mainloop()
            

