# Controller onde fica as validações do nosso algoritimo.

from model import Categoria, Produtos, Estoque, Vendas, Fornecedor
from dao import CategoriaDao, ProdutosDao, EstoqueDao, FornecedorDao, ClienteDao



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
            print('Categoria NÃO existe em nossa base de dados.')
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
        prod = ProdutosDao.ler()
        cat = CategoriaDao.ler_categoria()
        x = list(filter(lambda x: x.categoria.replace('\n', '') == categoria, cat))

        h = list(filter(lambda x: x.nome == nome, prod))
        if len(x) > 0:
            if len(h) == 0:
                produto = Produtos(nome, preco, categoria)
                ProdutosDao.salvar(produto)
                print('Produto Cadastrado com sucesso.')
            else:
                print('Produto existe no nosso estoque.')
        else:
            print('Categoria inexistente em nossa base de dados.')
        


    @classmethod
    def removerProduto(cls, nomeProduto):
        x = ProdutosDao.ler()

        produ = list(filter(lambda x: x.nome.replace('\n', '') == nomeProduto, x))
        if len(produ) == 0:
            print('Não existe esse produto em nossa base de dados.')
        else:
            for i in range(len(x)):
                if x[i].nome.replace('\n', '') == nomeProduto:
                    del x[i]
                    break

            print('Produto removido com sucesso')

            with open('produtos.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.nome + '|' + i.preco + '|' + i.categoria)



    @classmethod
    def alterarProduto(cls, alterarProduto, nome, preco, categoria):
        x = ProdutosDao.ler()

        pro = list(filter(lambda x: x.nome.replace('\n', '') == alterarProduto, x))
        if len(pro) == 0:
            print('Produto NÃO existe em nossa base de dados.')
        else:
            for i in range(len(x)):
                if x[i].nome.replace('\n', '') == alterarProduto:
                    del x[i]
                    break
            
            print('Produto em processo de alteração')

            with open('produtos.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.nome + '|' + i.preco + '|' + i.categoria)
        
            for i in pro:
                if not i.nome == nome: 
                    produtos = Produtos(nome, preco, categoria)
                    ProdutosDao.salvar(produtos)
                    print('Produto cadastrado com sucesso.')



# CLASSE DA ÁREA DE FORNECEDORES

class FornecedorController:

    @classmethod
    def cadastrar(cls, nome, telefone, cnpj, categoria):
        x = FornecedorDao.ler()

        forne = list(filter(lambda x: x.nome == nome, x))
        if len(forne) > 0:
            print('Fornecedor existe em nossa base de dados.')
        else:
            fornecedor = Fornecedor(nome, telefone, cnpj, categoria)
            FornecedorDao.salvar(fornecedor)
            print('Fornecedor cadastrado com sucesso.')


    @classmethod
    def removerFornecedor(cls, nomeFornecedor):
        x = FornecedorDao.ler()

        forne = list(filter(lambda x: x.nome.replace('\n', '') == nomeFornecedor, x))
        if len(forne) == 0:
            print('Fornecedor excluido ou NÃO existe em nossa base de dados')
        else:
            for i in range(len(x)):
                if x[i].nome == nomeFornecedor:
                    del x[i]
                    break

            print('Fornecedor removido com sucesso.')

            with open('fornecedor.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.nome + '|' + i.telefone + '|' + i.cnpj + '|' + i.categoria)


    @classmethod
    def alterarFornecedor(cls, alterarForne, nome, telefone, cnpj, categoria):
        x = FornecedorDao.ler()

        fornecedor = list(filter(lambda x: x.nome.replace('\n', '') == alterarForne, x))
        if len(fornecedor) == 0:
            print('Fornecedor NÃO existe em nossa base de dados.')
        else:
            for i in range(len(x)):
                if x[i].nome == alterarForne:
                    del x[i]
                    break
            
            with open('fornecedor.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.nome + '|' + i.telefone + '|' + i.cnpj + '|' + i.categoria)


            for i in fornecedor:
                if not i.nome == nome:
                    lista = Fornecedor(nome, telefone, cnpj, categoria)
                    FornecedorDao.salvar(lista)
                    print('Fornecedor alterado com sucesso.')

#CLASSES DE CLIENTES

class ClienteController:
    @classmethod
    def cadastrarCliente(cls, nome, cpf, email, telefone, endereco):
        x = ClienteDao.ler()    

        clt = list(filter(lambda x: x.nome.replace('\n', '') == nome, x))
        if len(clt) == 0:
            print('Cliente NÃO está cadastrado em nossa base de dados.')
        else:
            for i in range(len(x)):
                print(i)












# CLASSES DA ÁREA DE ESTOQUE:

class EstoqueController:
    @classmethod
    def cadastrarEstoque(cls, nome, preco, categoria, quantidade):
        x = EstoqueDao.ler()
        y = CategoriaDao.ler_categoria()
        z = list(filter(lambda x: x.categoria == categoria, y))

        est = list(filter(lambda x: x.nome == nome, x))
        if len(z) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                EstoqueDao.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso.')
            else:
                print('Produto já existe no estoque.')
        else: 
            print('Desculpe... tente novamente')
