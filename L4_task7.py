while True:
    try:
        n = int(input("Insert number: ")) #ввод крайнего числа в цепочке факториалов
    except:
        print("It's not an integer number!\nTry again")
        continue
    break
'''
Implementation of the function with the "yield" keyword, 
with the help of which the factorial of a number is calculated
---------------------------------------------------------------
Реализация функции с ключевым словом "yield", с помощью 
которой высчитывается факториал числа
'''
def fact(n):
    factorial = 1
    for i in range(2, n+1):
        factorial *= i
    yield factorial

'''
Applying the function fact(n) to all numbers in the range from 1 to n
Displaying result on the screen
---------------------------------------------------------------------
Применение функции fact(n) ко всем числам в диапазоне от 1 до n
Вывод результата на экран
'''
for m in range(1, (n + 1)):
    for el in fact(m):
        print(f"{m}! = {el}")