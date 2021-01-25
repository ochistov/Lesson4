from itertools import count, cycle #импорт функций count() и cycle() из модуля itertools

################################## Первый скрипт - задание а) ############################################
'''
Entering the first and last number of the list, 
as well as the step, handling the "error type" error
------------------------------------------------------
Ввод первого и последнего числа списка, шага, 
обработка ошибки "ValueError"
'''
while True:
    try:
        start = int(input("Insert first number: "))
        stop = int(input("Insert last number: "))
        step = int(input("Insert step: "))
    except:
        print("That's not an integer number!\nTry again")
        continue
    break

'''
Formation of a list using the count() function, displaying the result on the screen
-----------------------------------------------------------------------------------
Формирование списка с использованием функции count(), вывод результата на экран
'''
list1 = []
for el in count(start, step):
    list1.append(el)
    if el > stop:
        list1.pop()
        break
print(list1)

################################## Второй скрипт - задание б) ############################################
'''
Entering the number of times a list will be repeated
-----------------------------------------------------
Ввод числа повторений списка
'''
while True:
    try:
        repeat = int(input("Insert how much times need to repeat list: "))
    except:
        print("That's not an integer number!\nTry again")
        continue
    break

'''
Formation of the final list using the cycle() function, displaying 
the result on the screen
-------------------------------------------------------------------
Формирование итогового списка с использованием функции cycle(), вывод результата на экран
'''
list2 = []
cycler = cycle(list1)
while len(list2) < (len(list1) * repeat):
    list2.append(next(cycler))
print(list(list2))
    