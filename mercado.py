from typing import List, Dict
from time import sleep

from Models.Produto import Produto
from Utils.Helper import formata_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    """
    funcao principal na qual o usuario ira selecionar a funcao que deseja executar
    com 6 opcoes
    :return:
    """
    print('============================')
    print('======= Bem-vindo(s) =======')
    print('============================')

    print('Selecione uma opção:')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produto')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair')

    opcao: int = int(input())
    # lista de condiçao que podem ser acessadas
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Sistema finalizado')
        sleep(2)
        exit()
    else:
        print('Opçãp invalida!')
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('===================')
    nome: str = input('Informe o nome do produto:  ')
    preco: float = float(input('Informe o preço do produto:  '))

    if len(produtos) > 0:
        for item in produtos:
            if item.nome == nome:
                print("O produto ja foi cadastrado!")
                sleep(2)
                menu()

            else:
                produto: Produto = Produto(nome, preco)
                produtos.append(produto)
                print(f'O produto {produto.nome} foi cadastrado com sucesso!')
                sleep(2)
                menu()

    else:
        produto: Produto = Produto(nome, preco)
        produtos.append(produto)
        print(f'O produto {produto.nome} foi cadastrado com sucesso!')

    sleep(2)
    menu()


def listar_produto() -> None:
    """
    verifica se há produtos na lista, caso tenha, imprime um por um
    ao finalizar as duas condições, retorna ao menu
    :return:
    """
    if len(produtos) > 0:
        print('Produtos:')
        print('---------')
        for produto in produtos:
            print(produto)
            print('----------')
            sleep(1)
    else:
        print('Não tem produto cadastrado.')
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print("Informe o código do produto que deseja comprar: ")
        print("------------------------------------------------")
        print('Produtos:')
        print('---------')
        for produto in produtos:
            print(produto)
            print('----------')
            sleep(1)

        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:  # verifica se o carrinho tá vazio
                item_existente_carrinho: bool = False
                for item in carrinho:  # inicia uma varredura dentro do carrinho
                    quant = item.get(produto)  # verifica a qnt desse item, utilizando a chave do dic com get()
                    if quant:  # se já tiver o item ele acrescenta mais um
                        item[produto] = quant + 1
                        print(f"O produto {produto.nome} contem {quant + 1} items no carrinho")
                        item_existente_carrinho = True
                        sleep(2)
                        menu()
                    if not item_existente_carrinho:  # se nao tiver, ele adiciona o item
                        prod = {produto: 1}
                        carrinho.append(prod)
                        print(f"O produto {produto.nome} foi adicionado no carrinho.")
                        sleep(2)
                        menu()

            else:  # caso esteja, ele inicia o carrinho com o produto e a quantidade 1
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado no carrinho.')
                sleep(2)
                menu()
        else:
            print("O produto não foi encontrado.")
            sleep(2)
            menu()

    else:
        print('Nâo há produtos disponíveis!')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    # verifica se há items no carrinho
    if len(carrinho) > 0:
        print("Produtos no carrinho: ")

        for item in carrinho:
            # o conteudo do carrinho é um dicionario, por tanto precisa de outro for para percorrer os dados dele
            for dados in item.items():
                print(dados[0])
                print(f"Quantidade: {dados[1]}")
                print('-----------------------')
                sleep(2)
                menu()
    else:
        print("Não há produtos no carrinho.")
        sleep(2)
        menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos no carrinho:')
        for item in carrinho:
            # percorre o dicionario do carrinho
            for dados in item.items():
                # item.items() informa a chave e o valor do dicionarios
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]  # calculo do valor final com o preco e a quantidade de produtos pedidos
        print(f'Sua fatura é: {formata_moeda(valor_total)}')
        print('Pedido finalizado!')
        print('Obrigada!')
        carrinho.clear()
        sleep(5)
    else:
        print('Carrinho vazio.')
    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()

