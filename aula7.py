import turtle
def draw_bar(t, height): #faz a tartaruga t desenhar uma barra de altura.
    t.begin_fill() #inicia o rastro da tartaruga, mas pq os() ficam vazios?
    t.left(90)#vira pra direita num angulo de 90 graus
    t.forward(height) #o que isso faz??
    t.write("ABC"+str(height)) #o termo ABC entra na frente dos nº de xs
    t.right(90)#vira pra direita num angulo de 90
    t.forward(40)#define o comprimento (em x) de cada torre
    t.right(90) #vira pra direita num angulo de 90 graus
    t.forward(height)#o que isso faz?
    t.left(90)#vira pra esquerda num angulo de 90 graus
    t.end_fill()#finaliza o rastro da tartaruga, pq os () ficam vazios?
    t.forward(10) #define a distancia entre cada torre


wn = turtle.Screen() #inicia o programa turtle
wn.bgcolor("lightgreen") #o fundo da pagina  fica verde claro

tess = turtle.Turtle()
tess.color("blue","red")#define o rastro azul e o preenchimento em vermelho
tess.pensize(3)#determina a espessura do rastro da turtle

xs = [48,117,200,240,160,260,220] #esses valores são a frequencias em y

for a in xs:
    draw_bar(tess, a)#o que esse comando faz?

wn.mainloop()
