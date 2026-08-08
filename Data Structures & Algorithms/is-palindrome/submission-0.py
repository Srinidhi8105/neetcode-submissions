class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for char in s:
            if char.isalnum():
                word+=char.lower()

        n=len(word)
        i=0
        j=n-1

        while(i<j):
            if(word[i]==word[j]):
                i+=1
                j-=1
            else:
                return False
        return True