#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) Why and under what conditions?
    Memory usage: O(1) Why and under what conditions?"""
    # Check that all adjacent items are in order, return early if so
    if len(items) == 0:
        return True

    prev = items[0]

    for item in items:
        if item < prev:
            return False
        prev = item
    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    

    while is_sorted(items) == False:
        left_index = 0
        right_index = 1

        while right_index <= len(items) - 1:

            if items[right_index] < items[left_index]:
                #swap
                left_var = items[left_index]
                items[left_index] = items[right_index]
                items[right_index] = left_var

            left_index += 1
            right_index += 1

    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    pointer_to_unsorted = 0
    sorted_list = []

    # loop through all the items
    # if item is less than our currently pointed unsorted item, compare it to the temporary shortest item we have - initialized as the currently pointed unsorted. 
    # if less, shortest_temp variable is now assigned to this item
    for item in items:
        shortest_temp = items[pointer_to_unsorted]
        if item < items[pointer]:
            if item < shortest_temp:
                shortest_temp = item
            pointer += 1


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items


if __name__ == "__main__":
    order = [1, 2, 3, 10, 40]
    messy = [8,3,9,4,2,40,2,80,43]

    print(is_sorted(order))
    print(is_sorted(messy))

    print(bubble_sort(messy))