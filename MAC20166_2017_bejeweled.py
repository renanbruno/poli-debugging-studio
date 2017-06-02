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
#main()