''' NUmber of way to count up till a number N, given denominations'''


#Recusrsive solution
def count(S, n, m ):
    if n == 0: #only one solution exists do not include anything
        return 1
    if n < 0:
        return 0
    if m < 0 : #m < 0 for zero indexed programming languages
        return 0
 
    return count(S, n, m - 1 ) + count(S, n - S[m], m )

S=[1,5,10,25]
count(S,100,len(S)-1)



'''Dynamic Programming Solution '''
def changes(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in range(coin, amount + 1):
            ways[j]+= ways[j - coin]
    return ways[amount]
 
print changes(10, [1, 5, 10, 25])
#print changes(100000, [1, 5, 10, 25, 50, 100])
