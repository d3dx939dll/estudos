#!/usr/bin/python3
#filename: MyamotoMusachi.py

from random import choice

#wordlist mal feita
def gera_wordlist():
	nome = input('Nome Do Arquivo:')

	#edite seu arquivo por aqui
	arquivo = open(nome+'.txt', 'w')
	pergunta = int(input("Numero: "))
	lista = range(pergunta)
	
	for i in lista:
		arquivo.write(str(i)+"\n")

#gerador de senha
class gerador():
    # função top
    def gerador_senha(tamanho):
        caracteres = "0123456789abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/*$%#@!=\-"
        senha = ""
        for i in range(tamanho):
            senha += choice(caracteres)
        return senha


#gerador de caracteres
def gera(senha, n):
  char = [chr(i) for i in range(33, 123)]
  if (n > 0):
    for item in char: 
       gera(senha + item, n - 1)
  else:   
    print(senha)      

print('''

 __  __                             _        
|  \/  |_   _  __ _ _ __ ___   ___ | |_ ___  
| |\/| | | | |/ _` | '_ ` _ \ / _ \| __/ _ \ 
| |  | | |_| | (_| | | | | | | (_) | || (_) |
|_|  |_|\__, |\__,_|_| |_| |_|\___/ \__\___/ 
        |___/                                
 __  __                      _     _ 
|  \/  |_   _ ___  __ _  ___| |__ (_)
| |\/| | | | / __|/ _` |/ __| '_ \| |
| |  | | |_| \__ \ (_| | (__| | | | |
|_|  |_|\__,_|___/\__,_|\___|_| |_|_|
                                     


1 - Wordlist
2 - Gera Senha
3 - Numero Random
4 - Ajuda/Sobre
5 - Sair
''')

#decisao logica padrão :(
pergunta = input(">")
if pergunta == "1":
	print("\n[*] Gerador De Wordlist\n")
	gera_wordlist()

elif pergunta =='2':
	print("\n[*] Gerador De Senha\n")
	
	nome = input("Digite o nome de usuário: ")
	quantidade = int(input("Digite a quantidade de caracteres que deseja ter na senha: "))
	senha = gerador.gerador_senha(quantidade)
	print("Pass: {}".format(senha))
	print()

elif pergunta =='3':
	print("\n[*] Gerador De caracteres\n")
	texto = input("Texto:")
	vezes = int(input("Vezes: "))
	gera(texto, vezes)

elif pergunta == '4':
	print("\n[*Ajuda]\n(1) - Wordlist\n(2) - Gera Senha\n(3) - Numero Random\n(4) - Sobre")
	pergunta2 = input(">")

	if pergunta2 == '1':
		print("\n[*] - Wordlist")
		print("(*) Nome - Defina o nome para sua wordlist.")
		print("(*) Numero - Defina Ate Quantos numero Sua wordlist terá.")
	elif pergunta2 == '2':
		print("\n[*] Gera Senha")
		print("(*) Usuario - Nome Da Conta.")
		print("(*) Pass - Senha Gerada.")
	elif pergunta2 == '3':
		print("\n[*] Numero Random")
		print('(*) Texto - Frase ou texto na tela.')
		print('(*) Vezes - Numeros Aleatorios com os caracteres da tabela ASCII.')

	elif pergunta2 == '4':
		print("\n>> Sobre:")
		print('''
     _ _____     _       ___ _____ ___      _ _ _ 
  __| |___ /  __| |_  __/ _ \___ // _ \  __| | | |
 / _` | |_ \ / _` \ \/ / (_) ||_ \ (_) |/ _` | | |
| (_| |___) | (_| |>  < \__, |__) \__, | (_| | | |
 \__,_|____/ \__,_/_/\_\  /_/____/  /_/ \__,_|_|_|
                                                  
''')
		print("Programa criado por @d3dx939dll.")
elif pergunta =='5':
	print("Bye Myamoto...")

#Sobre

#Nome: MyamotoMusachi
#Data: 21/05/2021

#Referências

#Gera Senha: 
#https://pastebin.com/DZx3UX8n

#Gera Caracteres Aleatorio:
#https://pt.stackoverflow.com/questions/416088/como-fazer-um-gerador-de-senhas-sem-usar-v%c3%a1rios-loops#416114