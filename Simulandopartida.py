# IMPORTANDDO AS BIBLIOTECAS
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

#TIME 1
time_1 = [] # NOME DOS JOGADORES
over_geral_time1 = 0
team_1 = {
    'Gabriel': randint(45, 55), 
    'Luiz': randint(45, 55), 
    'Emanuel': randint(45, 55),
    'Hernanes': randint(45, 55),
    'Weverton': randint(45, 55), 
    'Deivid': randint(45, 55), 
    'Ismael': randint(45, 55)
}
for jogador, over in team_1.items():
    time_1.append(jogador)
    over_geral_time1 += over
forca_total_time1 = (over_geral_time1 / len(time_1) / 10)
# TIME 2
time_2 = []
over_geral_time2 = 0
team_2 = {
    'Marcos': randint(45, 55),
    'Renan': randint(45, 55),
    'Mateus': randint(45, 55),
    'Igor': randint(45, 55),
    'Everton': randint(45, 55),
    'Marquinhos': randint(45, 55),
    'Malcom': randint(45, 55)
}
for jogador, over in team_2.items():
    time_2.append(jogador)
    over_geral_time2 += over
forca_total_time2 = (over_geral_time2 / len(time_2) / 10)
# LANCES TIME 1
def lance_gol_time1():
    while True:
            player1 = choice(time_1)
            player2 = choice(time_1)
            player3 = choice(time_1)
            player4 = choice(time_1)
            if player1 != player2 != player3 != player4 != player1 != player2 != player3:
                print(f'\033[1;44;37mrecebe a bola {player1}, que repassa para {player2}..\033[m'.center(80))
                sleep(2)
                print(f'\033[1;44;37m{player2} distribui para {player3} que aciona {player4}\033[m'.center(80))
                sleep(2)
                print(f'\033[1;44;37m{player4} finaliza, e...\033[m'.center(80))
                sleep(3)
                print(" ")
                print(f'\033[1;31;42mGOOLLLL, é do {s_time}\033[m (Minuto {m}°)'.center(80))
                sleep(2)
                print(" ")
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
                print(' ')
                print(f'\033[1;44;37mDesperdiça a chance o jogador {player4} do {s_time}\033[m (Minuto {m}°)'.center(80))
                sleep(2)
                print(' ')
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
                print(' ')
                print(f'\033[1;44;37mO jogador {player4} acerta a trave...\033[m (Minuto {m}°)'.center(80))
                print(' ')
                sleep(2)
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
                print(" ")
                print(f'\033[1;44;37m Direto nas mãos do goleiro.\033[m (Minuto {m}°)'.center(80))
                sleep(2)
                print(" ")
                chutes1.append(1)
                posse1.append(1)
                chutes_gol1.append(1)
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
                print(' ')
                print(f'\033[1;31;42mGOOLLLL, é do {time_adv}\033[m (Minuto {m}°)'.center(80))
                print(' ')
                sleep(2)
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
                print(' ')
                print(f'\033[1;37;41mDesperdiça a chance o jogador {player4} do {time_adv} \033[m (Minuto {m}°)'.center(80))
                print(' ')
                sleep(2)
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
                print(' ')
                print(f'\033[1;37;41mO jogador {player4} acerta a trave...\033[m (Minuto {m}°)'.center(80))
                print(' ')
                sleep(2)
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
                print(' ')
                print(f'\033[1;37;41m Direto nas mãos do goleiro.\033[m (Minuto {m}°)'.center(80))
                print(' ')
                sleep(2)
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
    chutes_1 = uniform(0, 100) # Valor que vai gerar a finalização do time 1
    chutes_2 = uniform(0, 100) # Valor que vai gerar a finalização do time 2
    sleep(0.55)                   # BÔNUS ALEATÓRIO
    defesa_time1 = (uniform(0, 10) + uniform(0, 2.50)) # Valor que vai confirmar o gol do time 1
    defesa_time2 = (uniform(0, 10) + uniform(0, 2.50)) # Valor que vai confirmar o gol do time 2
    cartao_time1 = randint(0, 100) # Valor para gerar cartão para o time 1
    cartao_time2 = randint(0, 100) # Valor para gerar cartão para o time 2
    min.append(1) # Contador de minutos iterando em uma lista fora do loop.
    m = len(min) # Leitura de minutos toda vez que o Loop roda.
    if cartao_time1 > 99: # Condição cartão time 1
        player_y1 = choice(time_1)
        print(f'\033[1;44;37mCartão amarelo para {player_y1}\033[m {cartao_y}'.center(80))
        print(' ') 
    if cartao_time2 > 99: # Condição cartão time 1
        player_y2 = choice(time_2)
        print(f'\033[1;37;41mCartão amarelo para {player_y2}\033[m {cartao_y}'.center(80))
        print(' ')

    # GERADOR DE LANCES TIME 1
    if chutes_1 >= 95 and defesa_time2 > forca_total_time1: # Condição para gol do time 1
        lance_gol_time1()
    elif chutes_1 > 0 and chutes_1 < 10: # Condição para finalização para fora.
        lance1()
    elif chutes_1 > 20 and chutes_1 < 30: # Finalização nas mãos do goleiro.
        lance3()
    elif chutes_1 >= 92 and chutes_1 < 95: # Finalização na trave.
        lance2()

    # GERADOR DE LANCES TIME 2.
    if chutes_2 >= 95 and defesa_time1 > forca_total_time2:  # Condição para gol do time 2
        lance_gol_time2()
    elif chutes_2 > 0 and chutes_2 < 10: # Condição para finalização para fora.
        lance4()
    elif chutes_2 > 20 and chutes_2 < 30: # Finalização nas mãos do goleiro.
        lance6()
    elif chutes_2 >= 92 and chutes_2 < 95: # Finalização na trave
        lance5()
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
    chutes_1 = uniform(0, 100) # Gerador de finalização do time 1
    chutes_2 = uniform(0, 100) # Gerador de finalização do time 2
    defesa_time1 = (uniform(0, 10) + uniform(0, 2.50)) # Confirmação do gol do time 1
    defesa_time2 = (uniform(0, 10) + uniform(0, 2.50)) # Confirmação do gol do time 2
    cartoes1 = uniform(0, 103) # Gerador de cartão para o time 1
    cartoes2 = uniform(0, 103) # Gerador de cartão para o time 2
    cartao1 = choice(time_1) # Gerador de jogador que vai receber o cartão do time 1
    cartao2 = choice(time_2) # Gerador de jogador que vai receber o cartão do time 2
    min.append(1) # iteração fora do loop para contagem dos minutos.
    m = len(min)
    if cartoes1 > 101.83: # Condição para cartão time 1.
        print(' ')
        print(f'\033[1;37;44mCartão Amarelo para o jogador {cartao1}\033[m {cartao_y} (Minuto {m}°)'.center(90))
        print(' ')
        sleep(2)
    if cartoes2 > 101.83: # Condição para cartão time 2.
        print(' ')
        print(f'\033[1;37;41mCartão Amarelo para o jogador {cartao2}\033[m {cartao_y} (Minuto {m}°)'.center(90))
        print(' ')
        sleep(2)

    # GERADOR DE LANCES TIME 1
    if chutes_1 >= 95 and defesa_time2 > forca_total_time1: # Condição para gol time 1.
        lance_gol_time1()
    elif chutes_1 > 0 and chutes_1 < 15: # Condição de finalização desperdiçada.
        lance1()
    elif chutes_1 > 20 and chutes_1 < 35: # Condição de finalização defendida pelo goleiro.
        lance3()
    elif chutes_1 > 91 and chutes_1 < 95: # Condição de finalização na trave. 
        lance2()

    # GERADOR DE LANCES TIME 2
    if chutes_2 >= 95 and defesa_time1 > forca_total_time2: # Condição para gol time 2.
        lance_gol_time2()
    elif chutes_2 > 0 and chutes_2 < 15: # Condição de finalização desperdiçada.
        lance4()
    elif chutes_2 > 20 and chutes_2 < 35: # Condição de finalização defendida pelo goleiro.
        lance6()
    elif chutes_2 > 91 and chutes_2 < 95: # Condição de finalização na trave. 
        lance5()
    else:
        print(f'\033[1;33;41m JOGO ROLANDO.... \033[m (Minuto {m}°)'.center(80))
        posse_1 = randint(0, 1)
        if posse_1 == 0:
            posse1.append(1)
        elif posse_1 == 1:
            posse2.append(1)
        print(' ')

minutos = len(min)
print("\033[1;31;47m FIM DE JOGO \033[m".center(80))
sleep(2)

# Cálculo de estatísticas da partida

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

print(' ')
print(' ')
print('x' * 65)
print(' ')
print(' ')
print(f'\033[1;31;47mplacar:\033[m \033[1;37;41m{s_time} {resultado1} X {resultado2} {time_adv}\033[m'.center(90))
print(' ')
print(' ')
print(f'\033[1;31;47mChutes:\033[m \033[1;37;41m{s_time} {finalizacao1} x {finalizacao2} {time_adv}\033[m'.center(90))
print(' ')
print(' ')
print(f'\033[1;31;47mCHUTES A GOL:\033[m \033[1;37;41m{s_time} {chutes1_1} x {chutes2_2} {time_adv}\033[m'.center(90))
print(' ')
print(' ')
print(f'\033[1;31;47mPrecisão:\033[m \033[1;37;41m{s_time} {precisao1__1:.0f}% X {precisao2__2:.0f}% {time_adv}\033[m'.center(90))
print(' ')
print(' ')
print(f'\033[1;31;47mPosse De bola:\033[m \033[1;37;41m{s_time} {posse__1:.0f}% x {posse__2:.0f}% {time_adv}\033[m'.center(90))
print(' ')
print(' ')
print('×' * 65)
print(' ')
print(' ')