import numpy as np

# Создание массива чисел
array = np.array([1, 2, 3, 4, 5])

# Вывод массива
print(array)

# Вычисление суммы элементов массива
sum = np.sum(array)
print(f"Сумма элементов: {sum}")

# Вычисление среднего значения элементов массива
average = np.mean(array)
print(f"Среднее значение: {average}")

# Умножение каждого элемента массива на 2
multiplied_array = array * 2
print(f"Умноженный массив: {multiplied_array}")

# Вычисление квадратных корней элементов массива
square_roots = np.sqrt(array)
print(f"Квадратные корни: {square_roots}")