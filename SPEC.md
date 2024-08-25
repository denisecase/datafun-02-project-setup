# Specification for Project 2 Python Module

## Overview

The second module introduces additional Python programming basics including loops and branching. 
The module provides practical project setup techniques and a series of reusable functions for
drafting project folders (e.g. folders for a range of years, or from a list of folder names).

## Deliverable Names

Create a new GitHub repository with a default README.md.
In your GitHub repository, create new empty Python script as named below. 
Add your earlier utility script from Module 1 to your project repo. 

- GitHub Repository:  **datafun-02-project-setup**
- Documentation:      README.md
- New Script:         **yourname_project_setup.py**
- Utils Script:       **yourname_utils.py**

## Objective

Develop a Python module that demonstrates proficiency in loops, project folder creation using pathlib, and importing modules.
This module should include reusable functions for creating sets of project folders based on various criteria.

## Requirements

### 1. Opening Docstring

In your Python file, create a docstring with a brief introduction to your project.
For example:

```python
''' This module provides functions for creating a series of project folders. '''
```

### 2. Import Dependencies (At the Top, After the Opening Docstring)

Organize your project imports near the top of the file, following conventions.
For example, standard library imports first, then external library imports (we don't need any of these yet), then local module imports. 
Follow conventional package import organization. 
Import each package just once near the top of the file.  

Python import code example:

```python
import pathlib
import stellar_analytics_utils
```

Note: if we use "import pathlib" as shown, we must use "pathlib.Path" when working with a Path. 
Many other projects use "from pathlib import Path". 
When using this approach, you omit the initial pathlib in pathlib.Path, and just use Path.

### 3. Define Functions for Folder Creation

1. Define reusable functions to create a series of project folders.
1. Each function should have a clear purpose, input parameters, and return values if applicable.
1. Include a docstring for each function to describe its behavior.
1. Use for in range(), for in list, and while loops to demonstrate different looping techniques.
1. Use a list comprehension to demonstrate transforming a list into a new list.
1. Use conditional branching to demonstrate different folder creation options, such as including options to force lowercase or remove spaces.

Specific functions to implement and the technique to demonstrate.

Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).

```python
def create_folders_for_range(start, end):
```

Function 2. For Item in List: Develop a function to create folders from a list of names.

```python
def create_folders_from_list(folder_list):
```

Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").

```python
def create_prefixed_folders(folder_list, prefix):
```

Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).

```python
def create_folders_periodically(duration):
```

### 4. Always Join Paths with Pathlib

In your code, use pathlib to join paths and create folders.
Never use operating system-specific path symbols such as slashes, backslashes, or double back slashes.
For example:

```python
import pathlib

# Create a path object
project_path = pathlib.Path.cwd()

# Define the new sub folder path
data_path = project_path.joinpath('data')

# Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)
```

### 5. Define Main Function

Define a main() function to test the folder creation functions and demonstrate the use of imported modules.

Python main() function code example:

```python
def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline: {stellar_analytics_utils.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)
```

### Conditional Script Execution (at the end of the file)

Ensure the main function only executes when the script is run directly,
not when imported as a module by using standard boilerplate code.

```python
if __name__ == '__main__':
    main()
```

### Module Design

The code should be clear, well-organized, and demonstrate good practices.
Include comments and docstrings for clarity.

