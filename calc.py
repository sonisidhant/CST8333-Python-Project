######################
# calc.py
# By Sidhant Soni
# October 24, 2018
######################

# Declaring variables and assigning user input
a = input('Enter First Number: ');
b = input('Enter Second Number: ');

print('\n')

# Converting user input string to integer
firstN = int(a);
secondN = int(b);

# Making the list of two numbers using user input
numbers = [firstN,secondN];

# Defining a test case


def arthDivide(c,d):
    return c / d;

def add(c,d):
    return c + d;
# Function for operating arithmetic operation



def arithmetic():
    Sub = numbers[0] - numbers[1];
    Add = numbers[0] + numbers[1];
    modulus = numbers[0] % numbers[1];
    multiply = numbers[0] * numbers[1];

    print('Result of a-b = ', Sub);
    print('Result of a+b = ', Add);
    print('Result of a%b = ', modulus);
    print('Result of a/b = ', multiply, '\n');

# Function for operating comparison operation


def comparison():

    if numbers[0] == numbers[1]:
        print('number a and b are equal');
    else:
        print('Number a and b are not equal');

    if numbers[0] > numbers[1]:
        print('Number a is greater than b');
    else:
        print('Number a is smaller than b');

# Function for operating logic operation


def logic():
    if numbers[0] >= 10 and numbers[1] >=5:
        print('True')
    else:
        print('False')

    if numbers[0] > 10 or numbers[1] >= 5:
        print('True')
    else:
        print('False')

# Function for operating decision structure operation


def decisionStructure():
    age = int(input('Enter your age: '))

    if age >= 18:
        print('You are eligible for driving');
    else:
        print('Your age is less than 18. So, you are not eligible for driving.');

# Function for operating repetition structure operation


def repetitionStructure():
    firstNumber = int(input('Enter the number to start printing: '));
    secondNumber = int(input('Enter the number to finish printing: '))

    while(firstNumber<secondNumber):
        print('The number is: ', firstNumber);
        firstNumber += 1;

# Running all the functions


repetitionStructure();
arithmetic();
comparison();
logic();
decisionStructure();
