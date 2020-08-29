"""
Running Sum of 1d Array

"""


def running_sum(nums: list):
    """
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.
    :param nums: list of integers
    :return:

    Ex.:

    >>> running_sum([1,2,3,4])
    [1, 3, 6, 10]

    >>> running_sum([4,5,6,9,10,11])
    [4, 9, 15, 24, 34, 45]
    """
    if len(nums) > 1000 or len(nums) < 1:
        return
    
    resultado = [nums[0]]
    for n in range(1, len(nums)):
        resultado.append(nums[n] + resultado[n-1])
    return resultado

if __name__ == '__main__':
    print(running_sum([1,2,3,4]))
    print(running_sum([1,1,1,1]))
