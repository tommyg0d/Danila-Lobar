def func(x):
    if 0.2 <= x <= 0.9:
        import math
        return math.sin(x) 
    else: return 1

a = input('Введите число: ')

if a:
    print('Функция =',func(float(a)))
else: print('Введите число!')
