
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

# def sum_and_mult(arr: list):
#
#     sum_result = 0
#     mult_result = 1
#     for number in arr:
#         sum_result += number
#         mult_result *= number
#     return sum_result, mult_result
# d = [2, 56, 7, 21, 22, 19, 26]
# print(sum_and_mult(d))

# Max item and index: solution

#
# # Best time to buy and sell stock: solution
# def buy_and_sell_stock(prices: list):
#     max_profit = curr_profit = 0
#     for i in range(len(prices) - 1):
#         curr_profit = curr_profit + prices[i+1] - prices[i]
#         if curr_profit > max_profit:
#             max_profit = curr_profit
#         if curr_profit < 0:
#             curr_profit = 0
#     return max_profit
def sum_between_range(arr, min_val, max_val):
    total_sum = 0
    for num in arr:
        if min_val <= num <= max_val:
            total_sum += num
    return total_sum

my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_value = 3
max_value = 7


print(sum_between_range(my_array,min_value,max_value))


def increment_digits(digits):
    carry = 1  # Initialize carry to 1 to add 1 to the least significant digit
    n = len(digits)

    for i in range(n - 1, -1, -1):
        total = digits[i] + carry
        digits[i] = total % 10  # Update the current digit
        carry = total // 10  # Calculate the carry for the next iteration

    # If there is still a carry left after the loop, insert it as the new most significant digit
    if carry:
        digits.insert(0, carry)

# Example usage:
input_digits = [1, 2, 9]
increment_digits(input_digits)
print(input_digits)  # Output will be [1, 3, 0]
# This program starts by initializing a carry of 1 and then iterates through the list of digits from right to left. It adds the carry to the current digit, updates the current digit to the remainder of the sum, and calculates the carry for the next iteration. If there's still a carry left after the loop, it is inserted as the new most significant digit.
#
# This approach allows you to update the list to represent the integer D + 1.


def plus_one(digits):
    # Add 1 to the last digit
    digits[-1] += 1

    # Loop through the digits in reverse order
    for i in range(len(digits) - 1, 0, -1):
        # Check for carry-over
        if digits[i] == 10:
            digits[i] = 0
            digits[i - 1] += 1
        else:
            break  # No more carry-over, exit the loop

    # Special case: If the first digit is 10, change it to 1 and add a 0 at the end
    if digits[0] == 10:
        digits[0] = 1
        digits.append(0)

# Example usage:
input_digits = [1, 2, 9]
plus_one(input_digits)
print(input_digits)  # Output will be [1, 3, 0]
# This program follows the steps you outlined:
#
# It starts by adding 1 to the last digit.
# Then, it iterates through the digits in reverse, checking for carry-over (when a digit becomes 10). If there's a carry-over, it sets the current digit to 0 and adds 1 to the previous digit.
# It continues this process until there are no more carry-overs or until it reaches the most significant digit.
# Finally, if the first digit is 10 after the loop, it changes it to 1 and appends a 0 at the end.
# This program will correctly update the list to represent the integer D + 1.
adj = ["red","ripe","tasty"]
fruits = ["apple","banana","cherry"]

for i in adj:
    for j in fruits:
        print(i + ' ' + j)


def sort_list(arr:list):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

test_data = [4,2,1,7,5,3]

print(sort_list(test_data))

def bubble_sort_list(arr:list):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 -i ):
            if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[i]
    return arr

print(bubble_sort_list(test_data))

