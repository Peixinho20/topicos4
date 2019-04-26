class Ponto:
     def __init__(self):
         self.x = 0
         self.y = 0
 
p = Ponto()
q = Ponto()
 
print(p.x, p.y, q.x, q.y)
0 0 0 0

#ATRIBUTOS
p = Ponto()
p.x = 3
p.y = 4
print(p.x, p.y)
3 4
print(type(p))
<class '__main__.Ponto'> #RESULTADO DOS PRINTS
print(type(p.x))
<class 'int'> #RESULTADO DOS PRINTS


#Melhorando nosso inicializador
class Ponto:
     def __init__(self, x=0, y=0):
         self.x = x
         self.y = y
 
p = Ponto (4, 2)
q = Ponto (6, 3)
r = Ponto()
print(p.x, q.y, r.x)
4 3 0

INCOMPLETO
