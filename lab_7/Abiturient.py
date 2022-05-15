class Abiturient:
    __medal = "Награжден медалью или грамотой."  # статическое поле , тип private
    defaultPhone = "+1111111"
    indicatorMark = 6

    def __init__(self, id, surname, name, middle_name, adr, phone, mark=0): # инициализатор. Динамические поля
        self.id=id
        self.surname=surname
        self.name=name
        self.middle_name=middle_name
        self.adr=adr
        self.phone=phone
        self.__mark=mark

    @staticmethod  # статический метод
    def __accuracy(mark):   # сделаем метод приватным
        if isinstance(mark, float) or isinstance(mark, int)  and 1 <= mark <= 10: # проверим введенное значени в вызове
            return True # если условие выполняется
        return False

    def setMark(self, mark):  # сеттер. Устновка значения при условии из стат класса
        if Abiturient.__accuracy(mark): # подхватываем результат из статического метода
            self.__mark=mark
        else:
            print(f"Проверьте введенный средний балл у {self.surname}а, возможно превышен диапазон значений, который должен быть от 1 до 10")

    def getMark(self):  # геттер
        return self.__mark

    @classmethod  # метод класса
    def awards(cls):
        return (cls.__medal)

    def abData(self):       # метод экземпляра класса обьекта
        print(f"Абитуриент {self.surname} {self.name} имеет средний балл {self.__mark}")
        if self.__mark >= 8:
            print(self.awards(), "\n")


    @classmethod  # используем метод класса для проверки типа данных
    def verData(cls, other):
        if not isinstance(other, Abiturient):  # проверка , что other имеет тип  int или экземпляра класса
            raise TypeError(" тип не соответствует")
        return other if isinstance(other, (int, float)) else other.__mark

    def __gt__(self, other):
        mk = self.verData(other)
        if self.indicatorMark > mk:
            print(f"{self.name} {self.surname} имеет неудовлетворительные оценки?" )
            return self.indicatorMark > mk
        else:
            return " "

    def __lt__(self, other):
        mk = self.verData(other)
        if self.indicatorMark < mk:
                print(f"{self.name} {self.surname} не имеет неудовлетворительные оценки?" )
                return self.indicatorMark < mk
        else:
            return " "

    def __add__(self, other):
        mk = self.verData(other)
        return ((self.__mark + mk) / 2) # посчитаем средний балл двух абитуриентов

    def __getattribute__(self, item): #  с помощью метода може обратится к какому-либоа трибуту
        if item == "adr":  # например, для запрета прямого вызова этого атрибута
            raise ValueError("Нельзя получить это значение")
        else:
            return object.__getattribute__(self, item)  # к любому другому сможем обратиться
        # для этого создадим переменную ed? и попытаемся обратиться к ней

    def __getattr__(self, item): # обратимся к несуществующему полю
        return False    # выдаст False , вместо стандартной ошибки - AttributeError: 'Abiturient' object has no attribute 'f'

    def  __delattr__(self, item):
        object.__delattr__(self, item) # переопределим метод через верхний класс object

    def __str__(self):
        return (f" Name {self.name} Phone {self.phone}")  # вывод в строковом значении


ivan=Abiturient('1', "Иванов", "Иван", "Иванович","Минск Независимости 100", "+123456")
petr=Abiturient("2", "Петров", "Петр", "Петрович","Минск Победителей 50", "+234567")
igor=Abiturient("3", "Игорьев", "Игорь", "Игорьевич","Минск Пушкина 20", "+345678")
artem=Abiturient("3", "Артемов", "Артем", "Артемович","Минск Машерова 10", "+456789")

ivan.setMark(9)  ## установим  средний балл для Ивана в сеттер
petr.setMark(8.5)  ## установим  средний балл для Петра в сеттер
igor.setMark(4)  ## установим  средний балл для Петра в сеттер
artem.setMark(5)

# ivan.setMark(12) #  выдаст сообщение о неправильном вводе значения

# ivan.abData()  # вызов метода класса   В данном случае число >8 , что вызывет функцию surn_addate
# Abiturient.abData(petr)  # вызов обращения через класс
# artem.abData()
# igor.abData()
# print(artem.__dict__)  # вызов для проверки словаря  ивана

# print(ivan.__gt__(ivan), "\n") # None  #  вызов для __lt__ и __gt__
# print(petr.__gt__(petr), "\n") # None
# print(igor.__gt__(igor), "\n") # True
# print(artem.__gt__(artem), "\n") # True
#
# print(ivan.__lt__(ivan), "\n") # True
# print(petr.__lt__(petr), "\n") # True
# print(igor.__lt__(igor), "\n") # None
# print(artem.__lt__(artem), "\n") # None


# print(ivan.getMark())  #  вызов  геттера на консоль
# print(ivan.__dict__)  # вызов на консоль в формате словаря свойств по текущему экз. класса
# print(getattr(petr, "adr"))  # вызов информации по полю adr (адрес) , экз. класса petr
#
# print(artem.f)  # обращение к несуществующему полю через метод __getattr__  Вернет False
#
# del artem.mark  # вызов функции  __delattr__  который удалит атрибут mark для обьекта artem
#
# # пример вызова __getattribute__
# print(igor.adr)  # выдаст  "ValueError: Нельзя получить это значение"    Прописанное в методе

# print(artem, ivan) # вызов __str__   -   Name Артем Phone +456789  Name Иван Phone +123456

# print(artem.__add__(petr))   # вызов add с расчетом средноге балла двух абитуриентов