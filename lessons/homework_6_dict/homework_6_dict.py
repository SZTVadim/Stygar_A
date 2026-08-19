# Задание 1
student = {
    "name": "Иван",
    "age": 20,
    "course": 2,
    "city": "Москва"
}
print(student.keys())
print(student.values())

for key, value in student.items():
    print(f"{key}: {value}")

for value in student.values():
    print(value)

# Задание 2
student1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}
student3 = student1 | student2

student1.update(student2)

print(student1)
print(student2)
print(student3)
