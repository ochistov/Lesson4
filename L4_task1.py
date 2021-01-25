from argparse import ArgumentParser
parser = ArgumentParser()
'''
Set arguments
--------------------
Задание аргументов
'''
parser.add_argument('--hours', type = float)
parser.add_argument('--rate_in_hour', type = float)
parser.add_argument('--prize', type = float)

'''
Function that calculates the employee's salary using the formula from the task
----------------------------------------------------------------
Функция, рассчитывающая зарплату работника по формуле из задания
'''

def payment (hours, rate_in_hour, prize):
    salary = (rate_in_hour * hours) + prize
    return salary
args = parser.parse_args()

'''
Displaying result on the screen
---------------------------------
Вывод результата на экран
'''
print(f"In this period worker will receive {payment(args.hours, args.rate_in_hour, args.prize)} dollars")
