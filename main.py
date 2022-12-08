import random
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
            numbers[j][i] = int(input(f'x[{j},{i}] = '))

    for num in numbers:
        print(num)

def task_2_1():
    total = 0
    sell = []

    for day in range(1, 8):
        price = int(input(f'Введите продажи за {day} день: '))
        sell.append(price)

    for price_ in sell:
        total += price_

    print(f'Общий объем продаж составляет {total}')

def task_2_2():
    numbers = []

    for num in range(8):
        num = random.randint(0, 9)
        numbers.append(num)

    for numbers_ in numbers:
        print(numbers_)

def task_2_3():
    total = 0
    rain = []

    for month in range(1, 13):
        rain_of_month = int(input(f'Введите количество осадков за {month} месяц: '))
        rain.append(rain_of_month)
        total += rain_of_month


    print(f'Сумарное количество осадков за год составило {total} \n'
          f'Самое минимальное значение осадков составило {min(rain)} \n'
          f'Самое максимальное значение осадков составило {max(rain)}')

def task_2_4():
    total = 0
    numbers = []

    for num_ in range(1, 21):
        num = int(input(f'Введите {num_} число: '))
        total += num
        numbers.append(num)

    s_a = total / len(numbers)

    print(f'Самое минимальное число: {min(numbers)} \n'
          f'Самое максимальное число: {max(numbers)} \n'
          f'Сумма всех чисел: {total} \n'
          f'Среднее арифметическое всех чисел: {round(s_a, 2)}')

def task_2_5():
    print('error')

def task_2_6():
    nums = []
    spisok = int(input('Введите диапазон списка: '))
    n = int(input('Введите число n: '))

    for num in range(spisok + 1):
        nums.append(num)

    for num_ in nums:
        if n < num_:
            print(num_)

