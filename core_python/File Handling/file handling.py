# f=open('student.text','w')
# f.write("Hello Python\n")
# f.write("learning file handling")
# f.close()

'''Reading data from a File'''
'''Reads Entire line'''
# f=open("student.text",'r')
# data=f.read()
# print(data)
# f.close()

'''f.readline().. read one line at a time'''
# f=open('student.text','r')
# print(f.readline())
# print(f.readline())
# f.close()
'''f.readlines()..return lines in a list'''
# f=open('student.text','r')
# print(f.readlines())
# f.close() 

'''to avoid f.close()  using "with" '''
# with open('student.text','r') as f:
#     print(f.read())


'''Appending data to a file'''
'''Appending adds new data at the end without deleting existing content.'''
# with open('student.text','a') as f:
#     f.write('\nVenkatesh')
# with open('student.text','r') as f:
#     print(f.read())

# with open("student.text", "r") as f:
#     print(f.tell())
#     f.read(6)
#     print(f.tell())
#     print(f.read())

# with open("student.text", "r") as f:
#     f.seek(2)
#     print(f.read())

# with open('student.txt','w') as f:
#     f.write("venky venky\n")
#     f.write("python")

'''Count characters'''
# with open('student.txt','r') as f:
#     data=f.read()
#     print(len(data))

'''Count words'''
# with open('student.txt','r') as f:
#     data=f.read()
#     words=data.split()
#     print(len(words))

'''Count lines'''
# with open('student.txt','r') as f:
#     l=f.readlines()
#     print(len(l))

'''Creating and deleting files'''

'''Create a new file'''
# with open('new file','x') as f:
#     f.write("new file created")
# with open ("new file",'r') as f:
#     print(f.read())

'''Delete a file'''
# import os
# if os.path.exists('new file'):
#     os.remove('new file')
#     print('file deleted')
# else:
#     print("file not found")


'''Read and then append'''
# with open('student.text','a+') as f:
#     f.seek(0)
#     print(f.read())
#     f.write('\nnew student added')
#     f.seek(0)
#     print(f.read())
# import os
# if os.path.exists('student.text'):
#     os.remove('student.text')
#     print("deleted")
# else:
#     print("file not found")

    