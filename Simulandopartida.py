from time import sleep 
from random import randint, uniform, choice

# placar contador 

gol1s = list()
gol2s = list()
chutes1 = list()
chutes2 = list()
posse1 = list()
posse2 = list()
chutes_gol1 = list()
chutes_gol2 = list()
min = list()

# cartão amarelo e vermelho

cartao_y = '\033[1;33;43m  \033[m'
red = '\033[1;37;41m  \033[m'

# times que vão jogar 

# time 1
time_1 = ['Gabriel', 'Luiz', 'Emanuel', 'Hernanes', 'Weverton', 'Deivid', 'Ismael']

# time 2
time_2 = ['Marcos', 'Renan', 'Mateus', 'Igor', 'Everton', 'Marquinhos', 'Malcom']

# função space ou espaço

def space():
    print(' ')

# LANCES TIME 1
def lance_gol_time1():
    while True:
            player1, player2, player3, player4 = choice(time_1)
            if player1 != player2 != player3 != player4 != player1 != player2 != player3:
                print(f'\033[1;44;37mrecebe a bola {player1}, que repassa para {player2}..\033[m'.center(80))
                sleep(2)
                print(f'\033[1;44;37m{player2} distribui para {player3} que aciona {player4}\033[m'.center(80))
                sleep(2)
                print(f'\033[1;44;37m{player4} finaliza, e...\033[m'.center(80))
                sleep(3)
                space()
                print(f'\033[1;31;42mGOOLLLL, é do {s_time}\033[m (Minuto {m}°)'.center(80))
                space()
                gol1s.append(1)
                chutes1.append(1)
                posse1.append(1)
                chutes_gol1.append(1)
                break

def lance1():
    while True:
            player1 = choice(time_1)
            player2 = choice(time_1)
            player3 = choice(time_1)
            player4 = choice(time_1)
            if player1 != player2 != player3 != player4 != player1 != player2 != player3:
                print(f'\033[1;44;37mrecebe a bola {player1}, que repassa para {player2}..\033[m'.center(80))
                sleep(2)
                print(f'\033[1;44;37m{player2} distribui para {player3} que aciona {player4}..\033[m'.center(80))
                sleep(2)
                print(f'\033[1;44;37m{player4} finaliza, e...\033[m'.center(80))
                sleep(3)
                space()
                print(f'\033[1;44;37mDesperdiça a chance o jogador {player4} do {s_time}\033[m (Minuto {m}°)'.center(80))
                sleep(1)
                space()
                chutes1.append(1)
                posse1.append(1)
                break

def lance2():
    while True:
            player1 = choice(time_1)
            player2 = choice(time_1)
            player3 = choice(time_1)
            player4 = choice(time_1)
            if player1 != player2 != player3 != player4 != player1 != player2 != player3:
                print(f'\033[1;44;37mrecebe a bola {player1}, que repassa para {player2}..\033[m'.center(80))
                sleep(2)
                print(f'\033[1;44;37m{player2} distribui para {player3} que aciona {player4}..\033[m'.center(80))
                sleep(2)
                print(f'\033[1;44;37m{player4} finaliza, e...\033[m'.center(80))
                sleep(3)
                space()
                print(f'\033[1;44;37mO {player4} acerta a trave...\033[m (Minuto {m}°)'.center(80))
                space()
                sleep(1)
                chutes1.append(1)
                posse1.append(1)
                break

def lance3():
    while True:
            player1 = choice(time_1)
            player2 = choice(time_1)
            player3 = choice(time_1)
            player4 = choice(time_1)
            if player1 != player2 != player3 != player4 != player1 != player2 != player3:
                print(f'\033[1;44;37mrecebe a bola {player1}, que repassa para {player2}..\033[m'.center(80))
                sleep(2)
                print(f'\033[1;44;37m{player2} distribui para {player3} que aciona {player4}..\033[m'.center(80))
                sleep(2)
                print(f'\033[1;44;37m{player4} finaliza, e...\033[m'.center(80))
                sleep(3)
                space()
                print(f'\033[1;44;37m Direto nas mãos do goleiro.\033[m (Minuto {m}°)'.center(80))
                sleep(1)
                space()
                chutes1.append(1)
                posse1.append(1)
                chutes_gol1.append(1)
                sleep(1)
                break

# LANCE TIME 2

def lance_gol_time2():
    while True:
            player1 = choice(time_2)
            player2 = choice(time_2)
            player3 = choice(time_2)
            player4 = choice(time_2)
            if player1 != player2 != player3 != player4 != player1 != player2 != player3:
                print(f'\033[1;37;41mrecebe a bola {player1}, que repassa para {player2}..\033[m'.center(80))
                sleep(2)
                print(f'\033[1;37;41m{player2} distribui para {player3} que aciona {player4}..\033[m'.center(80))
                sleep(2)
                print(f'\033[1;37;41m{player4} finaliza, e...\033[m'.center(80))
                sleep(3)
                space()
                print(f'\033[1;31;42mGOOLLLL, é do {time_adv}\033[m (Minuto {m}°)'.center(80))
                space()
                sleep(1)
                gol2s.append(1)
                chutes2.append(1)
                posse2.append(1)
                chutes_gol2.append(1)
                break

def lance4():
    while True:
            player1 = choice(time_2)
            player2 = choice(time_2)
            player3 = choice(time_2)
            player4 = choice(time_2)
            if player1 != player2 != player3 != player4 != player1 != player2 != player3:
                print(f'\033[1;37;41mrecebe a bola {player1}, que repassa para {player2}..\033[m'.center(80))
                sleep(2)
                print(f'\033[1;37;41m{player2} distribui para {player3} que aciona {player4}..\033[m'.center(80))
                sleep(2)
                print(f'\033[1;37;41m{player4} finaliza, e...\033[m'.center(80))
                sleep(3)
                space()
                print(f'\033[1;37;41mDesperdiça a chance o jogador {player4} do {time_adv} \033[m (Minuto {m}°)'.center(80))
                space()
                sleep(1)
                chutes2.append(1)
                posse2.append(1)
                break

def lance5():
    while True:
            player1 = choice(time_2)
            player2 = choice(time_2)
            player3 = choice(time_2)
            player4 = choice(time_2)
            if player1 != player2 != player3 != player4 != player1 != player2 != player3:
                print(f'\033[1;37;41mrecebe a bola {player1}, que repassa para {player2}..\033[m'.center(80))
                sleep(2)
                print(f'\033[1;37;41m{player2} distribui para {player3} que aciona {player4}..\033[m'.center(80))
                sleep(2)
                print(f'\033[1;37;41m{player4} finaliza, e...\033[m'.center(80))
                sleep(3)
                space()
                print(f'\033[1;37;41mO jogador {player4} acerta a trave...\033[m (Minuto {m}°)'.center(80))
                space()
                sleep(1)
                chutes2.append(1)
                posse2.append(1)
                chutes_gol2.append(1)
                break

def lance6():
    while True:
            player1 = choice(time_2)
            player2 = choice(time_2)
            player3 = choice(time_2)
            player4 = choice(time_2)
            if player1 != player2 != player3 != player4 != player1 != player2 != player3:
                print(f'\033[1;37;41mrecebe a bola {player1}, que repassa para {player2}..\033[m'.center(80))
                sleep(2)
                print(f'\033[1;37;41m{player2} distribui para {player3} que aciona {player4}..\033[m'.center(80))
                sleep(2)
                print(f'\033[1;37;41m{player4} finaliza, e...\033[m'.center(80))
                sleep(3)
                space()
                print(f'\033[1;37;41m Direto nas mãos do goleiro.\033[m (Minuto {m}°)'.center(80))
                space()
                sleep(1)
                chutes2.append(1)
                posse2.append(1)
                chutes_gol2.append(1) 
                break

# Rodando o programa 👇🏾

print(' ')
print('-=-' * 20)
s_time = str(input('\n\033[1;37;44mDigite o nome da sua equipe:\033[m '))
print('-=-' * 20)
print(' ')
print('-=-' * 20)
time_adv = str(input('\033[1;37;41mDigite o nome do time adversário:\033[m '))
print(' ')
sleep(0.85)
print('\033[1;34;47m COMEÇA A PARTIDA... \033[m'.center(80))
sleep(0.85)
print(' ')
print(' ')

# LOOP que vai gerar o resultado da partida no primeiro tempo.

for c in range(0, 45):
    conf_gol1 = randint(0, 100)
    conf_gol2 = randint(0, 100)
    conf_lance1 = randint(0, 100)
    conf_lance2 = randint(0, 100)
    sleep(0.55)
    time_c1 = len(time_1)
    time_c2 = len(time_2)
    chutes_1 = uniform(0, 103)
    chutes_2 = uniform(0, 103)
    cartao_time1 = randint(0, 102)
    cartao_time2 = randint(0, 102)
    min.append(1)
    m = len(min)
    if cartao_time1 > 99:
        player_y1 = choice(time_1)
        print(f'\033[1;44;37mCartão amarelo para {player_y1}\033[m {cartao_y}'.center(80))
        space()
    if cartao_time2 > 99:
        player_y2 = choice(time_2)
        print(f'\033[1;37;41mCartão amarelo para {player_y2}\033[m {cartao_y}'.center(80))
        space()
    if chutes_1 > 100.00 and conf_gol1 > 90:
        lance_gol_time1()
    elif chutes_1 > 0 and chutes_1 < 5:
        lance1()
    elif chutes_1 > 102.98 and chutes_1 < 104.98:
        lance2()
    elif chutes_1 > 93.55 and chutes_1 < 98.55:
        lance3()
    if chutes_2 > 100.00 and conf_gol2 > 90:
        lance_gol_time2()
    elif chutes_2 > 5 and chutes_2 < 10:
        lance4()
    elif chutes_2 > 98 and chutes_2 < 100:
        lance5()
    elif chutes_2 > 93 and chutes_2 < 98:
        lance6()
    else:
        print(f'\033[1;33;41mJOGO ROLANDO....\033[m (Minuto {m}°)'.center(80))
        posse_1 = randint(0, 1) 
        if posse_1 == 0:
            posse1.append(1)
        elif posse_1 == 1:
            posse2.append(1)
        print(' ')

print('\033[1;31;43mFINAL DO PRIMEIRO TEMPO....\033[m'.center(80))
sleep(1)
print('......'.center(66))
sleep(1)
print(' .... '.center(66))
sleep(1)
print('  ..  '.center(66))
sleep(1)
print('  ..  '.center(66))
sleep(1)
print('\033[1;31;43mINICIA O SEGUNDO TEMPO...\033[m'.center(80))
print(' ')
sleep(3)
t = randint(44, 52)

#  SEGUNDO TEMPO 

for c in range(0, t):
    sleep(0.50)
    conf_lance1 = randint(0, 100)
    conf_lance2 = randint(0, 100)
    chutes_1 = uniform(0.0, 106.00)
    conf_gol1 = randint(0, 100)
    chutes_2 = uniform(0.0, 106.00)
    conf_gol2 = randint(0, 100)
    cartoes1 = uniform(0.0, 103.00)
    cartoes2 = uniform(0.0, 103.00)
    cartao = choice(time_1)
    cartao2 = choice(time_2)
    min.append(1)
    m = len(min)
    conf_gol1_t = randint(0, 1)
    conf_gol2_t = randint(0, 1)
    if cartoes1 > 101.83:
        space()
        print(f'\033[1;37;44mCartão Amarelo para o jogador {cartao}\033[m {cartao_y} (Minuto {m}°)'.center(90))
        space()
        sleep(2)
    if cartoes2 > 101.83:
        space()
        print(f'\033[1;37;41mCartão Amarelo para o jogador {cartao2}\033[m {cartao_y} (Minuto {m}°)'.center(90))
        space()
        sleep(2)
    if chutes_1 > 102.00 and conf_gol1 > 91:
        lance_gol_time1()
    elif chutes_1 > 0 and chutes_1 < 15:
        lance1()
    elif chutes_1 > 93 and chutes_1 < 98:
        lance2()
    elif chutes_1 > 86 and chutes_1 < 93:
        lance3()
    if chutes_2 > 102.00 and conf_gol2 > 91:
        lance_gol_time2()
    elif chutes_2 > 15 and chutes_2 < 30:
        lance4()
    elif chutes_2 > 93 and chutes_2 < 98:
        lance5()
    elif chutes_2 > 86 and chutes_2 < 93:
        lance6()
    else:
        print(f'\033[1;33;41m JOGO ROLANDO.... \033[m (Minuto {m}°)'.center(80))
        posse_1 = randint(0, 1)
        if posse_1 == 0:
            posse1.append(1)
        elif posse_1 == 1:
            posse2.append(1)
        space()

minutos = len(min)
print('\033[1;31;47m FIM DE JOGO \033[m'.center(75))
sleep(2)

# Cálculo de estatisticas da partida

resultado1 = len(gol1s)
resultado2 = len(gol2s)
finalizacao1 = len(chutes1)
finalizacao2 = len(chutes2)
precisao1__1 = (resultado1 / finalizacao1) * 100
precisao2__2 = (resultado2 / finalizacao2) * 100
posse_1 = len(posse1)
posse_2 = len(posse2)
posse__1 = (posse_1 / 90) * 100
posse__2 = 100 - posse__1
chutes1_1 = len(chutes_gol1)
chutes2_2 = len(chutes_gol2)

#  PRINT FINAL DE JOGO E ESTATISTICAS

space()
space()
print('x' * 65)
space()
space()
print(f'\033[1;31;47mplacar:\033[m \033[1;37;41m{s_time} {resultado1} X {resultado2} {time_adv}\033[m'.center(90))
space()
space()
print(f'\033[1;31;47mChutes:\033[m \033[1;37;41m{s_time} {finalizacao1} x {finalizacao2} {time_adv}\033[m'.center(90))
space()
space()
print(f'\033[1;31;47mCHUTES A GOL:\033[m \033[1;37;41m{s_time} {chutes1_1} x {chutes2_2} {time_adv}\033[m'.center(90))
space()
space()
print(f'\033[1;31;47mPrecisão:\033[m \033[1;37;41m{s_time} {precisao1__1:.0f}% X {precisao2__2:.0f}% {time_adv}\033[m'.center(90))
space()
space()
print(f'\033[1;31;47mPosse De bola:\033[m \033[1;37;41m{s_time} {posse__1:.0f}% x {posse__2:.0f}% {time_adv}\033[m'.center(90))
space()
space()
print('×' * 65)
space()
space()