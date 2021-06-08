def commands():
    print(
        "(action)Введите:\n\trow - для замены двух РЯДОВ\n\tcolumn - для замены двух СТОЛБЦОВ\n\tmin - для нахождения "
        "МИНИМАЛЬНОГО ЧИСЛА\n\tmax - для нахождения максимального числа\n\tq - для выхода из action")


def description():
    print(
        "--------------------------------------------------------\nДоступные команды:\n\t q - завершение "
        "программы\n\t help "
        "- Список доступных программ\n\t action - свап двух РЯДОВ или двух СТОЛБЦОВ матрицы или поиск МИНИМАЛЬНОГО "
        "или МАКСИМАЛЬНОГО чисел "
        "\n--------------------------------------------------------")


def action(tmp):
    a, b = map(int, input("Введите размер квадратной матрицы (через пробел): ").split())
    listt = []

    print("Введите элементы матрицы в зависимости от ее размера (через пробел):\n\tНапример, матрица 2x2 имеет "
          "вид:\n\t\t1 2\n\t\t2 3")
    for i in range(a):
        numbers = list(map(int, input().split()))
        listt.append(numbers)
    commands()
    while True:
        how = input()
        if how == 'q':
            return
        elif how == 'help':
            commands()
        elif how == 'row':
            try:
                c, d = map(int, input("Введите номера двух РЯДОВ для их обмена(нумерация от 1): ").split())
                print("Ваш результат: ")
                listt[c - 1], listt[d - 1] = listt[d - 1], listt[c - 1]
            except ValueError:
                print("Не возможно создать матрицу :(")
                commands()
            for numb in listt:
                print(*numb, end='\n')
            print("Напиши 'help' чтоб увидеть список доступных команд")

        elif how == 'column':
            e, b = map(int, input("Введите номера двух СТОЛБЦОВ для их обмена(нумерация от 1): ").split())
            print("Ваш результат: ")

            for j in range(a):
                listt[j][e - 1], listt[j][b - 1] = listt[j][b - 1], listt[j][e - 1]
            for numb in listt:
                print(*numb, end='\n')
            print("Напиши 'help' чтоб увидеть список доступных команд")
        elif how == 'min':
            min = listt[0][0]
            for i in listt:
                for j in i:
                    if j < min:
                        min = j
            print(f"{min} - минимальное число в заданной матрице")
            print("Напиши 'help' чтоб увидеть список доступных команд")
        elif how == 'max':
            max = listt[0][0]
            for i in listt:
                for j in i:
                    if j > max:
                        max = j
            print(f"{max} - максимальное число в заданной матрице")
            print("Напиши 'help' чтоб увидеть список доступных команд")
        else:
            commands()

