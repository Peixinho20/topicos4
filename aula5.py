#aula5 exercícios (revisando a aula 4 e fazendo os exercícios da aula 5)

#exemplo da aula 4

def do_twice (f):
    f ()
    f ()


def print_spam ():
    print ('spam')

do_twice ('print_spam')
spam #resultados do do_twice ('print_spam')
spam


'''
Digite este exemplo em um script e teste-o. Modifique do_twice para que sejam necessários dois argumentos (f,g) , um objeto de função (f) e um valor (g), e chame a função duas vezes (do_twice(f,g)), passando o valor (g) como um argumento.
'''

def do_twice (f,g):
    f(g)
    f(g)

do_twice(print,'choveu')#o f é print e o argumento (choveu) é o g.
choveu
choveu


'''
Escreva uma versão mais geral de print_spam, chamada print_twice, que use uma string como parâmetro e imprima duas vezes. 
'''

def do_twice (f,g):
     f(g)
     f(g)
 
def print_twice (f):
     print (f)
     print (f)
 
do_twice(print_twice,'sacoooo')
sacoooo
sacoooo
sacoooo
sacoooo

#Use a versão modificada de do_twice para chamar print_twice duas vezes, passando 'spam' como um argumento.

def print_twice (f):
    print(f) #usei só um print em comparação com anterior, se tivesse usado igual ao anterior, ele imprimiria quatro vezes.
 
do_twice(print_twice,'spam')
spam
spam


incompleta
