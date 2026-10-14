"""
Source: TheAlgorithms/Python
Repository: https://github.com/TheAlgorithms/Python
"""

"""
The merge sort algorithm.

For doctests, run the following command:
python -m doctest -v merge_sort.py
or
python3 -m doctest -v merge_sort.py
For manual testing, run:
python merge_sort.py
"""

from typing import Protocol


class Comparable(Protocol):
    def __lt__(self, other: object, /) -> bool: ...


def merge[T: Comparable](left: list[T], right: list[T]) -> list[T]:
    """
    Merge two sorted lists into a single sorted list.

    :param left: Left collection
    :param right: Right collection
    :return: Merged result
    """
    result: list[T] = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if right[j] < left[i]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort[T: Comparable](collection: list[T]) -> list[T]:
    """
    Sorts a list using the merge sort algorithm.

    :param collection: A collection with comparable items.
    :return: The collection ordered in ascending order.

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> merge_sort([])
    []

    >>> merge_sort([-2, -45, -5])
    [-45, -5, -2]
    """

    if len(collection) <= 1:
        return collection
    mid_index = len(collection) // 2
    return merge(merge_sort(collection[:mid_index]), merge_sort(collection[mid_index:]))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    try:
        user_input = input("Enter numbers separated by a comma:\n").strip()
        unsorted = [int(item) for item in user_input.split(",")]
        sorted_list = merge_sort(unsorted)
        print(*sorted_list, sep=",")
    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")
