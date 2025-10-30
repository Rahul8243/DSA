# Question 2:
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target. 

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []  

if __name__ == "__main__":
    nums = list(map(int, input("Enter array elements (space-separated): ").split()))
    target = int(input("Enter target value: "))
    
    sol = Solution()
    result = sol.twoSum(nums, target)
    
    print("\n Indices of numbers that add up to target:")
    print(result)

