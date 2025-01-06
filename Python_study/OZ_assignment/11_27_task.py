# # 과제 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def great(self):
        return f"안녕하세요, 제 이름은 {self.name}입니다. 나이는 {self.age}살입니다."
person = Person('홍길동', 20)
print (person.great())

# # 과제 2
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        return self.height * self.width
rectangle = Rectangle(10, 5)
print  (rectangle.area())

# 과제 3
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f'제목: {self.title}\t저자: {self.author}'
book = Book('파이썬 시작하기', '김경식')
print (book)


# 과제 4
class Employee:
    raise_amounnt = 1.04
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_salary(self):
        self.salary *= self.raise_amounnt
        self.salary = int(self.salary)

김오즈 = Employee('김오즈', 5000)
김이준 = Employee('김이준', 6000)

김이준.raise_amounnt = 1.04
김이준.apply_salary()
김오즈.apply_salary()

print(f"{김오즈.name}의 새로운 급여: {김오즈.salary}")
print(f"{김이준.name}의 새로운 급여: {김이준.salary}")

# # 과제 5
class Account:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print('입금완료!')
        else:
            print('입금액은 0보다 커야합니다.')
    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            print ('출금이 완료 되었습니다.')
        else:
            print('잔액이 부족하거나 출금액이 잘못되었습니다.')
    def get_balance(self):
        return self.__balance
    
account = Account("김이준")
account.deposit(50000)
account.withdraw(30000)
balance = account.get_balance()
print("잔액:", balance)

# # 과제 6
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def display_info(self):
        print(f'이 차량은 {self.make}에서 제조한 {self.model}입니다.')

class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self.payload = payload

    def display_info(self):
        super().display_info()
        print(f"적재량은 {self.payload}입니다.")

class Car(Vehicle):
    def __init__(self, make, model, seats):
        super().__init__(make, model)
        self.seats = seats

    def display_info(self):
        super().display_info()
        print(f"좌석 수는 {self.seats}개입니다.")

my_truck = Truck("현대", "포터", '2톤')
my_truck.display_info()

my_car = Car("현대", "투싼", 5)
my_car.display_info()
