```
Programming Assignment 2: Modulo and Number Theory Assignment
  by Patrick Tuttle
  License: MIT (See file for details.)

Link to GitHub Repo: https://github.com/Ptuttle91/ProgrammingAssignment2  

[Contents:]
  * About
  * Requirements
  * How to Run
  * How to Use
  * Reources Referenced
  * File Tree with Instructions


[ABOUT:]
  This project is modular application based off of a series of tasks provided in the Modulo and Number Theory PDF.
  Each task is given its own logical module, and the GUI will dynamically build input fields based on the requirements
  listed in the central 'Task Registry' module. Additionally, this program will also record a history of runs  that
  details the input, output, and a time/date stamp to allow easy review and grading for my professor, and a hope for
  a good grade by making his life easier.
  
  This project was developed using JetBrain's IDE, Pycharm.
  
  This project may push beyond the expectations, however I have chosen to do so as I desired to refresh and apply previosuly
  learned skills, and pick up some newer ones, such as the dynamic input fields. It is also worth noting that much of this
  had been initially drafted on paper and my phone's note app as I did not have access to my PC. The amount of time spent
  on this, including research for crafting functions, is over 35 hours.

[Requirements]
  * Pyhthon 3.10 or later

[How to Run:]
  1.) Download project folder from GitHub.
  2.) Unzip the file to desired directory.
  3.) In the "ProgrammingAssignment2-main" directory, initialize the 'main.py' file
        This may be done in a compiler, directly with Python, or through windows Power Shell. 

[How to Use:]
  1.) From the GUI, select the task that you want to grade from the dropdown menu.
  2.) Enter the required inputs (If any).
  3.) Click the 'Run Task' button to view the output.
    3.a) Please note, Task 6a does not require input. Simply clicking 'Run Task' will provide my written response
    3.b) The results from each completed task are added to the 'History' pane at the bottom.

[Resources used:]
  [Logging Module]
    - https://docs.python.org/3/library/dataclasses.html
    - https://peps.python.org/pep-0557/

 [History]
    - https://realpython.com/python-pathlib/

 [Task Registry]
    - https://peps.python.org/pep-0563
    - https://peps.python.org/pep-0649
    - https://typing.python.org/en/latest/spec/special-types.html
    - https://typing.python.org/en/latest/spec/callables.html

  [Modulo]
    - https://realpython.com/python-modulo-operator/

  [Ciphers]
    - https://docs.python.org/3/library/stdtypes.html#text-and-binary-sequence-type-methods-summary
    - https://www.w3schools.com/python/ref_string_join.asp

[File Tree:]
  Programming Assignment 2/  
    |  
    | - ReadMe.md
    | - Main.py (Entry Point for GUI)  
    | - GUI/  
      | - __init__.py  
      | - app.py (Contains the GUI functions, such as the dropdown, input fields, output displays, and export buttons.)  
    | - core/  
      | - __init__.py  
      | - modulo.py (Contains tasks 1-6)
      | - ciphers.py (Contains tasks 7 and 8)
      | - task_registry.py (Maps out title, callable path, and required input for interfacing with the GUI)  
      | - logging_module.py (Data class for logs)  
      | - history.py (Handles the entries from LogEntry and provides the function to export them into a .txt file)
    | - exports (This folder exists as a place to save logs to)  
      | - 

  
