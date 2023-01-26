'''1.1. Write a program in Python to allow the error of syntax to be handled using exception handling.'''

try:
    if 5>1                ##It's missing a colon So it's a SyntaxError
except SyntaxError:
    print('Hi')


try:
    eval("hello =")        ##Syntax error while parsing
except SyntaxError:
    print("Hey")

'''2. Write a program in Python to allow the user to open a file by using the argv module. If the
entered name is incorrect throw an exception and ask them to enter the name again. Make sure
to use read only mode.'''   


