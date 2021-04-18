class Solution:
    def isPalindrome(self, s: str) -> bool:
        punctuations = '''!()-[]{};:' "\`,<>./?@#$%^&*_~'''
        
        no_punct = ""
        for char in s:
            if char not in punctuations:
                char = char.lower()
                no_punct = no_punct + char
        print(no_punct)
        for i in range(len(no_punct)//2):
            if no_punct[i]!=no_punct[-i-1]:
                return False    
        return True
        