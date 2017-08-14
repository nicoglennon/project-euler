# Problem 2: Even Fibonacci numbers

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# MY SOLUTION

def even_fibonacci_sum(n):
    a = 0
    b = 1
    c = 0
    sum = 0

    while a + b < n:
        c = a + b
        a = b
        b = c
        if c % 2 == 0:
            sum = sum + c

    return sum

print(even_fibonacci_sum(4000000))
