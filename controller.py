# Controller onde fica as validações do nosso algoritimo.

from model import Categoria, Produtos, Estoque, Vendas, Fornecedor, Pessoas
from dao import CategoriaDao, ProdutosDao, EstoqueDao



# CLASSES DA ÁREA DE CATEGORIA

class CategoriaController:
    @classmethod
    def cadastrarCategoria(cls, novaCategoria):  # Cadastrar Categoria
        existe = False
        cateDal = CategoriaDao.ler_categoria()  
        print('')
        for i in cateDal: 
            if i.categoria.replace('\n', '') == novaCategoria:
                existe = True


        if not existe:
            CategoriaDao.salvarCategoria(novaCategoria)
            print('Categoria cadastrada com sucesso!')
        else:
            print('A categoria já existe em nossa base de dados.')



    @classmethod
    def removerCategoria(cls, removerCategoria):  # Remover Categoria
        x = CategoriaDao.ler_categoria()
        print('')
        cate = list(filter(lambda x: x.categoria.replace('\n', '') == removerCategoria, x))
        if len(cate) == 0:
            print(f'Categoria NÃO existe em nossa base de dados.')
        else:
            for i in range(len(x)):
                if x[i].categoria.replace('\n', '') == removerCategoria:
                    del x[i]
                    break
            
            print('Categoria removida com sucesso.')

            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)


    
    @classmethod
    def alterarCategoria(cls, alterarCategoria, alteradaCategoria):  # Alterar Categoria
        y = CategoriaDao.ler_categoria()
        print('')
        alt = list(filter(lambda x: x.categoria.replace('\n', '') == alterarCategoria, y))
        if len(alt) == 0:
            print('Categoria que deseja alterar... NÃO existe em nossa base de dados.')
        else:
            for i in range(len(y)):
                if y[i].categoria.replace('\n', '') == alterarCategoria:
                    del y[i]
                    break

            with open('categoria.txt', 'w') as arq:
                for i in y:
                    arq.writelines(i.categoria)

            existe = False
            for i in y: 
                if i.categoria.replace('\n', '') == alteradaCategoria:
                    existe = True
            if not existe:
                CategoriaDao.salvarCategoria(alteradaCategoria)
                print('Categoria alterada com sucesso!')


       

# CLASSES DA ÁREA DE PRODUTOS

class ProdutosController:
    @classmethod
    def cadastrarProduto(cls, nome, preco, categoria):
        existe = False
        prod = ProdutosDao.ler()
        for i in prod:
            if i == nome ==  preco == categoria:
                print(i)
                existe = True

        
        if not existe:
            ProdutosDao.salvar(Produtos(nome, preco, categoria))
            print('Produto cadastrado com sucesso.')
        else:
            print('Produto existe em nossa base de dados.')



    @classmethod
    def removerProduto(cls, removerProduto):
        x = ProdutosDao.ler()

        produto = list(filter(lambda x: x.produtos.replace('\n', '') == removerProduto, x))
        if len(produto) == 0:

            print(f'Categoria NÃO existe em nossa base de dados.')
        else:
            for i in range(len(x)):
                print(i)
                if x[i].produtos.replace('\n', '') == removerProduto:
                    del x[i]
                    break


            with open('produtos.txt', 'w') as arq:
                for i in x:
                    print(i)
                    arq.writelines(i.produtos)




# CLASSES DA ÁREA DE ESTOQUE:

class Estoque:
    @classmethod
    def cadastrarEstoque(cls, nome, produto):
        ...


