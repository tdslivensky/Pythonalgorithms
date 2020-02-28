def namer(name):
	return ('Hello {0}!'.format(name))
	

def fizzBuzz(range = 50):	
	i = 1
	result = []

	while i <= range:
		if i%3 == 0 and i%5 == 0:
			result.append('FizzBuzz')
		elif i%5 == 0:
			result.append('Buzz')
		elif i%3 == 0:
			result.append('Fizz')
		else:
			result.append(i)
		
		i += 1	
	
	return result	
		

	