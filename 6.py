class MyException(Exception):
    pass
def foo():
    print('1..')
    foo2()
 
def foo2():
    print('2..')
    foo3()
 
def foo3():
    print('3..')
    foo4()
 
def foo4():
    raise MyException('!!!Ошибка!!!')
 
foo()
