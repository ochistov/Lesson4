from functools import reduce #импорт функции reduce() из модуля functools
'''
Formation of a list of all even numbers in the range from 100 to 1000
------------------------------------------------------
Формирование списка всех четных чисел в диапазоне от 100 до 1000
'''
list_one = [el for el in range(100, 1001) if el % 2 == 0]

'''
Multiplying all elements of a list using lambda and reduce() function.
Displaying result on the screen
--------------------------------------------------------------------------
Перемножение всех элементов списка с использованием лямбда-функции 
и функции reduce(). Вывод результата на экран
'''
multiple_all = reduce(lambda x, y: x * y, list_one)
print(multiple_all)
