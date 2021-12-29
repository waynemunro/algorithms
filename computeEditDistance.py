# Compute Edit Distance
def computeEditDistance(s,t):
    def recurse(m, n):
        """
        return the minimum edit distance betewwn:
        - first m letters of s
        - first n letters of t
        """
        if m == 0:
            return n
        if n == 0:
            return m
        if s[m-1] == t[n-1]: # if last letters are the same
            return recurse(m-1, n-1)
        else:
            subCost = 1 + recurse(m-1, n-1)
            insCost = 1 + recurse(m, n-1)
            delCost = 1 + recurse(m-1, n)
            return min(subCost, insCost, delCost)
        # return 1 + min(recurse(m, n-1), recurse(m-1, n), recurse(m-1, n-1))
    return recurse(len(s), len(t))

print(computeEditDistance("kitten", "sitting"))
print(computeEditDistance("kitten", "kitten"))
print(computeEditDistance("a cat!", "the cats!"))
print(computeEditDistance("a cat!", "a cats!"))

