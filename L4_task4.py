'''
Entering a list and checking it for non-numeric characters
---------------------------------------------
Ввод списка и проверка его на содержание символов, отличных от цифр
'''
while True:
    try:
        start_list = input("Insert list of numbers, splitted by space: ").split()
        check_digit = [float(el) for el in start_list]
    except:
        print("Your list contains no-digit element!\nTry again")
        continue
    break
#start_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11] ### СПИСОК ИЗ ЗАДАНИЯ ДЛЯ ПРОВЕРКИ

'''
Find unique list items and display results on the screen
----------------------------------------------------------
Поиск уникальных элементов списка и вывод результатов на экран
'''
end_list = [start_list[i] for i in range(len(start_list)) if start_list.count(start_list[i]) == 1]
print(f"Here is the list of non-repeating elements: {end_list}")
