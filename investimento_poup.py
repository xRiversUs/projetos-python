#--simulador de investimento - Poupança--
deposito = float(input("Digite o valor do aporte: "))
taxa = float(input("Qual é a taxa da poupança em %? "))
meses = int(input("Quantos meses vai investir? "))
conversao = taxa/100
total = 0
for mes in range(1, meses +1):
    total = total + deposito
    total = total + (total * taxa)
print(f"Ao final do período, você terá: R${total:2f}")