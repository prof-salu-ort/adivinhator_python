'''
Bem vindos ao ADIVINHATOR 2026 (jogo da adivinhação)
################################***Regras***#########################################################
- o jogo sorteia um valor entre 1-100.
- o jogador a cada rodada tentar descobrir o numero secreto.
- a cada tentativa o jogo da uma dica para o jogador.
- cada tentativa é computada.
- ao descobrir o numero secreto, informa o total de tentativas e o tempo que demorou para adivinhar.
#####################################################################################################
'''

import time #biblioteca que trabalha com o tempo
import random #biblioteca que trabalho com aleatoriedade

#Sorteia um numero inteiro entre 1 e 100
NUMERO_SECRETO = random.randint(1, 100)

print('Bem-vindo ao ADIVINHATOR 2026')
print('Sorteando um número entre 1 e 100...')

#PARA A EXECUÇÃO DO PROGRAMA POR UM INTERVALO DE 3 SEGUNDOS
time.sleep(3)

print('*** Partida Iniciada ***')

#Captura o tempo no INICIO do programa
inicio = time.time()
print('COLA -->', NUMERO_SECRETO)
while True:
    numero = int(input('Informe um numero [1-100]: '))
    if numero > NUMERO_SECRETO:
        print('O Numero informado é MAIOR que o NUMERO_SECRETO')
    elif numero < NUMERO_SECRETO:
        print('O Numero informado é MENOR que o NUMERO_SECRETO')
    else:
        print('*** Partida Finalizada ***')
        print()
        print('PARABENS!!! Você descobriu o numero secreto.')
        break

#Captura o tempo no FINAL do programa
fim = time.time()

print(f'Tempo decorrido: {int(fim-inicio)} segundos')