def cabecalho(msg):
  print('\033[31m*\033[m'*38)
  print(f'\033[3;37m{msg:^35}\033[m')
  print('\033[32m*\033[m'*38)
  print()

def validacao(msg):
  
  while True:
    r = str(input(msg)).lower()
    if r == '':
      print('\nERRO: Você não digitou um valor!\n')
    elif r not in 'ABCDEabcde':
      print('\nERRO: Digite uma resposta válida!\n')
    else:
      return r
      break
      
  