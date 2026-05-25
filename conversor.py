#Ferramenta de Conversão Dólar x Real--
def converter(valor_dolar):
    taxa = 5.15
    valor_real = valor_dolar * taxa
    return valor_real
print("Conversor Dólar x Real")
preco = float(input("Digite o preço do produto em dólar: "))
resultado = converter(preco)
print(f"O valor em reais é:{resultado:.2f}")