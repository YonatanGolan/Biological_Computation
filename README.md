# Monotonic Regulation Checker

## Overview
This program identifies and checks monotonic conditions in finds all the monotonic regulation conditions of the reasoning engine.
The program show that the 18 rows correspond to the only regulation conditions that satisfy monotonic requirement and consider whether none, some or all of the activators/inhibitors are present.
The program also ensures that the identified sequences match the predefined set of desired sequences.
At the end the program plots the table of monotonic conditions.

## Table of Contents
1. [Input Data](#input-data)
2. [Functions](#functions)
   - [is_monotonic](#is_monotonic)
   - [find_monotonic_conditions](#find_monotonic_conditions)
   - [check_table](#check_table)
   - [plot_table](#plot_table)
3. [Output](#output)
4. [Usage](#usage)

## Input Data
The program doesn't take any input data. 
It's running over all possible binary sequences of length 9 and checks for monotonic conditions by rules defined in the is_monotonic function.
The program also uses a predefined set of desired rows (binary sequences) to check against the identified monotonic sequences.
## Functions

### is_monotonic
```python
def is_monotonic(row):
    if row == (0, 0, 0, 0, 0, 0, 0, 0, 0) or row == (1, 1, 1, 1, 1, 1, 1, 1, 1):
        return False
    if row[2] < row[1] or row[2] < row[0] or row[1] < row[0]:
        return False
    if row[5] < row[4] or row[5] < row[3] or row[4] < row[3]:
        return False
    if row[8] < row[7] or row[8] < row[6] or row[7] < row[6]:
        return False
    if row[5] > row[2] or row[8] > row[2] or row[8] > row[5]:
        return False
    if row[4] > row[1] or row[7] > row[1] or row[7] > row[4]:
        return False
    if row[6] > row[3] or row[6] > row[0] or row[3] > row[0]:
        return False
    return True
```
This function checks if a given row (binary sequence) is monotonic according to specific conditions. The row is considered non-monotonic if:
All elements are either 0s or 1s.
Certain patterns within the row are non-monotonic as specified in the function's conditions.

### find_monotonic_conditions
```python
def find_monotonic_conditions():
    monotonic_conditions = []
    all_possible_rows = list(itertools.product([0, 1], repeat=9))
    for row in all_possible_rows:
        if is_monotonic(row):
            monotonic_conditions.append(row)
    return monotonic_conditions
```
This function generates all possible 9-element binary sequences and checks each one for monotonicity using the 'is_monotonic' function.
It returns a list of rows that meet the monotonic criteria.

### check_table
```python
def check_table(table):
    for row in table:
        if row not in desired_rows:
            return False
    return True
```
This function checks if each row in the provided table exists in the predefined list of desired rows.
It returns True if all rows are found; otherwise, it returns False.

### plot_table
```python
def plot_table(monotonic_conditions):
    fig, ax = plt.subplots(figsize=(10, 4))
    table_data = np.array(monotonic_conditions, dtype=int)

    # Create a table
    col_labels = ['Activator_mode=0\nRepressor_mode=0', 'Activator_mode=1\nRepressor_mode=0',
                  'Activator_mode=2\nRepressor_mode=0',
                  'Activator_mode=0\nRepressor_mode=1', 'Activator_mode=1\nRepressor_mode=1',
                  'Activator_mode=2\nRepressor_mode=1',
                  'Activator_mode=0\nRepressor_mode=2', 'Activator_mode=1\nRepressor_mode=2',
                  'Activator_mode=2\nRepressor_mode=2']
    row_labels = [f'Regulation\ncondition {i}' for i in range(len(monotonic_conditions))]

    ax.axis('tight')
    ax.axis('off')
    table = ax.table(rowLabels=row_labels, colLabels=col_labels, cellLoc='center', loc='center',
                     cellColours=np.where(table_data == 1, 'red', 'white'))

    plt.show()
```
This function plot the table of monotonic conditions. The table displays the binary sequences that meet the monotonic criteria. The sequences are color-coded to highlight the presence of 1s.

## Output
The program outputs and plot a table of regulation conditions that satisfy the monotonic requirement.
The table is color-coded to highlight the presence of 1s in each sequence.

## Usage
1. Ensure that Python and necessary libraries (like numpy, itertools and matplotlib) are installed.
2. Run the program.