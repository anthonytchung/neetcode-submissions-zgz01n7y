class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        string = ""
        for char in s:
            if char.isalnum():
                string = string + char

        return string == string[::-1]