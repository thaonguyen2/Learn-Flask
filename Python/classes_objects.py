lottery_player_dict = {
    'name': 'Roft',
    'numbers': (5, 9, 12, 3, 1, 21)
}

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)

player = LotteryPlayer("Rolf")
print(player.name)
print(player.total())

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    def go_to_school1(self):
        print("I'm going to {}.".format(self.school))

    @classmethod
    def go_to_school2(cls):
        print("I'm going to school 2.")
        print("I'm a {}".format(cls))

    @staticmethod
    def go_to_school3():
        print("I'm going to school 3.")

anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(44)
# call class method
anna.go_to_school2()
# call static method
Student.go_to_school3()
Student.go_to_school2()

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        item = {'name': name, 'price': price}
        self.items.append(item)

    def stock_price(self):
        return sum(item['price'] for item in self.items)

    @classmethod
    def franchise(cls, store):
        new_store = cls("{} - franchise".format(store.name))
        return new_store

    @staticmethod
    def store_details(store):
        return "{}, total stock price {}".format(store.name, int(store.stock_price()))

store1 = Store("Blue")
store2 = Store.franchise(store1)
print(Store.store_details(store2))