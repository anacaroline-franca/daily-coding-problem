'''
[Product Array Puzzle]
Given an array of integers, return a new array such that each element at index i of the new array is 
the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''
#O(n) with division
def solution_1(a):
    result = []
    multiply_all = 1
    for num in a:
        multiply_all *= num
    
    for num in a:
        result.append(multiply_all/num)

    return result

#O(n) without division
def solution_2(a):
    left = [1] * (len(a)) #array to accumulate multiplication for elements on the left of index i
    right = [1] * (len(a)) #array to accumulate multiplication for elements on the right of index i
    result = []

    for i in range(1, len(a)):
        left[i] = a[i - 1] * left[i - 1]
    
    for i in range(len(a) - 2, -1, -1):
        right[i] = a[i + 1] * right[i + 1]

    for i in range(len(a)):
        result.append(left[i] * right[i])
    
    return result

a = [1, 2, 3, 4, 5]
print(solution_2(a))