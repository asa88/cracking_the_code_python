'''method to compute all permutations of a string of unique characters'''

def permutations(S):
    result=[""]
    for x in S:
        result.extend([x+item for item in result])     
    return result
s="abcd"
x=permutations(s)
