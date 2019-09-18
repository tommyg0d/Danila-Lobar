atomNum = input('Введите атомный номер элемента: ')

if atomNum:
    atomNum = int(atomNum)
    if atomNum == 3:
        print('Это Li!')
    elif atomNum == 25:
        print('Это Mn!')
    elif atomNum == 80:
        print('Это Hg!')
    elif atomNum == 17:
        print('Это Cl!')
    else: print('Данный элемент отсутствует')
else: print('Введите атомный номер элемента!')
