from enum import Enum
from random import randint, choice


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    BLOCK_DAMAGE_AND_REVERT = 4


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.health} damage: {self.damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        random_hero: Hero = choice(heroes)
        self.__defence = random_hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if hero.ability == SuperAbility.BLOCK_DAMAGE_AND_REVERT \
                        and self.defence != SuperAbility.BLOCK_DAMAGE_AND_REVERT:
                    hero.blocked_damage = 10
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    def __str__(self):
        return f'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def apply_super_power(self, boss, heroes):
        pass

    def attack(self, boss):
        boss.health -= self.damage


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        # Здесь добавим логику крита
        coeff = randint(2, 5)
        boss.health -= (self.damage * coeff)
        print(f'Warrior {self.name} hits critically {self.damage * coeff}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        # Здесь добавим логику буста
        pass


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        # Здесь добавим логику возврата блокированного урона боссу
        boss.health -= self.blocked_damage
        print(f'Berserk {self.name} reverted {self.blocked_damage}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        # Здесь добавим логику лечения
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


round_number = 0


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def show_statistics(boss, heroes):
    print(f'ROUND {round_number} ----------')
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and hero.ability != boss.defence:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def start_game():
    boss = Boss('Maxim', 1000, 50)
    warrior_1 = Warrior('Richard', 280, 20)
    warrior_2 = Warrior('William', 270, 15)
    magic = Magic('Alena', 290, 10)
    berserk = Berserk('Nurbek', 250, 10)
    doc = Medic('Mark', 250, 5, 15)
    assistant = Medic('Charly', 300, 5, 5)

    heroes_list = [warrior_1, warrior_2, magic, berserk, doc, assistant]
    show_statistics(boss, heroes_list)

    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
