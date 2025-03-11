import os 
#Limpando a tela
os.system('cls')

nomeproduto= input("Qual é o nome do produto?: ")
qa= float(input("Quanto foi adquirido?: "))
precounitario=float(input("Qual é o preço unitário?: "))

totalsemdesconto= (qa * precounitario)




print("O valor a pagar sem desconto é: ", totalsemdesconto)

if(qa <= 5):
    desconto = totalsemdesconto * 0.02
    print(" Valor do desconto: ", desconto)
    print("Valor total: " , totalsemdesconto - desconto)

elif(qa >5 and qa <=10  ):
    desconto= totalsemdesconto * 0.03
    print("Valor do desconto: " , desconto)
    print("Valortotal: ", totalsemdesconto- desconto )

elif(qa>10):
    desconto= totalsemdesconto * 0.5
    print("Valor do desconto: ", desconto )
    print("Valor total: ", totalsemdesconto - desconto )