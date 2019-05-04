#Aluno: Rafael Augusto Hentz
#1F 2019
#Professor Tiago Mazzutti
#Disciplina : Programação I
#Jogo da Velha
#Variáveis
import sys
global cont
global jogador
global x
global tbl
global jogo
vx=0
vo=0
vl=0
tbl=[[1,2,3],[4,5,6],[7,8,9]]
#Função para verificar se houve ganhador
def ganhou():

    if (tbl[0][0]==tbl[0][1]==tbl[0][2])or (tbl[1][0]==tbl[1][1]==tbl[1][2])or (tbl[2][0]==tbl[2][1]==tbl[2][2])or(tbl[0][0]==tbl[1][0]==tbl[2][0])or(tbl[0][1]==tbl[1][1]==tbl[2][1])or \
            (tbl[0][2] == tbl[1][2] == tbl[2][2]) or(tbl[0][0]==tbl[1][1]==tbl[2][2])or(tbl[0][2]==tbl[1][1]==tbl[2][0]):
        return True
    else:
        return
#Função para verificar se a casa digitada está ocupada
def ocupado(n):
    if n==1:
        if tbl[0][0]!=1:
            return False
    if n == 2:
        if tbl[0][1] != 2:
            return False
    if n == 3:
        if tbl[0][2] != 3:
            return False
    if n == 4:
        if tbl[1][0] != 4:
            return False
    if n == 5:
        if tbl[1][1] != 5:
            return False
    if n == 6:
        if tbl[1][2] != 6:
            return False
    if n == 7:
        if tbl[2][0] != 7:
            return False
    if n == 8:
        if tbl[2][1] != 8:
            return False
    if n == 9:
        if tbl[2][2] != 9:
            return False
#Função para exibir o tabuleiro com o placar e posições
def tab():
    global tbl

    print('|-----------------------------|')
    print('|        Retro Game 2000      |')
    print('|-----------------------------|')
    print('|Vitórias e Empates:          |')
    print('|  O:{}      X:{}      E:{}      |'.format(vo,vx,vl))
    print('|                             |')
    print('|-----------------------------|')
    print('|   ',tbl[0][0],'   |   ',tbl[0][1],'   |   ',tbl[0][2],'   |')
    print('|_________|_________|_________|')
    print('|   ', tbl[1][0], '   |   ', tbl[1][1], '   |   ', tbl[1][2], '   |')
    print('|_________|_________|_________|')
    print('|   ', tbl[2][0], '   |   ', tbl[2][1], '   |   ', tbl[2][2], '   |')
    print('|         |         |         |')
    print('|-----------------------------|')
#Função para colocar X ou O nas casas, definir o jogador e verificar se o jogo vai continuar
def jogando():
    global tbl,vx,vo,vl
    cont=0
    jogador=input('Digite qual jogador quer ser,X ou O: ')
    if jogador=='x':jogador='X'
    elif jogador=='o':jogador='O'
    while cont<9:
         print('Vez do %s'%jogador)
         x=int(input('Digite uma posição: '))
         if x>0 and x<10 :
             if x==1:
                 if ocupado(x)==False:
                     print('Casa ocupada')
                     continue
                 else:
                     tbl[0][0]=jogador
                     tab()
                     cont += 1
             if ganhou() == True:
                 break
             elif x == 2:
                 if ocupado(x)==False:
                     print('Casa Ocupada')
                     continue
                 else:
                     tbl[0][1] = jogador
                     tab()
                     cont += 1
             if ganhou() == True:
                 break
             elif x == 3:
                 if ocupado(x)==False:
                     print('Casa Ocupada')
                     continue
                 else:
                     tbl[0][2] = jogador
                     tab()
                     cont += 1
             if ganhou() == True:
                 break
             elif x == 4:
                 if ocupado(x)==False:
                     print('Casa Ocupada')
                     continue

                 else:
                     tbl[1][0] = jogador
                     tab()
                     cont += 1
             if ganhou() == True:
                 break
             elif x == 5:
                 if ocupado(x)==False:
                     print('Casa Ocupada')
                     continue

                 else:
                     tbl[1][1] = jogador
                     tab()
                     cont += 1
             if ganhou() == True:
                 break
             elif x == 6:
                 if ocupado(x)==False:
                     print('Casa Ocupada')
                     continue

                 else:
                    tbl[1][2] = jogador
                    tab()
                    cont += 1
             if ganhou() == True:
                 break
             elif x == 7:
                 if ocupado(x)==False:
                     print('Casa Ocupada')
                     continue

                 else:
                     tbl[2][0] = jogador
                     tab()
                     cont += 1
             if ganhou() == True:
                 break
             elif x == 8:
                 if ocupado(x)==False:
                     print('Casa Ocupada')
                     continue

                 else:
                     tbl[2][1] = jogador
                     tab()
                     cont += 1
             if ganhou() == True:
                 break
             elif x == 9:
                 if ocupado(x)==False:
                     print('Casa Ocupada')
                     continue

                 else:
                     tbl[2][2] = jogador
                     tab()
                     cont += 1
             if ganhou() == True:
                 break

             if jogador=='X' or jogador=='x':jogador='O'
             elif jogador=='O' or jogador=='o':jogador='X'
         else:
             print('Posição Inválida!!')
    if cont > 8:
        print('Velha!')
        vl+=1
        y = str(input('Quer jogar novamente(S/N)?'))
        if y == 'n' or y == 'N':
            sys.exit()
        elif y == 's' or y == 'S':
            tbl = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            jogo = True
            return
    if ganhou() == True:
        print('O jogo acabou!%s' % jogador, 'venceu!!')
        if jogador=='X':
            vx+=1
        elif jogador=='O':
            vo+=1
        y=str(input('Quer jogar novamente(S/N)?'))
        if y=='n' or y=='N':
            sys.exit()
        elif y=='s'or y=='S':
             tbl = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
             jogo =True
             return
#Executa o jogo enquanto a variável jogo for igual a True(verdadeiro)
jogo=True
print('Regras do jogo:\n '
       '1. O jogo só vai ter ganhador caso hajam três casas alinhadas \n'
       'com o mesmo símbolo, seja na horizontal, vertical ou diagonal.\n'
       '2.Os jogadores jogam um de cada vez.\n'
       '3.As posições variam de 1 a 9.\n'
       '4. Divirta-se bastante')
while jogo:
    tab()
    jogando()