#Etapa 1 - Cálculo do IMC
def calc_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

#Etapa 2 - Classificação do IMC
def classificar_imc(resultado):
    if resultado >= 25:
        return "ACIMA DO PESO"
    else:
        return "PESO IDEAL"
    
#Etapa 3 - Mensagem de Retorno
def mensagem(status):
    if status == "ACIMA DO PESO":
       return "atenção! Procure um médico⚠️"
    else:
        return "Parabéns! Você está no peso ideal 👌"
#Etapa 4 - Integração do Código
valor_peso = float(input("Digite o seu peso: "))
valor_altura = float(input("Digite a sua altura: "))

valor_imc = calc_imc(valor_peso,valor_altura)
resultado_imc = classificar_imc(valor_imc)
saida = mensagem(resultado_imc)

print("="*50)
print("Resultado do seu IMC")
print(f"\n seu IMC é:{valor_imc:.1f}")
print(f"\ {saida}")
print("="*50)