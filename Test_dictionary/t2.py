class Animal():
    """Общий класс, описывающий поведение животных"""

    def __init__(self, name, age):
        """Инициализируем атрибуты имя и возраст"""""
        self.name = name.title()
        self.age = age

    def animal_info(self):
        """Получить информацию по собаке"""""
        print(f'Данные животного:\nИмя: {self.name}\nВозраст: {self.age}')


class Dog(Animal):
    """Простая модель собаки"""""

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        """Определить частоту лая собаки по возрасту"""""

        if self.age < 7:
            print(f'Собака {self.name} лает в обычном режиме. Данной собаке {self.age} лет')
        else:
            print(f'Собака {self.name} лает чаще обычного. Данной собаке {self.age} лет')

    def sit(self):
        """Собака будет садиться по команде"""""

        print(f'Собака {self.name} села')

    def jump(self):
        """Собака прыгает по команде, если ее возраст меньше 10-ти лет"""""

        if self.age < 10:
            print(f'Собака {self.name} прыгнула. Данной собаке {self.age} лет')
        elif self.age > 10:
            print(f'Прыжок недоступен для собаки {self.name}. Данной собаке {self.age} лет')

    def animal_info(self):
        """Получить информацию по собаке"""""
        print(f'Данные животного:\nИмя: {self.name}\nВозраст: {self.age}\nПорода: {self.breed.title()}')


buddy = Dog(name='Tabby', age=4, breed='bulldog')
buddy.animal_info()
