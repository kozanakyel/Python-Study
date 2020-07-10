Python 3.8.2 (default, Apr  8 2020, 14:31:25) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1j*1j*
SyntaxError: invalid syntax
>>> 1j*1j
(-1+0j)
>>> 2+1j*3
(2+3j)
>>> (2+1j)*3
(6+3j)
>>> 0b1, 0b10000,0b1010101
(1, 16, 85)
>>> oct(64), hex(64),bin(64)
('0o100', '0x40', '0b1000000')
>>> int('0x40',16)
64
>>> eval('0o0100')
64
>>> '{0:o},{1:x},{2:b}'.format(64,64,64)
'100,40,1000000'
>>> x=0xFFFFFFFFFFFFFFFFFFFFFFFFF
>>> x
1267650600228229401496703205375
>>> oct(x)
'0o1777777777777777777777777777777777'
>>> bin(x)
'0b1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
>>> x = 1
>>> x<<2
4
>>> x|2
3
>>> x&1
1
>>> 144**.5
12.0
>>> import random
>>> random.randint(1,452)
352
>>> 0.1+0.1+0.1-0.3
5.551115123125783e-17
>>> from decimal import Decimal
>>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
Decimal('0.0')
>>> import decimal
>>> decimal.Decimal(1)/decimal.Decimal(7)
Decimal('0.1428571428571428571428571429')
>>> decimal.getcontext().prec=4
>>> decimal.Decimal(1)/decimal.Decimal(7)
Decimal('0.1429')
>>> pay=decimal.Decimal(str(1999+1.33))
>>> pay
Decimal('2000.33')
>>>  with decimal.localcontext() as ctx:

 ctx.prec = 2


 decimal.Decimal('1.00') / decimal.Decimal('3.00')
 
SyntaxError: unexpected indent
>>> from fractions import Fraction
>>> x=Fraction(1,3)
>>> y=Fraction(4,6)
>>> x
Fraction(1, 3)
>>> y
Fraction(2, 3)
>>> print(y)
2/3
>>> x+y
Fraction(1, 1)
>>> x*y
Fraction(2, 9)
>>> Fraction('.25')
Fraction(1, 4)
>>> (2.5).as_integer_ratio()
(5, 2)
>>> f=2.5
>>> z=Fraction(*f.as_integer_ratio())
>>> z
Fraction(5, 2)
>>> x
Fraction(1, 3)
>>> x+z
Fraction(17, 6)
>>> float(x)
0.3333333333333333
>>> float(z)
2.5
>>> float(x+z)
2.8333333333333335
>>> Fraction.from_float(1.75)
Fraction(7, 4)
>>> Fraction(*(1.75).as_integer_ratio())
Fraction(7, 4)
>>> (4.0/3).as_integer_ratio()
(6004799503160661, 4503599627370496)
>>> clean
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    clean
NameError: name 'clean' is not defined
>>> set([1,2,3,4])
{1, 2, 3, 4}
>>> set('spam')
{'a', 'm', 's', 'p'}
>>> s={'s','p','a','m'}
>>> s.add('alot')
>>> s
{'a', 'p', 'alot', 's', 'm'}
>>> s1={1,2,3,4}
>>> s1&{1,3}
{1, 3}
>>> {x**2 for x in [1,2,3,4]}
{16, 1, 4, 9}
>>> {c*4 for c in'spam'}
{'aaaa', 'mmmm', 'pppp', 'ssss'}
>>> s = {c*4 for c in'spam'}
>>> s | {'mmm','xxx'}
{'mmm', 'aaaa', 'mmmm', 'xxx', 'pppp', 'ssss'}
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined
>>> type(True)
<class 'bool'>
>>> isinstance(True,int)
True
>>> True==1
True
>>> True is 1
False
>>> True or false
True
>>> true + 4
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    true + 4
NameError: name 'true' is not defined
>>> True +4
5
>>> import stdio
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    import stdio
ModuleNotFoundError: No module named 'stdio'
>>> '%-10.2f  | %010.2f | %+8.af' %(32154.64,64.64868,4.6464)
'32154.64    | 0000064.65 |         f'
>>> reply = """
Greetings...
Hello %(name)s!
Your age squared is %(age)s
"""
>>> values = {'name':'bob','age':40}
>>> print(reply % values)

Greetings...
Hello bob!
Your age squared is 40

Python 3.8.2 (default, Apr  8 2020, 14:31:25) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> D = {'spam':2,'ham':1,'eggs':3}
>>> list(D.values())
[2, 1, 3]
>>> list(D.items())
[('spam', 2), ('ham', 1), ('eggs', 3)]
>>> D2 = ['toast':4,'muffin':5}
SyntaxError: invalid syntax
>>> D2 = {'toast':4,'muffin':5}
>>> D.update(D2)
>>> D
{'spam': 2, 'ham': 1, 'eggs': 3, 'toast': 4, 'muffin': 5}
>>> D.pop('muffin')
5
>>> 
