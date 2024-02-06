'''
name = "Игорь"

def homo(name, age=21):
	result = f"Hello {name}, you're {age} years old now! In 2 years you will already {age + 2}."
	return result

result = homo(name)
print(result)
'''

'''
def greet(name, gre="Hello"):
    print(gre, name)

# Вызов функции без указания значения для параметра greeting
greet("Игорь")  # Вывод: Hello John

# Вызов функции с явным указанием значения для параметра greeting
# greet("Игорь", "Hi")  # Вывод: Hi Alice
'''

'''
def power(base, exponent=2):
    result = base ** exponent
    return result

# Вызов функции с одним и двумя параметрами
result1 = power(3)
result2 = power(3, 3)
result3 = power(5, 2)

print("3 в квадрате:", result1)
print("3 в 3 степени:", result2)
print("5 в 5 степени:", result3)
'''

'''
def example_function():
    print("Привет из функции!")

# Вызов функции
example_function()
'''

'''
class Dog:
    # Конструктор класса
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Метод класса
    def bark(self):
        print(f"{self.name} says Woof!")

    # Еще один метод класса
    def celebrate_birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old!")

# Создание экземпляра класса
my_dog = Dog(name="Buddy", age=3)

# Использование методов класса
my_dog.bark()
my_dog.celebrate_birthday()

# Доступ к атрибутам класса
print(f"{my_dog.name} is {my_dog.age} years old.")
'''

class House():
		'''описание дома'''
		def __init__(self, street, number):
			'''свойства дома'''
			self.street = street
			self.number = number
			self.HouseAge = 0

		def build(self):
			'''статус дома, построен или нет'''
			print(f"Дома на улице {self.street} под номером {self.number} построен!")

		def age_of_House(self, year):
			'''типо возраст дома'''
			self.HouseAge += year


class ProspectHouse(House):     # Дочерний класс ProspectHouse, наследованние из основного класса House
	'''дома на проспекте кароч'''
	def __init__(self, number, prospect):
		super().__init__(self, number)
		self.prospect = prospect

PrHouse = ProspectHouse("Ленина", 2)
print(PrHouse.prospect)


		