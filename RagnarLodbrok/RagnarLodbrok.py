#!/usr/bin/python3
#filename: RagnarLodbrok.py

import wget
import requests
import os

#instalação de pacotes
print("Instalando Alguns Pacotes (Wget, Requests)\n")
os.system("pip install requests")
os.system("pip install wget")

#primeira função com wget
def baixar():
	endereco = input("Digite o link:")
	baixador = wget.download(endereco)

#segunda função com request
def baixar2():
	nome = input("Nome:")
	site = input("Link: ")
	f = open(nome,'wb')
	response = requests.get(site)
	f.write(response.content)
	f.close()

	print("Download Feito Com Sucesso!")

os.system("clear")

#apresentação do programa.
while True:
	print('''
  _    _    _    _    _    _     _    _    _    _    _    _    _  
 / \  / \  / \  / \  / \  / \   / \  / \  / \  / \  / \  / \  / \ 
( R )( a )( g )( n )( a )( r ) ( L )( o )( d )( b )( r )( o )( k )
 \_/  \_/  \_/  \_/  \_/  \_/   \_/  \_/  \_/  \_/  \_/  \_/  \_/ 


1 - WGET
2 - REQUEST
3 - Sobre
4 - Sair
	''')

	#variavel do programa

	escolha = input(">")
	
	#parte "logica" do programa
	#wget
	if escolha == '1':
		print('''
  _    _    _    _  
 / \  / \  / \  / \ 
( W )( G )( E )( T )
 \_/  \_/  \_/  \_/ 
''')
		print("Ex: ")
		baixar()

	#request
	elif escolha == '2':
		print('''
  _    _    _    _    _    _    _  
 / \  / \  / \  / \  / \  / \  / \ 
( R )( E )( Q )( U )( E )( S )( T )
 \_/  \_/  \_/  \_/  \_/  \_/  \_/ 

			  ''')
		print("Ex: Nome: nome do arquivo + Extensão \nLink: URL do Arquivo")
		baixar2()

	#sobre o programa
	elif escolha == '3':
		os.system("clear")
		print('''
			 \n>> Como Usar RagnarLodbrok?
			 \n[*] WGET - Passe uma url simples.
			 \n[*] Request - No campo de "Nome" coloque nome do arquivo junto com a extensão,\nem seguida no campo de link, insira sua url. 
			 \nFeito Por: @d3dx939dll''')

	#saida
	elif escolha =='4':
		break


#Sobre

#Nome:RagnarLodbrok
#Data:21/05/2021

#Referencias:

#1 > https://www.delftstack.com/pt/howto/python/download-image-in-python/
#2 > https://rschalch.github.io/wget-download-arquivos-com-python.html



