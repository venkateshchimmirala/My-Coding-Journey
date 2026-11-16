import threading,time
# '''Normal execution'''
# import time
# def task1():
#     for i in range(1,4):
#         print('Task 1 ',i)
#         time.sleep(1)
# def task2():
#     for i in range(1,4):
#         print("Task 2 ",i)
#         time.sleep(1)

# task1()
# task2()


# '''Using multithreading'''
# import threading
# import time

# def task1():
#     for i in range(1,4):
#         print("Task 1 ",i)
#         time.sleep(1)
# def task2():
#     for i in range(1,4):
#         print("Task 2 ",i)
#         time.sleep(1)

# t1=threading.Thread(target=task1)
# t2=threading.Thread(target=task2)

# t1.start()

# t2.start()
# t1.join()
# t2.join()

# print("All tasks completed")

# '''Creating and starting threads'''

# import threading

# def greet():
#     print("hello")
#     print("hi")

# t1=threading.Thread(target=greet)
# t2=threading.Thread(target=greet)
# t3=threading.Thread(target=greet)

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# print("completed")

# '''Passing arguments to a thread'''

# import threading
# import time
# def display(name):
#     print("Hello", name)
#     time.sleep(1)
#     print("Nice To Meet You")

# t1 = threading.Thread(target=display, args=("Ravi",))
# t2 = threading.Thread(target=display, args=("Kiran",))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# import threading
# import time
# def display(name):
#     print("Hello", name)
#     print("Nice To Meet You")

# t1 = threading.Thread(target=display, args=("Ravi",))
# t2 = threading.Thread(target=display, args=("Kiran",))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# import threading,time
# def task1():
#     for i in range(1,5):
#         print("task1 : ",i)
#         time.sleep(1)
# def task2():
#     for i in range(1,5):
#         print("task2 : ",i)
#         time.sleep(1)
# t1=threading.Thread(target=task1)
# t2=threading.Thread(target=task2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("hello")

# import threading
# import time

# sem = threading.Semaphore(3)

# def student(name):
#     with sem:
#         print(name, "entered the lab")
#         time.sleep(2)
#         print(name, "left the lab")

# for i in range(1, 6):
#     t = threading.Thread(target=student, args=(f"Student {i}",))
#     t.start()

# import threading

# def task():
#     print("Task running")

# t1 = threading.Thread(
#     target=task,
#     name="Download-Thread")

# t1.run()

# print(t1.name)
  

# import threading
# import time

# def background():
#     while True:
#         print("Background running")
#         time.sleep(1)

# t1 = threading.Thread(target=background)

# t1.daemon = True

# t1.start()

# print("Main completed")

# import threading

# sem = threading.Semaphore(1)

# def task():
#     with sem:
#         print("Hello")

# t1 = threading.Thread(target=task)
# t2 = threading.Thread(target=task)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Completed")

# import threading
# import time

# event = threading.Event()

# def student():
#     print("Student is waiting")

#     event.wait()
#     event.clear()
#     print("Student started learning")

# def teacher():
#     time.sleep(3)

#     print("Teacher says: Start!")

#     event.set()


# t1 = threading.Thread(target=student)
# t2 = threading.Thread(target=teacher)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Completed")

# import threading
# import time

# lock1 = threading.Lock()
# lock2 = threading.Lock()

# def task1():
#     with lock1:
#         print("Thread 1 acquired lock1")
#         time.sleep(1)

#         with lock2:
#             print("Thread 1 acquired lock2")

# def task2():
#     with lock1:
#         print("Thread 2 acquired lock2")
#         time.sleep(1)

#         with lock2:
#             print("Thread 2 acquired lock1")

# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)

# t1.start()
# t2.start()

'''Create two threads to print numbers 1–5 and 6–10.'''
# import threading
# def task1():
#     for i in range(1,5):
#         print("Task 1: ", i)
# def task2():
#     for i in range(6,10):
#         print("Task 2: ", i)
# t1=threading.Thread(target=task1)
# t2=threading.Thread(target=task2)
# t1.start()
# t2.start()


'''lock'''
# balance=1000
# def task(amount):
#     global balance
#     time.sleep(5)
#     if balance>=amount:
#         balance-=amount
#         print("withdraw sucess!")
       
#     else:
#         print("Failed")
# t1=threading.Thread(target=task,args=(500,))
# t2=threading.Thread(target=task,args=(700,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()








