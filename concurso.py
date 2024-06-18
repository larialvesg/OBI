entrada = input()
notas_entrada = input()

candidatos, aprovados = map(int, entrada.split())
L = list(map(int, notas_entrada.split()))
L.sort(reverse=True)

print(L[aprovados-1])
