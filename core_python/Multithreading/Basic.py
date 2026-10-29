'''Normal execution'''
import time
def task1():
    for i in range(1,4):
        print('Task 1 ',i)
        time.sleep(1)
def task2():
    for i in range(1,4):
        print("Task 2 ",i)
        time.sleep(1)

task1()
task2()


'''Using multithreading'''
import threading
import time

def task1():
    for i in range(1,4):
        print("Task 1 ",i)
        time.sleep(1)
def task2():
    for i in range(1,4):
        print("Task 2 ",i)
        time.sleep(1)

t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks completed")

'''Creating and starting threads'''

import threading

def greet():
    print("hello")
    print("hi")

t1=threading.Thread(target=greet)
t2=threading.Thread(target=greet)
t3=threading.Thread(target=greet)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("completed")

'''Passing arguments to a thread'''

import threading
import time
def display(name):
    print("Hello", name)
    time.sleep(1)
    print("Nice To Meet You")

t1 = threading.Thread(target=display, args=("Ravi",))
t2 = threading.Thread(target=display, args=("Kiran",))

t1.start()
t2.start()

t1.join()
t2.join()

import threading
import time
def display(name):
    print("Hello", name)
    print("Nice To Meet You")

t1 = threading.Thread(target=display, args=("Ravi",))
t2 = threading.Thread(target=display, args=("Kiran",))

t1.start()
t2.start()

t1.join()
t2.join()

import threading,time
def task1():
    for i in range(1,5):
        print("task1 : ",i)
        time.sleep(1)
def task2():
    for i in range(1,5):
        print("task2 : ",i)
        time.sleep(1)
t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()
print("hello")
