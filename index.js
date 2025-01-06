class Heroi {
    constructor(nome, idade, tipo) {
        this.nome = nome
        this.idade = idade
        this.tipo = tipo
    }

    atacar() {
        let arma;

        switch (this.tipo) {
            case 'Mago':
                arma = 'cajado';
                break;
            case 'Guerreiro':
                arma = 'espada';
                break;
            case 'Monge':
                arma = 'artes marciais';
                break;
            case 'Ninja':
                arma = 'shuriken';
                break;
        }

        console.log(`${this.tipo} atacou usando ${arma}`);
    }
}

Link = new Heroi('Link', 17, 'Guerreiro');
Link.atacar();

Gandalf = new Heroi('Gandalf', 1000, 'Mago')
Gandalf.atacar();
