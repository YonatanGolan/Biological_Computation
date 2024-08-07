import itertools
import numpy as np
import matplotlib.pyplot as plt

'''
Explanation of the Program:
This program identifies and checks monotonic conditions in finds all the monotonic regulation conditions of the reasoning engine.
The program show that the 18 rows correspond to the only regulation conditions that satisfy monotonic requirement and consider
whether none, some or all of the activators/inhibitors are present.
The program also ensures that the identified sequences match the predefined set of desired sequences.
At the end the program plots the table of monotonic conditions.

The program doesn't take any input data. 
It's running over all possible binary sequences of length 9 and checks for monotonic conditions by rules defined in the is_monotonic function.
The program also uses a predefined set of desired rows (binary sequences) to check against the identified monotonic sequences.

Output:
The program outputs and plot a table of regulation conditions that satisfy the monotonic requirement.
The table is color-coded to highlight the presence of 1s in each sequence
'''

desired_rows = [
    (0, 0, 1, 0, 0, 0, 0, 0, 0),
    (0, 1, 1, 0, 0, 0, 0, 0, 0),
    (0, 0, 1, 0, 0, 1, 0, 0, 0),
    (0, 1, 1, 0, 0, 1, 0, 0, 0),
    (0, 0, 1, 0, 0, 1, 0, 0, 1),
    (0, 1, 1, 0, 0, 1, 0, 0, 1),
    (0, 1, 1, 0, 1, 1, 0, 0, 0),
    (0, 1, 1, 0, 1, 1, 0, 0, 1),
    (0, 1, 1, 0, 1, 1, 0, 1, 1),
    (1, 1, 1, 0, 0, 0, 0, 0, 0),
    (1, 1, 1, 0, 0, 1, 0, 0, 0),
    (1, 1, 1, 0, 1, 1, 0, 0, 0),
    (1, 1, 1, 1, 1, 1, 0, 0, 0),
    (1, 1, 1, 0, 0, 1, 0, 0, 1),
    (1, 1, 1, 0, 1, 1, 0, 0, 1),
    (1, 1, 1, 1, 1, 1, 0, 0, 1),
    (1, 1, 1, 0, 1, 1, 0, 1, 1),
    (1, 1, 1, 1, 1, 1, 0, 1, 1),
]


def check_table(table):
    """ this function make sure each row in the table we've got is in the desired table we want to have"""
    for row in table:
        if row not in desired_rows:
            return False
    return True


def is_monotonic(row):
    if row == (0, 0, 0, 0, 0, 0, 0, 0, 0) or row == (1, 1, 1, 1, 1, 1, 1, 1, 1):
        return False
    if row[2] < row[1] or row[2] < row[0] or row[1] < row[0]: # check if the columns which repressor_mode is 0 are monotonic
        return False
    if row[5] < row[4] or row[5] < row[3] or row[4] < row[3]: # check if the columns which repressor_mode is 1 are monotonic
        return False
    if row[8] < row[7] or row[8] < row[6] or row[7] < row[6]: # check if the columns which repressor_mode is 2 are monotonic
        return False
    if row[5] > row[2] or row[8] > row[2] or row[8] > row[5]: # check if the columns which activator_mode is 2 are monotonic
        return False
    if row[4] > row[1] or row[7] > row[1] or row[7] > row[4]: # check if the columns which activator_mode is 1 are monotonic
        return False
    if row[6] > row[3] or row[6] > row[0] or row[3] > row[0] :# check if the columns which activator_mode is 0 are monotonic
        return False
    return True


def find_monotonic_conditions():
    monotonic_conditions = []
    all_possible_rows = list(itertools.product([0, 1], repeat=9))
    for row in all_possible_rows:
        if is_monotonic(row):
            monotonic_conditions.append(row)
    return monotonic_conditions


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


# Find monotonic conditions
monotonic_conditions = find_monotonic_conditions()

# Print results
print("Monotonic regulation conditions are found in rows:")
for idx, condition in enumerate(monotonic_conditions):
    print(f"Row {idx}: {condition}")

# Plot the table
plot_table(monotonic_conditions)

# Check if the table is correct
print(f"\nIs the table correct? {check_table(monotonic_conditions)}")
