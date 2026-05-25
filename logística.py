def cabecalho():
    print("\n" + "=" * 30)
    print(" SISTEMA DE LOGÍSTICA")
def calcular_frete(peso_carga):
    if peso <=20:
        return peso * 10.00
    else: 
        return peso * 15.00
cabecalho()
peso_item = float(input("Digite o peso em KG: "))
frete = calcular_frete(peso_carga)
print(F"o valor do frete é:R${frete:.2f}")
print("=" * 30)