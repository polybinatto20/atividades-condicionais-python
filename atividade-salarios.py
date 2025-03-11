import os 

#Limpar tela
os.system('cls')
print("ESCOLA APRENDER salário professores")
print("===================================")

nivelprof=int(input("Digite seu nível: "))
quantidadeaulas=int(input("Digite quantas aulas você leciona por semana:"))
                    
if(nivelprof == 12):
  salariofinal= nivelprof * quantidadeaulas * 4
  print("Seu salário é: ", salariofinal)

elif(nivelprof == 17 ):
  salariofinal= nivelprof * quantidadeaulas * 4
  print("Seu salário final é:  ", salariofinal)

elif(nivelprof == 25):
  salariofinal= nivelprof * quantidadeaulas * 4
  print("Seu salário final é: ",salariofinal )
                
                    