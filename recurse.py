a = int(input("Введите длину одной стороны \n "))
b = int(input("Введите длину второй стороны \n "))

if a!=b:
    print("Из прямоугольника со сторонами",a,"и",b, )
    side=[]  ## список для заполнения и хранения длин сторон при каждой итерации

    def makesq(a, b, n):
        if a==b:
            side.append(a)
            print("можно получить", n + 1, "квадрата (ов), со длинами сторон -",side, "соответственно")
            return
        elif a>b:
            side.append(b)
            makesq(a - b, b, n + 1)  # условие урезания стороны прямоугольника с увел прохода
        elif b>a:
            side.append(a)
            makesq(a, b - a, n + 1)

    makesq(a,b, n=0)

else:
    print(("Стороны равны. а значит фигура - квадрат! и она одна)"))

# иными способами не получается адекватно получать или выводить результаты в консоль
