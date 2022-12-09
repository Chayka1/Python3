import sys
from main import *

while True:
    print('1. Алгоритмичный тренажер \n' + '2. Задачи по програмированию \n' + '0.Выход из меню')
    exercise = input()

    if exercise == '1':
        while True:
            print('1. Напишите инструкцию, которая создает список с приведенными далее строковыми зна­ чениями: \'Эйнштейн\', \'Ньютон\', \'Коперник\' и \'Кеплер\'.\n' +
                  '2. Допустим, что переменная names ссылается на список. Напишите цикл for, который вы­ водит каждый элемент списка.\n' +
                  '3. Напишите инструкцию if-else, которая присваивает значение О переменной b, если переменная а меньше 1О. В противном случае она должна присвоить переменной b значение 99.\n' +
                  '4. Составьте блок-схему, которая демонстрирует общую логику суммирования значений в списке.\n' +
                  '5. Напишите функцию, которая принимает список в качестве аргумента (допустим, что спи­ сок содержит целые числа) и возвращает сумму значений в списке.\n' +
                  '6. Допустим, что переменная n a r n e s ссылается на список строковых значений. Напишите программный код, который определяет, находится ли имя\n' +
                  '7. Что напечатает приведенный ниже фрагмент кода?\n' +
                  '8. Напишите инструкцию, которая создает двумерный список с 5 строками и 3 столбцами. Затем напишите вложенные циклы, которые получают от пользователя целочисленное значение для каждого элемента в списке.\n' +
                  '0.Назад')
            exercise_1 = input()

            if exercise_1 == '1':
                task_1_1()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')

                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '2':
                task_1_2()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')

                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '3':
                task_1_3()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')

                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '4':
                task_1_4()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')

                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '5':
                task_1_5()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')

                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '6':
                task_1_6()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')

                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '7':
                task_1_7(1)
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')

                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '8':
                task_1_8()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')

                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_1 == '0':
                break

            else:
                print('Ошибка, введите правильное значение!')

    elif exercise == '2':
        while True:
            print('1. Общий объем продаж.\n'
                  '2. Генератор лотерейных чисел.\n'
                  '3. Статистика дождевых осадков.\n'
                  '4. Проrрамма анализа чисел.\n'
                  '5. Проверка допустимости номера расходноrо счета.\n'
                  '6. Больше числа п.\n'
                  '7. Экзамен на получение водительских прав.\n' +
                  '0.Назад')
            exercise_2 = input()

            if exercise_2 == '1':
                task_2_1()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')

                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_2 == '2':
                task_2_2()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')

                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_2 == '3':
                task_2_3()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')

                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_2 == '4':
                task_2_4()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')

                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_2 == '5':
                task_2_5()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')

                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_2 == '6':
                task_2_6()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')

                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            elif exercise_2 == '7':
                task_2_7()
                print('-----------------------------------------------')
                action = input('1.Выход из меню\n' + '0.Назад\n')

                while True:
                    if action == '1':
                        sys.exit()

                    elif action == '0':
                        break

            else:
                print('Ошибка, введите правильное значение!')

    elif exercise == '0':
        sys.exit()

    else:
        print('Ошибка, введите правильное значение!')