# Complexity: O(nlogn) in time because of sorting and O(1) space
def containsDuplicateBySort(nums):
    nums.sort()
    for i in range(len(nums) -1):
        if nums[i] == nums[i+1]:
            return True
    return False


# Complexity: O(n) time and O(n) space
def containsDuplicateByUsingSet(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(containsDuplicateBySort([1,2,3,1]))  # True
print(containsDuplicateBySort([1,2,3,4])) # False
print(containsDuplicateBySort([1,1,1,3,3,4,3,2,4,2])) # True

print(containsDuplicateByUsingSet([1,2,3,1])) # True
print(containsDuplicateByUsingSet([1,2,3,4])) # False
print(containsDuplicateByUsingSet([1,1,1,3,3,4,3,2,4,2])) #True


