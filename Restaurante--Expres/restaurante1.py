import os

class Restaurante:
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.avaliacoes = []

    def ativar_desativar(self):
        self.ativo = not self.ativo
        if self.ativo:
            return f'O restaurante {self.nome} foi ativado com sucesso.'
        else:
            return f'O restaurante {self.nome} foi desativado com sucesso.'

    def adicionar_avaliacao(self, nota):
        self.avaliacoes.append(nota)

    def calcular_media_avaliacoes(self):
        if not self.avaliacoes:
            return "Sem estrelas ainda."
        else:
            media = sum(self.avaliacoes) / len(self.avaliacoes)
            return f'{self.nome}    Média de estrelas: {media:.2f} ({len(self.avaliacoes)} estrelas)'

    def __str__(self):
        return f'Nome: {self.nome.ljust(20)}  Categoria: {self.categoria.ljust(22)}  Status: {"Ativado" if self.ativo else "Desativado"}'

class ProgramaExpresso:
    def __init__(self):
        self.restaurantes = [
            Restaurante('Laçador', 'Churrascaria', True),
            Restaurante('Legado', 'Porçoes', False),
            Restaurante('Hamburgueiro', 'Hamburgueria', False)
        ]

    def finalizar_app(self):
        os.system("clear")
        os.system("cls")
        print("Finalizando o app\n")

    def voltar_menu_principal(self):
        input("Digite uma tecla para voltar ao menu principal: ")

    def mostrar_subtitulo(self, texto):
        os.system("clear")
        linha = '*'*(len(texto))
        print(linha)
        print(texto)
        print(linha)
        print()

    def escolher_opcoes(self):
        self.mostrar_subtitulo('''𝑹𝒆𝒔𝒕𝒂𝒖𝒓𝒂𝒏𝒕𝒆 𝑬𝒙𝒑𝒓𝒆𝒔𝒔 𝑺𝒉𝒂𝒊𝒌𝒐𝒔𝒌𝒊 𝒆 𝑫𝒊𝒆𝒈𝒐''')
        print("1 - Cadastrar restaurante")
        print("2 - Listar restaurantes")
        print("3 - Ativar/Desativar restaurante")
        print("4 - Avaliar Restaurante")
        print("5 - Ver Estrelas")
        print("6 - Sair\n")

    def opcao_invalida(self):
        self.mostrar_subtitulo("Opção inválida\n".ljust(20))
        self.voltar_menu_principal()

    def listarRestaurantes(self):
        self.mostrar_subtitulo('Listando os Restaurantes'.ljust(20))
        print("Nome:".ljust(27), "Categoria:".ljust(34), "Status:".ljust(24))
        for restaurante in self.restaurantes:
            print(restaurante)

    def alternar_estado_restaurante(self):
        self.mostrar_subtitulo("Alterando o estado do restaurante".ljust(20))
        self.listarRestaurantes()
        nome_restaurante = input("Digite o nome do Restaurante que desejas alterar: ")
        restaurante_encontrado = False

        for restaurante in self.restaurantes:
            if nome_restaurante == restaurante.nome:
                restaurante_encontrado = True
                mensagem = restaurante.ativar_desativar()
                print(mensagem)
                break

        if not restaurante_encontrado:
            print("O restaurante não foi encontrado.")

        self.voltar_menu_principal()

    def avaliacao(self):
        self.mostrar_subtitulo("Avaliar Restaurante\n".ljust(20))
        self.listarRestaurantes()

        nome_restaurante = input("Digite o nome do restaurante que deseja avaliar: ")
        restaurante_encontrado = False

        for restaurante in self.restaurantes:
            if nome_restaurante == restaurante.nome:
                restaurante_encontrado = True
                while True:
                    nota = int(input("Digite estrelas de 1 a 5 para dar a este restaurante: "))
                    if 1 <= nota <= 5:
                        restaurante.adicionar_avaliacao(nota)
                        print(f"Você avaliou o restaurante {nome_restaurante} com as seguintes estrelas {nota}.")
                        break
                    else:
                        print("Por favor, digite uma estrela válida (entre 1 e 5).")

        if not restaurante_encontrado:
            print("Restaurante não encontrado.")

        self.voltar_menu_principal()

    def ver_media_avaliacoes(self):
        self.mostrar_subtitulo("Média de estrelas dos Restaurantes\n".ljust(20))
        for restaurante in self.restaurantes:
            print(restaurante.calcular_media_avaliacoes())

        self.voltar_menu_principal()

    def cadastrar_novo_restaurante(self):
        nome_do_restaurante = input("Digite o nome do novo restaurante: ")
        categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
        restaurante_novo = Restaurante(nome_do_restaurante, categoria)
        self.restaurantes.append(restaurante_novo)
        print(f"Você cadastrou o restaurante: {nome_do_restaurante}")

    def main(self):
        while True:
            try:
                self.escolher_opcoes()
                opcao_digitada = int(input("Digite a opção desejada: "))
                if opcao_digitada == 1:
                    print("Você escolheu cadastrar restaurante\n" )
                    self.cadastrar_novo_restaurante()
                elif opcao_digitada == 2:
                    self.listarRestaurantes()
                    self.voltar_menu_principal()
                elif opcao_digitada == 3:
                    self.alternar_estado_restaurante()
                elif opcao_digitada == 4:
                    self.avaliacao()
                elif opcao_digitada == 5:
                    self.ver_media_avaliacoes()
                elif opcao_digitada == 6:
                    print("Você escolheu sair do aplicativo\n")
                    self.finalizar_app()
                    break
                else:
                    self.opcao_invalida()
            except ValueError:
                print("Por favor, digite um número válido.")

if __name__ == "__main__":
    programa = ProgramaExpresso()
    programa.main()
