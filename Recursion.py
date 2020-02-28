# Recursion

# Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer

def rec_sum(n):
    
    # Base Case
    if n == 0:
        return 0
    
    # Recursion
    else:
        return n + rec_sum(n-1)
        
# Given an integer, create a function which returns the sum of all the individual digits in that integer. For example: if n = 4321, return 4+3+2+1        

def sum_func(n):
    # Base case
    if len(str(n)) == 1:
        return n
    
    # Recursion
    else:
        return n%10 + sum_func(n/10)
        
# Create a function called word_split() which takes in a string phrase and a set list_of_words. 
# The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. 
# You can assume the phrase will only contain words found in the dictionary if it is completely splittable.    

def word_split(phrase,list_of_words, output = None):
    
    # Checks to see if any output has been initiated.
    # If you default output=[], it would be overwritten for every recursion!
    if output is None:
        output = []
    
    # For every word in list
    for word in list_of_words:
        
        # If the current phrase begins with the word, we have a split point!
        if phrase.startswith(word):
            
            # Add the word to the output
            output.append(word)
            
            # Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
            # Remember to pass along the output and list of words
            return word_split(phrase[len(word):],list_of_words,output)
    
    # Finally return output if no phrase.startswith(word) returns True
    return output    