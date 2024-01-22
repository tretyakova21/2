# Инициализация переменных для сумм
positive_sum = 0
negative_sum = 0

# Принимаем 15 чисел от пользователя
for i in range(15):
    number = float(input(f"Введите число {i + 1}: "))
    
    if number > 0:
        positive_sum += number
    elif number < 0:
        negative_sum += number

# Вывод результатов
print(f"Сумма положительных чисел: {positive_sum}")
print(f"Сумма отрицательных чисел: {negative_sum}")