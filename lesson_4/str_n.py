def f(s,n):
    if len(s) > n:
        return s.upper()
    else: return s

s = input('Введите строку:\n')
n = input('Введите число: ')

if s:
    if n:
        print(f(s,int(n)))
    else: print('Введите число!')
else: print('Введите строку!')