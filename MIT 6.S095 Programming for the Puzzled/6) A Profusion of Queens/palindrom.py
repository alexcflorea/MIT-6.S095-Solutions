def isPalindrome(word):
    """
    word (string): word to test if palindrome
    """
    word = word.lower()
    start = word[0]
    end = word[-1]
    
    if len(word) <= 1: return True
    
    else:
        return start == end and isPalindrome(word[1:-1])

print(isPalindrome('kayaK'))
print(isPalindrome('kayaKs'))