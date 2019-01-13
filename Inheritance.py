####################
# File: Inheritance.py
# Created By: Sidhant Soni
# Date: 27-10-2018
####################

class A():
    """This is classA used for reading and printing name"""

    def __init__(self):
        """The constructor of the classA"""
        print("Class A running")

    def featureA(self):
        """The method featureA which takes the input as a name from the user and prints the name to the console"""
        name = input("Enter Your Name: ")
        print("Your name is " + name)


class B(A):
    """This is classB which inheritance the feature of classA"""

    def __init__(self):
        """The constructor of the classB"""
        print("Class B running")
        super().__init__()

    def featureB(self):
        """The method featureB which takes the input as a age from the user and prints the age to the console"""
        age = input("Enter Your age: ")
        print("Your age is: " + age)


class C(B):
    """This is classC which inheritance the feature of classB"""

    def __init__(self):
        """The constructor of classC"""
        super().__init__()
        print("Class c running")

    def featureC(self):
        """The method featureC which takes the input as a place from the user and prints the place to the console"""
        place = input("Enter the place where you live: ")
        print("You live in: " + place)
        print("Thanks for using my program created by Sidhant Soni")


"""Creating object of classC and accessing its methods"""
a3 = C()
a3.featureA()
a3.featureB()
a3.featureC()
