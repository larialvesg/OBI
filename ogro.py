mao_esquerda = int(input())
mao_direita = int(input())

if mao_esquerda > mao_direita:
    valor_final = mao_esquerda + mao_direita
    print(valor_final)

if mao_esquerda < mao_direita:
    valor_final = 2 * (mao_direita - mao_esquerda)
    print(valor_final)
