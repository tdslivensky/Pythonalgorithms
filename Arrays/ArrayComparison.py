A = [5,5,7,7]
B = [6,7,7,7,5]

def finder(arr1,arr2):
    
    # Sort the arrays
    arr1.sort()
    arr2.sort()
    
    # Compare elements in the sorted arrays
    for num1, num2 in zip(arr1,arr2):
        if num1!= num2:
            return num1
    
    # Otherwise return last element
    return arr1[-1]

def finderL(a,b):
    L = {}
    final = []
    for num in a:
        if num in L:
            L[num] += 1
        else:
            L[num] = 1
    
    for num in b:
        if num in L:
            L[num] -= 1
        else:
            L[num] = 1
            
     
    for num in L:
        if L[num] != 0:
            final.append(num) 
    
    print(final)

import collections

def finder2(arr1, arr2): 
    
    # Using default dict to avoid key errors
    d=collections.defaultdict(int) 
    
    # Add a count for every instance in Array 1
    for num in arr2:
        d[num]+=1 
    
    # Check if num not in dictionary
    for num in arr1: 
        if d[num]==0: 
            return num 
        
        # Otherwise, subtract a count
        else: d[num]-=1 