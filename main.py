import random
from time import sleep

top_lvl = ['top ', '-', '-', '-']
mid_lvl = ['mid ', '-', '-', '-']
bot_lvl = ['bot ', '-', '-', '-']


def krestik(top=top_lvl,mid=mid_lvl,bot=bot_lvl):
    print('Крестик')
    stolb = str(input('Введите строку(top,mid,bot):')).lower()

    if stolb == 'top':
        lvl = top
    elif stolb == 'mid':
        lvl = mid
    elif stolb == 'bot':
        lvl = bot
    else:
        print('Введите корректно строку')
        krestik()

    mesto = int(input('Введите столбец(1,2,3):'))

    if lvl[mesto] == '0':
        print('Здесь стоит 0.Выбирите другое место')
        krestik()
    elif lvl[mesto] == 'x':
        print('Вы уже заняли это место.Выбирите другое место')
        krestik()
    else:
        if lvl == top:
            top[mesto] = 'x'
        elif lvl == mid:
            mid[mesto] = 'x'
        elif lvl == bot:
            bot[mesto] = 'x'
    return doska(top, mid, bot)


def nolik(top=top_lvl,mid=mid_lvl,bot=bot_lvl):
    print('Нолик')
    stolb = str(input('Введите строку(top,mid,bot):')).lower()

    if stolb == 'top':
        lvl = top
    elif stolb == 'mid':
        lvl = mid
    elif stolb == 'bot':
        lvl = bot
    else:
        print('Введите корректно строку')
        nolik()

    mesto = int(input('Введите столбец(1,2,3):'))

    if lvl[mesto] == 'x':
        print('Здесь стоит x.Выбирите другое место')
        nolik()
    elif lvl[mesto] == '0':
        print('Вы уже заняли это место.Выбирите другое место')
        nolik()
    else:
        if lvl == top:
            top[mesto] = '0'
        elif lvl == mid:
            mid[mesto] = '0'
        elif lvl == bot:
            bot[mesto] = '0'
    return doska(top, mid, bot)


def doska(top=top_lvl, mid=mid_lvl, bot=bot_lvl):
    print('- - -| 1 | 2 | 3')
    print(str(top[0]) + ' | ' + str(top[1]) + ' | ' + str(top[2]) + ' | ' + str(top[3]))
    print('- - -+ - + - + -')
    print(str(mid[0]) + ' | ' + str(mid[1]) + ' | ' + str(mid[2]) + ' | ' + str(mid[3]))
    print('- - -+ - + - + -')
    print(str(bot[0]) + ' | ' + str(bot[1]) + ' | ' + str(bot[2]) + ' | ' + str(bot[3]))
    print('######################')


def CheckWin(top=top_lvl, mid=mid_lvl, bot=bot_lvl,):
    if top[1] == top[2] == top[3] != '-':
        print('Win:' + top[1])
        return False
    elif mid[1] == mid[2] == mid[3] != '-':
        print('Win:' + mid[1])
        return False
    elif bot[1] == bot[2] == bot[3] != '-':
        print('Win:' + bot[1])
        return False
    elif top[1] == mid[2] == bot[3] != '-':
        print('Win:' + top[1])
        return False
    elif top[3] == mid[2] == bot[1] != '-':
        print('Win:' + top[3])
        return False
    elif top[1] == mid[1] == bot[1] != '-':
        print('Win:' + top[1])
        return False
    elif top[2] == mid[2] == bot[2] != '-':
        print('Win:' + top[2])
        return False
    elif top[3] == mid[3] == bot[3] != '-':
        print('Win:' + top[3])
        return False
    elif top[3] != '-' and top[2] != '-' and top[1] != '-' and mid[3] != '-' and mid[2] != '-' and mid[1] != '-' and bot[3] != '-' and bot[2] != '-' and bot[1] != '-':
        print('Ничья')
        return False
    else:
        return True


def Game(top=top_lvl, mid=mid_lvl, bot=bot_lvl):
    seconond = input('Выбирите режим игры(1-игрок против игрока, 2-игрок против мистера рандома, 3-мистер рандом против мистера рандома):')
    first = input('Кто будет ходить первым?(1-крестик,2-нолик):')
    if seconond == '2':
        fird = input('Ввыберете кто ходит первый(1-вы,2-Мистер рандом):')

    if first == '1' and seconond == '1':
        doska()
        while CheckWin():
            krestik()
            if CheckWin() == False:
                break
            nolik()

    elif first == '2' and seconond == '1' and fird == '1':
        doska()
        while CheckWin():
            nolik()
            if CheckWin() == False:
                break
            krestik()

    elif first == '1' and seconond == '2' and fird == '1':
        doska()
        wag = '0'
        while CheckWin():
            krestik()
            if CheckWin() == False:
                break
            Mr_random(wag='0')

    elif first == '1' and seconond == '2' and fird == '2':
        doska()
        wag = '0'
        while CheckWin():
            Mr_random(wag=wag)
            if CheckWin() == False:
                break
            krestik()

    elif first == '2' and seconond == '2' and fird == '1':
        doska()
        wag = 'x'
        while CheckWin():
            krestik()
            if CheckWin() == False:
                break
            Mr_random(wag=wag)

    elif first == '2' and seconond == '2' and fird == '2':
        doska()
        wag = 'x'
        while CheckWin():
            Mr_random(wag=wag)
            if CheckWin() == False:
                break
            krestik()

    elif first == '1' and seconond == '3':
        doska()
        while CheckWin():
            Mr_random(wag='x')
            sleep(2)
            if CheckWin() == False:
                break
            Mr_random(wag='0')
            sleep(2)

    elif first == '2' and seconond == '3':
        doska()
        while CheckWin():
            Mr_random(wag='0')
            sleep(2)
            if CheckWin() == False:
                break
            Mr_random(wag='x')
            sleep(2)

    else:
        print('Введите коректный номер')
        Game()


def Mr_random(top=top_lvl, mid=mid_lvl, bot=bot_lvl, wag='x'):
    lvls = (top, mid, bot)
    lvl = random.choice(lvls)
    stolbs = (1, 2, 3)
    stolb = random.choice(stolbs)
    if lvl[stolb] == '-':
        lvl[stolb] = wag
        return doska(top, mid, bot)
    else:
        Mr_random(wag=wag)



Game()


