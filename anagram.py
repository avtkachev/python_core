'''Задача на проверку анаграмм может встретиться на алгоритмической секции собеседования на python-разработчика.

Анаграмма – это состояние, при котором одна строка или число переставляются таким образом; каждый символ измененной 
строки или числа должен быть частью другой строки или числа. Другими словами, строка называется анаграммой другой, 
если вторая является простой перестановкой первой строки. Например: Python и yphton являются анаграммами; Java и avaJ также являются анаграммами.'''

def anagram_check(str1, str2):
    # перобразуем строку в список
    list1 = list(str1)
    list2 = list(str2)
    # сортируем значения списка
    list1.sort()
    list2.sort()

    position = 0
    matches = True
    try:
        while position < len(str1) and matches:
            if list1[position] == list2[position]:
                position = position + 1
            else:
                matches = False      
    except IndexError as err:
        print('Возникла ошибка!') 
    else:
        return matches
    finally:
        print('Длины строк не совпадают!')
    
print(anagram_check('python', 'thonp'))