import os
from modelos.gerenciador import GerenciadorInfectado

class InterfaceUsuario:
    def __init__(self):
        self.gerenciador = GerenciadorInfectado()

    def mostrar_subtitulo(self, texto):
        os.system('cls' if os.name == 'nt' else 'clear')
        linha = '*' * len(texto)
        print(linha)
        print(texto)
        print(linha)
        print()

    def finalizar_app(self):
        self.mostrar_subtitulo('Finalizando o aplicativo')
        exit()

    def chamar_nome_do_app(self):
        print('''
            PӨᄂIӨVIDΛ
        ''')

    def voltar_ao_menu_principal(self):
        input('\nDigite uma tecla para voltar ao menu principal')
        self.main()

    def opcao_invalida(self):
        print('Opção inválida\n')
        self.voltar_ao_menu_principal()

    def exibir_opcoes(self):
        print("1 Cadastrar Infectado")
        print("2 Exibir número de infectados")
        print("3 Tratamentos")
        print("4 Quantidade de vacinados")
        print("5 Sair\n")

    def cadastrar_novo_infectado(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        nome_do_infectado = input('Digite o nome do novo infectado:')
        idade = input(f'Digite a idade do infectado {nome_do_infectado}: ')
        self.gerenciador.adicionar_infectado(nome_do_infectado, idade)
        self.voltar_ao_menu_principal()

    def listar_infectados(self):
        self.mostrar_subtitulo('Listando os infectados:')
        self.gerenciador.listar_infectados()
        self.voltar_ao_menu_principal()

    def listar_tratamentos(self):
        self.mostrar_subtitulo('Listando os tratamentos:')
        self.gerenciador.listar_tratamentos()
        self.voltar_ao_menu_principal()

    def listar_vacinados(self):
        self.mostrar_subtitulo('Listando a quantidade de vacinados:')
        self.gerenciador.listar_vacinados()
        self.voltar_ao_menu_principal()

    def escolher_opcoes(self):
        try:
            opcao_digitada = int(input("Escolher uma opção"))
            print("Você selecionou:", opcao_digitada, "\n")
            if opcao_digitada == 1:
                self.cadastrar_novo_infectado()
            elif opcao_digitada == 2:
                self.listar_infectados()
            elif opcao_digitada == 3:
                self.listar_tratamentos()
            elif opcao_digitada == 4:
                self.listar_vacinados()
            elif opcao_digitada == 5:
                self.finalizar_app()
            else:
                self.opcao_invalida()
        except ValueError:
            self.opcao_invalida()

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.chamar_nome_do_app()
        self.exibir_opcoes()
        self.escolher_opcoes()
