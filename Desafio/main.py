# Considerações:
# 1) O arquivo dados.json deve estar na mesma pasta que o arquivo main.py
# 2) A solução dos exercicios foi concentrada em um único arquivo para facilitar a execução e avaliação do código, porém, em um ambiente de produção, cada exercício seria separado em arquivos distintos.


#  Técnica:
#  1) 
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(f"Valor da soma é {SOMA}")
#  Ao final do processamento o valor da variável SOMA é 91. 

#  2) 
def is_fibonacci(num):
    # Inicializa os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1
    
    # Gera a sequência até o número ser maior ou igual ao informado
    while a <= num:
        if a == num:
            return True  # Se o número for encontrado, pertence à sequência
        a, b = b, a + b  # Atualiza os valores da sequência
    
    return False  # Se o loop terminar, o número não pertence à sequência

# Número a verificar
numero = 7

# Verifica e imprime o resultado
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")


#  3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#  • O menor valor de faturamento ocorrido em um dia do mês;
#  • O maior valor de faturamento ocorrido em um dia do mês;
#  • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#  IMPORTANTE:
#  a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#  b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

# Carrega os dados do arquivo JSON
with open("Desafio\dados.json", "r") as file:
    faturamento = json.load(file)

# Filtra os dias com faturamento válido (maior que 0)
faturamento_valido = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

# Calcula o menor e o maior valor de faturamento
menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)

# Calcula a média mensal
media_mensal = sum(faturamento_valido) / len(faturamento_valido)

# Conta os dias em que o faturamento foi superior à média mensal
dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

# Exibe os resultados
print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")


#  4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#  • SP – R$67.836,43
#  • RJ – R$36.678,66
#  • MG – R$29.229,88
#  • ES – R$27.165,48
#  • Outros – R$19.849,53

#  Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

# Calcula o valor total mensal
total_mensal = SP + RJ + MG + ES + Outros

# Estabelece um dicionário com os valores de faturamento por estado
estados = {"SP": SP, "RJ": RJ, "MG": MG, "ES": ES, "Outros": Outros}

# Calcula e exibe o percentual de representação de cada estado
for estado, valor in estados.items():
    percentual = (valor / total_mensal) * 100
    print(f"Percentual de representação de {estado}: {percentual:.2f}%")


#  5) Escreva um programa que inverta os caracteres de um string.

#  IMPORTANTE:
#  a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#  b) Evite usar funções prontas, como, por exemplo, reverse;

string = "Aprovado"
string_invertida = ""

# Loop para percorrer a string de trás para frente
for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]
    print(string_invertida)
