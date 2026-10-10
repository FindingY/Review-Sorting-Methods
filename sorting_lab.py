"""
Sorting Algorithms Visualization Lab

Complete the TODO sections.

Do not use list.sort() or sorted() to perform the sorting.
"""

import random
import time
import platform
import subprocess
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# Settings
# ------------------------------------------------------------

DEFAULT_LIST_SIZE = 20
MIN_VALUE = 1
MAX_VALUE = 100
ANIMATION_DELAY = 0.10
SOUND_ENABLED = True
LOW_FREQUENCY = 200
HIGH_FREQUENCY = 1200


# ------------------------------------------------------------
# Sound Functions
# ------------------------------------------------------------

def value_to_frequency(value):
    """
    Convert a list value into a frequency.

    TODO:
        Map values from MIN_VALUE through MAX_VALUE
        into frequencies from LOW_FREQUENCY through HIGH_FREQUENCY.

        Smaller values should produce lower pitches.
        Larger values should produce higher pitches.
    """
    pass


def play_value_sound(value):
    """
    Play a short sound whose pitch depends on value.

    TODO:
        1. Return immediately if SOUND_ENABLED is False.
        2. Convert value to a frequency using value_to_frequency().
        3. Play a short sound using an appropriate method for
           the current operating system.
        4. Make sure sound errors do not crash the program.

    HINT:
        platform.system() can help determine whether the
        computer is running Windows, macOS, or Linux/Unix.
    """
    pass


# ------------------------------------------------------------
# Utility Functions
# ------------------------------------------------------------

def generate_list(size=DEFAULT_LIST_SIZE):
    list = []
    counter = 0
    while counter < size:
        list.append(random.randint(MIN_VALUE, MAX_VALUE))
        counter += 1
    return list


def draw_list(values, title="Sorting"):
    """
    Draw the current list as a bar graph.

    You do not need to modify this function unless you want to
    experiment with the visualization.
    """
    plt.clf()

    plt.bar(range(len(values)), values)

    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")

    plt.pause(ANIMATION_DELAY)


# ------------------------------------------------------------
# Sorting Algorithms
# ------------------------------------------------------------

def selection_sort(values):
    """
    Sort values using Selection Sort.

    TODO:
        1. Move through each position in the list.
        2. Find the smallest value in the unsorted portion.
        3. Swap it into the correct position.
        4. Call draw_list() after an important change.
        5. Call play_value_sound() for a meaningful value.
    """
    for start in range(len(values)):
        min_index = start
        for num in range(start+1, len(values)):
            if values[num] < values[min_index]:
                min_index = num

        values[start], values[min_index] = values[min_index], values[start]
        draw_list(values)
        play_value_sound(values[start])

    draw_list(values)

def bubble_sort(values):
    """
    Sort values using Bubble Sort.

    TODO:
        Compare adjacent values and swap values that are
        out of order.

        Call draw_list() after each swap.
        Also call play_value_sound() for one of the swapped values.
    """
    for start in range(len(values)):
        for end in range(len(values) - 1, 0, -1):
            for i in range(end):
                if values[i] > values[i + 1]:
                    values[i], values[i + 1] = values[i + 1], values[i]
                    draw_list(values)
                    play_value_sound(values[i])



def insertion_sort(values):
    """
    Sort values using Insertion Sort.

    TODO:
        Insert each new value into the correct position
        within the already-sorted portion of the list.

        Call draw_list() as values move.
        Play the value currently being inserted.
    """
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1

        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j = j - 1

        values[j + 1] = key
        draw_list(values)

    draw_list(values)

def merge(left, right):
    """
    Merge two already-sorted lists.
    Return one sorted list containing all values.
    """
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(values):
    """
    Sort values using Merge Sort.
    """
    if len(values) <= 1:
        return values

    middle = len(values) // 2

    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])

    merged = merge(left, right)

    for i in range(len(merged)):
        values[i] = merged[i]
        play_value_sound(values[i])
        draw_list(values)

    return values
def quick_sort(values):
    """
    OPTIONAL CHALLENGE

    Sort values using Quick Sort.

    You may create helper functions such as partition().

    TODO:
        Implement Quick Sort and visualize important steps.
        Play the pivot or a value involved in a swap.
    """
    pass


# ------------------------------------------------------------
# Algorithm Explanations / Pseudocode
# ------------------------------------------------------------

def print_selection_info():
    print("""Selection Sort:

Explanation:
Selection Sort finds the smallest value in the unsorted
part of the list and swaps it into the correct position.
It repeats this process until the list is sorted.

Pseudocode:
FOR each position in the list:
    Set the current position as the minimum
    FOR each remaining value:
        IF the value is smaller than the minimum:
            Update the minimum
    Swap the minimum into the current position""")


def print_bubble_info():
    """
    TODO:
        Print:
        1. A short explanation of Bubble Sort in your own words.
        2. Pseudocode for Bubble Sort.
    """
    pass


def print_insertion_info():
    """
    TODO:
        Print:
        1. A short explanation of Insertion Sort in your own words.
        2. Pseudocode for Insertion Sort.
    """
    pass


def print_merge_info():
    """
    TODO:
        Print:
        1. A short explanation of Merge Sort in your own words.
        2. Pseudocode for Merge Sort.
    """
    pass


def print_quick_info():
    """
    OPTIONAL CHALLENGE

    TODO:
        Print:
        1. A short explanation of Quick Sort in your own words.
        2. Pseudocode for Quick Sort.
    """
    pass


def print_info_menu():
    print()
    print("ALGORITHM INFORMATION")
    print()
    print("1. Selection Sort")
    print("2. Bubble Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Return to Main Menu")
    print()


def algorithm_info_menu():
    """
    Display explanations and pseudocode for the sorting algorithms.

    TODO:
        Complete the menu logic below if your instructor asks you
        to make changes or additions.
    """

    while True:

        print_info_menu()

        choice = input("Choice: ").strip()

        if choice == "1":
            print_selection_info()

        elif choice == "2":
            print_bubble_info()

        elif choice == "3":
            print_insertion_info()

        elif choice == "4":
            print_merge_info()

        elif choice == "5":
            print_quick_info()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please enter a number from 1 through 6.")


# ------------------------------------------------------------
# Menu
# ------------------------------------------------------------

def print_menu():
    print()
    print("SORTING VISUALIZER")
    print()
    print("1. Generate New Random List")
    print("2. Selection Sort")
    print("3. Bubble Sort")
    print("4. Insertion Sort")
    print("5. Merge Sort")
    print("6. Quick Sort")
    print("7. Algorithm Information / Pseudocode")
    print("8. Exit")
    print()


def main():

    # Interactive plotting allows the graph to update repeatedly.
    plt.ion()

    values = generate_list()

    while True:

        print()
        print("Current List:")
        print(values)

        print_menu()

        choice = input("Choice: ").strip()

        if choice == "1":
            values = generate_list()
            draw_list(values, "New Random List")

        elif choice == "2":
            working_list = values.copy()
            draw_list(working_list, "Selection Sort")
            selection_sort(working_list)
            print("Sorted List:")
            print(working_list)

        elif choice == "3":
            working_list = values.copy()
            draw_list(working_list, "Bubble Sort")
            bubble_sort(working_list)
            print("Sorted List:")
            print(working_list)

        elif choice == "4":
            working_list = values.copy()
            draw_list(working_list, "Insertion Sort")
            insertion_sort(working_list)
            print("Sorted List:")
            print(working_list)

        elif choice == "5":
            working_list = values.copy()
            draw_list(working_list, "Merge Sort")

            # You may need to modify this section depending on
            # how you implement merge_sort().
            result = merge_sort(working_list)

            if result is not None:
                working_list = result

            print("Sorted List:")
            print(working_list)

        elif choice == "6":
            working_list = values.copy()
            draw_list(working_list, "Quick Sort")

            result = quick_sort(working_list)

            if result is not None:
                working_list = result

            print("Sorted List:")
            print(working_list)

        elif choice == "7":
            algorithm_info_menu()

        elif choice == "8":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 through 8.")

    plt.ioff()
    plt.close()


if __name__ == "__main__":
    main()
