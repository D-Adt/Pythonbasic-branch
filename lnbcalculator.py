number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))
operation = input('''
Please type in the math operation you would like to complete:
Basic (+, -, /, *)
Scietific (Sin, Cos, Tan, Cosec, Sec, Cot, pi, sqrt)
''')
import math



if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

elif operation =='sin':
    print(math.sin(number_1))
    print(math.sin(number_2))
    
elif operation == 'cos':
    print(math.cos(number_1))
    print(math.cos(number_2))

elif operation == 'tan':
    print(math.tan(number_1))
    print(math.tan(number_2))

elif operation == 'cosec':
    print(math.cosec(number_1))
    print(math.cosec(number_2))
    
elif operation == 'sec':
    print(math.sec(number_1))
    print(math.sec(number_2))

elif operation == 'cot':
    print(math.cot(number_1))
    print(math.cot(number_2))

elif operation == 'pi':
    print(math.pi)

elif operation == 'sqrt':
    print(math.sqrt(number_1))
    print(math.sqrt(number_2))

else:
    print('You have not typed a valid operator, please run the program again.')
