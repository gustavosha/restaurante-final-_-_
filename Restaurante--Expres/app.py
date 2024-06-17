import os

amigos = [
    {'nome': 'Cadu'},
    {'nome': 'Lucas'},
    {'nome': 'Shai'}
]

def finalizar_app():
    os.system("clear")
    os.system("cls")
    print("Finalizando o app\n")

def voltar_menu_principal():
    input("Digite uma tecla para voltar ao menu principal: ")

def mostrar_subtitulo(texto):
    os.system("clear")
    print(texto)
    print()

def escolher_opcoes():
    mostrar_subtitulo("Book for friends\n")
    print("1 - Cadastrar amigo")
    print("2 - Listar amigo")
    print("3 - Sair\n")

def opcao_invalida():
    mostrar_subtitulo("Opção inválida\n")
    voltar_menu_principal()
            
def chamar_nome_do_app():
    print("""Listar amigo""")

def listarAmigos():
    mostrar_subtitulo('Listando os amigos')
    for amigo in amigos:
        nome_amigo = amigo['nome']
        print(f'-{nome_amigo}')

def cadastrar_novo_amigo():
    nome_do_amigo = input("Digite o nome do novo amigo: ")
    dados_do_amigo = {'nome': nome_do_amigo}
    amigos.append(dados_do_amigo)
    print(f"Você cadastrou o amigo: {nome_do_amigo}")

def main():
    while True:
        try:
            escolher_opcoes()
            opcaodigitada = int(input("Digite a opção desejada: "))
            if opcaodigitada == 1:
                print("Você escolheu cadastrar um amigo\n")
                cadastrar_novo_amigo()
                main()
            elif opcaodigitada == 2:
                listarAmigos()
                voltar_menu_principal()
                main()
            elif opcaodigitada == 3:
                print("Você escolheu sair do aplicativo\n")
                finalizar_app()
                break
            else:
                opcao_invalida()
                main()
        except ValueError:
            main()

if __name__ == "__main__":
    finalizar_app()
    main()