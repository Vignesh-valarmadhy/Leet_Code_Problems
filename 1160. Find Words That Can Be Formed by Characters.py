# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once).

# Return the sum of lengths of all good strings in words.

 

# Example 1:

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:

# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def can_form(word, chars):
            char_count = Counter(chars)
            for char in word:
                if char_count[char] <= 0:
                    return False
                char_count[char] -= 1
            return True
        result = 0
        for word in words:
            if can_form(word, chars):
                result += len(word)
        return result