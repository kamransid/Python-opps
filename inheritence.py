class Calculator:
    def multiplyNums(x,y):
        return x+y

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def inputSides(self):
        self.sides = [float(input('Enter side '+str(i+1)+' :')) for i in range(self.n)]
    def dispSides(self):
            for i in range(self.n):
                print('side', i+1 , 'is', self.sides[i])

class Traingle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
    def findArea(self):
        a,b,c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print('The are is %0.2f' %area)

Calculator.multiplyNums = staticmethod(Calculator.multiplyNums)

bhai = Calculator

print(Calculator.multiplyNums(1,2))
print(bhai.multiplyNums(1,2))


t = Traingle()
print(t.n)
paisa = Traingle
print(paisa)
print(isinstance(paisa, Traingle))
print(isinstance(t, Traingle))
t.inputSides()
t.dispSides()
t.findArea()