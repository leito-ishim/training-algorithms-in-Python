# Given an integer x, return true if x is a palindrome, and false otherwise.

def is_palindrome(x):
    x = str(x)
    for i in range(0, len(x) // 2):
        if x[i] != x[len(x) - 1 - i]:
            return False
    return True


print(is_palindrome(121))
print(is_palindrome(-212))
print(is_palindrome(10))
