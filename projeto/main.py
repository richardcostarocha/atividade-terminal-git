from relogio import Relogio
from respostas import Respostas
from museu import Museu
from bomba import Bomba
from os import system
from time import sleep
system('cls')
if(__name__ == "__main__"):
    relogio = Relogio()
    museu = Museu()
    print('-='*60)
    print(f'''
                               \U0001F3E0
                  Você está na delegacia, são 7 horas.
                  
                  Foi capturado um suspeito ''\U0001F464'' de terrorismo na capital de São Paulo. 

                  Você será o detetive ''\U0001F46E''  que fará o interrogatorio.

                  "VOCÊ TEM ATÉ ÁS 11 HORAS PARA DESCOBRIR O LOCAL DA '' \U0001F4A3 ''!!"

                  obs : Caso contrário, a \U0001F4A3 BOMBA \U0001F4A3 irá explodir, atingindo todos os presentes no local da bomba...



                  ''')
    print('-='*60)
    resp = str(
        input("Quer pegar o caso? \U0001F440 [S/N]: ").strip().upper()[0])
    system('cls')
    if resp in 'S':
        while True:
            print(
                '\n  Você está interrogando um suspeito, escolha uma das perguntas à seguir:')
            saida, resposta = Respostas.pergunta1()
            relogio.avancaTempo(20)
            system('cls')
            print(f'Já são: {relogio}')
            if resposta == 1:
                fala = 'SUSPEITO:estava viajando com meus amigos!'
                for c in fala:
                    sleep(0.15)
                    print(c, end='', flush=True)
                sleep(2)
            elif resposta == 2:
                fala = 'SUSPEITO:estou em São Paulo já faz umas 3 semanas.'
                for c in fala:
                    sleep(0.15)
                    print(c, end='', flush=True)
                sleep(2)
            elif resposta == 3:
                fala = 'SUSPEITO:...'
                for c in fala:
                    sleep(0.15)
                    print(c, end='', flush=True)
                sleep(2)
            brk = Bomba.explodir(relogio.horas)
            if brk == True:
                break
            if saida == True:
                break
        while brk == False:
            saida, resposta = Respostas.pergunta2()
            relogio.avancaTempo(20)
            system('cls')
            print(f'Já são: {relogio}')
            if resposta == 1:
                fala = 'SUSPEITO:Tá doido!! Não sei do que você está falando!'
                for c in fala:
                    sleep(0.15)
                    print(c, end='', flush=True)
                sleep(2)
            elif resposta == 2:
                fala = 'SUSPEITO:Não! Ela falou que iria ficar na casa dos pais enquanto eu viajava.'
                for c in fala:
                    sleep(0.15)
                    print(c, end='', flush=True)
                sleep(2)
            elif resposta == 3:
                fala = 'SUSPEITO:O nome deles é: Fernando, Thiago, Vinicius e Roberta.\n Mas, o Thiago é so um conhecido do Vinicius, não sei realmente quem ele é.'
                for c in fala:
                    sleep(0.15)
                    print(c, end='', flush=True)
                sleep(2)
            brk = Bomba.explodir(relogio.horas)
            if brk == True:
                break
            if saida == True:
                break
        while brk == False:
            saida, resposta = Respostas.pergunta3()
            relogio.avancaTempo(20)
            system('cls')
            print(f'Já são: {relogio}')
            if resposta == 1:
                fala = 'SUSPEITO:Carla? O que ela está fazendo em São Paulo com o Thiago?\U0001F42E \n Ainda por cima saindo desse Motel!'
                for c in fala:
                    sleep(0.15)
                    print(c, end='', flush=True)
                sleep(2)
            elif resposta == 2:
                fala = 'SUSPEITO:Não, desde que fui enquadrado, eles me abandonaram.'
                for c in fala:
                    sleep(0.15)
                    print(c, end='', flush=True)
                sleep(2)
            elif resposta == 3:
                fala = 'SUSPEITO:Fernando eu conheci em uma briga de bar.\nVini, a gente joga bola as vezes.\n Roberta, ela é uma amiga de um cursinho que frequento!\n Já o Thiago é um conhecido do Vini.'
                for c in fala:
                    sleep(0.15)
                    print(c, end='', flush=True)
                sleep(2)
            brk = Bomba.explodir(relogio.horas)
            if brk == True:
                break
            if saida == True:
                break
        while brk == False:
            saida, resposta = Respostas.pergunta4()
            relogio.avancaTempo(20)
            system('cls')
            print(f'Já são: {relogio}')
            if resposta == 1:
                fala = 'SUSPEITO:Filho da ****, desgraçado, ainda confiei naquele canalha!'
                for c in fala:
                    sleep(0.15)
                    print(c, end='', flush=True)
                sleep(2)
            elif resposta == 2:
                fala = 'SUSPEITO:Beleza, depois do que o canalha aprontou, não tem o porquê acobertar ele...'
                for c in fala:
                    sleep(0.15)
                    print(c, end='', flush=True)
                sleep(2)
                system('cls')
                print(f'Já são: {relogio}')
                fala = 'SUSPEITO:estavamos eu e Thiago com planos de explodir o museu de arte Assis Chateaubriand...'
                for c in fala:
                    sleep(0.15)
                    print(c, end='', flush=True)
                sleep(2)
                system('cls')
                print(f'Já são: {relogio}')
                fala = 'SUSPEITO:esses corruptos do museu vem contrabandeando artes importantes de Recife...'
                for c in fala:
                    sleep(0.15)
                    print(c, end='', flush=True)
                sleep(2)
                system('cls')
                print(f'Já são: {relogio}')
                fala = 'SUSPEITO:como de tudo que a gente tentava não dava certo, a única opção para eles não sairem ganhando, era explodindo tudo!'
                for c in fala:
                    sleep(0.15)
                    print(c, end='', flush=True)
                sleep(2)
                system('cls')
            elif resposta == 3:
                fala = 'SUSPEITO:Eu não sou terrorista!! O Thiago que é!!'
                for c in fala:
                    sleep(0.15)
                    print(c, end='', flush=True)
                sleep(2)
            brk = Bomba.explodir(relogio.horas)
            if brk == True:
                break
            if saida == True:
                break
        if brk == False:
            fala = 'Teremos que ir ao museu encontrar essa bomba, antes que exploda...'
            for c in fala:
                sleep(0.15)
                print(c, end='', flush=True)
            sleep(2)
            relogio.avancaTempo(30)
            system('cls')
            print('Chegamos ao museu, onde vamos começar a procurar?:')
        while brk == False:
            print(f'Já são: {relogio}')
            local = int(input('''
               1.Salão principal
               2.Banheiros
               3.Sala das cameras
               4.Cofre
               5.Deposito
               R:'''))
            system('cls')
            if local == 1:
                Museu.salao_principal()
            elif local == 2:
                Museu.banheiros()
            elif local == 3:
                Museu.sala_das_cameras()
                museu.pista -= 1
            elif local == 4:
                Museu.cofre()
            elif local == 5:
                Museu.deposito()
                museu.pista -= 1
            if museu.pista == 0:
                break
            print('ok, vamos procurar mais...')
            brk = Bomba.explodir(relogio.horas)
            if brk == True:
                break
            relogio.avancaTempo(20)
        if relogio.horas < 11:
            system('cls')
            fala = 'Beleza, acho que já sei onde ta a bomba e de que tipo ela é...'
            for c in fala:
                sleep(0.15)
                print(c, end='', flush=True)
            sleep(2)
            system('cls')
            fala = 'É isso, sabia que ele tinha posto nessa sala a esquerda. Tenho que tomar cuidado com os celulares pra não ativar a bomba...'
            for c in fala:
                sleep(0.15)
                print(c, end='', flush=True)
            sleep(2)
            system('cls')
            print('Trabalho feito!')
            print('Parabéns!! Você conseguiu desarmar a bomba a tempo.')
