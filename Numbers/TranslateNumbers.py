# Программа, которая преобразовывает числа.

number = int(input("Введите число для преобразовывания: "))
result2 = bin(number)
result8 = oct(number)
result16 = hex(number)

print(f"Двоичная система счисления: {result2[2:]}")
print(f"Восьмеричная система счисления: {result8[2:]}")
print(f"Шестнацатеричная системе счисления: {result16[2:]}")