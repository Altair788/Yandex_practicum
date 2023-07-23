# try:
    #  здесь написан код, который в некоторых ситуациях
    #  может создать исключение
    #  программа попробует выполнить этот код
def calc_share(apples, friends):
    friends_number = int(friends.split()[0])
    return int(apples/friends_number)

apples = 17

for friends in ['7 друзей', '2 друга', '0 друзей', 'один враг']:
    try:
        if calc_share(apples, friends) == 1:
            print(f'каждому достанется по {calc_share(apples, friends)} яблоку')
        elif 2 <= calc_share(apples, friends) <= 4:
            print(f'каждому достанется по {calc_share(apples, friends)} яблока')
        else:
            print(f'каждому достанется по {calc_share(apples, friends)} яблок')
    except ZeroDivisionError:
        print('на ноль делить нельзя')
    except ValueError:
        print(f'из строки "{friends}" не получилось достать число')


# except TypeError1:
    #  здесь описываем, что следует делать,
    #  если будет "выброшено" исключение типа TypeError1.
# except TypeError2:
    #  а здесь разработчик описывает, как быть, если перехвачено
    #  исключение типа TypeError2.

