print(issubclass(list, object))
#print(issubclass(5.5, object))
print(issubclass(set, object))
# print(issubclass(, object))

class Base1:
    pass
class Base2:
    pass
class Derived(Base1, Base2):
    pass

print(Derived.__mro__)
print(Base1.mro())
print(Base1.__mro__)