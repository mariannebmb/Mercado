from Utils.Helper import formata_moeda


class Produto:
    contador: int = 1  # vai associar o valor a um produto

    def __init__(self: object, nome: str, preco: float) -> None:
        self.__codigo: int = Produto.contador
        self.__nome = nome
        self.__preco = preco
        Produto.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    def __str__(self):
        return f'Codigo: {self.codigo} \nNome: {self.nome} \nPreco: {formata_moeda(self.preco)}'


