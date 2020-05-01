"""
13. wordcount
Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.
A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.
Ou seja...
Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.
Por exemplo:
$ python wordcount.py --count letras.txt
a 2
b 4
c 3
B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.
Ou seja...
Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.
Por exemplo:
$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2
Abaixo já existe um esqueleto do programa para você preencher.
Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.
Seu trabalho é implementar as funções print_words() e depois print_top().
"""

import sys

def popula_dicionario(contents):
	dictCount={}
	contents = contents.splitlines()
	for linha in contents:
		for char in linha:
			char = char.lower()
			if char in dictCount:
				dictCount[char]=int(dictCount.get(char))+1							
			else:
				dictCount[char]=1
	return dictCount


def print_words(filename):
	f=open(filename, "r")
	contents =f.read()
	dictCount=popula_dicionario(contents)

	# imprime chave e valor do dicionario
	for chave, valor in dictCount.items():
		print(f'{chave} {valor}') 

	f.close()	


def print_top(filename):
	f=open(filename, "r")
	dictOrder={}
	contents =f.read()
	dictCount=popula_dicionario(contents)

	# Insere na Ordem
	for chave, valor in list(dictCount.items()):		
		chave = max(dictCount, key=dictCount.get)
		dictOrder[chave] = dictCount.get(chave)
		dictCount.pop(chave)

	#Imprime o dicionario
	for chave, valor in dictOrder.items():
		print(f'{chave} {valor}') 

	f.close()

# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()

