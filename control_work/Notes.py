import os


# Функция для создания новой заметки
def create_note():
    note_title = input("Введите заголовок заметки: ")
    note_content = input("Введите текст заметки: ")

    with open(f"{note_title}.txt", "w") as note_file:
        note_file.write(note_content)
    print(f"Заметка '{note_title}' создана успешно.")


# Функция для чтения списка всех заметок
def list_notes():
    notes = [file.split(".txt")[0] for file in os.listdir() if file.endswith(".txt")]

    if not notes:
        print("Список заметок пуст.")
    else:
        print("Список заметок:")
        for note in notes:
            print(f"- {note}")


# Функция для чтения заметки по её заголовку
def read_note():
    note_title = input("Введите заголовок заметки для чтения: ")

    try:
        with open(f"{note_title}.txt", "r") as note_file:
            note_content = note_file.read()
        print(f"Заметка '{note_title}':\n{note_content}")
    except FileNotFoundError:
        print(f"Заметка с заголовком '{note_title}' не найдена.")


# Функция для редактирования существующей заметки
def edit_note():
    note_title = input("Введите заголовок заметки для редактирования: ")

    try:
        with open(f"{note_title}.txt", "r") as note_file:
            note_content = note_file.read()

        print(f"Заметка '{note_title}':\n{note_content}")

        new_content = input("Введите новый текст заметки: ")

        with open(f"{note_title}.txt", "w") as note_file:
            note_file.write(new_content)
        print(f"Заметка '{note_title}' успешно отредактирована.")
    except FileNotFoundError:
        print(f"Заметка с заголовком '{note_title}' не найдена.")


# Функция для удаления заметки
def delete_note():
    note_title = input("Введите заголовок заметки для удаления: ")

    try:
        os.remove(f"{note_title}.txt")
        print(f"Заметка '{note_title}' успешно удалена.")
    except FileNotFoundError:
        print(f"Заметка с заголовком '{note_title}' не найдена.")


# Основной цикл программы
while True:
    print("\nВыберите действие:")
    print("1. Создать заметку")
    print("2. Список заметок")
    print("3. Читать заметку")
    print("4. Редактировать заметку")
    print("5. Удалить заметку")
    print("6. Выход")

    choice = input("Введите номер действия: ")

    if choice == "1":
        create_note()
    elif choice == "2":
        list_notes()
    elif choice == "3":
        read_note()
    elif choice == "4":
        edit_note()
    elif choice == "5":
        delete_note()
    elif choice == "6":
        print("Программа завершена.")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите действие из списка.")
