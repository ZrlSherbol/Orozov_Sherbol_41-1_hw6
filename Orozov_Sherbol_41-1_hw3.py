class Computer():
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_memory(self):
        return self.__memory

    def set_memory(self, memory):
        self.__memory = memory

    def make_computations(self):
        result = self.get_cpu() * self.get_memory()
        return result

    def __str__(self):
        return (f'Computer: cpu: {self.__cpu}, memory: {self.__memory}')

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

class Phone(Computer):
    def __init__(self, cpu, memory, sim_cards_list):
        super().__init__(cpu, memory)
        self.__sim_cards_list = sim_cards_list

    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def call(self, call_to_number):
        print(f'Идет звонок на номер: {call_to_number} с сим-карты: {self.__sim_cards_list} Beeline')

    def __str__(self):
        return (f'Phone: cpu: {self.get_cpu()}, memory: {self.get_memory()}, '
                f'SIM cards list: {self.__sim_cards_list}')

class SmartPhone(Phone, Computer):
    def __init__(self, cpu, memory, sim_cards_list):
        Phone.__init__(self, cpu, memory, sim_cards_list)
        Computer.__init__(self, cpu, memory)

    def use_gps(self, location):
        print(f'Маршрут до локации {location} сделан')

    def __str__(self):
        return (f'SmartPhone: cpu: {self.get_cpu()}, memory: {self.get_memory()}, '
                f'SIM cards list: {self.get_sim_cards_list()}')

Microsoft = Computer( 13400, 512)
Iphone_12 = Phone(1234, 128, '+996220563789')
PocoX5 = SmartPhone(214, 224, '+996220563789')
Iphone_15 = SmartPhone(2144, 128, '+996220563789')

print(Microsoft)
print(Iphone_12)
print(PocoX5)
print(Iphone_15)

Iphone_12.call('+1234567890')
PocoX5.use_gps('New York')
print("make_computations:", PocoX5.make_computations())
print("Equality:", Iphone_12 == Iphone_15)
print("Not equal:", PocoX5 != Iphone_15)
print("Greater than:", PocoX5 > Microsoft)
print("Less than:", Iphone_12 < PocoX5)
print("Greater than or equal to:", PocoX5 >= Iphone_15)
print("Less than or equal to:", Iphone_15 <= Microsoft)