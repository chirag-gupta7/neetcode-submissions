class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for char in s.lower():
            if char.isalnum():
                cleaned.append(char)
        word = "".join(cleaned)
        return word == word[::-1]