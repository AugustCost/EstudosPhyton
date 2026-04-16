#condicionais
#if, elif e else
'''
E ai Augusto, vamos sair hoje?
Se eu terminar o trabalho aqui, eu consigo.
'''
trabalho_terminado = False
if trabalho_terminado == True:
    print('Opa, vamos sair!')
else:
    print('Não posso sair agora.')

'''
Ei, voce consegue me ajudar a mover essas caixas la pra fora hoje a tarde?
se eu estiver livre, sim mas, se nao der pede meu irmao pra te ajudar
'''

estou_livre = False
if estou_livre == True:
    print('Eu consigo te ajudar')
else:
    print('peça ajuda ao meu irmão.')

'''
Eu cheguei na aula atrasado, ainda posso entrar?
se essa n for sua terceira vez chegando atrasado, então sim, caso contrario irá tomar uma suspensão
'''

numero_de_atraso = 1
if numero_de_atraso >=3:  
    print('você está suspenso')
elif numero_de_atraso == 1:
    print('Pode entrar, porém caso tome mais 2 faltas, irá ser suspenso')
elif numero_de_atraso ==2:
    print('pode entrar, porém caso tome mais 1 falta, irá ser suspenso')
else:
   print('Pode entrar!')

'''
Encontre o maior entre dois numeros
'''

primeiro_valor = input('digite o primeiro numero')
segundo_valor = input('digite o segundo numero')

if primeiro_valor > segundo_valor:
    print('o primeiro valor é o maior')
else:
    print('segundo valor é maior')