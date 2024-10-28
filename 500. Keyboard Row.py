# # Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# # In the American keyboard:

# # the first row consists of the characters "qwertyuiop",
# # the second row consists of the characters "asdfghjkl", and
# # the third row consists of the characters "zxcvbnm".


# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# Example 2:

# Input: words = ["omk"]
# Output: []
# Example 3:

# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        valid_words = []
        for word in words:
            w = set(word.lower())
            if w <= line1 or w <= line2 or w <= line3:
                valid_words.append(word)
        return valid_words