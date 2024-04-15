class Contact:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @property
    def street(self):
        return self.__street

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value


class Animal:
    def __init__(self, name, age, contact):
        self.__name = name
        self.__age = age
        if type(contact) == Contact:
            self.__contact = contact
        else:
            raise ValueError('Invalid contact. It must be of data type Contact')
        self.__was_born()

    def __was_born(self):
        print(f'Animal {self.__name} was born!')

    def set_age(self, new_age):
        if type(new_age) is not int or new_age <= 0:
            raise ValueError('Invalid age. It must be positive integer')
        else:
            self.__age = new_age

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def info(self):
        return (f'NAME: {self.__name} AGE: {self.__age} BIRTH YEAR: {2024 - self.__age}\n'
                f'CONCACT INFO: {self.__contact.city}, {self.__contact.street} {self.__contact.number}')

    def speak(self):
        raise NotImplementedError('Method speak not implemented')

class Cat(Animal):
    def __init__(self, name, age, contact):
        super(Cat, self).__init__(name, age, contact)

    def speak(self):
        print('Myau')


class Fish(Animal):
    def __init__(self, name, age, contact):
        super(Fish, self).__init__(name, age, contact)

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, commands, contact):
        super(Dog, self).__init__(name, age, contact)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, new_commands):
        self.__commands = new_commands

    def info(self):
        return super().info() + f'\nCOMMANDS: {self.__commands}'

    def speak(self):
        print('Gav')


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins, contact):
        super(FightingDog, self).__init__(name, age, commands, contact)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    def info(self):
        return super().info() + f'\nWINS: {self.__wins}'

    def speak(self):
        print('Rrr gav')


# some_animal = Animal('Anim', 2)
# print(some_animal.get_name())
# some_animal.set_age(3)
# print(some_animal.info())

contact_1 = Contact('Bishkek', 'Isanova', 55)
cat = Cat('Tom', 1, contact_1)
# print(cat.info())

fish = Fish('Nemo', 4, contact_1)

dog = Dog('Reks', 5, 'Sit', contact_1)
dog.commands = 'Sit, run'
# print(dog.commands)
# print(dog.info())

# contact_2 = Contact('Osh', 'Lenina', 1)
#         a = b
fighting_dog = FightingDog('Tim', 2, 'Fight', 9,
                           Contact('Osh', 'Lenina', 1))
# print(fighting_dog.info())

# contact_1.number = 77
# print(cat.info())
# print(dog.info())

animals_list = [cat, fish, dog, fighting_dog]
for animal in animals_list:
    print(animal.info())
    animal.speak()