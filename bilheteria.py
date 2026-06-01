#Aluno 1: Formato de Nome do Filme
def formatar(nome):
    return nome.upper()
#Aluno 2: Verificação de Acesso
def verificador(idade):
    if idade >=18:
        return "Autorizado"
    else:
        return "Não Autorizado"
#Aluno 3: Mensagem de Retorno
def gerar_mensagem(status):
    if status == "Autorizado":
       return "tenha uma ótima sessão"
    else:
        return "Sinto muito, idade não autorizada"
#Aluno 4: Integrador do projeto
nome_filme = input("Digite o nome do Filme: ")
idade_filme = int(input("Digite a sua idade: "))
filme = formatar(nome_filme)
status_final = verificador(idade_filme)
mensagem = gerar_mensagem(status_final)
print(f"\nfilme:{filme}")
print(f"status:{status_final}")
print(f"aviso:{mensagem}")