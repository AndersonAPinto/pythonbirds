class Pessoa:
    def cumprimentar(self):  # método pertence sempre a uma class.
        # self, significa que o método esta sempre chamando o OBJETO.
        return f'Olá Mundo! {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())  # self já declara o objeto como primeiro parâmetro.
