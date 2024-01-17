import random


class Character:
    def __init__(self, name, health, damage, speed, level):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed
        self.level = level

    def get_info(self):
        """Вывести характеристики экземпляра класса"""""
        print(f'Character class: {self.name}\nStats: \nHealth: {self.health}\nDamage: {self.damage}\nSpeed: {self.speed}')

    def lvl_up(self):
        self.health = int(self.health + (self.health * 0.1))
        self.damage = int(self.damage + (self.damage * 0.1))
        self.speed = int(self.speed + (self.speed * 0.1))
        self.level += 1

        print(f'lvl up!')

    def test_strike(self):
        """Нанести тестовый удар по манекену"""""
        dummy_health = 1000

        current_hit = random.randint(1, self.damage)
        print(f'{self.name} strikes dummy with {current_hit} damage!\nCurrent dummy health: {dummy_health - current_hit}')


warrior = Character(name='Reckless', health=100, damage=50, speed=10, level=1)
ninja = Character(name='Akari', health=80, damage=70, speed=20, level=1)

warrior.get_info()
print()
warrior.lvl_up()
print()
warrior.get_info()
