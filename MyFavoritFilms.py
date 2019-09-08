Films = dict([('Shawshank redemption', 'Drama'), ('Gost', 'Drama'), ('Pianist', 'Drama'), ('Gladiator', 'Advanture'), ('Inception', 'Advanture'), ('The Revenant', 'Advanture'), ('Lord of the rings', 'Fantasy'), ('Avatar','Fantasy'), ("Harry Potter", 'Fantasy')])

f = str(input('Введите название фильма: '))

Film = [f]
for film in Film:
    if film in Films:
        print('Фильм в вашем списке ' + f + ' - ' + Films[film])
    else:
        print('Фильма нету')
