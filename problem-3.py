# Problem 3: Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# MY SOLUTION:

import math

def prime_factors(number):
  # define our return value largest_prime_factor
  largest_prime_factor = None

  # test if number divides by 2 (as many times as it does):
  while number % 2 == 0:
    largest_prime_factor = 2
    number = number/2

  # at this point, the number must be odd! try dividing it by every odd number from 3 to the square root of the number (as many times as it divides):
  odd_divisor = 3
  while odd_divisor <= number:
    # if it divides the number, set the prime_factor to the odd_divisor and divide the number by the odd_divisor:
    while number % odd_divisor == 0:
      number = number/odd_divisor
      largest_prime_factor = odd_divisor
    # once number does not divide by the odd_divisor anymore, move on to the next odd number:
    odd_divisor += 2
  # return the last (and thus largest) prime factor:
  return largest_prime_factor
