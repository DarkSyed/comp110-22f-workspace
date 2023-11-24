# EX04 - Function Lists Man

__author__ = "730720671"

"""Ex 04, Functions, Etc."""

def all(nums: list, target: int) -> bool:
    """All Function"""
    # Checks to see if the list is empty, otherwise false
    if not nums:
        return False
    # Indexes through :)
    i = 0
    # while loop within function to iterate through nums
    while i < len(nums):
        if nums[i] != target:
            return False 
        i += 1
    # Returns bool, if matched correct otherwise false as shown within the while loop
    return True

def max(input: list[int]) -> int:
    """the max function"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    # first element of list
    max_val = input[0]

    # uses while loop to find the max value
    x = 1
    while x < len(input):
        if input[x] > max_val:
            max_val = input[x]
        x += 1
    return max_val

def is_equal(first_list: list[int], second_list: list[int]) -> bool: 
    """Is equal function """ 
    checker = True
    # Check if the lists are different
    if len(first_list) != len(second_list):
        return False
    # While loop to iterate through both lists
    
    j = 0
    # counter

    while j < len(first_list):
        if first_list[j] != second_list[j]:
            return False
        j += 1
    #is returning true IF every element at every index is equal in both lists.
    return checker