# (Глумний Тимур КН-33.2)
# Словник для зберігання даних про студентів
students = {
    "Глумний Тимур Вікторович": {
        "group": "КН-33.2",
        "course": 2,
        "grades": {
            "Програмування": 5,
            "Алгоритми": 4,
            "Чисельні методи": 4
        }
    },
    "Руденко Данііл Вадимович": {
        "group": "КН-33.2",
        "course": 2,
        "grades": {
            "Математичні методи": 5,
            "Чисельні методи": 4
        }
    },
    "Чорномаз Вікторія Батьківна": {
        "group": "КН-33.1",
        "course": 2,
        "grades": {
            "Математичні методи": 4,
            "Чисельні методи": 4
        }
    }
}

# (Глумний Тимур КН-33.2)
# Функція для додавання нового студента
def add_student():
    pib = input("Введіть ПІБ студента: ")
    if pib in students:
        print(f"Студент '{pib}' вже є в базі даних.")
        return
    
    try:
        group = input("Введіть групу студента: ")
        course = int(input("Введіть курс студента (число): "))
        subject_count = int(input("Кількість предметів: "))

        grades = {}
        for _ in range(subject_count):
            subject = input("Назва предмета: ")
            grade = int(input(f"Оцінка за предмет '{subject}' (1-5): "))
            grades[subject] = grade

        students[pib] = {
            "group": group,
            "course": course,
            "grades": grades
        }
        print(f"Студента '{pib}' успішно додано.")
    except ValueError:
        print("Невірний формат введених даних. Спробуйте ще раз.")
