'''
Provides a simple interface for a user to calculate math operations
for inputs. 

Notes:
	Currently only supports average, but more functionality
	will be supported in upcoming versions.
'''

def average(x, y):
	'''
	Returns the average of `x` and `y`.
	Argument: `x` an int or float
	Argument: `y` an int or float
	Returns: average of `x` and `y` as a float.
	'''
	return (x + y) / 2
	
	
def print_intro():
	'''
	Prints an introduction message for the math function program.
	'''
	print('Welcome to the math function program!')


def main():
	'''
	Introduces a user to the program and prompts them for two numbers,
	outputting the average.
	'''
	print_intro()
	print('Provide two numbers to calculate the average for.')
	x = float(input('Enter a number: '))
	y = float(input('Enter a number: '))
	if x > y: 
		print(f'{x} is greater than {y}')
	elif x < y:
		print(f'{y} is greater than {x}')
	print(f'Average of {x} and {y}: {average(x, y)}')


if __name__ == '__main__':
	main()
