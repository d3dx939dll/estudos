import os
import time
print("\n\nJaxTeller 1.0")

def ping():
	os.system('clear')
	print("Ping")
	site = input("Digite o site:")
	os.system('ping -w1 '+ site)
	print("\nObs:Esperamos 5 Segundos\n")
	time.sleep(5)

def traceroute():
	os.system('clear')
	print("Traceroute")
	site = input("Digite o site:")
	os.system('traceroute '+ site)
	print("\nObs:Esperamos 5 Segundos\n")
	time.sleep(5)

def whois():
	os.system('clear')
	print("Whois")
	site = input("Digite um site:")
	os.system('whois '+ site)
	print("\nObs:Esperamos 5 Segundos\n")
	time.sleep(5)
while True:
	print("Menu - Pobre \n1 - Ping \n2 - Traceroute\n3 - Whois \n4 - Sobre \n5 - Sair")
	resposta = input("\n>")

	if resposta == '1':
		ping()
	elif resposta == '2':
		traceroute()
	elif resposta == '3':
		whois()
	elif resposta =='4':
		os.system('clear')
		print("\nSobre:\nUm programa feito com ferramentas do sistema Linux.\nFeito Por @d3dx939dll\n")
	elif resposta =='5':
		print("Saindo...")
		break
'''
Feito Por @d3dx939dll
Obs: Projeto feito em base de estudo basico de python.
'''
