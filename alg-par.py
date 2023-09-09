
def find_missing_element(arr1:list,arr2:list):
    arr1.sort()
    arr2.sort()

    for l1 in range(len(arr2)):
        if arr1[l1] != arr2[l1]:
            print(str(arr1[l1]) + " is the missing number")
            return
    print(str(arr1[-1]) + " is the missing number")


ls_arr1 = [1,2,3,4,5,6,7,8]
ls_arr2 = [3,7,2,1,4,6,5]

find_missing_element(ls_arr1,ls_arr2)


def largest_count_sum(arr:list):
    current_sum = max_sum = arr[0]
    for numb in arr[1:]:
        current_sum = max(current_sum + numb, numb)
        max_sum = max(max_sum,current_sum)
    return max_sum
test_list =[-4,2,-1,5]
print(largest_count_sum(test_list))

count = 0


def check_mountain_array(arr: list):
    i = 1
    while i < len(arr) and arr[i - 1] > arr[i]:
        i += 1

    if i == 1 or i == len(arr):
        return False

    while len(arr) > i and arr[i - 1] < arr[i]:
        i += 1

    if i == len(arr):
        return True
    else:
        return False
arr_ls1 = [2,3,4,5,3,1]
print(check_mountain_array(arr_ls1))

def valid_Mountain(arr:list, n):
    left = 0
    right = n - 1
    while left < n - 1 and arr[left] < arr[left + 1]:
        left = left + 1

    while right > 0 and arr[right - 1] > arr[right]:
        right = right - 1

    if left > 0 and left == right and right < n - 1:
        return True
    else:
        return False

arr_ls = [2,3,4,5,3,1]
l = [2,3,4,6,6]
print(valid_Mountain(arr_ls,5))
print(valid_Mountain(l,5))

# Given an array arr[] of size N, the task is to find the maximum possible sum of i*arr[i] when the array can be rotated any number of times.
#
# Examples :
#
# Input: arr[] = {1, 20, 2, 10}
# Output: 72.We can get 72 by rotating array twice.
# {2, 10, 1, 20}
# 20*3 + 1*2 + 10*1 + 2*0 = 72
#
# Input: arr[] = {10, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# Output: 330
# We can get 330 by rotating array 9 times.
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
# 0*1 + 1*2 + 2*3 … 9*10 = 330


def max_sum_rotation(arr, n):
    # set the maximum sum to the
    # minimum possible value
    max_sum = float('-inf')

    # loop through all possible rotations
    for i in range(n):

        # set the current sum to zero
        sum = 0

        # loop through all elements in the array
        for j in range(n):
            # calculate the index of the current element after rotation
            index = (i + j) % n

            # add the product of the element with its index to the sum
            sum += j * arr[index]

        # update the maximum sum if necessary
        max_sum = max(max_sum, sum)

    # return the maximum sum obtained over all rotations
    return max_sum


# Test case
arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
print(max_sum_rotation(arr, n))

# def greater_neighbors(a):
#     g1 = []
#     acc = 0
#     for x in range(1, len(a) - 1):
#          if(a[x + 1] > a[x] < a[x - 1]):
#              acc += 1
#     return g1.append(acc)
# d = [2, 56, 7, 21, 22, 19, 26]
# print(greater_neighbors(d))
#     acc = 0
#     a = [int(s) for s in input().split()]
#     for x in range(1, len(a) - 1):
#         if(a[x] > a[x + 1] and a[x] < a[x - 1]):
#            acc += 1
#     print(acc)

# def peaks(lst):
#     num = 0
#     leni = len(lst)
#     print(leni)
#     for i in range(1, leni - 1):
#         if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
#             num = num + 1
#     for i in range(leni):
#         print(i)
#         if i == 0:
#             if lst[i] > lst[i + 1]:
#                 num = num + 1
#         elif i == leni + 1:
#             if lst[i] > lst[i - 1]:
#                 num = num + 1
#     return num
#
# d = [2, 56, 7, 21, 22, 19, 26]
# print(peaks(d))