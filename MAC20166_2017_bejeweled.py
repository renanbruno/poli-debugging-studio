	'''
		Este código não tem o intuito de servir como base para nenhum EP na Escola Politécnica,
		apenas sendo utilizado como guia para facilitar a detecção e correção de eventuais bugs.

		Também não propomos esgotar todos os casos possíveis de erro nas funções descritas no EP,
		mas só talvez os casos de erro mais comuns e mais esperados.

		Este código não é oficial da Escola Politécnica nem do IME ou outras instituições da USP. Foi feito por
		um aluno, com única intenção de facilitar correções e debugging nos seus respectivos códigos. 

		Se notar algum bug ou algum teste essencial que esteja faltando, comente no meu repositório do Github:
		https://github.com/lucasmsobrinho/poli-debugging-studio
	
		Como usar?
			1. Faça uma cópia de segurança do código do seu EP.
			2. Certifique-se de que o seu código não possui erros de compilação.
			3. Copie todo o código desse arquivo no lugar da chamada da função principal: main()
	'''

	def exibe_matriz(tabuleiro_inicial, tabuleiro_esperado, tabuleiro_retornado):
	'''
	Exibe lado a lado os tabuleiros INICIAL, ESPERADO, RETORNADO, MAPA DE ERROS ( - , X ) = ( acerto, erro )

	Exemplo de saída correta: após uso da função __deslocar (tabuleiro)__
	A B C B   =>    A         =>  A         =|  - - - -
	A   A B   =>    A   C B   =>  A   C B   =|  - - - -
	B   C C   =>    B   A B   =>  B   A B   =|  - - - -
	D         =>    D B C C   =>  D B C C   =|  - - - -

	Exemplo de saída incorreta: após uso da função __deslocar (tabuleiro)__
	A B C B   =>    A         =>  A   C B   =>  - - X X
	A   A B   =>    A   C B   =>  A   C B   =>  - - - -
	B   C C   =>    B   A B   =>  B   A B   =>  - - - -
	D         =>    D B C C   =>  D B C C   =>  - - - -

	'''

	if(len(tabuleiro_esperado) == len(tabuleiro_retornado) and len(tabuleiro_esperado[0]) == len(tabuleiro_retornado[0])):
		erros = 0
		print()
		print("TABULEIRO INICIAL => TABULEIRO ESPERADO => TABULEIRO RETORNADO => MAPA DE ERROS")
		print()
		for i in range(len(tabuleiro_inicial)):
			for j in range(len(tabuleiro_inicial[0])):
				print(tabuleiro_inicial[i][j], end = " ")
			print("   =>", end="   ")

			for j in range(len(tabuleiro_inicial[0])):
				print(tabuleiro_esperado[i][j], end = " ")
			print("   =>", end="   ")

			for j in range(len(tabuleiro_inicial[0])):
				print(tabuleiro_retornado[i][j], end = " ")
			print("   =>", end="   ")

			for j in range(len(tabuleiro_inicial[0])):
				if(tabuleiro_esperado[i][j] == tabuleiro_retornado[i][j]):
					print("-", end = " ")
				else:
					print("X", end = " ")
					erros += 1
			print()
		if(erros>0):
			print("Numero de erros : %d" % erros)
		print()
	else:
		print("Tabuleiro Esperado e Tabuleiro Retornado não possuem mesmas dimensoes!")


def testes_unitarios ():
	'''
		Realiza uma série de testes em todas as funções do EP2, com exceção das funções Exibir e Criar.
	'''
	testes = 0
	# Testes função trocar
	# Erros previstos:
	# 1. trocar elementos não vizinhos
	# 2. trocar elementos que não formam sequencia de 3 ou mais
	tabuleiro_inicial = [ ['A', 'B', 'D', 'A'],
						  ['A', 'A', 'C', 'A'],
						  ['B', 'C', 'B', 'D'],
						  ['D', 'D', 'A', 'D']]

	tabuleiro_esperado = [ ['A', 'B', 'D', 'A'],
						   ['A', 'A', 'C', 'A'],
						   ['B', 'C', 'B', 'D'],
						   ['D', 'D', 'A', 'D']]

	tabuleiro_retornado = [ ['A', 'B', 'D', 'A'],
							['A', 'A', 'C', 'A'],
							['B', 'C', 'B', 'D'],
							['D', 'D', 'A', 'D']]

	trocar(2,0,3,2,tabuleiro_retornado)
	if (tabuleiro_esperado == tabuleiro_retornado):
		testes += 1
		print("\nTeste 1[trocar]: Aprovado")
	else:
		print("\nTeste 1[trocar]: Reprovado")
		print("	Erros mais comuns:")
		print("	1. trocar elementos não vizinhos")
		print("	2. trocar elementos que não formam sequencia de 3 ou mais")
		exibe_matriz(tabuleiro_inicial, tabuleiro_esperado, tabuleiro_retornado)
######################################################################################
	tabuleiro_esperado = [ ['A', 'B', 'D', 'A'],
						   ['A', 'A', 'C', 'A'],
						   ['B', 'C', 'B', 'D'],
						   ['D', 'D', 'A', 'D']]
	
	tabuleiro_retornado = [ ['A', 'B', 'D', 'A'],
							['A', 'A', 'C', 'A'],
							['B', 'C', 'B', 'D'],
							['D', 'D', 'A', 'D']]

	tabuleiro_retornado = list(tabuleiro_inicial)
	trocar(0,2,3,2,tabuleiro_retornado)
	if (tabuleiro_esperado == tabuleiro_retornado):
		testes += 1
		print("\nTeste 2[trocar]: Aprovado")
	else:
		print("\nTeste 2[trocar]: Reprovado")
		print("Erros mais comuns:")
		print("1. trocar elementos não vizinhos")
		print("2. trocar elementos que não formam sequencia de 3 ou mais")
		exibe_matriz(tabuleiro_inicial, tabuleiro_esperado, tabuleiro_retornado)
######################################################################################
	tabuleiro_esperado = [ ['A', 'B', 'D', 'A'],
						   ['A', 'A', 'A', 'C'],
						   ['B', 'C', 'B', 'D'],
						   ['D', 'D', 'A', 'D']]

	tabuleiro_retornado = [ ['A', 'B', 'D', 'A'],
							['A', 'A', 'C', 'A'],
							['B', 'C', 'B', 'D'],
							['D', 'D', 'A', 'D']]

	tabuleiro_retornado = list(tabuleiro_inicial)
	trocar(1,2,1,3,tabuleiro_retornado)
	if (tabuleiro_esperado == tabuleiro_retornado):
		testes += 1
		print("\nTeste 3[trocar]: Aprovado")
	else:
		print("\nTeste 3[trocar]: Reprovado")
		print("	Erros mais comuns:")
		print("	1. trocar elementos não vizinhos")
		print("	2. trocar elementos que não formam sequencia de 3 ou mais")
		exibe_matriz(tabuleiro_inicial, tabuleiro_esperado, tabuleiro_retornado)
######################################################################################
	# Testes função eliminar
	# Erros previstos:
	tabuleiro_inicial = [ ['A', 'B', 'A', 'D'],
						  ['A', 'A', 'A', 'A'],
						  ['B', 'C', 'A', 'D'],
						  ['D', 'D', 'A', 'D']]

	tabuleiro_esperado = [ ['A', 'B', ' ', 'D'],
						   [' ', ' ', ' ', ' '],
						   ['B', 'C', ' ', 'D'],
						   ['D', 'D', ' ', 'D']]

	tabuleiro_retornado = [ ['A', 'B', 'A', 'D'],
							['A', 'A', 'A', 'A'],
							['B', 'C', 'A', 'D'],
							['D', 'D', 'A', 'D']]

	num = eliminar(tabuleiro_retornado)
	if (tabuleiro_esperado == tabuleiro_retornado and num == 7):
		testes += 1
		print("\nTeste 4[eliminar]: Aprovado")
	else:
		print("\nTeste 4[eliminar]: Reprovado")
		print("	Erros mais comuns:")
		print("	1. Não elimina todas as sequencias")
		print("	2. Conta duas vezes as intersecoes entre cadeias")
		print("	3. Problemas na função eliminar_cadeia")
		exibe_matriz(tabuleiro_inicial, tabuleiro_esperado, tabuleiro_retornado)
		print("Numero de eliminados esperado: 7 ")
		print("Numero de eliminados retornado: %d " % num)
######################################################################################
	tabuleiro_inicial = [ ['A', 'B', 'A'],
						  ['A', 'A', 'C'],
						  ['B', 'A', 'A']]

	tabuleiro_esperado = [ ['A', 'B', 'A'],
						   ['A', 'A', 'C'],
						   ['B', 'A', 'A']]

	tabuleiro_retornado = [ ['A', 'B', 'A'],
							['A', 'A', 'C'],
							['B', 'A', 'A']]

	num = eliminar(tabuleiro_retornado)
	if (tabuleiro_esperado == tabuleiro_retornado and num == 0):
		testes += 1
		print("\nTeste 5[eliminar]: Aprovado")
	else:
		print("\nTeste 5[eliminar]: Reprovado")
		print("	Erros mais comuns:")
		print("	1. Não elimina todas as sequencias")
		print("	2. Conta duas vezes as intersecoes entre cadeias")
		print("	3. Problemas na função eliminar_cadeia")
		print("	4. Problemas nas funções identificar_cadeias_verticais/horizontais")
		exibe_matriz(tabuleiro_inicial, tabuleiro_esperado, tabuleiro_retornado)
		print("Numero de eliminados esperado: 0 ")
		print("Numero de eliminados retornado: %d " % num)
######################################################################################
	# Testes função identificar_cadeias_verticais
	tabuleiro_inicial = [ ['C', 'C', 'C', 'C', 'C'],
						  ['D', 'C', 'B', 'A', 'A'],
						  ['D', 'C', 'B', 'D', 'D'],
						  ['D', 'C', 'B', 'B', 'B'],
						  ['A', 'C', 'B', 'D', 'B']]
	lista_esperada = [ [1,0,3,0], [0,1,4,1], [1,2,4,2]]
	lista_retornada = identificar_cadeias_verticais(tabuleiro_inicial)

	if (lista_esperada == lista_retornada):
		testes += 1
		print("\nTeste 6[id_cad_v]: Aprovado")
	else:
		print("\nTeste 6[id_cad_v]: Reprovado")
		print("	Erros mais comuns:")
		print("	1. Não identificar propriamente as cadeias no início/final do tabuleiro")
		print("	2. Identificar um elemento a mais/a menos nas cadeias")
		print(tabuleiro_inicial)
		print("Lista esperada:")
		print(lista_esperada)
		print("Lista retornada:")
		print(lista_retornada)
		print()
######################################################################################
	tabuleiro_inicial = [ ['D', 'D', 'A', 'D'],
						  ['A', 'E', 'C', 'D'],
						  ['B', 'A', 'B', 'A'],
						  ['B', 'A', 'B', 'D']]

	lista_esperada = []
	lista_retornada = identificar_cadeias_verticais(tabuleiro_inicial)

	if (lista_esperada == lista_retornada):
		testes += 1
		print("\nTeste 7[id_cad_v]: Aprovado")
	else:
		print("\nTeste 7[id_cad_v]: Reprovado")
		print("	Erros mais comuns:")
		print("	1. Não identificar propriamente as cadeias no início/final do tabuleiro")
		print("	2. Identificar um elemento a mais/a menos nas cadeias")
		print(tabuleiro_inicial)
		print("Lista esperada:")
		print(lista_esperada)
		print("Lista retornada:")
		print(lista_retornada)
		print()

######################################################################################
	# Testes função identificar_cadeias_horizontais
	tabuleiro_inicial = [ ['C', 'C', 'C', 'C', 'C'],
						  ['D', 'C', 'B', 'A', 'A'],
						  ['D', 'C', 'B', 'D', 'D'],
						  ['D', 'C', 'B', 'B', 'B'],
						  ['A', 'C', 'B', 'D', 'B']]
	lista_esperada = [ [0,0,0,4], [3,2,3,4] ]
	lista_retornada = identificar_cadeias_horizontais(tabuleiro_inicial)

	if (lista_esperada == lista_retornada):
		testes += 1
		print("\nTeste 8[id_cad_h]: Aprovado")
	else:
		print("\nTeste 8[id_cad_h]: Reprovado")
		print("	Erros mais comuns:")
		print("	1. Não identificar propriamente as cadeias no início/final do tabuleiro")
		print("	2. Identificar um elemento a mais/a menos nas cadeias")
		print(tabuleiro_inicial)
		print("Lista esperada:")
		print(lista_esperada)
		print("Lista retornada:")
		print(lista_retornada)
		print()
######################################################################################
	tabuleiro_inicial = [ ['D', 'D', 'A', 'D'],
						  ['A', 'E', 'C', 'D'],
						  ['B', 'A', 'B', 'A'],
						  ['B', 'A', 'B', 'D']]

	lista_esperada = []
	lista_retornada = identificar_cadeias_horizontais(tabuleiro_inicial)

	if (lista_esperada == lista_retornada):
		testes += 1
		print("\nTeste 9[id_cad_h]: Aprovado")
	else:
		print("\nTeste 9[id_cad_h]: Reprovado")
		print("	Erros mais comuns:")
		print("	1. Não identificar propriamente as cadeias no início/final do tabuleiro")
		print("	2. Identificar um elemento a mais/a menos nas cadeias")
		print(tabuleiro_inicial)
		print("Lista esperada:")
		print(lista_esperada)
		print("Lista retornada:")
		print(lista_retornada)
		print()

######################################################################################
	# Testes função eliminar_cadeia 
	tabuleiro_inicial = [ ['C', 'C', 'C', 'C', 'C'],
						  ['D', 'C', 'B', 'A', 'A'],
						  ['D', 'C', 'B', 'D', 'D'],
						  ['D', 'C', 'B', 'B', 'B'],
						  ['A', 'C', 'B', 'D', 'B']]
	cadeia = [1,0,3,0]
	tabuleiro_esperado = [ ['C', 'C', 'C', 'C', 'C'],
						   [' ', 'C', 'B', 'A', 'A'],
						   [' ', 'C', 'B', 'D', 'D'],
						   [' ', 'C', 'B', 'B', 'B'],
						   ['A', 'C', 'B', 'D', 'B']]

	tabuleiro_retornado = [ ['C', 'C', 'C', 'C', 'C'],
							['D', 'C', 'B', 'A', 'A'],
							['D', 'C', 'B', 'D', 'D'],
							['D', 'C', 'B', 'B', 'B'],
							['A', 'C', 'B', 'D', 'B']]

	num = eliminar_cadeia(tabuleiro_retornado,cadeia)
	if (tabuleiro_esperado == tabuleiro_retornado and num == 3):
		testes += 1
		print("\nTeste 10[elim_cad]: Aprovado")
	else:
		print("\nTeste 10[elim_cad]: Reprovado")
		print("	Erros mais comuns:")
		print("	1. Eliminar elementos a mais/a menos")
		exibe_matriz(tabuleiro_inicial, tabuleiro_esperado, tabuleiro_retornado)
		print("Numero de eliminados esperado: 3 ")
		print("Numero de eliminados retornado: %d " % num)
######################################################################################
	tabuleiro_inicial = [ ['A', 'B', 'A', 'D'],
						  ['A', 'A', 'A', 'A'],
						  ['B', 'C', 'A', 'D'],
						  ['D', 'D', 'A', 'D']]
	cadeia = [1,0,1,3]
	tabuleiro_esperado = [ ['A', 'B', 'A', 'D'],
						   [' ', ' ', ' ', ' '],
						   ['B', 'C', 'A', 'D'],
						   ['D', 'D', 'A', 'D']]

	tabuleiro_retornado = [ ['A', 'B', 'A', 'D'],
							['A', 'A', 'A', 'A'],
							['B', 'C', 'A', 'D'],
							['D', 'D', 'A', 'D']]
	num = eliminar_cadeia(tabuleiro_retornado,cadeia)
	if (tabuleiro_esperado == tabuleiro_retornado and num == 4):
		testes += 1
		print("\nTeste 11[elim_cad]: Aprovado")
	else:
		print("\nTeste 11[elim_cad]: Reprovado")
		print("	Erros mais comuns:")
		print("	1. Eliminar elementos a mais/a menos")
		exibe_matriz(tabuleiro_inicial, tabuleiro_esperado, tabuleiro_retornado)
		print("Numero de eliminados esperado: 4 ")
		print("Numero de eliminados retornado: %d " % num)        
######################################################################################
	# Testes função deslocar
	tabuleiro_inicial = [ ['A', 'B', 'A', 'D'],
						  ['A', ' ', ' ', ' '],
						  ['B', ' ', ' ', ' '],
						  ['D', 'D', 'A', ' ']]

	tabuleiro_esperado = [ ['A', ' ', ' ', ' '],
						   ['A', ' ', ' ', ' '],
						   ['B', 'B', 'A', ' '],
						   ['D', 'D', 'A', 'D']]

	tabuleiro_retornado = [ ['A', 'B', 'A', 'D'],
							['A', ' ', ' ', ' '],
							['B', ' ', ' ', ' '],
							['D', 'D', 'A', ' ']]
	deslocar(tabuleiro_retornado)
	if (tabuleiro_esperado == tabuleiro_retornado and num == 4):
		testes += 1
		print("\nTeste 12[deslocar]: Aprovado")
	else:
		print("\nTeste 12[deslocar]: Reprovado")
		print("	Erros mais comuns:")
		print("	1. Nao deslocar todas as colunas")
		print("	2. Problemas com a funcao deslocar_coluna")
		exibe_matriz(tabuleiro_inicial, tabuleiro_esperado, tabuleiro_retornado)
######################################################################################
	# Testes função deslocar_coluna
	# 1. "Datamoshing" da coluna ( repetição da celula mais superior )
	# 2. Deslocar a coluna para cima
	tabuleiro_inicial = [ ['A', 'B', 'A', 'D'],
						  ['A', ' ', 'A', ' '],
						  ['B', ' ', ' ', ' '],
						  ['D', 'D', 'A', ' ']]

	tabuleiro_esperado = [ ['A', 'B', ' ', 'D'],
						   ['A', ' ', 'A', ' '],
						   ['B', ' ', 'A', ' '],
						   ['D', 'D', 'A', ' ']]

	tabuleiro_retornado = [ ['A', 'B', 'A', 'D'],
							['A', ' ', 'A', ' '],
							['B', ' ', ' ', ' '],
							['D', 'D', 'A', ' ']]
	deslocar_coluna(tabuleiro_retornado, 2)
	if (tabuleiro_esperado == tabuleiro_retornado):
		testes += 1
		print("\nTeste 13[deslocar_col]: Aprovado")
	else:
		print("\nTeste 13[deslocar_col]: Reprovado")
		print("	Erros mais comuns:")
		print("	1. trocar elementos não vizinhos")
		print("	2. trocar elementos que não formam sequencia de 3 ou mais")
		exibe_matriz(tabuleiro_inicial, tabuleiro_esperado, tabuleiro_retornado)
######################################################################################
	tabuleiro_inicial = [ ['A', 'B', 'A'],
						  ['A', 'C', ' '],
						  ['B', 'C', ' ']]

	tabuleiro_esperado = [ ['A', 'B', 'A'],
						   ['A', 'C', ' '],
						   ['B', 'C', ' ']]

	tabuleiro_retornado = [ ['A', 'B', 'A'],
							['A', 'C', ' '],
							['B', 'C', ' ']]

	deslocar_coluna(tabuleiro_retornado, 1)
	if (tabuleiro_esperado == tabuleiro_retornado):
		testes += 1
		print("\nTeste 14[deslocar_col]: Aprovado")
	else:
		print("\nTeste 14[deslocar_col]: Reprovado")
		print("	Erros mais comuns:")
		print("	1. trocar elementos não vizinhos")
		print("	2. trocar elementos que não formam sequencia de 3 ou mais")
		exibe_matriz(tabuleiro_inicial, tabuleiro_esperado, tabuleiro_retornado)
######################################################################################
	# Testes função existem_movimentos_validos
	tabuleiro_inicial = [ ['A', 'B', 'A', 'D'],
						  ['D', 'A', 'B', 'D'],
						  ['B', 'C', 'C', 'B'],
						  ['D', 'D', 'A', 'A']]
	valor = existem_movimentos_validos(tabuleiro_inicial)
	valor_esperado = True
	if valor_esperado == valor:
		testes += 1
		print("\nTeste 15[ex_mov_val]: Aprovado")
	else:
		print("\nTeste 15[ex_mov_val]: Reprovado")
		print("Possibilidade : trocar [0,1] com [1,1] ")
######################################################################################
	tabuleiro_inicial = [ ['A', 'B', 'A'],
						  ['A', 'C', 'C'],
						  ['B', 'C', 'A']]
	valor = existem_movimentos_validos(tabuleiro_inicial)
	valor_esperado = False
	if valor_esperado == valor:
		testes += 1
		print("\nTeste 16[ex_mov_val]: Aprovado")
	else:
		print("\nTeste 16[ex_mov_val]: Reprovado")
		print("Nao existem movimentos validos!")
######################################################################################
	tabuleiro_inicial = [ ['A', 'F', 'E', 'D', 'A', 'B'],
						  ['A', 'F', 'A', 'D', 'D', 'A'],
						  ['B', 'C', 'B', 'B', 'E', 'E'],
						  ['D', 'D', 'E', 'C', 'E', 'D'],
						  ['B', 'F', 'F', 'B', 'A', 'B'],
						  ['D', 'B', 'A', 'D', 'C', 'D']]
	valor = existem_movimentos_validos(tabuleiro_inicial)
	valor_esperado = True
	if valor_esperado == valor:
		testes += 1
		print("\nTeste 17[ex_mov_val]: Aprovado")
	else:
		print("\nTeste 17[ex_mov_val]: Reprovado")
		print("Dica fornecida :  ", end ="")
		print(dica)
######################################################################################
	# Testes função obter_dicas
	tabuleiro_inicial = [ ['A', 'B', 'A', 'D'],
						  ['D', 'A', 'B', 'D'],
						  ['B', 'C', 'C', 'B'],
						  ['D', 'D', 'A', 'A']]
	dica = obter_dica(tabuleiro_inicial)
	dica_esperada_1 = (0,1)
	dica_esperada_2 = (1,1)
	if dica == dica_esperada_1 or dica == dica_esperada_2:
		testes += 1
		print("\nTeste 18[dicas]: Aprovado")
	else:
		print("\nTeste 18[dicas]: Reprovado")
		print("Dica fornecida :  ", end ="")
		print(dica)
		print("Dica esperadas : ", end="")
		print(dica_esperada_1, end= " ou ")
		print(dica_esperada_2)

######################################################################################
	tabuleiro_inicial = [ ['A', 'B', 'A'],
						  ['A', 'C', 'C'],
						  ['B', 'C', 'A']]
	dica = obter_dica(tabuleiro_inicial)
	dica_esperada = (-1,-1)
	if dica == dica_esperada:
		testes += 1
		print("\nTeste 19[dicas]: Aprovado")
	else:
		print("\nTeste 19[dicas]: Reprovado")
		print("Dica fornecida :  ", end ="")
		print(dica)
		print("Dica esperada : ", end="")
		print(dica_esperada)

######################################################################################
	tabuleiro_inicial = [ ['A', 'F', 'E', 'D', 'A', 'B'],
						  ['A', 'F', 'A', 'D', 'D', 'A'],
						  ['B', 'C', 'B', 'B', 'E', 'E'],
						  ['D', 'D', 'E', 'C', 'E', 'D'],
						  ['B', 'F', 'F', 'B', 'A', 'B'],
						  ['D', 'B', 'A', 'D', 'C', 'D']]
	dica = obter_dica(tabuleiro_inicial)
	dica_esperada_1 = (2,0)
	dica_esperada_2 = (2,1)
	if dica == dica_esperada_1 or dica == dica_esperada_2:
		testes += 1
		print("\nTeste 20[dicas]: Aprovado")
	else:
		print("\nTeste 20[dicas]: Reprovado")

		print("Dica fornecida :  ", end ="")
		print(dica)
		print("Dicas esperadas : ", end="")
		print(dica_esperada_1, end=" ou ")
		print(dica_esperada_2)
	


	print("\nBateria de testes encerrada !")
	print("\nTestes aprovados : [%d/20]" % testes )
testes_unitarios()
"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,
  DECLARO QUE SOU A ÚNICA PESSOA AUTORA E RESPONSÁVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E, PORTANTO, NÃO CONSTITUEM ATO DE DESONESTIDADE ACADÊMICA,
  FALTA DE ÉTICA OU PLÁGIO.
  DECLARO TAMBÉM QUE SOU A PESSOA RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE NÃO DISTRIBUÍ OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Renan Bruno
  NUSP : 10332980
  Turma: T6
  Prof.: Kelly Rosa Braghetto

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma referência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.

  Exemplo:
  - O algoritmo Quicksort foi baseado em
  https://pt.wikipedia.org/wiki/Quicksort
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
"""
# ======================================================================
#
#   FUNÇÕES FORNECIDAS: NÃO DEVEM SER MODIFICADAS
#
# ======================================================================
import random
random.seed(0)

def main():
    '''
    Esta é a função principal do seu programa. Ela contém os comandos que
    obtêm os parâmetros necessários para criação do jogo (número de linhas,
    colunas e cores), e executa o laço principlal do jogo: ler comando,
    testar sua validade e executar comando.

    ******************************************************
    ** IMPORTANTE: ESTA FUNÇÃO NÃO DEVE SER MODIFICADA! **
    ******************************************************
    '''
    print()
    print("=================================================")
    print("             Bem-vindo ao Gemas!                 ")
    print("=================================================")
    print()

    pontos = 0
    # lê parâmetros do jogo
    num_linhas = int(input("Digite o número de linhas [3-10]: ")) # exemplo: 8
    num_colunas = int(input("Digite o número de colunas [3-10]: ")) # exemplo: 8
    num_cores = int(input("Digite o número de cores [3-26]: ")) # exemplo: 7
    # cria tabuleiro com configuração inicial
    tabuleiro = criar (num_linhas, num_colunas)
    completar (tabuleiro, num_cores)
    num_gemas = eliminar (tabuleiro)
    while num_gemas > 0:
        deslocar (tabuleiro)
        completar (tabuleiro, num_cores)
        num_gemas = eliminar (tabuleiro)
    # laço principal do jogo
    while existem_movimentos_validos(tabuleiro) == True: # Enquanto houver movimentos válidos...
        exibir (tabuleiro)
        comando = input("Digite um comando (perm, dica, sair ou ajuda): ")
        if comando == "perm":
            linha1 = int(input("Digite a linha da primeira gema: "))
            coluna1 = int(input("Digite a coluna da primeira gema: "))
            linha2 = int(input("Digite a linha da segunda gema: "))
            coluna2 = int(input("Digite a coluna da segunda gema: "))
            print ()
            valido = trocar ( linha1, coluna1, linha2, coluna2, tabuleiro)
            if valido:
                num_gemas = eliminar (tabuleiro)
                total_gemas = 0
                while num_gemas > 0:
                    # Ao destruir gemas, as gemas superiores são deslocadas para "baixo",
                    # criando a possibilidade de que novas cadeias surjam.
                    # Devemos então deslocar gemas e destruir cadeias enquanto houverem.
                    deslocar (tabuleiro)
                    completar (tabuleiro, num_cores)
                    total_gemas += num_gemas
                    print("Nesta rodada: %d gemas destruidas!" % num_gemas )
                    exibir (tabuleiro)
                    num_gemas = eliminar (tabuleiro)
                pontos += total_gemas
                print ()
                print ("*** Você destruiu %d gemas! ***" % (total_gemas))
                print ()
            else:
                print ()
                print ("*** Movimento inválido! ***")
                print ()
        elif comando == "dica":
            pontos -= 1
            linha, coluna = obter_dica (tabuleiro)
            print ()
            print ("*** Dica: Tente permutar a gema na linha %d e coluna %d ***" % (linha, coluna))
            print ()
        elif comando == "sair":
            print ("Fim de jogo!")
            print ("Você destruiu um total de %d gemas" % (pontos))
            return
        elif comando == "ajuda":
            print("""
============= Ajuda =====================
perm:  permuta gemas
dica:  solicita uma dica (perde 1 ponto)
sair:  termina o jogo
=========================================
                  """)
        else:
            print ()
            print ("*** Comando inválido! Tente ajuda para receber uma lista de comandos válidos. ***")
            print ()
    print("*** Fim de Jogo: Não existem mais movimentos válidos! ***")
    print ("Você destruiu um total de %d gemas" % (pontos))

def completar (tabuleiro, num_cores):
    ''' (matrix, int) -> None

    Preenche espaços vazios com novas gemas geradas aleatoriamente.

    As gemas são representadas por strings 'A','B','C',..., indicando sua cor.
    '''
    alfabeto = ['A','B','C','D','E','F','G','H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num_linhas = len (tabuleiro)
    num_colunas = len (tabuleiro[0])
    for i in range (num_linhas):
        for j in range (num_colunas):
            if tabuleiro[i][j] == ' ':
                gema = random.randrange (num_cores)
                tabuleiro[i][j] = alfabeto[gema]


# ======================================================================
#
#   FUNÇÕES A SEREM IMPLEMENTADAS POR VOCÊ
#
# ======================================================================

def criar (num_linhas, num_colunas):
    ''' (int,int) -> matrix

    Cria matriz de representação do tabuleiro e a preenche com
    espaços vazios representados por ' '.

    Retorna a matriz criada.
    '''
    matriz = []

    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(' ')
            
        matriz.append(linha)
    
    return matriz

def exibir (tabuleiro):
    ''' (matrix) -> None

    Exibe o tabuleiro.
    '''
    num_linhas  = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    
    print ("    ", end="")
    for x in range(len(tabuleiro[0])):
        print (x, end=" ")
    print ("", end="\n")
    print ("  ", end="")
    print ("+", end="-")    
    for y in range(len(tabuleiro[0])):
        print ("-", end="-")
    print ("+", end="\n")   

    for i in range(len(tabuleiro)):
        print (i,"|", end=" ")
        for j in range(len(tabuleiro[i])):
            print(tabuleiro[i][j], end=" ")
        print ("|")
    print ("  ", end="")
    print ("+", end="-")
    for y in range(len(tabuleiro[0])):
        print ("-", end="-")
    print ("+", end="\n")
    print()

def trocar (linha1, coluna1, linha2, coluna2, tabuleiro):
    ''' (int,int,int,int,matrix) -> Bool

    Permuta gemas das posições (linha1, coluna1) e (linha2, coluna2) caso
    seja válida (isto é, gemas são adjacentes e geram cadeias), caso contrário
    não altera o tabuleiro.

    Retorna `True` se permutação é válida e `False` caso contrário.
    '''
    v = identificar_cadeias_verticais (tabuleiro) 
    h = identificar_cadeias_horizontais (tabuleiro)

    cond = False
    c = False
    

    if linha1 < len(tabuleiro) and linha1 == linha2:
        if coluna1 == coluna2+1 or coluna1 == coluna2-1:
            c = True
    if coluna1 < len(tabuleiro[linha1]) and coluna1 == coluna2:
        if linha1 == linha2+1 or linha1 == linha2-1:
            c = True

    if linha2 < len(tabuleiro) and coluna2 < len(tabuleiro[linha2])and c == True:
        
        aux1 = tabuleiro[linha1][coluna1]
        aux2 = tabuleiro[linha2][coluna2]
        tabuleiro[linha1][coluna1] = aux2
        tabuleiro[linha2][coluna2] = aux1
        v = identificar_cadeias_verticais (tabuleiro)
        h = identificar_cadeias_horizontais (tabuleiro)
        if len(v) > 0 or len(h) > 0:
            cond = True
        else:
            tabuleiro[linha2][coluna2] = aux2
            tabuleiro[linha1][coluna1] = aux1
        

        return cond


def eliminar (tabuleiro):
    ''' (matrix) -> int

    Elimina cadeias de 3 ou mais gemas, substituindo-as por espaços (' ').

    Retorna número de gemas eliminadas.
    '''
    num_eliminados = 0
    h = identificar_cadeias_horizontais(tabuleiro)
    v = identificar_cadeias_verticais(tabuleiro)

    if len(h) > 0:
        for x in range(len(h)):
            z = eliminar_cadeia(tabuleiro, h[x])
            num_eliminados += z
    if len(v) > 0:
        for y in range(len(v)):
            w = eliminar_cadeia(tabuleiro, v[y])
            num_eliminados += w
    

    return num_eliminados


def identificar_cadeias_horizontais (tabuleiro):
    ''' (matrix) -> list

    Retorna uma lista contendo cadeias horizontais de 3 ou mais gemas. Cada cadeia é
    representada por uma lista `[linha, coluna_i, linha, coluna_f]`, onde:

    - `linha`: o número da linha da cadeia
    - `coluna_i`: o número da coluna da gema mais à esquerda (menor) da cadeia
    - `coluna_f`: o número da coluna da gema mais à direita (maior) da cadeia

    Não modifica o tabuleiro.
    '''
    cadeias_horizontais = []

    for i in range(len(tabuleiro)):
        n = 1
        j = 0
        while j < len(tabuleiro[i])-1:
            while n+j <= (len(tabuleiro[i])-1) and tabuleiro[i][j] == tabuleiro[i][j+n]:
                if tabuleiro[i][j] == tabuleiro[i][j+n]:
                    n += 1
            if n >= 3:    
                cadeias_horizontais.append([i, j, i, j+n-1])
                j += n-1
            n = 1
            j += 1
            
            
    return cadeias_horizontais

def identificar_cadeias_verticais (tabuleiro):
    ''' (matrix) -> list

    Retorna uma lista contendo cadeias verticais de 3 ou mais gemas. Cada cadeia é
    representada por uma lista `[linha_i, coluna, linha_f, coluna]`, onde:

    - `linha_i`: o número da linha da gemas mais superior (menor) da cadeia
    - `coluna`: o número da coluna das gemas da cadeia
    - `linha_f`: o número da linha mais inferior (maior) da cadeia

    Não modifica o tabuleiro.
    '''
    cadeias_verticais = []
    i = 0

    for j in range(len(tabuleiro[i])):
        n = 1
        while i < len(tabuleiro):
            while n+i <= (len(tabuleiro)-1) and tabuleiro[i][j] == tabuleiro[i+n][j]:
                if tabuleiro[i][j] == tabuleiro[i+n][j]:
                    n += 1
            if n >= 3:    
                cadeias_verticais.append([i, j, i+n-1, j])
                i += n-1
            n = 1
            i += 1
        i = 0
            

    return cadeias_verticais

def eliminar_cadeia (tabuleiro, cadeia):
    ''' (matrix,list) -> int

    Elimina (substitui pela string espaço `" "`) as gemas compreendidas numa cadeia,
    representada por uma lista `[linha_inicio, coluna_inicio, linha_fim, coluna_fim]`,
    tal que:

    - `linha_i`: o número da linha da gema mais superior (menor) da cadeia
    - `coluna_i`: o número da coluna da gema mais à esquerda (menor) da cadeia
    - `linha_f`: o número da linha mais inferior (maior) da cadeia
    - `coluna_f`: o número da coluna da gema mais à direita (maior) da cadeia

    Retorna o número de gemas eliminadas.
    '''
    num_eliminados = 0
    
    if cadeia[0] == cadeia[2]:
        coluna_i = cadeia[1]
        coluna_f = cadeia[3]
        linha = cadeia[0]
        for j in range(coluna_i,coluna_f+1):
            if tabuleiro[linha][j] != ' ':
                tabuleiro[linha][j] = ' '
                num_eliminados += 1

    if cadeia[1] == cadeia[3]:
        linha_i = cadeia[0]
        linha_f = cadeia[2]
        coluna = cadeia[3]
        for i in range(linha_i,linha_f+1):
            if tabuleiro[i][coluna] != ' ':
                tabuleiro[i][coluna] = ' '
                num_eliminados += 1
            
    
    return num_eliminados


def deslocar (tabuleiro):
    ''' (matrix) -> None

    Desloca gemas para baixo deixando apenas espaços vazios sem nenhuma gema acima.
    '''

    for j in range(len(tabuleiro[0])):
        deslocar_coluna(tabuleiro, j)
        
        
def deslocar_coluna (tabuleiro, j):
    ''' (matrix, int) -> None

    Desloca as gemas na coluna j para baixo, ocupando espaços vazios.
    '''

    x = len(tabuleiro)-1
    while x > 0:
        if tabuleiro[x][j] != " ":
            x -= 1
        else:
            i = x
            while i > 0:
                tabuleiro[i][j] = tabuleiro[i-1][j]
                i -= 1
            tabuleiro[0][j] = " "
        x -= 1
                    

def existem_movimentos_validos (tabuleiro):
    '''(matrix) -> Bool

    Retorna True se houver movimentos válidos, False caso contrário.
    '''

    cond = False

    if obter_dica != -1:
        cond = True

    return cond


def obter_dica (tabuleiro):
    '''(matrix) -> int,int

    Retorna a posição (linha, coluna) de uma gema que faz parte de uma
    permutação válida.

    Se não houver permutação válida, retorne -1,-1.
    '''

    linha = -1
    coluna = -1
    i = 0
    j = 0
    
    for i in range(len(tabuleiro)):
        k = i+1
        for j in range(len(tabuleiro[i])):
            l = j+1
            if i < len(tabuleiro) and k < len(tabuleiro) :
                if trocar(i, j, k, j, tabuleiro) == True:
                    linha = i
                    coluna = j
                    aux1 = tabuleiro[i][j]
                    aux2 = tabuleiro[k][j]
                    tabuleiro[i][j] = aux2
                    tabuleiro[k][j] = aux1
            if j < len(tabuleiro[i]) and l < len(tabuleiro[i]):
                if trocar(i, j, i, l, tabuleiro) == True:
                    linha = i
                    coluna = j
                    aux1 = tabuleiro[i][j]
                    aux2 = tabuleiro[i][l]
                    tabuleiro[i][j] = aux2
                    tabuleiro[i][l] = aux1
            
                    
    return linha, coluna


main()

