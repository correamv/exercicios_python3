"""
Shuffle the Array
"""
def shuffle(nums: list, n):
    """
    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

    Return the array in the form [x1,y1,x2,y2,...,xn,yn].
    :param nums: list of integers with length 2n
    :param n: limiter of elements in the array

    Ex.:

    >>> shuffle(nums = [2,5,1,3,4,7], n = 3)
    [2, 3, 5, 4, 1, 7]

    >>> shuffle(nums = [1,2,3,4,4,3,2,1], n = 4)
    [1, 4, 2, 3, 3, 2, 4, 1]

    """
    if 1< len(nums) > 500:
        return
    
    i = 0
    resultado = []
    while i < n:
        resultado.append(nums[i])
        resultado.append(nums[n+i])
        i+=1
    return resultado

if __name__ == '__main__':
    print(shuffle(nums=[1,2,4,5,7,5], n=3))
    print(shuffle(nums=[1,2,3,4,4,3,2,1], n = 4))
