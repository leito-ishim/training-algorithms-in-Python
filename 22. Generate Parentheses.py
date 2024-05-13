# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



def generateParenthesis(n):
    def genRecursive(n, left, right, s):
        if len(s) == n * 2:
            res.append(s)
            return

        if left < n:
            genRecursive(n, left + 1, right, s + '(')

        if right < left:
            genRecursive(n, left, right + 1, s + ')')
    res = []
    genRecursive(n, 0, 0, '')
    return res


print(generateParenthesis(3))
print(generateParenthesis(1))
print(generateParenthesis(7))
print(generateParenthesis(8))
print(generateParenthesis(11))
