def filter_symbol(values, filter = 3):
    result = []
    for value in values:
        if len(value) <= filter:
            result.append(value)
    return result

values = input("Введите строки через пробел: ").split()
result = filter_symbol(values)
print(f'Введённые слова:\n{values}.\n\nОтсортированные слова:\n{result}.')
