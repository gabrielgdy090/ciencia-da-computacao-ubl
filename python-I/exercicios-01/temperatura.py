print("delta=(b**2)-(4*a*c)")
a=int(input("Digite o valor de a?"))
b=int(input("Digite o valor de b?"))
c=int(input("Digite o valor de c?"))

delta=(b**2)-(4*a*c)
x1=(((-1)*b)-(delta**0.5))/(2*a)
x2=(((-1)*b)-(delta**0.5))/(2*a)
if delta>0:
    print("A equação possui 2 raízes distintas)
if x1!=x2:
    print("O valor de x1 é ",x1 and "O valor de x2 é",x2)
        
if delta<0:
    print("A equação não possui raízes reais")
    
if delta==0:
    print("A equação possui 1 raiz real dupla, isto é x==x")
if x1==x2:
    print(x1 or x2)
        
