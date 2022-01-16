
################   ЛАБ. 1
# # задание 1
# # задача 15 Определить есть ли среди заданных целых чисе A, B, C, D хотя бы одно чётное.

##  РЕШЕНИЕ
##### (Нужно выбрать и активировать один  из двух вариантов ввода чисел :авто или  вручную!)
####     Ввод чисел автоматически рандомно
import random
print("  Рандомно автоматически задано 4 числа: A, B, C, D. \n Проверим их на наличие четного числа! \n" )
list=[random.randint(-10, 10) for i in range(4)]

# ####     Ввод чисел вручную
# # abcd=["A", "B", "C", "D"]
# # list=[]
# # for i in range(len(abcd)):
# #     a = int (input("Введите число: " + abcd[i]+ "\n "))
# #     list.append(a)

import time
print(" Идет поиск четного числа, подождите!  \n")  ## немного приукрасим, для антуража)
time.sleep(3)

i = 0
while i<= 3:
    if (list[i]) % 2 == 0:
        print("             Ура, четное число найдено!\n ")
        break
    i += 1
else:
    print("         Увы, четного числа нет!\n")

choice = input(" Для просмотра заданного списка чисел нажмите - Y \n Для выхода из программы - любую другую клавишу ")
while choice.lower() == "y":
    print("\n Были введены следующие числа:")
    for i in range(4):
        print(list[i], end="\t    ")
    break
print("\n Работа программы завешена!")



# задание 2.вариант 4. Торговая фирма в первый день работы реализовала товаров на P тыс. руб., а затем ежедневно увеличивала
# выручку на 3%. Какой будет выручка фирмы в тот день, когда она впервые превысит заданное значение Q? Сколько
# дней придется торговать фирме для достижения этого результата?

## РЕШЕНИЕ
#### ВАРИАНТ решения № 1  С ПОСТОЯННЫМ УВЕЛИЧИВАЮЩИМСЯ ДОХОДОМ В 3% ОТ ПЕРВОГО ДНЯ
income_day = int (input("Введите сумму дохода в первый день "+ "\n "))
q = int (input("Введите планируемую валовую сумму дохода, для расчета количества дней, при ежедневном увеличении дохода равном 3% "+ "\n "))
val_income = []    # инициализируем список
inc_nex_days = income_day # инициализируем переменную ежедневного дохода

sum_income_day = 0 # иниц. переменной суммы дохода за все дни
i=1.03   # иниц. счетчик нач. множителя = 3%
while sum_income_day < q:
    val_income.append(inc_nex_days)
    inc_nex_days= income_day*i   # ведем счет овсегла от начального значения(первый день)
    i+=0.03  #  далее увеличиваем счетчик на 3%
    sum_income_day += inc_nex_days  # считаем общ.сумму прибавляя сумму каждого дня

print(val_income)
print("Валовой доход при ежедневном росте дохода в 3% составит : "+str(round(sum_income_day,2)))   # сумма валовая
print("Потребуется " + str(len(val_income)) + " дня(ей), чтоб достичь планируемую сумму" +str(q))  # количество элементов списка, те. дней для задачи

#### ВАРИАНТ решения № 2 С ОДИНАКОВЫМ РЕГУЛЯРНЫМ ДОХОДОМ 3% ПОСЛЕ ПЕРВОГО ДНЯ
income_day = int (input("Введите сумму дохода в первый день "+ "\n "))
q = int (input("Введите валовую сумму дохода, для расчета количества дней, при ежедневном увеличении дохода равном 3% "+ "\n "))
val_income = [income_day, ]
inc_nex_days = income_day * 1.03

sum_income_day = income_day
while sum_income_day < q:
    val_income.append(inc_nex_days)
    sum_income_day += inc_nex_days

# print(sum_income_day)   # сумма валовая
print(val_income)
print("Валовой доход в 3% при ежедневном одинаковом доходе после первого дня составит : "+str(round(sum_income_day,2)))
# print(len(val_income))  # количество элементов списка, те. дней для задачи
print("Потребуется " + str(len(val_income)) + " дня(ей), чтоб достичь планируемую сумму" +str(q))  # количество элементов списка, те. дней для задачи


# задание 3. Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
# # Размер списка n ввести с клавиатуры. В соответствии со своим вариантом написать программу по условию,
# # представленному в таблице ниже.
### вариант 6      Удалить все элементы с заданным значением, если они имеются в списке.

# ## РЕШЕНИЕ
import random
B= int (input("Введите размер списка\n"))
A= [random.randint(0,99) for i in range (B)]
print(A)
i = 25 # задаем значение для поиска

if i in A:
    while i in A:
        A.remove(i)
        print("Число " +str(i)+ " удалено")
    print(A)
else:
    print("Число " +str(i)+ " не найдено")

### + Вариант 8     Найти значение максимального элемента списка.
print("Максимальное значение списка: " +str(max(A)))



