'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

def exists_complement(numbers_list, k):
    for number in numbers_list:
        complement = k - number
        if (complement in numbers_list):
            return True
    return False

numbers_list = [10, 15, 3, 7]
k = 17

print(exists_complement(numbers_list, k))