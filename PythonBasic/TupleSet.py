Python 3.8.2 (default, Apr  8 2020, 14:31:25) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> t = (1,2,3)
>>> t
(1, 2, 3)
>>> t = ('one',2)
>>> t[0]
'one'
>>> t[-1]
2
>>> t = ('a','a','b')
>>> t.count('a')
2
>>> t.index('a')
0
>>> t.index('b'ArithmeticError)
SyntaxError: invalid syntax
>>> t
('a', 'a', 'b')
>>> myList = [1,2,3]
>>> myList[0] = 'new'
>>> myList
['new', 2, 3]
>>> t[0] = 'new'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    t[0] = 'new'
TypeError: 'tuple' object does not support item assignment
>>> myset = set()
>>> myset
set()
>>> myset.add(1)
>>> myset
{1}
>>> myset.add(2)
>>> myset
{1, 2}
>>> myset.add(2)
>>> myset
{1, 2}
>>> mylist = [1,1,1,1,2,2,2,2,2,3,3,3]
>>> set(mylist)
{1, 2, 3}
>>> True
True
>>> False
False
>>> type(False)
<class 'bool'>
>>> 1 > 2
False
>>> 1 == 1
True
>>> b
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> b = None
>>> b
>>> (1,2) + (3,4)
(1, 2, 3, 4)
>>> (1,2)*4
(1, 2, 1, 2, 1, 2, 1, 2)
>>> T = (1,2,3,4)
>>> T[0],T[1:3]
(1, (2, 3))
>>> 