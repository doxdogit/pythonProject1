#STORING INPUT
"""name = input('Please enter your name:')
print('Hello', name)
print('Welcome to my program')
print('Remember this is fun, is not it?', name, '!')
"""
#CONCAT
"""name = input('Please enter your name:')
print('Hello' + name, end='')
print('This is my program')
print('Enjoy' + name + '!')
"""

#CAST
"""name = input('Please enter your name:')
print('This is my program, Enjoy it' + name)
num1 = input('Please enter a whole number: ')
num2 = input('Now enter another whole number: ')
print('input is:', type(num1), type(num2))
total = num1 + num2
print('Total:', total, type(total))
total = int(num1) + int(num2)
print('Total:', total, type(total))
total = float(num1) + float(num2)
print('Total: ' + str(total), type(total))
"""

#GUESS
"""import random

num = random.randint(1, 50)
flag = True
guess = 0
print('Guess a number 1-50: ', end='')

while flag == True:
    guess = input()
    if not guess.isdigit():
        print('Invalid! Enter only digit 1-50')
        break
    elif int(guess) < num:
            print('Too low, try again: ', end='')
    elif int (guess) > num:
            print('Too high, try again: ', end='')
    else:
        print('Correct.. my number is ' + guess)
        flag = False
"""

#Arithmentic
print('Learning Math \n')
name = input('What is your name: ')
print('This is an Easy Game to Learn Math,', name)
num1 = input('Enter a whole number: ')
num2 = input('Enter another whole number: ')
print('addition: \t', int(num1), '+', int(num2), '=', int(num1) + int(num2))
print('Subtraction:\t', int(num1), '-', int(num2), '=', int(num1) - int(num2))
print('Multiplication:\t', int(num1), '*', int(num2), '=', int(num1) * int(num2))
print('Division:\t', int(num1), '/', int(num2), '=', int(num1) / int(num2))
print('Floor Division:\t', int(num1), '/', int(num2), '=', int(num1) // int(num2))
print('Remainder:\t', int(num1), '%', int(num2), '=', int(num1) % int(num2))
print('Exponent:\t', int(num1), '**', int(num2), '=', int(num1) ** int(num2))
