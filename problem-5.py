#Problem 5: Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



def find_smallest_multiple():
    # create the divisor list but exclude 1 thru 10 - if integers are divisible by 11-20, they will be divisible by them as well
    divisors = [11,12,13,14,15,16,17,18,19,20]
    # starting multiple is 20 - must be at least this to be divisible by 20
    multiple = 20
    # set 'found' flag to False
    found = False

    while found == False:
        for div in divisors:
            # if the multiple is not divisible by the current divisor, add 20 to the multiple and break the divisor loop
            if multiple % div != 0:
                multiple += 20
                break
            # if the multiple is divisible by div, and div is the last item in the divisor list (20), set 'found' flag to true
            elif div == 20:
                found = True
    return multiple

print find_smallest_multiple()
