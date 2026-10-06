# Sorting Algorithms Visualization Lab

## Overview

In this lab, you will implement several standard sorting algorithms in Python and create a visualization showing how each algorithm changes a list as it sorts.

Your final program will be **menu driven**. The user should be able to generate a random list, choose a sorting algorithm, watch the algorithm sort the list, and then choose another option.

You will practice:

- Implementing standard sorting algorithms
- Breaking a program into functions
- Working with lists
- Using recursion
- Using `matplotlib`
- Creating a menu-driven program
- Comparing sorting algorithms

---

## Files

This repository contains:

```text
sorting_visualization_lab/
├── README.md
├── sorting_lab.py
└── plot_example.py
```

### `sorting_lab.py`

This is your starter file. Complete the functions marked with `TODO`.

### `plot_example.py`

This is a small example showing how to display and update a list using a bar graph.

You may use ideas from this file in your lab.

---

# GitHub Workflow

For this lab, you will complete your work in a GitHub repository and submit the **public URL to your completed repository**.

You should make regular commits as you work rather than waiting until the very end.

---

## Step 1 — Clone the Repository

Your instructor will provide the URL for the starter repository.

Open a terminal and move to the folder where you want to keep your course work.

Then clone the repository:

```bash
git clone REPOSITORY_URL
```

For example:

```bash
git clone https://github.com/username/sorting-visualization-lab.git
```

After cloning, move into the repository folder:

```bash
cd sorting-visualization-lab
```

You can check the files with:

```bash
ls
```

You should see files such as:

```text
README.md
sorting_lab.py
plot_example.py
```

---

## Step 2 — Open the Repository in VS Code

From inside the repository folder, you can open the project in VS Code with:

```bash
code .
```

If the `code` command is not configured on your computer, you may open VS Code normally and use:

**File → Open Folder**

Then select the cloned repository folder.

---

## Step 3 — Run the Starter Code

Before changing anything, make sure Python is working.

Run:

```bash
python sorting_lab.py
```

Depending on your computer, you may need:

```bash
python3 sorting_lab.py
```

You should also test the plotting example:

```bash
python plot_example.py
```

If `matplotlib` is not installed, install it with:

```bash
python -m pip install matplotlib
```

or:

```bash
python3 -m pip install matplotlib
```

---

## Important Matplotlib Note

When a sorting animation is running, **do not close the Matplotlib graph window** until the sort has finished.

The Python program may still be trying to update the graph. If you close the graph window while the animation is running, the terminal may appear to freeze or stop responding normally.

Wait until the sorting animation finishes and the program returns to the menu before closing the graph window.

If your terminal does appear to get stuck, press:

```bash
Ctrl+C
```

This will interrupt the running Python program and return you to the command line.

After that, you can restart the lab with:

```bash
python sorting_lab.py
```

or:

```bash
python3 sorting_lab.py
```

---


## Step 4 — Build Your Solution

Complete the `TODO` sections in:

```text
sorting_lab.py
```

You should work incrementally.

A suggested order is:

1. `generate_list()`
2. Selection Sort
3. Bubble Sort
4. Insertion Sort
5. Merge Sort
6. Algorithm explanations and pseudocode
7. Quick Sort, if assigned
8. Final testing of the menu and visualization

Test your program frequently rather than writing the entire program before running it.

---

## Step 5 — Check Your Git Status

As you work, use:

```bash
git status
```

This will show which files have changed.

For example, after editing `sorting_lab.py`, Git may report that the file has been modified.

---

## Step 6 — Commit Your Work

After completing a meaningful portion of the lab, save a commit.

First add your changes:

```bash
git add .
```

Then commit:

```bash
git commit -m "Complete selection sort"
```

Later commits might look like:

```bash
git commit -m "Add bubble and insertion sort"
```

or:

```bash
git commit -m "Complete sorting visualizations"
```

Your commit messages should briefly describe what you changed.

Do not use one enormous final commit if you can reasonably avoid it.

---

## Step 7 — Push to GitHub

Send your local commits to GitHub with:

```bash
git push
```

If this is your first push and Git gives you additional instructions, follow the command it provides.

After pushing, open your repository on GitHub and confirm that your updated files appear there.

---

## Step 8 — Make Sure the Repository Is Public

Your final repository must be publicly viewable.

On GitHub:

1. Open your repository.
2. Open **Settings**.
3. Find the repository visibility settings.
4. Confirm that the repository is **Public**.

Do not submit a repository link that your instructor cannot access.

Before submitting, it is a good idea to open the repository URL in a private/incognito browser window to confirm that it can be viewed without logging into your account.

---

## Step 9 — Final Check

Before submitting, verify that your public repository contains:

```text
README.md
sorting_lab.py
plot_example.py
```

Your completed `sorting_lab.py` should:

- Run without errors.
- Generate random lists.
- Implement the required sorting algorithms.
- Display the sorting process graphically.
- Provide explanation/pseudocode options.
- Use a working menu.
- Continue running until the user chooses to exit.
- Avoid using `sort()` or `sorted()` to perform the required sorts.

Run one final test:

```bash
python sorting_lab.py
```

Then commit and push any final changes:

```bash
git add .
git commit -m "Complete sorting visualization lab"
git push
```

---


# Part 1 — Setup

You will need Python and `matplotlib`.

Install `matplotlib` if necessary:

```bash
python -m pip install matplotlib
```

Run the plotting example:

```bash
python plot_example.py
```

Run your lab program:

```bash
python sorting_lab.py
```

---

# Part 2 — Random Lists

Complete:

```python
generate_list(size=20)
```

The function should return a list containing `size` random integers.

For example, a generated list might look like:

```text
[42, 17, 83, 6, 51, 29, 94, 11]
```

Use values that work well in a bar graph, such as integers from 1 through 100.

---

# Part 3 — Selection Sort

Complete:

```python
selection_sort(values)
```

Implement Selection Sort manually.

The basic idea is:

1. Begin at the first unsorted position.
2. Search the remaining unsorted portion for the smallest value.
3. Swap that value into the current position.
4. Repeat.

Your function should call the visualization function after an important change to the list.

A good choice is to update the graph after each swap.

---

# Part 4 — Bubble Sort

Complete:

```python
bubble_sort(values)
```

Bubble Sort repeatedly compares neighboring values.

If two neighboring values are out of order, swap them.

Continue making passes through the list until the list is sorted.

Update the visualization after each swap.

---

# Part 5 — Insertion Sort

Complete:

```python
insertion_sort(values)
```

Insertion Sort builds a sorted portion of the list one item at a time.

For each new value:

1. Save the value being inserted.
2. Shift larger values to the right.
3. Insert the saved value into the correct position.

Update the visualization as values move.

---

# Part 6 — Merge Sort

Complete:

```python
merge_sort(values)
```

You will probably also want a helper function such as:

```python
merge(...)
```

Merge Sort uses recursion.

It works in two major stages.

## Divide

Repeatedly split the list into smaller pieces.

## Merge

Combine sorted pieces back together.

Because Merge Sort does not naturally swap values in the same way as Selection Sort or Bubble Sort, you will need to think carefully about when to update the visualization.

Your final result should still allow the user to see the list gradually becoming sorted.

---

# Part 7 — Optional Challenge: Quick Sort

Complete:

```python
quick_sort(values)
```

Quick Sort:

1. Chooses a pivot.
2. Partitions values around the pivot.
3. Recursively sorts the resulting portions.

You may use any reasonable pivot strategy.

This portion may be treated as an extension or bonus depending on instructor directions.

---

# Part 8 — Algorithm Explanation and Pseudocode

For **each sorting algorithm**, write a function that prints:

1. A short explanation of how the algorithm works.
2. Pseudocode describing the major steps of the algorithm.

For example, you will complete functions such as:

```python
def print_selection_info():
    print("Selection Sort")
    print()
    print("Explanation:")
    print("...")
    print()
    print("Pseudocode:")
    print("...")
```

You should create an information function for each sorting method:

```python
print_selection_info()
print_bubble_info()
print_insertion_info()
print_merge_info()
print_quick_info()
```

Your explanation should be written in your own words.

Your pseudocode should describe the algorithm clearly without simply copying your Python code.

For example, Selection Sort pseudocode might have a structure like:

```text
FOR each position in the list
    assume the current position contains the smallest value

    FOR each remaining value
        IF a smaller value is found
            remember its position

    swap the smallest value into the current position
```

Do **not** copy this exact example as your submitted Selection Sort pseudocode. Write your own version that accurately describes your implementation.

Your program should provide a menu option that allows the user to display the explanation and pseudocode for any sorting algorithm.

A suggested submenu is:

```text
ALGORITHM INFORMATION

1. Selection Sort
2. Bubble Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort
6. Return to Main Menu
```

Selecting an algorithm should print that algorithm's explanation and pseudocode to the terminal.

---

# Part 9 — Visualization


The starter file contains:

```python
draw_list(values, title="")
```

Use this function to display the current state of the list.

The graph should show one bar for each element of the list.

For example:

```python
draw_list(values, "Selection Sort")
```

The `plot_example.py` file demonstrates the basic idea.

Do **not** worry about making an elaborate animation system. The purpose of the visualization is to make the behavior of the sorting algorithms visible.

---

# Part 10 — Menu-Driven Program

Your final program should repeatedly display a menu similar to:

```text
SORTING VISUALIZER

Current List:
[42, 17, 83, 6, 51, 29]

1. Generate New Random List
2. Selection Sort
3. Bubble Sort
4. Insertion Sort
5. Merge Sort
6. Quick Sort
7. Algorithm Information / Pseudocode
8. Exit

Choice:
```

The program should continue until the user chooses **Exit**.

When the user selects a sorting algorithm, your program should:

1. Make a copy of the current list.
2. Visualize the sorting algorithm operating on that copy.
3. Display the final sorted list.

Using a copy allows the user to run multiple algorithms on the same original data.

For example:

```python
working_list = values.copy()
selection_sort(working_list)
```

---

# Part 11 — Questions

Create a short document or add your answers to the end of this README if instructed.

Answer the following questions.

1. Which sorting algorithm seems to make the most swaps or movements?

2. Which algorithm is easiest to understand by watching the visualization?

3. Compare Selection Sort and Bubble Sort. How does the sorted portion of the list develop differently?

4. Compare Insertion Sort and Selection Sort.

5. What is visually different about Merge Sort compared with the first three algorithms?

6. Complete the table.

| Algorithm | Typical / Expected Time Complexity |
|---|---|
| Selection Sort | |
| Bubble Sort | |
| Insertion Sort | |
| Merge Sort | |
| Quick Sort | |

7. Which algorithm would you expect to work best for a very large randomly ordered list? Explain briefly.

---

# Program Requirements

Your program must:

- Use functions.
- Use the provided menu structure or a comparable menu.
- Generate random lists.
- Implement the sorting algorithms manually.
- Display the sorting process graphically.
- Provide a student-written explanation and pseudocode for each sorting algorithm.
- Include a menu option for displaying the explanation/pseudocode for each algorithm.
- Allow the user to run more than one algorithm.
- Continue running until the user chooses to exit.

You may **not** use:

```python
values.sort()
```

or:

```python
sorted(values)
```

to perform the sorting.

---

# Suggested Program Structure

A reasonable program structure is:

```text
generate_list()

draw_list()

selection_sort()
bubble_sort()
insertion_sort()

merge()
merge_sort()

quick_sort()

print_selection_info()
print_bubble_info()
print_insertion_info()
print_merge_info()
print_quick_info()

print_menu()
print_info_menu()

main()
```

You may create additional helper functions if they make your program easier to understand.

---

# Testing Suggestions

Before adding visualization, test each sorting algorithm with small lists.

For example:

```python
[5, 2, 8, 1, 3]
```

Your result should be:

```python
[1, 2, 3, 5, 8]
```

Also test:

```python
[1, 2, 3, 4, 5]
```

and:

```python
[5, 4, 3, 2, 1]
```

After the algorithm works correctly, add calls to `draw_list()`.

---

# Submission

Your final submission is the **public GitHub URL for your completed repository**.

Submit a link in a form similar to:

```text
https://github.com/yourusername/sorting-visualization-lab
```

Do **not** submit:

- A ZIP file
- Only the `.py` file
- A screenshot of your code
- A link to an individual file inside the repository
- A private repository that your instructor cannot access

Your submission should link to the **main page of the public repository**.

Before submitting, click your own link and confirm that the repository is visible and that your most recent code has been pushed.

## Final Submission Checklist

- [ ] Repository is public
- [ ] `sorting_lab.py` is complete
- [ ] Program runs successfully
- [ ] Visualizations work
- [ ] Algorithm explanations/pseudocode are included
- [ ] Required sorting algorithms are implemented manually
- [ ] Latest changes have been committed
- [ ] Latest commits have been pushed to GitHub
- [ ] Submitted link points to the main repository page

**Final submission: Public GitHub repository URL**
