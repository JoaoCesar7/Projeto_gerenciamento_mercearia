# Dal fica responsavel pelo Armazenamento persistente

from model import Categoria, Produtos, Estoque, Vendas, Fornecedor, Pessoas, Cliente


# CLASSES DA ÁREA DE CATEGORIA:

class CategoriaDao:
    @classmethod
    def salvarCategoria(cls, categoria: Categoria):  # Salvar Categoria.
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria + '\n')


    @classmethod
    def ler_categoria(cls):  # Ler Categoria para exclusão.
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()


        cate = []

        if len(cls.categoria) > 0:
            for i in cls.categoria:
                cate.append(Categoria(i))


        return cate



    @classmethod
    def lercategoria(cls):  # o usuário visualizar o que há em categoria.
        arquivo = open('categoria.txt', 'r')
        lista_categoria = arquivo.readlines()
        return lista_categoria





# CLASSES DA ÁREA DE PRODUTOS:

class ProdutosDao:
    @classmethod
    def salvar(cls, produtos: Produtos): # Salvar Produto
        with open('produtos.txt', 'a') as arq:
            arq.writelines(produtos.nome + ' ' + produtos.preco + ' ' + produtos.categoria + '\n')



    @classmethod
    def ler(cls):
        with open('produtos.txt', 'r') as arq:
            cls.produtos = arq.readlines()

    
        produ = []

        if len(cls.produtos) > 0:
            for i in cls.produtos:
                produ.append(Produtos(i[0], i[1], i[2]))


        return produ




# CLASSES DE ESTOQUES:

class EstoqueDao:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + '|' + produto.preco + '|' + produto.categoria + '|' + str(quantidade))
            arq.writelines('\n')

    
    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

    





# CLASSES DE FORNECEDOR:

class Fornecedor:
    ...







# CLASSES PESSOAS:

class Pessoas:
    ...
