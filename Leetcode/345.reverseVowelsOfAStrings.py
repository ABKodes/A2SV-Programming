class Solution:
    def reverseVowels(self, s: str) -> str:
        size = len(s)
        a = list(s)
        left = 0
        right = size - 1
        vowels = set("aeiouAEIOU") 
        
        while left < right:
            if a[left] in vowels and a[right] in vowels:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1
            elif a[left] not in vowels:
                left += 1
            elif a[right] not in vowels:
                right -= 1
        
        return ''.join(a)