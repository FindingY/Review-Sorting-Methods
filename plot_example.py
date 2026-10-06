"""
Simple Matplotlib Sorting Visualization Example

This file demonstrates how a list of numbers can be displayed
as a bar graph and updated repeatedly.

It does NOT implement one of the sorting algorithms from the lab.
"""

import time
import matplotlib.pyplot as plt


def draw_list(values, title="List Visualization"):
    """
    Display the current list as a bar graph.
    """

    plt.clf()

    plt.bar(range(len(values)), values)

    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")

    plt.pause(0.25)


def main():

    # Turn on interactive plotting.
    plt.ion()

    values = [8, 3, 6, 1, 7, 4, 2, 5]

    draw_list(values, "Original List")

    # Pause briefly so the original arrangement can be seen.
    time.sleep(1)

    # This loop is ONLY a visualization example.
    #
    # Each pass swaps one pair of neighboring values.
    # The point is to show how changing the list and then
    # calling draw_list() updates the graph.

    for i in range(len(values) - 1):

        values[i], values[i + 1] = values[i + 1], values[i]

        draw_list(values, "Updating the List")

    # Leave the final graph visible.
    plt.ioff()
    plt.show()


if __name__ == "__main__":
    main()
