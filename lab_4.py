
class Abiturient:
    __medal = "Награжден медалью или грамотой."  # статическое поле , тип private

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


ivan=Abiturient('1', "Иванов", "Иван", "Иванович","Минск Независимости 100", "+123456")
petr=Abiturient("2", "Петров","Петр","Петрович","Минск Победителей 50", "+234567")

ivan.setMark(8.7)  ## установим  средний балл для Ивана в сеттер
petr.setMark(7.5)  ## установим  средний балл для Петра в сеттер

# ivan.setMark(12) #  выдаст сообщение о неправильном вводе значения

ivan.abData()  # вызов метода класса   В данном случае число >8 , что вызывет функцию surn_addate
Abiturient.abData(petr)  # вызов обращения через класс

# print(ivan.getMark())  #  вызов  геттера на консоль
# print(ivan.__dict__)  # вызов на консоль в формате словаря свойств по текущему экз. класса
# print(getattr(petr, "adr"))  # вызов информации по полю adr (адрес) , экз. класса petr


