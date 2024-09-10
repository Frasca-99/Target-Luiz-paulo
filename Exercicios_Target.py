# Exercício 1
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(f"O valor final da SOMA é: {SOMA}")

# Exercício 2
def is_fibonacci(n):
    a, b = 0, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    return False

numero = int(input("Informe um número: "))
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

    # Exercício 3
    import json

    # Exemplo de dados JSON
    faturamento_json = '''
    {
        "faturamento": [1000, 2000, 3000, 0, 1500, 2500, 0, 0, 0, 5000, 0, 7000]
    }
    '''

    dados = json.loads(faturamento_json)
    faturamento = dados["faturamento"]

    # Remover dias sem faturamento (dias com valor 0)
    faturamento = [f for f in faturamento if f > 0]

    # Menor e maior valor
    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)

    # Cálculo da média
    media_mensal = sum(faturamento) / len(faturamento)

    # Dias com faturamento acima da média
    dias_acima_media = len([f for f in faturamento if f > media_mensal])

    print(f"Menor faturamento: R${menor_faturamento:.2f}")
    print(f"Maior faturamento: R${maior_faturamento:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_media}")

    # Exercício 4
    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    faturamento_total = sum(faturamento_estados.values())

    for estado, valor in faturamento_estados.items():
        percentual = (valor / faturamento_total) * 100
        print(f"{estado}: {percentual:.2f}% do faturamento total")


        # Exercício 5
        def inverter_string(s):
            invertida = ""
            for i in range(len(s) - 1, -1, -1):
                invertida += s[i]
            return invertida


        string = input("Informe uma string: ")
        print(f"String invertida: {inverter_string(string)}")



