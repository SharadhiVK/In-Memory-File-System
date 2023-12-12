# In-Memory File System

An in-memory file system implementation supporting various functionalities, including directory navigation, file operations, and a bonus feature for saving and loading the file system state.

## Overview

This project implements a simple in-memory file system in [Python](https://www.python.org/) to mimic basic terminal-like commands for file and directory manipulation.

## Functionalities Implemented

- **mkdir:** Create a new directory.
- **cd:** Change the current directory.
- **ls:** List the contents of the current or specified directory.
- **grep:** Search for a specified pattern in a file (bonus feature).
- **cat:** Display the contents of a file.
- **touch:** Create a new empty file.
- **echo:** Write text to a file.
- **mv:** Move a file or directory to another location.
- **cp:** Copy a file or directory to another location.
- **rm:** Remove a file or directory.

### Bonus - Save and Reload State

- **save_state:** Save the current file system state to a file.
- **load_state:** Load the file system state from a file.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) (version 3.x)

### Implemented Functionalities:

The In-Memory File System has been designed to provide the following functionalities:

1. **Directory Management:**
   - Creating new directories.
   - Changing the current working directory.
   - Listing the contents of a directory.

2. **File Operations:**
   - Creating empty files.
   - Writing and displaying the contents of files.
   - Copying, moving, and removing files.

3. **Search and Display:**
   - Searching for a pattern in a file and displaying matching lines.

4. **State Persistence:**
   - Saving and loading the file system state to/from a file.

### Improvements to Design:

- Implemented a robust file node structure to represent files and directories.
- Ensured proper handling of edge cases, such as attempting to copy a file to a non-existent directory.
- Optimized file and directory navigation for better performance.

### Instructions for Running and Testing:

1. **Run the Program:**
   - Clone the repository to your local machine.
   - Ensure you have Python installed.
   - Run the program using the command: `python main.py`

2. **Run Tests:**
   - Install test dependencies: `pip install -r requirements-test.txt`
   - Run unit tests: `python -m unittest test_InMemoryFileSystem.py`

3. **View Test Coverage:**
   - Install coverage.py: `pip install coverage`
   - Measure test coverage: `coverage run -m unittest test_InMemoryFileSystem.py`
   - View coverage report: `coverage report -m`

### Test Dependencies
Make sure to install the test dependencies before running the tests:
pip install -r requirements-test.txt

### Sample Output
After running the tests, you should see an output similar to the following:

...
----------------------------------------------------------------------
Ran 7 tests in 0.002s

FAILED (failures=2, errors=3)




###  Troubleshooting
If you encounter issues during testing, consider the following troubleshooting tips:

-Ensure that you have the correct dependencies installed using pip install -r requirements.txt.
-Double-check that the test data and file paths specified in the test cases are accurate






