#https://docs.python.org/3/library/turtle.html#appearance

'''
1) Modifique o programa da tartaruga (primeiro exemplo) para que, antes de criar a 
janela, ele solicite que o usuário insira a cor de fundo desejada. Ele deve armazenar 
as respostas do usuário em uma variável e modificar a cor da janela de acordo com os 
desejos do usuário.
'''
import turtle
a = str(input('Digite a cor de fundo desejada:'))
jn = turtle.Screen()
jn.bgcolor(a)

'''
2)Faça modificações similares para permitir que o usuário mude a cor da tartaruga durante a execução do programa.
'''

b = str(input('Se desejar pode mudar a cor da tratura também:'))
teca = turtle.Turtle()
teca.colo(b)

'''
2a)Faça o mesmo para a largura da caneta da tartaruga. Dica: seu diálogo com o usuário retornará uma string, mas o método pensize espera que seu argumento seja um int. Então, você precisará converter a string em um int antes de passá-la para pensize.
'''

c = int(input('Se quiser pode mudar também a largura da caneta'))
teca.pensize(c)

'''
4)desenhe um quadrado, usando a forma de tartaruga, ao invés da flecha, para desenhar.
'''
teca = turtle.shape("turtle")
for i in [0,1,2,3]:
    teca.forward(60)#medida de cada lado da figura
    teca.left(90)#faz a tartaruga virar 90°
jn.mainloop ()

INCOMPLETO
