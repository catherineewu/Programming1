def vertical_numbers(n):
    index = 1
    while 10 > n > 0:
        print(index)
        n = n - 1
        index += 1
    return n


def write_vertical(n):
    if n < 10:
        print(n)
        return

    write_vertical(n // 10)
    print(n % 10)


def factorial(n):
    # Base case: n = 0, factorial(0) = 1
    # Recurrence relations: factorial(n) = n * factorial(n - 1)
    if n == 0:  # Conditions to STOP recursion
        return 1  # Final return value

    return n * factorial(n - 1)  # Recurrence relation


def is_palindrome(word):
    # Base case: ''
    # Recurrence relations: is_palindrome(abba) = is_palindrome(bb)
    if len(word) == 0 or len(word) == 1:  # Stop recursion condition
        return True  # Innermost return value

    if word[0] == word[-1]:  # Checks that first and last letters of word are same
        return is_palindrome(word[1:len(word) - 1])
    return False


def add_num_list(nums):
    """su = add_num_list([3, 6, 17, 2, -4, 0, 1]), print(su), 25"""
    if len(nums) == 1:
        return nums[0]
    else:
        return add_num_list(nums[1:]) + nums[0]


def sum_recursion_list(rlist):
    # test rlist: [1, 2, [3,4], [5,6]], answer: 21
    if len(rlist) == 1:
        if isinstance(rlist[0], int):
            return rlist[0]
        elif len(rlist[0]) == 1:
            return rlist[0][0]
    if isinstance(rlist[0], int):
        return sum_recursion_list(rlist[1:]) + rlist[0]
    elif len(rlist[0]) == 1:
        return sum_recursion_list(rlist[1:]) + rlist[0][0]
    else:
        store = rlist[0][0]
        del rlist[0][0]
        return sum_recursion_list(rlist) + store


def fibonacci_sequence(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)


def sum_digits(n):
    if n // 10 == 0:
        return n
    else:
        return sum_digits(n // 10) + n % 10


# Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
def sum_minus_two(n):
    if n - 2 <= 0:
        return n
    else:
        return n + sum_minus_two(n-2)


# Power of a to b
def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power(a, b - 1)


# Greatest common divisor of 2 integers
def gcd(a, b):
    low = min(a, b)
    high = max(a, b)

    if low == 0:
        return high
    if low == 1:
        return 1
    else:
        return gcd(low, high % low)


# print(fibonacci_sequence(7))
# print(sum_digits(456))
# print(sum_minus_two(10))
# print(gcd(12, 14))
