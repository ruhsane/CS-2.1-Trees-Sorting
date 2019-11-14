#!python
import random


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is emptys
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list

    pointer = 0
    second_pointer = 0
    merged = []

    while items1 and items2:
        if items1[pointer] < items2[second_pointer]:
            merged.append(items1[pointer])
            pointer += 1
            if pointer == len(items1):
                merged += items2[second_pointer:]
                break

        else:
            merged.append(items2[second_pointer])
            second_pointer += 1
            if second_pointer == len(items2):
                merged += items1[pointer:]
                break

    return merged

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order

    middle = len(items) // 2                    # O(1)
    first_half_sort = sorted(items[:middle])    # O(n/2) for splitting + O(nlogn) for sorting
    last_half_sort = sorted(items[middle:])     # O(n/2) + O(nlogn)
                                                # total: O(nlogn)

    print(first_half_sort)
    print(last_half_sort)

    print(merge(first_half_sort, last_half_sort))

    # return merge(first_half_sort, last_half_sort)
    for i, item in enumerate(merge(first_half_sort, last_half_sort)):
        items[i] = item
    

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order

    if len(items) == 0 or len(items) == 1:
        return items

    middle = len(items) // 2
    first_half_sort = merge_sort(items[:middle])
    last_half_sort = merge_sort(items[middle:])

    # return merge(first_half_sort, last_half_sort)
    sorted_items = merge(first_half_sort, last_half_sort)
    # for i, item in enumerate(merge(first_half_sort, last_half_sort)):
    #     items[i] = item
    items[:] = sorted_items

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    
    pivot = items[low]
    pivot_index = low

    for i in range(low+1, high+1):
        if items[i] < pivot:
            items.insert(low, items.pop(i))
            pivot_index += 1

    # mid = (low + high) // 2
    # l = list(sorted([items[low], items[mid], items[high]]))
    # pivot = l[1]

    # if pivot == items[low]:
    #     pivot_index = low
    # elif pivot == items[high]:
    #     pivot_index = high
    # elif pivot == items[mid]:
    #     pivot_index = mid

    # for index in range(low, high+1):
    #     print(index)
    #     print(items)
    #     if items[index] <= pivot:
            
    #         if index > pivot_index:
    #             items.insert(low, items.pop(index))
    #             pivot_index += 1

    #     else:

    #         if index < pivot_index:
    #             items.insert(high, items.pop(index))
    #             pivot_index -= 1

    print(items)
    return pivot_index


def quick_sort(items, left_pointer=None, right_pointer=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    if len(items) == 0 or len(items) == 1:
        return

    if left_pointer == None and right_pointer == None:
        left_pointer = 0
        right_pointer = len(items) -1

    if left_pointer >= right_pointer:
        return items

    pivot_index = partition(items, left_pointer, right_pointer)
    quick_sort(items, left_pointer, pivot_index)
    quick_sort(items, pivot_index + 1, right_pointer)
    return items


if __name__ == "__main__":
    # print(merge([0,1,5,7,20],[2,3,4,10]))

    # print(split_sort_merge([1,8,2,6,3]))
    # print(partition([1,8,2,6,3],0,2))
    print(quick_sort([1,8,2,2,6,3,0,5],0,7))