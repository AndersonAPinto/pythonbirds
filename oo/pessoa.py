class Pessoa:
    def __init__(self, nome = None, idade = 30):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá Mundo{ id(self)}'

if __name__ == '__main__':
    p = Pessoa('Ana Paula')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Anderson'
    print(p.nome)
    print(p.idade)
