#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n) where n is amount of numbers
    Memory usage: O(n) where n is amount of numbers"""
    # Find range of given numbers (minimum and maximum integer values)
    minimum = min(numbers)
    maximum  = max(numbers)

    # Create list of counts with a slot for each number in input range
    count_list = [0 for _ in range(minimum, maximum + 1)]


    # Loop over given numbers and increment each number's count
    for number in numbers:
        count_list[number - minimum] += 1 
    print(count_list)
    # Loop over counts and append that many numbers into output list
    output = []
    for index, count in enumerate(count_list):
        number = index + minimum
        if count > 0:
            output.extend([number] * count)
    return output

    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

numbers = [2,2,2,6,4,9,6,8,2,1,7,2]
print(counting_sort(numbers))