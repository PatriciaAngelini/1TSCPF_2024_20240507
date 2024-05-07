titulo = 'Potenciacao'
print(f'{titulo:^30}')

base = int(input('Entre com a base: '))
exponencial = int(input('Entre com o exponecial: '))

total = 1
i = 1
if base <= 1 or exponencial < 2:
    print("A base deve ser maior que 1 e o exponencial maior igual a 2")
else:
    # for _ in range(exponencial):
    #    total = total * base
    # print(f'{base} elevado {exponencial} é igual a {total}')
    while i <= exponencial:
        #total = total * base
        total *= base
        i += 1
    print(f'{base} elevado {exponencial} é igual a {total}')

