#This module serves as a central registry to describe each task in a way that will be friendly to the GUI
#It will:
# - Keep the GUI decoupled
# - Define what inputs each task expects so suitable fields can be rendered in the GUI
# - Allow expansion or new entries should the need arise
# How?: 1) GUI will load tasks. 2) User selects task.  3) GUI renders field from input. 4) GUI resolves function with call.
# See ReadMe.md for references used.

from __future__ import annotations

import importlib
from dataclasses import dataclass
from typing import Any, Callable



def resolve_callable(callable_path: str) -> Callable[..., Any]:
    if ":" not in callable_path:
        raise ValueError(
            "Error: The callable_path must look like 'package.module:function_name'"
            f"(got: {callable_path})"
        )

    module_name, func_name = callable_path.split(":", 1)
    module = importlib.import_module(module_name)
    func = getattr(module, func_name)
    return func

@dataclass(frozen=True)
class InputSpecification:
    name: str
    kind: str
    label: str | None = None
    placeholder: str | None = None

@dataclass(frozen=True)
class TaskSpecification:
    task_id: str
    title: str
    description: str
    callable_path: str
    inputs: list[InputSpecification]
    output_label: str ="Output"

TASKS: list[TaskSpecification] = [
    TaskSpecification(
        task_id="Task 1",
        title="Task 1 - Congruent Mod Range",
        description="List all of the integers x in [lower, upper] such that x = b (mod n).",
        callable_path="core.modulo:congruent_mod",
        inputs=[
            InputSpecification(name="b", kind="int", label="b"),
            InputSpecification(name="n", kind="int", label="n"),
            InputSpecification(name="lower", kind="int", label="Lower bound"),
            InputSpecification(name="upper", kind="int", label="Upper bound"),
        ],
        output_label="Task 1 - Congruent Mod Range",
    ),

    TaskSpecification(
        task_id="Task 2",
        title="Task 2 - Divisors",
        description="Return all positive divisors of x.",
        callable_path="core.modulo:divisors",
        inputs=[
            InputSpecification(name="x", kind="int", label="x"),
        ],
        output_label="Task 2 - Divisors: ",
    ),

    TaskSpecification(
        task_id="Task 3",
        title="Task 3 - Greatest common divisor",
        description="Return the greatest common divisor(a, b) using the divisors() function from Task 2.",
        callable_path="core.modulo:greatest_common_divisor",
        inputs=[
            InputSpecification(name="a", kind="int", label="a"),
            InputSpecification(name="b", kind="int", label="b"),
        ],
        output_label="Task 3 - Greatest Common Divisor",
    ),

    TaskSpecification(
        task_id="Task 4",
        title="Task 4 - Multiplicative Inverse",
        description="Return the multiplicative inverse of a (mod n) if it exists.",
        callable_path="core.modulo:multiplicative_inverse",
        inputs=[
            InputSpecification(name="a", kind="int", label="a"),
            InputSpecification(name="b", kind="int", label="b"),
            InputSpecification(name="n", kind="int", label="n"),
        ],
        output_label="Task 4 - Multiplicative Inverse or None: ",
    ),

    TaskSpecification(
        task_id="Task 5",
        title="Task 5 - Relatively Prime, using tasks 2 and 3",
        description="Return True if a and b are relatively prime. If not, return False",
        callable_path="core.modulo:relatively_prime",
        inputs=[
            InputSpecification(name="a", kind="int", label="a"),
            InputSpecification(name="b", kind="int", label="b"),
        ],
        output_label="Task 5 - Relatively prime?",
    ),

    TaskSpecification(
        task_id="Task 6A",
        title="Task 6A - An Explanation or Euclidean Algorithm",
        description="Written task to return my explanation of euclidean algorithms",
        callable_path="core.modulo:task6a_euclidean_writeup",
        inputs=[],
        output_label="Task 6-A Write-Up:",
    ),

    TaskSpecification(
        task_id="Task 6B",
        title="Task 6B - A Relatively Prime Euclidean Algorithm",
        description="Return True if a and b are relatively prime using Euclid's algorithm. If not, return False",
        callable_path="core.modulo:relatively_prime_euclid",
        inputs=[
            InputSpecification(name="a", kind="int", label="a"),
            InputSpecification(name="b", kind="int", label="b"),
        ],
        output_label="Relatively prime?"
    ),

    TaskSpecification(
        task_id="Task 7",
        title="Task 7 - Move-Over Cipher Encryption",
        description="Encrypt a word using a Move-Over cipher with a key of K.",
        callable_path="core.ciphers:move_over_encrypt",
        inputs=[
            InputSpecification(name="key", kind="int", label="Key (k)"),
            InputSpecification(name="word", kind="str", label="Word"),
        ],
        output_label="Task 7 - Move Over Cipher Encrypted Text",
    ),

    TaskSpecification(
        task_id="Task 8",
        title="Task 8 - Skip Ahead Cipher Encryption",
        description="Encrypt a word using a Skip Ahead cipher with a key of K.",
        callable_path="core.ciphers:skip_ahead_encrypt",
        inputs=[
            InputSpecification(name="word", kind="str", label="Word"),
            InputSpecification(name="key", kind="int", label="Key (k)"),
        ],
        output_label="Task 8 - Skip Ahead Cipher Encrypted Text",
    ),
]

def get_task_titles()->list[str]:
    # This function will return titles in the order as they appear in the registry
    return [t.title for t in TASKS]

def get_task_by_title(title: str)->TaskSpecification:
    # Allows TaskSpecification lookup by title
    for t in TASKS:
        if t.title == title:
            return t
    raise KeyError(f"Error: Task with title {title} not found")

def get_task_by_id(task_id: str)->TaskSpecification:
    # Allows lookup of TaskSpecification by task_id
    for t in TASKS:
        if t.task_id == task_id:
            return t
    raise KeyError(f"Error: Task with id {task_id} not found")
