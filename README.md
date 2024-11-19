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
