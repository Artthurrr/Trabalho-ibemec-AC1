a = float(input("digite o coeficiente a :"))
b = float(input("digite o coeficiente b :"))
c = float(input("digite o coeficiente c :"))

delta = (b ** 2) - 4*a*c

if delta < 0 :
   print("Não existe raiz real")
elif delta == 0:
    x1 = (-b + delta ** 0.5) / (2*a)
print("Raiz: ",x1) 
 
x1 = (-b + delta ** 0.5) / (2*a)
x2 = (-b - delta ** 0.5) / (2*a)
print("Primeira Raiz: ",x1)
print("Segunda Raiz: ",x2)
