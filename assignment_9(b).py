# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of
#  words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation 
# sequence from beginWord to endWord, or 0 if no such sequence exists.



from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])  # (current_word, steps)

        while queue:
            word, steps = queue.popleft()
            
            # If reached the end word
            if word == endWord:
                return steps

            # Try changing each letter
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in word_set:
                        queue.append((new_word, steps + 1))
                        word_set.remove(new_word)  # mark as visited

        return 0  
    
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(Solution().ladderLength(beginWord, endWord, wordList))

