class Transport:
    def __init__(self, the_model, the_year, the_color):
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color

class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        super().__init__(the_model, the_year, the_color)


class Car(Transport):
    # class attributes
    counter = 0

    # constructor                       # parameters
    def __init__(self, the_model, the_year, the_color, penalties=0):
        # attributes / fields
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties
        Car.counter += 1

    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')

    def signal(self, number_of_times, sound):
        sound += ' '
        print(f'Car {self.model} makes signal: {sound * number_of_times}')


class Truck(Car):
    counter = 0
    def __init__(self, the_model, the_year, the_color, penalties=0, load_capacity=0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity
        Truck.counter += 1

    def load_cargo(self, type_of_cargo, weight):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity} kg.')
        else:
            print(f'You successfully loaded cargo of {type_of_cargo} ({weight} kg.)')


print(f'FACTORY CAR produced: {Car.counter}')

my_number = 45
print(my_number)
bmw_car = Car('BMW X7', 2020, 'blue')
print(bmw_car)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} COLOR: {bmw_car.color} '
      f'PENALTIES: {bmw_car.penalties}')

honda_car = Car(penalties=900, the_model='Honda Fit', the_color='red', the_year=2009)
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} COLOR: {honda_car.color} '
      f'PENALTIES: {honda_car.penalties}')
# honda_car.color = 'green'
honda_car.change_color('green')
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} NEW COLOR: {honda_car.color} '
      f'PENALTIES: {honda_car.penalties}')

bmw_car.drive('Osh')
honda_car.drive('Kant')
honda_car.drive('Tokmok')
honda_car.signal(3, 'beeep')

print(f'FACTORY CAR produced: {Car.counter}')

boeing_plane = Plane('Boeing f-45', 2023, 'white')
print(f'MODEL: {boeing_plane.model} YEAR: {boeing_plane.year} COLOR: {boeing_plane.color}')

kamaz_truck = Truck('Kamaz Honda', 2006,
                    'yellow', 1200, 35000)
print(f'MODEL: {kamaz_truck.model} YEAR: {kamaz_truck.year} COLOR: {kamaz_truck.color} '
      f'PENALTIES: {kamaz_truck.penalties} LOAD CAPACITY: {kamaz_truck.load_capacity}')
kamaz_truck.load_cargo('potatoes', 40000)
kamaz_truck.load_cargo('apples', 20000)
kamaz_truck.drive('Batken')


print(f'FACTORY CAR produced: {Car.counter}')
print(f'FACTORY TRUCK produced: {Truck.counter}')




