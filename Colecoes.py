Colecoes
Sao as variaveis que apresentam mais de um valor
elas podem ser do mesmo tipo ou de tipos diferentes
TODA colecao é um elemento ITERAVEL, ou seja q eu posso percorrer

LISTA
a primeira q veremos
a mais poderosa e mais comum
FLEXIVEL (permite inserir elementos, modificar, excluir)
MUTAVEIS, EXPANSIVEIS, ORDENADAS, PERMITEM DUPLICADOS
PERMITEM TIPOS DIFERENTES
SAO ACESSADAS POR INDICES

print('LISTAS\n')
minhaLista = ['cafe', 'agua', 'acucar']
print(minhaLista)
                #-5    -4       -3     -2          -1
                #0     1        2       3           4
minhaLista = ['cafe', 'agua', 'acucar', 'cafe', 'rosa']
print(minhaLista)

print('primeiro elemento:', minhaLista[0])
print('segundo elemento:', minhaLista[1])
print('ultimo elemento ordem comum:', minhaLista[4])
print('segundo elemento ordem inversa:', minhaLista[-1])

#slicing
# a mesma construcao do range
#zero:tamanho - 1:pulo

                #-5    -4       -3     -2          -1
                #0     1        2       3           4
minhaLista = ['cafe', 'agua', 'acucar', 'cafe', 'rosa']
print('\nPequena Lista - Slicing')
pequenaLista = minhaLista[1:3]
print(pequenaLista)
pequenaLista = minhaLista[-2:-5:-1]
print(pequenaLista)
minhaListaInversa = minhaLista[::-1]
print(minhaListaInversa)

palavra = 'JOCA'
print(f'{palavra} {palavra[::-1]}')

                #-5    -4       -3     -2          -1
                #0     1        2       3           4
minhaLista = ['cafe', 'agua', 'acucar', 'cafe', 'pimenta']
print('\nAcrescentando Elementos')
print(minhaLista)
#acrescenta no final
minhaLista.append('canela')
print(minhaLista)
#acrescentar em uma posicao
minhaLista.insert(3, 'nibs cacau')
print(minhaLista)


print('\nEliminar Elementos')
print(minhaLista)
print('Eliminar o ultimo')
minhaLista.pop()
print(minhaLista)
print('Eliminar item especifico 3')
minhaLista.pop(3)
print(minhaLista)
print('Eliminar o ultimo com del')
del minhaLista[-1]
print(minhaLista)

print('Eliminar todos elementos')
minhaLista.clear()
print(minhaLista)
print('Apagar a lista')
del minhaLista

print('Construtores')
outraLista = []
print(outraLista)

outraLista = list(('chantilly', 'baunilha'))
print(outraLista)

print('Extender Lista')
complementoLista = ['raspas limao', 'flor de sal']
print(complementoLista)
outraLista.extend(complementoLista)
print(outraLista)

novaLista = pequenaLista + complementoLista
print(novaLista)

onde = novaLista.index('raspas limao')
print('Posicao raspas:', onde)

if 'chantilly' in outraLista:
    print('Chantilly presente')

print('LISTAS SAO ODERNAVEIS SE FOREM DO MESMO TIPO')
print(novaLista)
novaLista.sort()
print(novaLista)

listaNaoOrdenavel = [2, 'teste', 'resultado', True]
print(listaNaoOrdenavel)
#listaNaoOrdenavel.sort()
