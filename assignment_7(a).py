#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true


from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

if __name__ == "__main__":
    s = input("Enter string s: ")
    t = input("Enter string t: ")
    
    sol = Solution()
    result = sol.isAnagram(s, t)
    
    print("\n Are they anagrams?:", result)

