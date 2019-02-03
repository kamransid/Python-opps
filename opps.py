# class Parrot:
#     species = 'bird'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sing(self, song):
#         return '{} sings {}'.format(self.name, song)
#     def dance(self):
#         return '{} is now dancing'.format(self.name)

# blu = Parrot('Blu', 10)
# print(blu.sing('lalalalala'))
# print(blu.dance())
# woo = Parrot('Woo', 15)
# blu.species = 'Kamal'
# print('Blu is a {}'.format(blu.__class__.species))
# print('Blu is a {0}'.format(blu.species))

# print('Woo is a {0}'.format(woo.__class__.species))
# print('Woo is a {0}'.format(woo.species))

# print('{} is {} years old'.format(blu.name, blu.age))
# print('{} is {} year old'.format(woo.name, woo.age))

print('*******Inheritance********')
class Bird:
    def __init__(self):
        print('Bird is ready')
    def whoisThis(self):
        print('Bird')
    def swim(self):
        print('Swim fast')

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print('Penguin is ready')
    def whoisThis(self):
        print('Penguin')
    def run(self):
        print('Run Faster')

p = Penguin()
p.whoisThis()
p.swim()
p.run()




# t = Bird()
