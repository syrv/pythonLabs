#7 Скопировать из файла F1 в файл F2 все строки, которые содержат только одно слово.
# Найти самое длинное слово в  файле F2.

f = open("test.txt", "w")  #создание  нового файла и заполнение
f.write("Она пришла с мороза,\n"  # dввод данных в файл №1
"Раскрасневшаяся,\n"
"Наполнила комнату\n"
"Ароматом воздуха и духов,\n"
"Звонким голосом\n"
"И совсем неуважительной к занятиям\n"
"Болтовнёй.\n"
"(А. Блок)")
f.close()

f = open("test.txt", "r")   # открытие и считывание
print(f.read())
f.close()


f2 = open("test2.txt", "a")  # открываем второй файл


with open("test.txt", "r") as file1:
    while True:  # проводим итерацию по строкам
        line = file1.readline()  # используя метод readline
        index = line.find(" ")  # далее ищем строку с подходящим индексом (пробелом)
        if index == -1:    # если такового нет, то индекс будет равен -1
            f2.write(line)  # и такую строку вписываем в 2-ой файл
        if not line:  # если же строки больше нет ,то выходим из цикла
            break
f2.close()  # закрываем 2-ой файл

f2 = open("test2.txt", "r")   # открытие и считывание 2-ой файл
print(f2.read())
f2.close()


f2 = open("test2.txt", "r") # открываем 2-ой файл для чтения
longestWord = f2.readlines()  # считываение файла в формат списка
print (f"Самое длинное слово в файле f2 : {max(longestWord)}")  # сравнение элементов списка функцией max
f2.close()

  # или так

with open("test2.txt", "r") as file2:
    longestWord = file2.readlines()  # считываение файла в формат списка
    print(f"Самое длинное слово в файле f2 : {max(longestWord)}")  # сравнение элементов списка функцией max