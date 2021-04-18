'''
Using Lambda function to conver and process input to clean, lowercase string
Then using iteration to go over each ele and check for equality
Time complexity : O(n)
Space complexity : O(n)
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        
#         reversed_chars_list = filtered_chars_list[::-1]
#         return filtered_chars_list == reversed_chars_list

        for i in range(len(filtered_chars_list)//2):
            if filtered_chars_list[i]!=filtered_chars_list[-i-1]:
                return False    
        return True