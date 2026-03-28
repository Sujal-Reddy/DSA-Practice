# Problem: Two Sum
# Platform: LeetCode
# Approach: HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSum(nums, target):
    prevMap = {}

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in prevMap:
            return [prevMap[diff], i]

        prevMap[nums[i]] = i

    return []


# Example run
nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))

# Explanation:
# We use a hashmap to store numbers we have seen.
# For each number, we check if (target - number) exists in the hashmap.
# If yes, we found the pair.