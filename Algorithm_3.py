# Task 1.
# Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.

arr1 = [198, 3, 4, 9, 10, 9, 2]

def find_two_lowest(arr):
    list = []
    if len(set(arr)) == 1:
        return [-1, -1]

    list.append(min(arr))
    smallest_arr = min(arr)
    count_of_sm = arr.count(smallest_arr)
    for i in range(count_of_sm):
        arr.remove(smallest_arr)
    list.append(min(arr))
    return list

arr = [198, 3, 4, 9, 10, 9, 2]
print(find_two_lowest(arr))


# Task 2
# Given a list of numbers, return the inverse of each. Each positive becomes a negative,
# and the negatives become positives.

def invert_list(arr: list):

    list1 = []
    for i in arr:
        invert_number = i * -1
        list1.append(invert_number)
    return list1

num_list = [1, 5, -2, 4]

print(invert_list(num_list))

# Task 3
# Implement a function that returns the difference between the largest and the smallest value in a given list.
# The list contains positive and negative numbers. All elements are unique.

def max_diff(arr: list):
    if len(arr) == 0:
        return 0
    arr.sort()
    diff_arr = arr[-1] - arr[0]
    return diff_arr

d_list = [3, 5, 7, 2]
print(max_diff(d_list))

# Task 4
# Write a function that counts the number of elements in a given list larger than their adjacent neighbors.#

def count_larger_neighbors(arr: list):
    emt_list = []
    count = 0
    for i in range(1, len(arr) - 1):
        if (arr[i]) > (arr[i - 1]) and (arr[i]) > (arr[i + 1]):
             n1 = arr[i]
        elif (arr[i - 1]) > (arr[i]) and (arr[i -1]) > (arr[i + 1]):
             n1 = arr[i - 1]
        else:
            n1 = arr[i + 1]
        count += 1
        emt_list.append(n1)
    return (count, emt_list)
cnl = [2, 56, 7, 21, 22, 19, 26]
print(count_larger_neighbors(cnl))


# Task 5
# Given an array. Find the minimum element in the list and subtract it from each element in the array.

def subtract_min(arr: list):
    min_element = min(arr)
    new_list =[]
    for sm in arr:
        n = sm - min_element
        new_list.append(n)
    return new_list
sl1 = [9, 2, 5, 4, 7, 6, 1]
print(subtract_min(sl1))