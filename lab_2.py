
################ ЛАБ. 2
# Задание 1. Задачи на одномерные списки
# Вариант 4
# Найдите произведение элементов списка с нечетными номерами.
# Найдите наибольший элемент списка, затем удалите его и выведите новый
# список.

## РЕШЕНИЕ
# import random
# import copy
#
# list=[random.randrange(1,30) for i in range (7)] # рандомно заполняем список
#
# odd=[] # список для нечетных номеров
# for i in list:  # находим нечетный номера и помещаем в список
#     if i%2 == 1:
#         odd.append(i)
#
# prod=1
# for j in range(len(odd)):   # поиск произведения списка
#     prod*=odd[j]
#
# wo_max=copy.deepcopy(odd)  # копируем "глубоким копированием" первоначальный список, чтоб он не изменился вслед
# wo_max.remove(max(wo_max))  #  удаляем максимальное число
#
# print(str(list)+"- список заданный рандомно")
# print(str(odd)+" - список отобранных нечетных чисел")
# print(str(prod)+" - произведение нечетных чисел")
# print(str(wo_max)+" - новый список без максимального значения")


# Задание 2. Задачи на многомерные списки
# Вариант 3. Даны две квадратных таблицы чисел. Требуется построить третью,
# каждый элемент которой равен сумме элементов, стоящих на том же
# месте в 1-й и 2-й таблицах.

# ## РЕШЕНИЕ
# import random
# import numpy as np
# first=0  # указываем НАЧАЛЬНОЕ число диапазона знач для  матриц
# last=49   # указываем ПОСЛЕДНЕЕ число диапазона знач для  матриц
# s=10  # размер матрицы
# matrixs=[]  # инициализация списка для матриц
#
# n=1
# for j in range(2):
#     n = np.array([[random.randrange(first,last) for i in range(s)] for i in range(s)])  # заполнняем матрицы рандомно
#     matrixs.append(n)
#     print("\n Матрица " + str(j+1) + "\n" + str(n))

# sumtrx=sum(matrixs)
# print("\n Матрица 3 показывает сумму 1-ой и 2-ой матриц поэлементно \n " + str(sumtrx))
