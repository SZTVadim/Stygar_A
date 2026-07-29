# Задание 1

text = "Привет"
number_1 = 42
number_2 = 3.14
list_ = [1, 2, 3]

print(type(text))
print(type(number_1))
print(type(number_2))
print(type(list_))

# Задание 2
conversion = "python PROGRAMMING"
lower_text = conversion.lower()
upper_text = conversion.upper()
capitalized_text = conversion.capitalize()
title_text = conversion.title()

print(lower_text)
print(upper_text)
print(capitalized_text)
print(title_text)

# Задание 3
print(" Hello World ".strip())
print(" Hello World ".lstrip())
print(" Hello World ".rstrip())

# Задание 4
text = "яблоко,банан,апельсин,груша"
fruits = text.split(",")
print(fruits)

text = " | ".join(fruits)
print(text)

# Задание 5
text_1 = "Я изучаю Python. Python - это круто!"
new_text_1 = text_1.replace("Python", "Java")
print(new_text_1)

# Задание 6
text_search = "Python программирование на Python"
print(text_search.index("Python"))
print(text_search.count("Python"))
print(text_search.find("Java"))

# Задание 7
print("Hello123".isalnum())
print("12345".isdigit())
print("Hello".isalpha())
print("  ".isspace())

# Задание 8
text_by_srez = "Python very good"
print(text_by_srez[:3])
print(text_by_srez[-3:])
print(text_by_srez[::2])
print(text_by_srez[::-1])

# Задание 9
print("Он сказал: \"Привет\"")
print("Первая строка\nВторая строка")
