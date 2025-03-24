class Dog:
    # атрибуты класса (общие для всех объектов)
    def __init__(self, name, age, breed, weight):
        self.name = name  # (строка) - имя собаки.
        self.age = age  # (целое число) - возраст собаки в годах
        self.breed = breed # (строка) - порода собаки
        self.weight = weight   # (число с плавающей запятой) - вес собаки в килограммах.
        self.is_vaccinated = False   # (логическое значение) - статус вакцинации собаки (True или False).
    # методы объекта
    def bark(self): # - метод, который возвращает строку, имитирующую лай собак
        return 'Гав-гав'

    def get_human_age(self): # метод, который возвращает возраст собаки в «человеческих годах» (умножив на 7)
        return self.age * 7

    def vaccinate(self): # -метод, который устанавливает статус вакцинации собаки на True
        self.is_vaccinated = True

    def description(self): # метод, который возвращает строку с информацией о
                          # собаке (имя, возраст, порода, вес, статус вакцинации)
        status_vaccinate = 'вакцинирована' if self.is_vaccinated else 'не вакцинирована'
        return (f'Имя: {self.name}, возраст (количество лет): {self.age}, порода: {self.breed}, вес (кг): {self.weight}, статус вакцинации: {status_vaccinate}')

dog_1 = Dog(name='Эльба', age=3, breed='немецкая овчарка', weight=5.5)
dog_1.vaccinate()
print(dog_1.description())
print('"Человеческий" возраст - ', dog_1.get_human_age())
print(dog_1.bark())
