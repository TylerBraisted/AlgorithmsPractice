
'''
    Binary Search:
    Given an array of integers called nums which is sorted in ascending order, and an integer called target, write a function to search target in nums.
    If target exists, then return its index. Otherwise, return -1. Algorithm must have O(log n) runtime complexity

    Time:   O(log N), where N is the number of integers in the array
    Space: O(1), constant space

'''
def binarySearch(nums, target):
  first = 0
  last = len(nums) - 1
  
  while first <= last:
    middle = (first + last) // 2
    if nums[middle] == target:
      return middle
    elif nums[middle] < target:
      first = middle + 1
    else:
      last = middle - 1
  
  #Return -1 if target not found
  return -1 
