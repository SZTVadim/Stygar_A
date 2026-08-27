# Задание 1


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"'{self.title}' автор {self.author}, {self.pages} стр."

    def is_long(self):
        if self.pages > 300:
            return True
        else:
            return False


Book_1 = Book("Руслан и Людмила", "Пушкин", 5)
Book_2 = Book("Тараканище", "Чуковский", 80)
Book_3 = Book("1864", "Оруэлла", 384)

print(Book_1.get_info())
print(Book_2.get_info())
print(Book_3.get_info())

# Задание 2


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return True
        else:
            print("Недостаточно средств")
            return False

    def get_balance(self):
        return self.balance


accounts_1 = BankAccount("Alex", 1000)
accounts_2 = BankAccount("Irina", 300)

accounts_1.deposit(500)
accounts_2.deposit(100)

accounts_1.withdraw(2000)
accounts_2.withdraw(100)

print(accounts_1.get_balance())
print(accounts_2.get_balance())
