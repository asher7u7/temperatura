"""----------Programa para -------------------
-----------convertir temperatura--------------
----------------------------------------------"""


print("-------------------------------------")
print("-----conversor de temperatura--------")
print("-------------------------------------")

#input
c=int(input("digite grados celcius: "))

#procedure
k=c+273.15
f=1.8*c+32

#output
print("\nResultado\n")
print(str(c) + " Grados Celcius es igual a \n" + str(k) + " Grados Kelvin  \n"+ str(f) + " Grados fahrenheit")
