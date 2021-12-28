# In this example we are getting an array of numbers and a target value
# and we have to find two numbers in the array that sum up we get the
# target value or return empty array

# First way is to implament two for loops O(n^2) time | O(1) space
def twoNumSum(array, targetSum):
    for i in range(len(array - 1)):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

# Second way is to use hash table, first we itarate through the array
# then we get the target and subtract the current number, if the result
# is in the hash table we return it: target - num in hash
# O(n) time | O(n) space
def twoNumSum(array, targetSum):
    nums = {}
    for num in array:
        if targetSum - num in nums:
            return [targetSum - num, num]
        else:
            nums[targetSum] = True

    return []

# The last algorithm is to use left and right pointer and checking if
# left + right = sum, if sum is greather then target then right - 1
# or if sum is less then target then left + 1
# O(nlog(n)) time | O(1) space
def twoNumSum(array, targetSum):
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]

        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []






