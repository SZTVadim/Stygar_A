# ЗАДАНИЕ 1
fruits = ["яблоко"]
fruits.append("банан")
print(fruits)

fruits.extend(["апельсин", "груша"])
print(fruits)

fruits.insert(1, "виноград")
print(fruits)

# ЗАДАНИЕ 2
fruits = ["яблоко", "банан", "апельсин", "банан"]
fruits.remove("банан")
print(fruits)

last = fruits.pop()
print(last)
print(fruits)

# ЗАДАНИЕ 3
fruits = ["яблоко", "банан", "апельсин", "банан"]
print(fruits.index("банан"))
print(fruits.count("банан"))

# ЗАДАНИЕ 4
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)
