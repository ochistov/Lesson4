'''
Display all numbers from 20 to 240 in multiples of 20 or 21. 
One line solution
---------------------------------------------------------------
Вывод на экран всех чисел от 20 до 240 кратных 20 или 21. 
Решение в одну строку
'''
print(f"Here is all numbers from 20 to 241\nmultiples of 20 or 21:\n{[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}")
