from enum import Enum


class Color(Enum):
    RED = '\033[91m'
    GREEN = '\033[92m'
    DARK_BLUE = '\033[34m'


class Drawable:
    def draw(self, emoji):
        print(emoji)


class MusicPlayable:
    # def __init__(self):
    #     pass

    def play_music(self, song):
        print(f'Now is playing {song}.')

    def stop_music(self):
        print(f'Music stopped')


class SmartPhone(MusicPlayable, Drawable):
    pass


class Car(MusicPlayable, Drawable):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        if type(color) != Color:
            raise TypeError('Type of color must be Color')
        else:
            self.__color = color

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def drive(self):
        print(f"Car {self.__model} is driving")

    def __str__(self):
        return (f'YEAR: {self.__year} MODEL: {self.__model} '
                f'COLOR: {self.__color.value}{self.__color.name}' + '\033[0m')

    def __gt__(self, other):
        return self.__year > other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year

    def __ge__(self, other):
        return self.__year >= other.__year

    def __le__(self, other):
        return self.__year <= other.__year


class FuelCar(Car):
    __total_fuel = 0

    @classmethod
    def buy_fuel(cls, amount):
        cls.__total_fuel += amount

    @classmethod
    def get_total_fuel(cls):
        return cls.__total_fuel

    @staticmethod
    def get_fuel_type():
        return 'AI - 95'

    def __init__(self, model, year, color, fuel_bank):
        # super().__init__(model, year, color)
        # super(FuelCar, self).__init__(model, year, color)
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f"Car {self.model} is driving by fuel")

    def __str__(self):
        return super().__str__() + f' FUEL BANK: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f"Car {self.model} is driving by electricity")

    def __str__(self):
        return super().__str__() + f' BATTERY: {self.__battery}'


class HybridCar(ElectricCar, FuelCar):
    def __init__(self, model, year, color, fuel_bank, battery):
        FuelCar.__init__(self, model, year, color, fuel_bank)
        ElectricCar.__init__(self, model, year, color, battery)


# some_car = Car('Ford Focus', 2000, 'blue')
# print(some_car)
FuelCar.buy_fuel(500)
print(f'FACTORY FUEL CAR has {FuelCar.get_total_fuel()} '
      f'({FuelCar.get_fuel_type()}) litters.')

camry_car = FuelCar('Toyota Camry', 2022, Color.RED, 85)
print(camry_car)

tesla_car = ElectricCar('Tesla Model X', 2023, Color.DARK_BLUE, 25000)
print(tesla_car)

prius_car = HybridCar('Toyota Prius', 2019, Color.GREEN, 70, 15000)
print(prius_car)
prius_car.drive()
print(HybridCar.mro())

number_1 = 9
number_2 = 3
print(f'Number one is bigger than number two: {number_1 > number_2}')
print(f'Camry car is better than prius car: {camry_car > prius_car}')
print(f'Camry car is the same with prius car: {camry_car == prius_car}')
print(f'{camry_car + prius_car}')

# FuelCar.total_fuel -= 100
print(f'FACTORY FUEL CAR has {FuelCar.get_total_fuel()} '
      f'({FuelCar.get_fuel_type()}) litters.')

if tesla_car.model == 'Tesla Model X':
    print('This car is cool!')

if tesla_car.color == Color.DARK_BLUE:
    print('This car is beautiful!')

tesla_car.play_music('Song 1')

samsung = SmartPhone()
samsung.play_music('Best song')
tesla_car.draw('🏎️')
samsung.draw('📱')