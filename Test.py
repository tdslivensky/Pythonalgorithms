# clear the screen
import os 
import NamerModule
os.system('cls')

firstName = 'Tim'

# print stuff
print (firstName + ", Hello World!")

#data types
string = 'this is a string'
number = 9
lists = [9,12,'Tim']
tuples = (9,12) # immutable and used with parentheses 
dictionary = {} # also called hashes in other languages.

dictionary['Key'] = 'Value'

#strings 

talking = 'I said "need to clean my room"'
talking2= 'I said \'need to clean my room\''
# note: \n for new line print  \ for escape

aString = "my name is Tim S."

print (aString.capitalize())
print (aString.title())

print(NamerModule.namer('Tim'))
print(NamerModule.fizzBuzz(15))

# classes 