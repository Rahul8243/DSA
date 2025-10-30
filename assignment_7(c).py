#Question 3:
# Given an array of integers nums and an integer k, return the total number of 
# subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array


from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  
        
        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in prefix_count:
                count += prefix_count[prefix_sum - k]
            prefix_count[prefix_sum] += 1
        
        return count


if __name__ == "__main__":
    nums = list(map(int, input("Enter array elements (space-separated): ").split()))
    k = int(input("Enter target sum k: "))
    
    sol = Solution()
    result = sol.subarraySum(nums, k)
    
    print("\n Total number of subarrays with sum =", k, "is:", result)
