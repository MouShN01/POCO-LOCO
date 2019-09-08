Films = dict([('Shawshank redemption', 'Drama. Producer - Frank Darabont.'), ('Ghost', 'Drama. Producer - Lisa Weinstein.'), ('Pianist', 'Drama. Producer - Roman Polański.'), ('Gladiator', 'Advanture. Producer - Ridley Scott.'), ('Inception', 'Advanture. Producer - Christopher Jonathan.'), ('The Revenant', 'Advanture. Producer - Alejandro González.'), ('Lord of the rings', 'Fantasy. Producer - Peter Robert Jackson.'), ('Avatar','Fantasy. Producer - James Cameron.'), ("Harry Potter", 'Fantasy. Producer - Christopher Columbus.')])
i = 1
for film in Films:
    print(str(i) + '. ' + film)
    i +=1

f = str(input('Введите название фильма для подробной информации: '))

Film = [f]
for film in Film:
    if film in Films:
        print('Фильм в вашем списке: ' + f + ' - ' + Films[film])
    else:
        print('Такого фильма нету в списке.')
