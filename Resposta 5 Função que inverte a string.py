# Função que inverte a string
def inverter_string(s):
    # Inicializa uma string vazia para armazenar o resultado
    string_invertida = ""
    
    # Percorre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    
    return string_invertida

# Entrada da string (pode ser definida diretamente ou recebida como input)
string_original = input("Digite uma string para ser invertida: ")

# Chama a função e exibe o resultado
resultado = inverter_string(string_original)
print(f"String invertida: {resultado}")
