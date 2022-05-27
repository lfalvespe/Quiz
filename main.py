from questoes import Questoes
from prova import Prova
import uteis
import os
from random import shuffle

msg = 'Ult. Prof. V1.0 - English Test'
uteis.cabecalho(msg)
print(f'{"INÍCIO":^38}\n')

q1 = Questoes('O verbo "Pretend" significa:', 'e',
               'Pretender',
               'Preferir',
               'Persuadir',
               'Promover',
               'Fingir')

q2 = Questoes('Qual o plural de dentes em inglês?', 'a',
               'Teeth',
               'Tooth',
               'Teethe',
               'Toot',
               'Denth')
q3 = Questoes('Complete: _____ mice in the garden.', 'b',
               'There is',
               'There are',
               'Are',
               'is',
               'isnt')

q4 = Questoes('O Past Participle de Begin é:', 'd',
               'Begin',
               'Begins',
               'Began',
               'Begun',
               'Beginning')

q5 = Questoes('Marque a alternativa incorreta:', 'c',
               'Expensive - Caro',
               'Inflood - Enchente',
               'Sheep - Barato',
               'Earthquake - Terremoto',
               'Roof - Teto')

q6 = Questoes('Could you ______ me some money?', 'a',
               'Lend',
               'Invite',
               'Have',
               'Buy',
               'Spend')

lista = [q1, q2, q3, q4, q5, q6]
shuffle(lista)
sortida = [lista[0], lista[1], lista[2], lista[3], lista[4], lista[5]]

p1 = Prova(sortida[0], sortida[1],sortida[2], sortida[3], sortida[4], sortida[5])

nome = str(input('\033[3mDigite o seu nome: ')).strip().capitalize()
print(f'\n\033[3;36mBem vindo(a), \033[4m{nome.upper()}.\033[m')
_ = input(' \n\n\033[35mPressione Enter para iniciar o seu teste.\033[m')
os.system('cls' if os.name == 'nt' else 'clear')
uteis.cabecalho(msg)

while True:
  acertos = 0

  for c in p1.prova.keys():
    resp = ''
    print(c, '-', f'\033[30;47m{p1.prova[c].pergunta}\033[m')
    print()
    for k, v in p1.prova[c].opcoes.items():
      print(k, v)
    print()
    
    resp = uteis.validacao('\033[3;30;44mSua Resposta:\033[m ')
    print()
    if (resp == p1.prova[c].resposta):
      print('\033[32mResposta Correta!!!!\033[m\n')
      acertos+=1
      c = input('\033[3;34mPressione Enter para continuar: \033[m')
      os.system('cls' if os.name == 'nt' else 'clear')
      uteis.cabecalho(msg)
    else:
      print('\033[31mVocê Errou!!!\033[m\n')
      c = input('\033[3;34mPressione Enter para continuar: \033[m')
      os.system('cls' if os.name == 'nt' else 'clear')
      uteis.cabecalho(msg)
  
  print(f'### Resultado de {nome} ###\n')
  print(f'\033[1;34;40mTotal de Acertos: {acertos}\033[m')
  
  print()
    
  while True:
    
    refazer = str(input('\033[35mRefazer Teste? [S/N]: \033[m'))
    if refazer not in 'SsNn':
      print("Digite S ou N")
      continue
    if refazer in 'Ss':
      os.system('cls' if os.name == 'nt' else 'clear')
      uteis.cabecalho(msg)
      break
    elif refazer in 'Nn':
      break
  if refazer in 'Nn':
    print(f'\n\n\033[33m{" FIM ":*^38}\033[m')
    break

    