#This module serves as a central registry to describe each task in a way that will be friendly to the GUI
#It will:
# - Keep the GUI decoupled
# - Define what inputs each task expects so suitable fields can be rendered in the GUI
# - Allow expansion or new entries should the need arise
# How?: 1) GUI will load tasks. 2) User selects task.  3) GUI renders field from input. 4) GUI resolves function with call.
# See ReadMe.md for references used.
