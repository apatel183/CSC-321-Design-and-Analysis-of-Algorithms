##Arpan Patel##
##CSC321 Coin Change##
def dynamic_coin_change(denom, A):
    n = len(denom)
    C = [[0 for list in range (A+1)]
    for k in range(n)]
    for j in range (A+1):
       C[n-1][j] = j
    for i in range (n-2,-1,-1):
        for j1 in range(0, A+1):
            if (denom[i] > j1 or C[i+1][j1] < 1 + C[i][j1-denom[i]]):
                C[i][j1] = C[i +1][j1]
            else:
                C[i][j1] = 1 + C[i][j1-denom[i]]
    return C[0][A]


#let user input 
denom,A = eval(input("Please enter denominations and amount ex:([4,3,1], 6): "))
answer = dynamic_coin_change(denom,A)
print("Least number of coins needed to make change for that amount is ", answer)


#testing code
#print(dynamic_coin_change([4,3,1], 6)) # 2 
#print(dynamic_coin_change([50,25,10,5,1], 96)) # 5
#print(dynamic_coin_change([16,9,5,1], 36)) #4


