from modelos.interface import InterfaceUsuario

def main():
    app = InterfaceUsuario()

    # Adicionando infectados predefinidos
    app.gerenciador.adicionar_infectado('Marta', '3')
    app.gerenciador.adicionar_infectado('João', '5')
    app.gerenciador.adicionar_infectado('Alice', '7')

    app.main()

if __name__ == "__main__":
    main()