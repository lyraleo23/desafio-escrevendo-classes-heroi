class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        arma = None

    
        match self.tipo:
            case 'Mago':
                arma = 'cajado'
            case 'Guerreiro':
                arma = 'espada'
            case 'Monge':
                arma = 'artes marciais'
            case 'Ninja':
                arma = 'shuriken'

        print(f'{self.tipo} atacou usando {arma}')

# Link = Heroi('Link', 17, 'Guerreiro')
# Link.atacar()

# Gandalf = Heroi('Gandalf', 1000, 'Mago')
# Gandalf.atacar()

nome_heroi = input('Digite o nome do herói: ')
idade_heroi = int(input('Digite a idade do herói: '))
tipo_heroi = input('Digite o tipo do herói: ')

heroi = Heroi(nome_heroi, idade_heroi, tipo_heroi)
heroi.atacar()
