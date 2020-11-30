Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
l=[1,"hi","python",2}
SyntaxError: invalid syntax
>>> 
>>> l=[1,"hi","python",2]
>>> print(l[3:])
[2]
>>> print(l[0:2]);
[1, 'hi']
>>> print(l)
[1, 'hi', 'python', 2]
>>> print(l+l)
[1, 'hi', 'python', 2, 1, 'hi', 'python', 2]
>>> print(l*3)
[1, 'hi', 'python', 2, 1, 'hi', 'python', 2, 1, 'hi', 'python', 2]
>>> 
print(l)
[1, 'hi', 'python', 2]
>>> 
