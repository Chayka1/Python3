def task_1_1():
    name = ['Энштейн', 'Ньютон', 'Коперник', 'Кеплер']

    print(name)

def task_1_2():
    names = ['Максим', 'Архип', 'Андрей', 'Женя']

    for name in names:
        print(name)

def task_1_3():
    numbers1 = list(range(100))
    numbers2 = []

    for num in numbers1:
        numbers2.append(num)

    print(f'numbers1 = {numbers1} \nnumbers2 = {numbers2}')

def task_1_4():
    total = 0
    numbers = list(range(5))

    for num in numbers:
        total += num

    print(f'Сумма чисел в списке {numbers} равна {total}')

def task_1_5():
    total = 0
    numbers = list(range(-5, 5))

    for num in numbers:
        total += num

    print(f'Сумма чисел в списке {numbers} равна {total}')

def task_1_6():
    names = ['Максим', 'Руби', 'Андрей', 'Женя']

    if 'Руби' in names:
        print('Привет, Руби!')
    else:
        print('Руби отсутствует!')

def task_1_7():
    list1 = [40, 50, 60]
    list2 = [10, 20, 30]
    list3 = list1 + list2
    print(list3)

#def task(): f
    #lst=[[int(input("x["+str(i)+","+str(j)+"]=")) for j in range(3)] for i in range(5)]

def task_1_8():
    numbers = [[0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0]]

    for j in range(5):
        for i in range(3):
            numbers[j][i] = int(input(f'x[{i},{j}] = '))

    for num in numbers:
        print(num)



