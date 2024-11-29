
import calculos
#with open("respostas.txt", "w") as arquivo:
#    arquivo.write("  ")

print(" Olá, qual conta você deseja realizar?\n Para uma conta de soma digite 1 \n")
print("para uma conta de subtração digite 2 \n para uma conta de divisão digite 3 \n")
print("para uma conta de multiplicação digite 4 \n para uma conta de potencia digite 5 \n e para uma conta de raiz quadrada digite 6")

conta = int(input("Operação esolhida: "))
valor1 = int(input("Agora escolha um numero: "))
valor2 = int(input("E agora o segundo numero: "))
if conta == 1:
   with open("respostas.txt", "a") as arquivo:

     v=calculos.soma(valor1,valor2)
    
     arquivo.write(str(v))
if conta == 2:
   with open("respostas.txt", "a") as arquivo:
     v=calculos.sub(valor1,valor2)
     arquivo.write(str(v))
  
   with open("respostas.txt", "a") as arquivo:
     arquivo.write( "\n")
  
if conta == 3:
   with open("respostas.txt", "a") as arquivo:
     v=calculos.divi(valor1,valor2)
     arquivo.write(str(v))
  
   with open("respostas.txt", "a") as arquivo:
     arquivo.write( "\n")
  

if conta == 4:
   with open("respostas.txt", "a") as arquivo:
     v=calculos.multi(valor1,valor2)
     arquivo.write(str(v))
  
   with open("respostas.txt", "a") as arquivo:
     arquivo.write( "\n")

if conta == 5:
   with open("respostas.txt", "a") as arquivo:
     v=calculos.poten(valor1,valor2)
     arquivo.write(str(v))
  
   with open("respostas.txt", "a") as arquivo:
     arquivo.write( "\n")

if conta == 6:
   with open("respostas.txt", "a") as arquivo:
     v=calculos.raizQuad(valor1)
     arquivo.write(str(v))
  
   with open("respostas.txt", "a") as arquivo:
     arquivo.write( "\n")
  

  

  
