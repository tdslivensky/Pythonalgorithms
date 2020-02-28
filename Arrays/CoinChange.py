# solution 1 Classic recursion

def classicRecursion(target, coins):
    #target is the value we are adding up to and coins is our change
    # ie (10,[1,5,10])
    # we want to return the min number of coins to get to 10 
    
    #default minimum of coins
    minimumCoins = target
    
    #Base case
    if target in coins:
        return 1
    else:
    #recursive call
    # For every coin in coins that is less that the target
        for i in [c for c in coins if c <= target]:
            
            #add a coin to a counter and run the funciton on target - i
            numberOfCoins = 1 + classicRecursion(target-i,coins)
            
            # if the counter is less that the default min 
            # then you have a lower change count
            if numberOfCoins < minimumCoins:
                minimumCoins = numberOfCoins
    return minimumCoins  

# This solution is problematic for two reason
# 1. it only works for US change ie. change with 1,5,10 etc. 
# 2. it is slow becuase you are recalculating values 
# this is an indication memoization is needed


# Solution 2 Memoization 

target = 45
coins = [1,5,10,25]
Known = [0] * (target+1)

def memoRecursion (target, coins, knownResults):
    # target is the value we are adding up to ie (10)
    # coins is our change ie ([1,5,10])
    # knownResults is the values we have already computed 
    # we want to return the min number of coins to get to 10 
    
   #default the output to target
    minimumCoins = target
    
    # Base case
    if target in coins:
        knownResults[target] = 1
        return 1
    # if we have already computed the value of a call of this function
    # and have stored it. return that value. 
    elif knownResults[target] > 0:
        return knownResults[target]
    else:
        #new values
        for i in [c for c in coins if c <= target]:
            # create a recursive call that includes know results 
            numberOfCoins = 1 + memoRecursion(target-i,coins,knownResults)
            
            # if the counter is less that the default min 
            # then you have a lower change count
            if numberOfCoins < minimumCoins:
                minimumCoins = numberOfCoins
                knownResults[target] = minimumCoins

    return minimumCoins