def print_poema():
...     print('um dois três quatro,')
...     print('quatro três dois um.')
... 
>>> print(print_poema)
<function print_poema at 0x7f027fe9fc80>
>>> 
>>> type(print_poema)
<class 'function'>
>>> print_poema
<function print_poema at 0x7f027fe9fc80>
>>> 
>>> print_poema()
um dois três quatro,
quatro três dois um.


----------------------------------------------------------------------------------------------------

def do_twice(f,x):
    f(x)
    f(x)

def print_twice(g):
    print(g)
    print(g)

do_twice(print_twice,'spam')


incompleta
