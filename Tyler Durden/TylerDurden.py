#!/bin/usr/python
#Filename: cal.py
#Calculadora em python "Classica" com adição e subtração.

#função para somar :v
def mais():
	
	#intro foda
	print(''' 
		# = = = = = Cal.py = = = = = #
		           "Adicao"
		          
		# = = = = = = = = = = = = =  #
		''')
	
	#valores
	a = int(input("Digite o Primeiro Valor: "))
	b = int(input("Segundo Valor: "))
	
	#somando
	c = a +  b
	
	#final
	print("Resultado Final:", c)

#mini funcao para subtrair
def menos():
	
	#intro foda 2
	print(''' 
		# = = = = = Cal.py = = = = = #
		         "Subtracao"
		          
		# = = = = = = = = = = = = =  #
		''')
	
	#valores a e b
	a = int(input("Digite o Primeiro Valor: "))
	b = int(input("Segundo Valor: "))
	
	#subtraindo
	c = a -  b
	
	#valor final
	print("Resultado Final:", c)


#menu topzera se e louco kkkk
print('''
*Cal.py

1 - Adicao
2 - Subtracao
3 - Sair
	''')

#decisao logica do programa 
pergunta = input(">")
if pergunta == '1':
		mais()

elif pergunta =='2':
		menos()
		
elif pergunta =='3':
		exit
else:
	print("Acho que houve um erro :/")

#sim eu fiz um menu com if e else :/
'''
Mini programa basico feito em estudos basicos de python :V
Depois mande um salve para @d3dx939dll
'''