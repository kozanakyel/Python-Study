Python 3.8.2 (default, Apr  8 2020, 14:31:25) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> table = {'Phyton': 'Guido van rossu',
	 'Perl': 'Larry Wall',
	 'Tcl': 'John Ousterhout'}
>>> 
>>> language = 'Phyton'
>>> creator = table[language]
>>> creator
'Guido van rossu'
>>> for lang in table:
	print(lang,'\t',table[lang])

	
Phyton 	 Guido van rossu
Perl 	 Larry Wall
Tcl 	 John Ousterhout
>>> dic = {'name':23,'name':46}
>>> dic
{'name': 46}
>>> L = []
>>> L[99] = 'spam'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    L[99] = 'spam'
IndexError: list assignment index out of range
>>> D = {}
>>> D[99] = 'spam'
>>> D
{99: 'spam'}
>>> Matrix = {}
>>> Matrix[(2,3,4)] = 88
>>> Matrix[(7,8,9)] = 99
>>> x=2;y=3;z=4;
>>> Matrix[(x,y,z)]
88
>>> Matrix
{(2, 3, 4): 88, (7, 8, 9): 99}
>>> Matrix[(2,3,6)]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    Matrix[(2,3,6)]
KeyError: (2, 3, 6)
>>> if (2,3,6) in Matrix
SyntaxError: invalid syntax
>>> if (2,3,6) in Matrix:
	print(Matrix[(2,3,6)])
	else:
		
SyntaxError: invalid syntax
>>> if (2,3,6) in Matrix:
	print(Matrix[(2,3,6)])
... else:
	
SyntaxError: invalid syntax
>>> if (2,3,6) in Matrix: ...
	print(Matrix[(2,3,6)])
... else: ...
SyntaxError: unexpected indent
>>> import aydbm
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    import aydbm
ModuleNotFoundError: No module named 'aydbm'
>>> import anydbm
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    import anydbm
ModuleNotFoundError: No module named 'anydbm'
>>> import cgi
>>> form = cgi.FieldStorage()
>>> if 'name' in form:
	showReply('Hello, ' + form['name'].value)

	
>>> dict.fromkeys(['a','b')],0)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> dict.fromkeys(['a','b'),0)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> dict.fromkeys(['a','b'],0)
{'a': 0, 'b': 0}
>>> list(zip(['a','b','c'], [1,2,3]))
[('a', 1), ('b', 2), ('c', 3)]
>>> D = dict(zip(['a','b','c'], [1,2,3]))
>>> D
{'a': 1, 'b': 2, 'c': 3}
>>> D = {k: v for (k,v) in (['a','b','c'], [1,2,3])}
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    D = {k: v for (k,v) in (['a','b','c'], [1,2,3])}
  File "<pyshell#43>", line 1, in <dictcomp>
    D = {k: v for (k,v) in (['a','b','c'], [1,2,3])}
ValueError: too many values to unpack (expected 2)
>>> D = {k: v for (k,v) in zip(['a','b','c'], [1,2,3])}
>>> D
{'a': 1, 'b': 2, 'c': 3}
>>> D = { x: x ** 2 for x in [1,2,3,4]}
>>> D
{1: 1, 2: 4, 3: 9, 4: 16}
>>> D = {c.lower(): c + '!' for c in ['SPAM','EGGS','Ham']}
>>> D
{'spam': 'SPAM!', 'eggs': 'EGGS!', 'ham': 'Ham!'}
>>> D = dict(a=1,b=2,c=3)
>>> D
{'a': 1, 'b': 2, 'c': 3}
>>> K = D.keys()
>>> K
dict_keys(['a', 'b', 'c'])
>>> list(K)
['a', 'b', 'c']
>>> V = D.values()
>>> V
dict_values([1, 2, 3])
>>> list(V)
[1, 2, 3]
>>> list(d.items())
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    list(d.items())
NameError: name 'd' is not defined
>>> list(D.items())
[('a', 1), ('b', 2), ('c', 3)]
>>> K[0]
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    K[0]
TypeError: 'dict_keys' object is not subscriptable
>>> list(K)[0]
'a'
>>> for k in D.keys(): print(k)

a
b
c
>>> del D['b']
>>> D
{'a': 1, 'c': 3}
>>> Ks = D.keys()
>>> Ks.sort()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    Ks.sort()
AttributeError: 'dict_keys' object has no attribute 'sort'
>>> Ks = list(Ks)
>>> Ks.sort()
>>> for k in Ks: print(k)

a
c
>>> Ks = D.keys()
>>> for k in sorted(Ks): print(k, D[k])

a 1
c 3
>>> 