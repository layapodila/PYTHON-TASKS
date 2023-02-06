'''1.1. Write a program in Python to allow the error of syntax to be handled using exception handling.'''

try:
    eval ("3 by 5")
except SyntaxError:
    print("an error occured wrt import,eval,compile,exec")


try:
    eval("hello =")        ##Syntax error while parsing
except SyntaxError:
    print("Hey")

'''2. Write a program in Python to allow the user to open a file by using the argv module. If the
entered name is incorrect throw an exception and ask them to enter the name again. Make sure
to use read only mode.'''   

import sys
import os
#f=open('/Users/Lekha/Desktop/PYTHON TASKS/Extra-Task/file1.py','r')
#print(f.read())
#f.close()
name=input("enter filename with extension: ")
file_name = os.path.basename(sys.argv[0])
if name != file_name:
    name=input("enter file name again: ")
    print("user entered: ",name)
else:
    open(sys.argv[1],'r')
​
print("file_name is: ", file_name)

'''3. Write a program to handle an error if the user entered a number more than four digits it should
return “The length is too short/long !!! Please provide only four digits”'''

num=input("enter number: ")
if len(num)>4 or len(num)<4:
    print("The length is too short/long!! Pls provide only 4 digits")
    num=input("enter number again: ")


'''4.Create a login page backend to ask users to enter the username and password. Make sure to
ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
should not be more than 3 times.'''

attempts=0
while attempts<3:
    username=input('username?')
    password=input('password?')
    if username=='correctusername'and password=='correctpassword':
        print('you are in!')
    else:
        attempts+=1
        print('Re-type the password!')
        if attempts==3:
            print('too many attempts')

'''6'''

f=open("doc.txt",'r')
try:
    readfile=f.read()
    print("content of file is: ", readfile)
    
    s=readfile.split("\n")
    print("\n",s)
    def func():
        for i in range(0,4):
            print(len(s[i]))
            l=len(s[i])
            string=s[i]
            if l%2 ==0:
                return string
            i=i+1
    
    z=func()
    print("\nthe returned string is : ", z)

finally:
    f.close()

            