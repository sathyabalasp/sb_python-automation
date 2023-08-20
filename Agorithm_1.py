# Task 1. There is a program that prints the numbers from 1 to 100.
# If the number is divisible of 3, print “Bin”
# If the number is divisible of 7, print “Go”
# For numbers which are divisible of 3 and 7, print “BinGo”

def bingo(n):
    for i in range(1, n + 1 ):
         if i % 3 == 0 and i % 7 == 0:
             print('BinGO')
         elif i % 3 == 0:
             print('Bin')
         elif i % 7 == 0:
             print('Go')
         else:
             print(i)

print(bingo(100))

# Task 2. Compute the sum of digits in all numbers from 1 to n. When a function gets a number n,
# find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

def sum_of_digits(n):
    final_sum = 0
    for a in range(0, n + 1 ):  # 0(a),1(b),2(c),3(d),4(e),5(f)
        final_sum = final_sum + a  #  +=  # 0+ 0(a)  =0 , 0+1(b) =1  , 1+2(c) =3  , 3+3(d) = 6 , 6+4(e) = 10 , 10+5(F) =15
    return final_sum
print('sum of the digits:',sum_of_digits(5))

# Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.

def find_max(a: int, b: int, c: int):

    if a < b and c < b:
        max = b
    elif b < a and c < a:
        max  = a
    elif b < c and a < c:
        max = c
    else:
        max = 0
    return max

print(find_max(124, 21, 32))

# 2. Leap year. When a function gets a year, the code detects if it is a leap year or not.
#
# How to approach this task
# A leap year is exactly divisible by 4
# If it’s a century year (divisible by 100), it is a leap year if it’s also divisible by 400.
# If it’s divisible by 100 and not divisible by 400, it’s not a leap year.


def leap_year(year: int):

    if year % 4 > 0:
        year_leap = False
    elif year % 100 == 0 and year % 400 > 0:
        year_leap = False
    else:
        year_leap = True
    return year_leap

print(leap_year(2024))

# Fibonacci. The Fibonacci sequence is a series of numbers where each number is the
# sum of the two preceding ones. Print out the Fibonacci sequence until the given n-th in the sequence.
# Example: n = 7, print out the sequence: 0, 1, 1, 2, 3, 5, 8

def fibonacci_sequence(n):

    fib_sequence = [0, 1]

    for i in range(2, n):
        fib_s = fib_sequence[i - 2] + fib_sequence[i - 1]
        fib_sequence.append(fib_s)
    return fib_sequence

print(fibonacci_sequence(7))







