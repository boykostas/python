import webbrowser
import hashlib
import os
import tkinter as tk


def check_password_strength(password):
    """
   Написать программу на Python, которая проверяет вводимый пользователем пароль на сложность:
— не менее 8 символов
— наличие прописных и строчных букв
— наличие цифр
и переводит его в хэш-значение.
    """
    if len(password) < 8:
        return "Пароль слишком короткий. Минимальная длина - 8 символов."

    if not any(c.isupper() for c in password) or not any(c.islower() for c in password):
        return "Пароль должен содержать как прописные, так и строчные буквы."

    if not any(c.isdigit() for c in password):
        return "Пароль должен содержать хотя бы одну цифру."


    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def on_check_button_click():
    user_password = password_entry.get()
    hashed_result = check_password_strength(user_password)
    if hashed_result:
        hash_label.config(text=f"Хэш-значение вашего пароля: {hashed_result}")
        # Записываем хэш-значение в файл
        with open("password_hash.txt", "w") as file:
            file.write(hashed_result)
    else:
        print()


root = tk.Tk()
root.title("Проверка пароля и хэширование")

password_label = tk.Label(root, text="Введите пароль:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

check_button = tk.Button(root, text="Проверить сложность", command=on_check_button_click)
check_button.pack()

hash_label = tk.Label(root, text="")
hash_label.pack()

root.mainloop()
