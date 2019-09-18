film = input('Выбрать фильм: ')
day = input('Выбрать день(сегодня, завтра): ')
time = input('Выбрать время: ')
tickets = input('Выбрать кол-во билетов: ')

films = {
    'Пятница': {
            12: 250,
            16: 350,
            20: 450
        },
    'Чемпионы': {
            10: 250,
            13: 350,
            16: 350
        },
    'Пернатая банда': {
            10: 350,
            14: 450,
            18: 450
        }
}

if film in films:
    time = int(time)
    
    if time in films[film]:
        
        if day == 'сегодня':
            skidka = 0
        elif day == 'завтра':
            skidka = 5
        else: print('Ошибка ввода')
        
        if tickets:
            tickets = int(tickets)
            if tickets >= 20:
                skidka = skidka + 20
            value = tickets * films[film][time]
            value = value - value/100*skidka
            print('Результат:',value,'руб.')
        else: print('Ошибка ввода')
        
    else: print('Ошибка ввода')
    
else: print('Ошибка ввода')
