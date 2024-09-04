import json

# Função que lê o arquivo JSON
def ler_dados_faturamento(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados  # Retorna os dados diretamente, sem acessar 'faturamento_diario'

# Função principal para calcular os valores solicitados
def calcular_faturamento(caminho_arquivo):
    faturamento_diario = ler_dados_faturamento(caminho_arquivo)
    
    # Filtrar os dias com faturamento maior que zero
    valores_validos = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]
    
    if not valores_validos:
        print("Não há valores de faturamento válidos.")
        return

    # Calcular o menor e o maior faturamento
    menor_faturamento = min(valores_validos)
    maior_faturamento = max(valores_validos)

    # Calcular a média mensal
    media_mensal = sum(valores_validos) / len(valores_validos)

    # Contar os dias com faturamento acima da média mensal
    dias_acima_media = sum(1 for valor in valores_validos if valor > media_mensal)

    # Exibir os resultados
    print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
    print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")

# Caminho do arquivo JSON
caminho_arquivo = 'C:/Users/Windows 10/Desktop/Teste Target/dados.json'

# Executar o cálculo do faturamento
calcular_faturamento(caminho_arquivo)
