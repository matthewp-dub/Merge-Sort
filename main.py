# Merge sort recursive function
def merge_sort(array):
    if len(array) > 1:

        # Splits the list into two halves
        mid = len(array) // 2
        left = array[mid:]
        right = array[:mid]

        # The recursion
        merge_sort(left)
        merge_sort(right)

        # Counters for iterating through the two lists and original list
        left_it = 0
        right_it = 0
        main_it = 0

        # The actual sorting algorithm
        while left_it < len(left) and right_it < len(right):
            if left[left_it] < right[right_it]:
                array[main_it] = left[left_it]
                left_it += 1
            else:
                array[main_it] = right[right_it]
                right_it += 1
            main_it += 1

        while left_it < len(left):
            array[main_it] = left[left_it]
            left_it += 1
            main_it += 1

        while right_it < len(right):
            array[main_it] = right[right_it]
            right_it += 1
            main_it += 1


if __name__ == "__main__":
    # Enter list here
    sample_list = [5, 4, 2, 1, 3, 95959595]
    merge_sort(sample_list)
    print(sample_list)
