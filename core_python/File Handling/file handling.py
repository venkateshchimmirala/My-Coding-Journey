f=open('student.text','w')
f.write("Hello Python\n")
f.write("learning file handling")
f.close()

'''Reading data from a File'''
'''Reads Entire line'''
f=open("student.text",'r')
data=f.read()
print(data)
f.close()

'''f.readline().. read one line at a time'''
f=open('student.text','r')
print(f.readline())
print(f.readline())
f.close()
'''f.readlines()..return lines in a list'''
f=open('student.text','r')
print(f.readlines())
f.close() 

'''to avoid f.close()  using "with" '''
with open('student.text','r') as f:
    print(f.read())


'''Appending data to a file'''
'''Appending adds new data at the end without deleting existing content.'''
with open('student.text','a') as f:
    f.write('\nVenkatesh')
with open('student.text','r') as f:
    print(f.read())

with open("student.text", "r") as f:
    print(f.tell())
    f.read(6)
    print(f.tell())
    print(f.read())

with open("student.text", "r") as f:
    f.seek(2)
    print(f.read())

with open('student.txt','w') as f:
    f.write("venky venky\n")
    f.write("python")

'''Count characters'''
with open('student.txt','r') as f:
    data=f.read()
    print(len(data))

'''Count words'''
with open('student.txt','r') as f:
    data=f.read()
    words=data.split()
    print(len(words))

'''Count lines'''
with open('student.txt','r') as f:
    l=f.readlines()
    print(len(l))

'''Creating and deleting files'''

'''Create a new file'''
with open('new file','x') as f:
    f.write("new file created")
with open ("new file",'r') as f:
    print(f.read())

'''Delete a file'''
import os
if os.path.exists('new file'):
    os.remove('new file')
    print('file deleted')
else:
    print("file not found")


'''Read and then append'''
with open('student.text','a+') as f:
    f.seek(0)
    print(f.read())
    f.write('\nnew student added')
    f.seek(0)
    print(f.read())
import os
if os.path.exists('student.text'):
    os.remove('student.text')
    print("deleted")
else:
    print("file not found")

    
'''Write a Python program to create a file named data.txt and write five lines of text into it'''
with open('data.txt','w')as f:
    f.write("Python")

'''Write a program to read and display the entire contents of an existing text file'''
with open('data.txt','r')as f:
    print(f.read())


'''Write a program to read a file one line at a time using readline()'''
with open('data.txt','r')as f:
    print(f.readline())

'''Write a program to append a new sentence to an existing file without deleting its previous contents.'''
with open('data.txt','a')as f:
    f.write("Learning Python")

'''Write a program to count the total number of characters in a file.'''
with open('data.txt','r')as f:
    data=f.read()
    print(len(data))

'''Write a program to count the number of lines in a text file.'''
with open('data.txt','r')as f:
    data=f.readlines()
    print(len(data))

'''Write a program to count the number of words in a file.'''
with open('data.txt','r')as f:
    data=f.read()
    words=data.split()
    print(len(words))

'''Write a program to create a new file using exclusive creation mode and handle the case where the file already exists.'''
try:
    with open('data1.txt','x')as f:
        f.write("new file created")
        print("created")
except Exception as e:
    print('file already exits',e)

'''Write a program to count the number of vowels, consonants, digits, and spaces in a text file.'''
with open("venky.txt",'w')as f:
    f.write("a4b ")
with open('venky.txt','r')as f:
    data=f.read()
v=c=d=s=0
for i in data:
    if i.lower() in 'aeiou':
        v+=1
    elif i.isalpha():
        c+=1
    elif i.isdigit():
        d+=1
    elif i==' ':
        s+=1
print("vowels: ",v)
print("consonants: ",c)
print("Digits: ",d)
print("Spaces: ",s)

'''Write a program to count how many times a particular word appears in a file.'''
with open('data.txt','w')as f:
    f.write('Python is easy\nPython is powerful\nI love Python')
with open('data.txt','r')as f:
    data=f.read()
    print(data)
words=data.split()
w=input("Enter word to search: ")
c=0
for i in words:
    if i.lower()==w.lower():
        c+=1
print("Count: ",c)

'''Write a program to display only those lines that contain the word Python.'''
with open('data.txt','r')as f:
    for i in f:
        if 'Python' in i:
            print(i,end=' ')

'''Write a program to copy the contents of one text file into another file.'''
with open('data.txt','r')as f:
    source=f.read()
with open("data1.txt",'w')as f:
    f.write(source)

'''Write a program to read a file and display its contents in reverse line orde'''
with open('data.txt','r')as f:
    data=f.readlines()
for i in data[::-1]:
    print(i,end='')

# '''Write a program to find the longest word in a text file.'''
with open('data.txt','r')as f:
    data=f.read()
word=data.split()
# print(word)
longest=''
for i in word:
    if len(i)>len(longest):
        longest=i
print(longest)

'''Write a program to replace every occurrence of a specified word with another word and save the updated content.'''
with open('data.txt','r')as f:
    data=f.read()
old=input("enter  the word to replace: ")
new=input("enter new word: ")
data=data.replace(old,new)
with open('data.txt','w')as f:
    f.write(data)
with open('data.txt','r')as f:
    print(f.read())


'''Write a program to merge the contents of two text files into a third file.'''
with open('data.txt','r')as f:
    data1=f.read()
with open("siva.txt",'r')as f:
    data2=f.read()
with open("mergedata.txt",'w')as f:
    f.write(data1)
    f.write('\n')
    f.write(data2)
with open('mergedata.txt','r')as f:
    print(f.read())

'''. Write a program to display the first N lines of a file, where N is provided by the user.'''
n=int(input())
with open('mergedata.txt','r')as f:
    data=f.readlines()
# print(data)
for i in data[:n]:
    print(i,end='')

' Write a Python program using a context manager (with) to open a'
' text file in read mode, read the entire content using read(), and print the number of characters in the file.'
with open('data.txt','r')as f:
    data=f.read()
print(len(data))

''' Write a program that opens a file using a context manager, reads all lines using 
readlines(), and prints only the lines that contain more than 10 characters.'''
with open('mergedata.txt','r')as f:
    data=f.readlines()
for i in data:
    if len(i)>10:
        print(i,end='')

''' Write a program that creates a file and writes 3 lines using write(), reopens the same file in 
append mode, appends 2 more lines, and finally reads and prints the complete file content.'''
with open('student.txt','w')as f:
    f.write("Good Morning\nGood afternoon\nGoodNight\n")
with open('student.txt','a')as f:
    f.write("hi\nbye")
with open('student.txt','r')as f:
    print(f.read())

''' Write a program that opens a file in read mode, reads the first 10 characters
, prints the current cursor position using tell(), moves the cursor back to the beginning 
using seek(0), and reads the full content again.'''
with open('student.txt','r')as f:
    print(f.read(10))
    print(f.tell())
    f.seek(0)
    print(f.read())

''' Create a custom context manager using a class that opens a file in write mode
 in the __enter__ method, writes a line to the file, closes the file in the __exit__
   method, and properly prints or logs any exception information received in __exit__.'''
class a:
    def __init__(self,fn):
        self.fn=fn
    def __enter__(self):
        self.f=open(self.fn,'r')
        return self.f
    def __exit__(self, exc_type, exc, tb):
        self.f.close()
o=a('data.txt')
with o as f:
    f.seek(0)
    print(f.read())

