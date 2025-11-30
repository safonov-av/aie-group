


#--------HW01----------#
import numpy as np

print(f"NumPy version: {np.__version__}")

#--- 2. Создание массивов

list_data = [10, 20, 30, 40, 50]
arr_from_list = np.array(list_data)

arr_zeros = np.zeros((3, 4))

arr_arange = np.arange(0, 21, 2)

print("Массив из списка:", arr_from_list)
print("Массив нулей (3x4):\n", arr_zeros)
print("Массив arange:", arr_arange)

#--- 3. Демонстрация атрибутов массива

test_matrix = np.ones((5, 2))

print("Массив:\n", test_matrix)
print(f"Форма массива (shape): {test_matrix.shape}") # (5, 2)
print(f"Тип данных (dtype): {test_matrix.dtype}")
print(f"Количество измерений (ndim): {test_matrix.ndim}")

#--- 4. Индексирование и срезы

data = np.array([100, 200, 300, 400, 500, 600])

element = data[2]
print(f"Элемент с индексом 2: {element}")

slice_arr = data[1:4]
print(f"Срез [1:4]: {slice_arr}")

step_slice = data[::2]
print(f"Каждый второй элемент: {step_slice}")

arr_a = np.array([1, 2, 3, 4, 5])
arr_b = np.array([5, 4, 3, 2, 1])

arr_sum = arr_a + arr_b
print(f"Сумма массивов: {arr_sum}")

arr_mult = arr_a * 10
print(f"Умножение массива A на 10: {arr_mult}")

mean_val = np.mean(arr_a)
max_val = np.max(arr_a)
std_val = np.std(arr_a)

print(f"Среднее значение A: {mean_val}")
print(f"Максимальное значение A: {max_val}")
print(f"Стандартное отклонение A: {std_val:.2f}")