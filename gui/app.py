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

        # This builds the default core state
        self.history = History()
        self.current_task = None
        self.input_vars: dict[str, tk.StringVar] = {}

        # This builds the layout of the GUI
        self._build_top_controls()
        self._build_input_area()
        self._build_output_area()
        self._build_history_area()

        # This holds the initialization
        titles = get_task_titles()
        if titles:
            self.task_combo.set(titles[0])
            self._on_task_change()

        def run(self) -> None:
            self.root.mainloop()

    # The following functions build the UI

    def _build_top_controls(self)->None:
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.pack(fill="x")

        ttk.Label(frame, text="Select the Task: ").pack(side="left")

        self.task_combo = ttk.Combobox(
            frame,
            values=get_task_titles(),
            state="readonly",
            width=45,
        )
        self.task_combo.pack(side="left")
        self.task_combo.bind("<<ComboboxSelected>>", lambda _e: self._on_task_change)

        self.run_button = ttk.Button(frame, text="Run Task", command=self._run_task)
        self.run_button.pack(side="left", padx=10)

        self.export_btn = ttk.Button(frame, text="Export Results", command=self._export_log)
        self.export_btn.pack(side="left", padx=10)

    def _build_input_area(self)->None:
        outer=ttk.Frame(self.root, text="Inputs", padding="10 10 10 10")
        outer.pack(fill="x")

        self.inputs_container = ttk.Frame(outer, padding="10 10 10 10")
        self.inputs_container.pack(fill="x")

        self.task_desc = ttk.Label(outer, text="", wraplength=900, justify="left")
        self.task_desc.pack(fill="x", padx=10,0)

    def _build_output_area(self)->None:
        frame = ttk.Frame(self.root, text="Output", padding="10 10 10 10")
        frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.output_text = ttk.Text(frame, height=8, wrap="words")
        self.output_text.pack(fill="both", expand="yes", padx=10, pady=10)

    def _build_history_area(self)->None:
        frame = ttk.LabelFrame(self.root, text="Run History Preview", padding="10 10 10 10")
        frame.pack(fill="both", expand="yes", padx=10, pady=(0,10))

        self.history_text = tk.Text(frame, height=10, wrap="words")
        self.history_text.pack(fill="both", expand="yes")

        self._refresh_history_preview()

    # The following functions build the Task Selection process.

    def _on_task_change(self)->None:
        title = self.task_combo.get()
        self.current_task = get_task_by_title(title)

        self.task_desc.config(text=self.current_task.description)

        for child in self.input_container.winfo_children():
            child.destroy()

        self.input_vars.clear()

        if not self.current_task.inputs:
            ttk.Label(self.input_container, text="No Inputs!").pack(anchor="w")
            return

        for spec in self.current_task.inputs:
            row = (ttk.Frame(self.input_container)
            row.pack(fill="x",pady=3)
            
            label_text = spec.label if spec.label else spec.name
            ttk.Label(row, text=f"{label_text}:").pack(side="left")
            
            var = tk.StringVar()
            self.input_vars[spec.name] = var
            
            entry = ttk.Entry(row, textvariable=var, width=40)
            entry.pack(side="left")
            
        
