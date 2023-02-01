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



            