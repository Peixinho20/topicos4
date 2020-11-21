1)
def tipo(x):
    print(type(x)
    print(x)
tipo(x) #coloque o valor de x, não precisa ser numérico
        #se for frase, tem que colocar entre aspas simples


exercício 1:
#Crie uma funcão que tome um argumento e imprima o valor e o tipo dele.

>>>def poema_topicos(): #definindo a função no terminal
    print('Essa terra tem palmeiras')
    print('Onde canta o sabiá.')


>>> poema_topicos # onde a função está
<function poema_topicos at 0xb76993d4>

>>> poema_topicos() # o valor da função
Nessa terra tem palmeiras
Onde canta o sabiá

>>> type(poema_topicos)
<class 'function'>

>>> type(poema_topicos()) # resposta do exercício
Nessa terra tem palmeiras
Onde canta o sabiá.
<class 'NoneType'>
