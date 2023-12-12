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

### Running the Program

1. Clone the repository:
   ```bash
   git clone https://github.com/SharadhiVK/InMemoryFileSystem.git
   cd InMemoryFileSystem   
2. Execute the program:
   python script.py
   
4. Follow the on-screen instructions to interact with the in-memory file system.

###  Testing
Running Tests
To run the unit tests for the In-Memory File System, use the following command:
python -m unittest test_InMemoryFileSystem.py

Test Coverage
To measure test coverage using coverage.py, run the following commands:

Install coverage.py (if not installed)
pip install coverage

Measure test coverage
coverage run -m unittest test_InMemoryFileSystem.py
coverage report -m

Test Dependencies
Make sure to install the test dependencies before running the tests:
pip install -r requirements-test.txt

Sample Outputs
After running the tests, you should see an output similar to the following:

...
----------------------------------------------------------------------
Ran 7 tests in 0.002s

FAILED (failures=2, errors=3)




###  Troubleshooting
If you encounter issues during testing, consider the following troubleshooting tips:

-Ensure that you have the correct dependencies installed using pip install -r requirements.txt.
-Double-check that the test data and file paths specified in the test cases are accurate






The test_InMemoryFileSystem.py provides unit test cases for the code.

