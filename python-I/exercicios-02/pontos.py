import math

x1=float(input("Digite um número: "))
y1=float(input("Digite um número: "))
x2=float(input("Digite um número: "))
y2=float(input("Digite um número: "))

distancia=math.sqrt((x1-x2)**2 + (y1-y2)**2)

if distancia>=10:
    print("longe")
else:
    print("perto")
