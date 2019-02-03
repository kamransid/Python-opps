class MyNewClass:
    '''This is it'''
    pass

# t = MyNewClass()
# print(t.__doc__)

print(isinstance(MyNewClass, MyNewClass))#false

print(MyNewClass.__doc__)

class MyClass:
    'This is my second class'
    a = 10
    def func(self):
        print('Hello')
    def aalu():
        print('I am aalu')

print(MyClass.a)
print(MyClass.aalu())
print(MyClass.func)
ob = MyClass()
print(ob.func)



