from modelos.infectado import Infectado

class GerenciadorInfectado:
    def __init__(self):
        self.infectados = []
        self.tratamentos = ["Remdesivir", "Dexametasona", "Plasma Convalescente"]  
        self.vacinados = {"Pfizer": 10, "Moderna": 8, "AstraZeneca": 7}  

    def adicionar_infectado(self, nome, idade):
        novo_infectado = Infectado(nome, idade)
        self.infectados.append(novo_infectado)
        print(f'O infectado {nome} foi cadastrado com sucesso')

    def listar_infectados(self):
        print("Listando os Infectados:\n")
        print(f'-Nome do Infectado'.ljust(24), '-Idade'.ljust(20))
        for infectado in self.infectados:
            print(f'-{infectado.nome}'.ljust(24), f'-{infectado.idade}'.ljust(20))
        print("\nTotal de infectados cadastrados:", len(self.infectados))

    def listar_tratamentos(self):
        print("Listando os Tratamentos Disponíveis:\n")
        for tratamento in self.tratamentos:
            print(f'- {tratamento}')
        print("\nTotal de tratamentos disponíveis:", len(self.tratamentos))

    def listar_vacinados(self):
        print("Listando a quantidade de vacinados por tipo de vacina:\n")
        for vacina, quantidade in self.vacinados.items():
            print(f'- {vacina}: {quantidade} vacinados')
        print("\nTotal de vacinados:", sum(self.vacinados.values()))
