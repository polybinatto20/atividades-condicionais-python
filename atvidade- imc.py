import os

#Limpando a tela
os.system('cls')

peso=int(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))

imc= peso / (altura*altura)



if(imc ==16.9):
 print("Você está muito abaixo do peso", imc)

elif(imc >=17 and imc<= 18.4 ):
 print("Você está abaixo do peso ", imc)

elif(imc >= 18.5 and imc<=24.9 ):
 print("Você está com o peso normal ", imc)

elif(imc >=25 and imc== 29.9 ):
 print("Você está acima do peso" , imc)

elif(imc ==30 and imc==34.9):
 print("Obesidade grau 1", imc)
elif( imc>=40 ):
 print("Obesidade grau 2", imc)

elif(imc>40):
 print("Obesidade grau 3 ", imc)
