# Problem 4: Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


# method to reverse a string
def reversed_string(string):
    return string[::-1]

# method to check if a number is a palindrome
def palindrome(number):
    if str(number) == reversed_string(str(number)):
        return True
    else:
        return False

# method to find the largest palindrome product, given number of digits of the multiplicand and multiplier
def largest_palindrome_product(number_of_digits):
    # create the starting_num, the largest number given the number_of_digits
    starting_num = int('9' * number_of_digits)

    #set the return value, largest_palindrome, to None
    largest_palindrome = None

    # set the outer index i to the starting_num
    i = starting_num
    while i > 1:
        # set the inner index j to i (to avoid repetition, this number decreases with i)
        j= i
        while j > 1:
            prod = i * j
            # efficiency: if at any point the product is less than or eq to the current largest_palindrome, drop the current loop
            if prod <= largest_palindrome:
                break
            # if product is greater than current largest_palindrome, check if it is a palindrome and set it to largest_palidrome if it is
            elif palindrome(prod):
                largest_palindrome = prod
            j -= 1
        i -= 1
    return largest_palindrome

# return result for 3-digit multiplicand and multiplier
print largest_palindrome_product(3)
