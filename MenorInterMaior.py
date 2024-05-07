titulo = 'Menor Inter Maior'
print(f'{titulo:^30}')

n1 = int(input('Entre com o 1o numero: '))
n2 = int(input('Entre com o 2o numero: '))
n3 = int(input('Entre com o 3o numero: '))

print(f'Os numeros {n1}, {n2}, {n3}', end=' ')
# if n1 > n2:
#     t = n1
#     n1 = n2
#     n2 = t
#
# if n1 > n3:
#     t = n1
#     n1 = n3
#     n3 = t
#
# if n2 > n3:
#     t = n2
#     n2 = n3
#     n3 = t

if n1 > n2:
    n1, n2 = n2, n1

if n1 > n3:
    n1, n3 = n3, n1

if n2 > n3:
    n2, n3 = n3, n2

print(f'são menor:{n1}, inter:{n2}, maior:{n3}')
print('teste de commit local')
