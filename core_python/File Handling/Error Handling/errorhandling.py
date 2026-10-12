'''Handle division by zero.'''
a=10
b=0
try:
    print(a/b)
except ZeroDivisionError as e:
    print("Error",e)


'''Handle invalid integer input.'''
try:
    n=int(input("enter a number: "))
except ValueError:
    print("please enter a  valid interger")


'''Handle an invalid list index.'''
try:
    a=[10,20,30,40,50]
    i=int(input("enter an index: "))
    if i>=len(a):
        raise IndexError("Plase Enter a valid index number")
    print(a[i])
except ValueError:
    print("Please enter an integer value")


'''Handle a missing dictionary key.'''
try:
    a={'name':'venky','age':18,'gender':'M'}
    print(a['salary'])
except KeyError:
    print("Key Not Found")


'''Demonstrate try, except, else and finally.'''
try:
    a=int(input("Enter an interger: "))
    b=int(input("Enter an divisior: "))
    print(a/b)
except ValueError:
    print("please enter a valid integer")
except ZeroDivisionError:
    print("can not divide by zero")
else:
    print("No error occured")
finally:
    print("The program finished")


'''Build a calculator with exception handling.'''
try:
    a=float(input("Enter a Number: "))
    b=float(input("Enter  a Number: "))
    op=input("Enter an Operator (=,-,*,/): ")
    if op=='+':
        print(a+b)
    elif op=='-':
        print(a-b)
    elif op=='*':
        print(a*b)
    elif op=='/':
        print(a/b)
    else:
        print("Invalid operator")
except ValueError as e:
    print("Enter a Valid number",e)
except ZeroDivisionError as e:
    print("can not divide by zero",e)


'''Keep asking until the user enters a positive integer.'''
while True:
    try:
        a=int(input("Enter a number: "))
        if a>0:
            print("Valid Number!",a)
            break
        else:
            print('please Enter a postive number!')
    except ValueError:
        print("Error: enter an integer")


'''Raise ValueError when marks are outside 0–100.'''
try:
    m=int(input("Enter marks: "))
    if not 0<=m<=100:
        raise ValueError("marks should be between 0 and 100")
    print("valid marks: ",m)
except ValueError as e:
    print(e)


'''Create an InvalidAgeError custom exception.'''
class InvalidAgeError(Exception):
    pass
try:
    a=int(input("Enter Age: "))
    if a<18:
        raise InvalidAgeError("Age Should Be Above 17")
    print("valid Age")
except InvalidAgeError as e:
    print('Error: ',e)


'''Create a bank account with an InsufficientBalanceError.'''
class  InsufficientBalanceError(Exception):
    pass
try:
    balance=5000
    amount=int(input("Enter an amount to withdraw: "))
    if amount<0:
        raise ValueError("amount should be postive")
    if amount>balance:
        raise InsufficientBalanceError("InsufficientBalanceError")
    balance-=amount
    print("Withdraw sucessfully completed")
    print("Balance : ",balance)
except InsufficientBalanceError as e:
    print("failed",e)


'''Use nested exception handling for input and list access.'''
a=[10,20,30,40,50]
try:
    try:
        i=int(input("Enter Index Number: "))
    except ValueError as e:
        print("Enter valid an integer",e)
    else:
        try:
            print('value: ',a[i])
        except IndexError as e:
            print("Index out of range",e)
except Exception as e:
    print("undefined error",e)


'''• Create a class Person whose constructor takes age as an argument. Raise a 
ValueError if the age is less than 0.'''
class person:
    def __init__(self,age):
        try:
            if age<0:
                raise ValueError("Age must be postive")
            print("Eligible!")
        except ValueError as e:
            print(e)
p=person(18)
p=person(-1)


'''• Write a function named find_length(obj) that uses a loop to calculate the 
length of the given object without using the built-in len() function. The 
function should return the calculated length if the object is iterable. If a 
non-iterable object such as an integer is passed, the function should raise and 
handle a TypeError, and print an appropriate error message explaining what 
# happens when an integer is sent as input.'''
def find_lenght(obj):
    c=0
    try:
        for i in obj:
            c+=1
        return c
    except TypeError as e:
        print("interger is not iterable",e)
print(find_lenght([10,20,30,40]))
print(find_lenght('python'))
print(find_lenght(100))


'''• Create a class Student with an attribute marks. Implement a method 
set_marks(marks) that raises a ValueError if marks are not in the range 0 to 
100.'''
class student:
    def set_marks(self,marks):
        try:
            if not  0<=marks<=100:
                raise ValueError("Marks must be between 0 to 100")
            print("marks: ",marks)
        except ValueError as e:
            print(e)
s=student()
s.set_marks(110)


'''• Create a custom exception named InvalidAgeError. Create a class Voter with a 
method check_eligibility(age) that raises this exception if age is less than 18.'''
class InvalidAgeErroe(Exception):
    pass
class voter:
    def check_eligibility(self,age):
        try:
            if age<18:
                raise InvalidAgeErroe("Age must be above 18 0r 18")
            print("Eligible for Vote")
        except InvalidAgeErroe as e:
            print(e)
c=voter()
c.check_eligibility(17)
c.check_eligibility(19)
    

'''• Create a class BankAccount with an attribute balance. Implement a method 
withdraw(amount) that raises an exception if the withdrawal amount is greater 
than the available balance.'''
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def Withdraw(self,amount):
        try:
            if amount>self.balance:
                raise Exception("insufficiantamount")
            self.balance-=amount
            print("Withdraw sucessfully completed")
            print("Remaing Amount: ",self.balance)
        except Exception as e:
            print(e)
c=BankAccount(5000)
c.Withdraw(2000)
c.Withdraw(6000)


'''• Create a class PasswordValidator with a method validate(password). Raise an 
exception if the password length is less than 8 characters.'''
class Passwordvalidator:
    def validate(self,password):
        try:
            if len(password)<8:
                raise Exception("Password Must contains 8 characters")
            print("Valid Password!")
        except Exception as e:
            print(e)
p=Passwordvalidator()
p.validate("venky")
p.validate("venkatesh")


'''• Create a class UserInput with a method get_integer(value). Handle ValueError 
and TypeError using separate except blocks.'''
class userinput:
    def get_integer(self,value):
        try:
            n=int(value)
            print("integer ",n)
        except ValueError:
            print("invalid value")
        except TypeError:
            print("Invalid Type")
c=userinput()
c.get_integer(10)
c.get_integer("ab")


'''• Create a base class Shape with a method area() that raises 
NotImplementedError. Create a child class Rectangle that overrides and 
implements the area method.'''

'''• Create a class Service with a method that calls another method which raises an 
exception. Catch and handle the exception in the Service class.'''
class service:
    def divide(self):
        return 10/0
    def process(self):
        try:
            result=self.divide()
            print("Result: ",result)
        except ZeroDivisionError:
            print("can't divide with zero")
c=service()
c.process()


'''• Create a class Transaction with a method process() that uses try, except, and 
finally blocks to ensure a cleanup message is always printed.'''
class Transaction:
    def process(self):
        try:
            print("processing")
            print(10/0)
        except ZeroDivisionError:
            print("Transaction Failed")
        finally:
            print("completed Thank you")
c=Transaction()
c.process()


'''• Create a class LoginSystem with a method login(password) that raises an 
exception for an incorrect password and handles the exception outside the class'''
class LoginSystem:
    def login(self,password):
        if password!='venky':
            raise Exception("Invalid Password")
        print("Valid Password")
c=LoginSystem()
try:
    c.login("venkyy")
except Exception as e:
    print(e)
