#Calculator w/ 4 functions in variables

is_exit = False

# addition, subtraction, multiplication, divition.
def add(a, b):
	return a + b

def sub(a, b):
	return a - b

def mul(a, b):
	return a * b

def div(a, b):
	return a / b


# while loop of the calculator.
while is_exit == False:

	user_input = input('Choose (add, sub, mul, div: ) and type (exit) to exit program: ')

	if user_input == 'exit':
		print('exiting program...')
		break

	first_Input = int(input('Enter first Value: '))
	second_Input = int(input('Enter Second Value: '))



	if user_input == 'add':
		total = add(first_Input, second_Input)
		print(total)

	elif user_input == 'sub':
		loss = sub(first_Input, second_Input)
		print(loss)

	elif user_input == 'mul':
		com = mul(first_Input, second_Input)
		print(com)

	elif user_input == 'div':
		diff = div(first_Input, second_Input)
		print(diff)

	else:
		print('invalid')