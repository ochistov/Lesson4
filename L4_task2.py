'''
Entering a list and checking for non-digit characters
------------------------------------------------------------
Ввод списка и проверка на наличие символов, отличных от цифр
'''
while True:
    try:
        start_list = input("Enter list: ").split()
        check_int = [int(el) for el in start_list]
    except:
        print("Your list contains not integer number!\nPlease try again")
        continue
    break

#start_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55] ####### СПИСОК ИЗ ЗАДАНИЯ ДЛЯ ПРОВЕРКИ
'''
Solution and displaying result on the screen 
-----------------------------------------------
Решение и вывод результата на экран
'''
end_list = [start_list[i] for i in range(1, (len(start_list) - 1)) if int(start_list[i]) > int(start_list[i - 1])]
print(f"Here is your list: {end_list}")
