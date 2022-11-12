#цели самое главное создать правильную алгоритмику
# 1. создать таблицу(поле игровое) 3*3
# 2. наименование поле игрового krestiki_noliki
# 3. нужно создать поле через функцию def buildindtabulate
# 4. через функцию def делим на 3 строки range



krestiki_noliki= list(range(1,10))

def buildindtabulate (krestiki_noliki):

    for a in range(3):
        print ("  ", krestiki_noliki[0+a*3], "  ", krestiki_noliki[1+a*3], "  ", krestiki_noliki[2+a*3], "  ")

# 5. через функцию def создаем условия

def take_input(players):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + players+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(krestiki_noliki[player_answer-1]) not in "X◯"):
                krestiki_noliki[player_answer-1] = players
                valid = True
            else:
                print ("Клетка занята")
        else:
            print ("Числа вводить возможно только 1-9")

# 6. создаем выйгрышные комбинации через функцию def

def Win_win(krestiki_noliki):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for one in win_coord:
        if krestiki_noliki[one[0]] == krestiki_noliki[one[1]] == krestiki_noliki[one[2]]:
            return krestiki_noliki[one[0]]
    return False

# 7. Условия "Ничья" и как понять?? kто выйграл??

def yslovie (krestiki_noliki):
    counter = 0
    win = False
    while not win:
        buildindtabulate(krestiki_noliki)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("◯")

        counter += 1
        if counter > 4:
            tmp = Win_win(krestiki_noliki)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    buildindtabulate(krestiki_noliki)

yslovie(krestiki_noliki)
#. проверка условий
