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
    "Чорномаз Вікторія Романівна": {
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

# (Руденко Данііл КН-33.2)
# Функція для видалення студента
def remove_student():
    pib = input("Введіть ПІБ студента для видалення: ")
    if pib in students:
        del students[pib]
        print(f"Студента '{pib}' видалено.")
    else:
        print(f"Студент '{pib}' не знайдений в базі даних.")

# (Руденко Данііл КН-33.2)
# Функція для виведення списку студентів
def display_students():
    if not students:
        print("Немає студентів для відображення.")
        return

    for pib, info in students.items():
        print(f"\nПІБ: {pib}")
        print(f"Група: {info['group']}")
        print(f"Курс: {info['course']}")
        print("Оцінки:")
        for subject, grade in info['grades'].items():
            print(f"  {subject}: {grade}")

# (Чорномаз Вікторія КН-33.1)
# Функція для редагування оцінок студента
def edit_grades():
    pib = input("Введіть ПІБ студента, оцінки якого потрібно змінити: ")
    if pib not in students:
        print(f"Студента '{pib}' не знайдено.")
        return

    grades = students[pib]["grades"]
    for subject in grades:
        try:
            new_grade = int(input(f"Введіть нову оцінку за '{subject}' (1-5): "))
            if 1 <= new_grade <= 5:
                grades[subject] = new_grade
            else:
                print("Оцінка повинна бути в діапазоні від 1 до 5.")
        except ValueError:
            print("Оцінка повинна бути числом.")

    print(f"Оцінки студента '{pib}' оновлено.")
# (Глумний Тимур КН-33.2)
# Основне меню для користувача
def main():
    while True:
        print("\nМеню:")
        print("1. Додати нового студента")
        print("2. Показати всіх студентів")
        print("3. Видалити студента")
        print("4. Редагувати оцінки студента")
        print("5. Вийти з програми")

        choice = input("Виберіть дію (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            edit_grades()
        elif choice == "5":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Запуск програми
main()
