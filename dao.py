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
            arq.writelines(produtos.nome + ' ' + produtos.preco + ' ' + produtos.categoria)
            arq.writelines('\n')



    @classmethod
    def ler(cls):
        with open('produtos.txt', 'r') as arq:
            cls.produto = arq.readlines()

    
        produ = []

        if len(cls.produto) > 0:
            for i in cls.produto:
                produ.append(Produtos(i[0], i[1], i[2]))


        return produ



    @classmethod
    def lerProduto(cls):
        arquivos = open('produtos.txt', 'r')
        lista_arquivos = arquivos.readlines()
        return lista_arquivos





# CLASSES DE ESTOQUES:

class EstoqueDao:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.produtos + '|' + str(quantidade))
            arq.writelines('\n')

    
    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        forne = []

        if len(cls.estoque) > 0:
            ...

    


# CLASSES DE FORNECEDOR:

class Fornecedor:
    
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedor.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + '' + fornecedor.telefone + '' + fornecedor.cnpj + '' + fornecedor.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedor.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()


        fornec = []

        if len(cls.nome) > 0:
            for i in cls.nome:
                fornec.append(i)


        return fornec




# CLASSES PESSOAS:

class Pessoas:
    ...
