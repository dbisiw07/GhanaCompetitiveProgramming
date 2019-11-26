#Steps:
# There are many ways to solve this:
#The key to the solution is to realise that for every number X in the array, you are essentially trying to find
# a corresponding number Y such that X + Y = target.

# O(n) time and O(n) space

def two_number_sum(numbers, target):
    seen = set() # use a set or a map for a constant lookup
    for num in numbers:
        potential_match = target - num
        if potential_match in seen:
            return [num, potential_match]
        else:
            seen.add(num)
    return [] # return empty if you reach here without finding numbers that sum to target

# An alternative solution that has O(nlogn) time and O(1) space by doing away with the temporary storage
#Steps
# 1. Sort the input array
# 2. have two pointers left and right to point to the beginning and end of the array
# 3. while left < right:
#      find the sum of the numbers pointed by left and right and call it say current_sum
#      if the current_sum calculated above is equal to the target, then you are done, just return numbers pointed by left and right
#      else if the current_sum is less than target, then it means you are aiming at increasing your next current sum and since you
#       sorted the array, move the left pointer by 1
#      Similarly if the current_sum is greater than the target, decrease the right by 1 to aim at getting a lesser next current sum
#      Note that you are taking advantage of the fact that you sorted the array first

def two_number_sum(numbers, target):
    left, right = 0, len(numbers) -1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [numbers[left], numbers[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
