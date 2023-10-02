import json
import os
from datetime import datetime

# Путь к файлу с заметками
NOTES_FILE = "notes.json"

# Проверка существования файла с заметками
if not os.path.exists(NOTES_FILE):
    with open(NOTES_FILE, "w") as f:
        json.dump([], f)

# Функция для добавления заметки
def add_note():
    title = input("Введите заголовок заметки: ")
    message = input("Введите текст заметки: ")

    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_note = {"id": len(notes) + 1, "title": title, "message": message, "timestamp": timestamp}

    notes.append(new_note)

    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)

    print("Заметка успешно добавлена.")

# Функция для вывода списка заметок
def list_notes(date_filter=None):
    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)

    if date_filter:
        filtered_notes = [note for note in notes if note["timestamp"].startswith(date_filter)]
        if not filtered_notes:
            print("Заметок с выбранной датой не найдено.")
        else:
            print("Заметки с выбранной датой:")
            for note in filtered_notes:
                print(f"{note['id']}. {note['title']} ({note['timestamp']})")
    else:
        if not notes:
            print("Список заметок пуст.")
        else:
            print("Список заметок:")
            for note in notes:
                print(f"{note['id']}. {note['title']} ({note['timestamp']})")


# Функция для чтения заметки по ID
def read_note():
    note_id = int(input("Введите ID заметки для чтения: "))

    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)

    for note in notes:
        if note["id"] == note_id:
            print(f"Заметка {note['id']} ({note['timestamp']}):\n{note['title']}\n{note['message']}")
            return

    print(f"Заметка с ID {note_id} не найдена.")


# Функция для редактирования заметки по ID
def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))

    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)

    for note in notes:
        if note["id"] == note_id:
            title = input("Введите новый заголовок: ")
            message = input("Введите новый текст: ")
            note["title"] = title
            note["message"] = message
            note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(NOTES_FILE, "w") as f:
                json.dump(notes, f, indent=4)

            print(f"Заметка {note['id']} успешно отредактирована.")
            return

    print(f"Заметка с ID {note_id} не найдена.")


# Функция для удаления заметки по ID
def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))

    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)

    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            with open(NOTES_FILE, "w") as f:
                json.dump(notes, f, indent=4)
            print(f"Заметка {note_id} успешно удалена.")
            return

    print(f"Заметка с ID {note_id} не найдена.")


# Основной цикл программы
while True:
    print("\nВыберите действие:")
    print("1. Добавить заметку")
    print("2. Список заметок")
    print("3. Читать заметку")
    print("4. Редактировать заметку")
    print("5. Удалить заметку")
    print("6. Выход")

    choice = input("Введите номер действия: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        date_filter = input(
            "Введите дату (год-месяц-день) для фильтрации (или нажмите Enter для вывода всех заметок): ")
        list_notes(date_filter)
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
