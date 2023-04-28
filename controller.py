# Controller onde fica as validações do nosso algoritimo.

from model import Produtos, Vendas, Fornecedor, Cliente, Funcionario
from dao import (
    CategoriaDao,
    EstoqueDao,
    FornecedorDao,
    ClienteDao,
    FuncionarioDao,
    VendasDao,
)
from datetime import datetime

DATA_BASE = 'data_base/'


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
        cate = list(
            filter(
                lambda x: x.categoria.replace('\n', '') == removerCategoria, x
            )
        )
        if len(cate) == 0:
            print('Categoria NÃO existe em nossa base de dados.')
        else:
            for i in range(len(x)):
                if x[i].categoria.replace('\n', '') == removerCategoria:
                    del x[i]
                    break

            print('Categoria removida com sucesso.')

            with open(DATA_BASE + 'categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)

    @classmethod
    def alterarCategoria(
        cls, alterarCategoria, alteradaCategoria
    ):  # Alterar Categoria
        y = CategoriaDao.ler_categoria()
        print('')
        alt = list(
            filter(
                lambda x: x.categoria.replace('\n', '') == alterarCategoria, y
            )
        )
        if len(alt) == 0:
            print(
                'Categoria que deseja alterar... NÃO existe em nossa base de dados.'
            )
        else:
            for i in range(len(y)):
                if y[i].categoria.replace('\n', '') == alterarCategoria:
                    del y[i]
                    break

            with open(DATA_BASE + 'categoria.txt', 'w') as arq:
                for i in y:
                    arq.writelines(i.categoria)

            print('Categoria alterada com sucesso')

            existe = False
            for i in y:
                if i.categoria.replace('\n', '') == alteradaCategoria:
                    existe = True
            if not existe:
                CategoriaDao.salvarCategoria(alteradaCategoria)
                print('Categoria alterada com sucesso!')


# CLASSES DA ÁREA DE PRODUTOS(ESTOQUE)


class EstoqueController:
    @classmethod
    def cadastrar_produto(cls, nome, preco, categoria, quantidade):
        prod = EstoqueDao.ler()
        cat = CategoriaDao.ler_categoria()
        x = list(
            filter(lambda x: x.categoria.replace('\n', '') == categoria, cat)
        )

        h = list(
            filter(lambda x: x.produto.nome.replace('\n', '') == nome, prod)
        )
        if len(x) > 0:
            if len(h) == 0:
                print('')
                produto = Produtos(nome, preco, categoria)
                EstoqueDao.salvar(produto, quantidade)
                print('Produto Cadastrado com sucesso.')
            else:
                print('Produto existe no nosso estoque.')
        else:
            print('Categoria inexistente em nossa base de dados.')

    @classmethod
    def remover_produto(cls, nome_produto):
        x = EstoqueDao.ler()

        produ = list(
            filter(
                lambda x: x.produto.nome.replace('\n', '') == nome_produto, x
            )
        )
        if len(produ) == 0:
            print('Não existe esse produto em nossa base de dados.')
        else:
            for i in range(len(x)):
                if x[i].produto.nome.replace('\n', '') == nome_produto:
                    del x[i]
                    break

            print('Produto removido com sucesso')

            with open(DATA_BASE + 'estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(
                        i.produto.nome
                        + '|'
                        + i.produto.preco
                        + '|'
                        + i.produto.categoria
                        + '|'
                        + i.quantidade
                    )

    @classmethod
    def alterar_produto(
        cls, alterar_produto, nome, preco, categoria, quantidade
    ):
        x = EstoqueDao.ler()

        pro = list(
            filter(
                lambda x: x.produto.nome.replace('\n', '') == alterar_produto,
                x,
            )
        )
        if len(pro) == 0:
            print('Produto NÃO existe em nossa base de dados.')
        else:
            for i in range(len(x)):
                if x[i].produto.nome.replace('\n', '') == alterar_produto:
                    del x[i]
                    break

            print('Produto em processo de alteração')

            with open(DATA_BASE + 'estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(
                        i.produto.nome
                        + '|'
                        + i.produto.preco
                        + '|'
                        + i.produto.categoria
                        + '|'
                        + quantidade
                    )
                    arq.writelines('\n')

            for i in pro:
                if not i.produto.nome == nome:
                    produtos = Produtos(nome, preco, categoria)
                    EstoqueDao.salvar(produtos, quantidade)
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
    def remover_fornecedor(cls, nome_fornecedor):
        x = FornecedorDao.ler()

        forne = list(
            filter(lambda x: x.nome.replace('\n', '') == nome_fornecedor, x)
        )
        if len(forne) == 0:
            print('Fornecedor excluido ou NÃO existe em nossa base de dados')
        else:
            for i in range(len(x)):
                if x[i].nome == nome_fornecedor:
                    del x[i]
                    break

            print('Fornecedor removido com sucesso.')

            with open(DATA_BASE + 'fornecedor.txt', 'w') as arq:
                for i in x:
                    arq.writelines(
                        i.nome
                        + '|'
                        + i.telefone
                        + '|'
                        + i.cnpj
                        + '|'
                        + i.categoria
                    )

    @classmethod
    def alterarFornecedor(cls, alterarForne, nome, telefone, cnpj, categoria):
        x = FornecedorDao.ler()

        fornecedor = list(
            filter(lambda x: x.nome.replace('\n', '') == alterarForne, x)
        )
        if len(fornecedor) == 0:
            print('Fornecedor NÃO existe em nossa base de dados.')
        else:
            for i in range(len(x)):
                if x[i].nome == alterarForne:
                    del x[i]
                    break

            with open(DATA_BASE + 'fornecedor.txt', 'w') as arq:
                for i in x:
                    arq.writelines(
                        i.nome
                        + '|'
                        + i.telefone
                        + '|'
                        + i.cnpj
                        + '|'
                        + i.categoria
                    )

            for i in fornecedor:
                if not i.nome == nome:
                    lista = Fornecedor(nome, telefone, cnpj, categoria)
                    FornecedorDao.salvar(lista)
                    print('Fornecedor alterado com sucesso.')


# CLASSES DA ÁREA DE CLIENTES


class ClienteController:
    @classmethod
    def cadastrarCliente(cls, nome, cpf, email, telefone, endereco):
        x = ClienteDao.ler()

        clt = list(filter(lambda x: x.nome.replace('\n', '') == nome, x))
        if len(clt) > 0:
            print('Cliente existe em nossa base de dados.')
        else:
            client = Cliente(nome, cpf, email, telefone, endereco)
            ClienteDao.salvar(client)
            print('Cliente cadastrado com sucesso')

    @classmethod
    def removerCliente(cls, nome_cliente):
        x = ClienteDao.ler()

        lista = list(
            filter(lambda x: x.nome.replace('\n', '') == nome_cliente, x)
        )
        if len(lista) == 0:
            print('Cliente NÃO existe em nossa base de dados.')
        else:
            for i in range(len(x)):
                if x[i].nome == nome_cliente:
                    del x[i]
                    break

            print('Cliente removido com sucesso')

            with open(DATA_BASE + 'clientes.txt', 'w') as arq:
                for i in x:
                    arq.writelines(
                        i.nome
                        + '|'
                        + i.cpf
                        + '|'
                        + i.email
                        + '|'
                        + i.telefone
                        + '|'
                        + i.endereco
                    )

    @classmethod
    def alterarCliente(cls, nomeCliente, nome, cpf, email, telefone, endereco):
        x = ClienteDao.ler()

        lista_client = list(
            filter(lambda x: x.nome.replace('\n', '') == nomeCliente, x)
        )
        if len(lista_client) == 0:
            print('Cliente NÃO existe em nossa base de dados.')
        else:
            for i in range(len(x)):
                if x[i].nome == nomeCliente:
                    del x[i]
                    break

            with open(DATA_BASE + 'clientes.txt', 'w') as arq:
                for i in x:
                    arq.writelines(
                        i.nome
                        + '|'
                        + i.cpf
                        + '|'
                        + i.email
                        + '|'
                        + i.telefone
                        + '|'
                        + i.endereco
                    )

            for i in lista_client:
                if not i.nome == nome:
                    alterado = Cliente(nome, cpf, email, telefone, endereco)
                    ClienteDao.salvar(alterado)
                    print('Cliente alterado com sucesso')


# CLASSES DA ÁREA DE FUNCIONARIO


class FuncionarioController:
    @classmethod
    def cadastrar_funcionario(cls, nome, cpf, email, telefone, endereco, clt):
        x = FuncionarioDao.ler()

        lista_clt = list(filter(lambda x: x.nome.replace('\n', '') == nome, x))
        if len(lista_clt) > 0:
            print('Funcionário existente em nossa base de dados')
        else:
            lista = Funcionario(nome, cpf, email, telefone, endereco, clt)
            FuncionarioDao.salvar(lista)
            print('Funcionário cadastrado com sucesso')

    @classmethod
    def remover_funcionario(cls, remover_func):
        x = FuncionarioDao.ler()

        lista_funcionario = list(
            map(lambda x: x.nome.replace('\n', '') == remover_func, x)
        )
        if len(lista_funcionario) == 0:
            print('Funcionário Não existe em nossa base de dados')
        else:
            for i in range(len(x)):
                if x[i].nome == remover_func:
                    del x[i]
                    break

            print('Funcionário cadastrado com sucesso')

            with open(DATA_BASE + 'funcionario.txt', 'w') as arq:
                for i in x:
                    arq.writelines(
                        i.nome
                        + '|'
                        + i.cpf
                        + '|'
                        + i.email
                        + '|'
                        + i.telefone
                        + '|'
                        + i.endereco
                        + '|'
                        + i.clt
                    )

    @classmethod
    def alterar_funcionario(
        cls, nome_funcionario, nome, cpf, email, telefone, endereco, clt
    ):
        x = FuncionarioDao.ler()

        lista = list(
            filter(lambda x: x.nome.replace('\n', '') == nome_funcionario, x)
        )
        if len(lista) == 0:
            print('Funcionário NÃO existe em nossa base de dados')
        else:
            for i in range(len(x)):
                if x[i].nome == nome_funcionario:
                    del x[i]
                    break

            with open(DATA_BASE + 'funcionario.txt', 'w') as arq:
                for i in x:
                    arq.writelines(
                        i.nome
                        + '|'
                        + i.cpf
                        + '|'
                        + i.email
                        + '|'
                        + i.telefone
                        + '|'
                        + i.endereco
                        + '|'
                        + i.clt
                    )

            for i in lista:
                if not i.nome == nome:
                    fun = Funcionario(
                        nome, cpf, email, telefone, endereco, clt
                    )
                    FuncionarioDao.salvar(fun)
                    print('Funcionário alterado com sucesso')


# ÁREA DO CAIXA


class VendasController:
    @classmethod
    def caixa_controller(
        cls,
        itens_vendidos,
        vendedor,
        comprador,
        quantidade_vendida,
        valor_total,
    ):
        list_estoque = EstoqueDao.ler()
        list_funcionario = FuncionarioDao.ler()

        estoque = list(
            filter(
                lambda nome_produto: nome_produto.produto.nome
                == itens_vendidos,
                list_estoque,
            )
        )
        funcionario = list(
            filter(
                lambda nome_fucnionario: nome_fucnionario.nome == vendedor,
                list_funcionario,
            )
        )

        estoque_temp = []

        if len(funcionario) > 0:
            if len(estoque) > 0:
                for i in range(len(list_estoque)):
                    if (
                        list_estoque[i].produto.nome == itens_vendidos
                    ):  # Se o nome do produto é igual

                        estoque_quant_prod = int(list_estoque[i].quantidade)

                        if estoque_quant_prod >= quantidade_vendida:
                            preco_uni = int(
                                list_estoque[i].produto.preco
                            )  # Preco do produto

                            multiplicacao = preco_uni * quantidade_vendida

                            if valor_total >= multiplicacao:
                                total = (
                                    valor_total - multiplicacao
                                )   # subtração do valor do usuario com a conta final

                                print('')
                                print(f'repasse do usuário R${total}')

                                print(
                                    f'Data da venda {datetime.now().strftime("%d/%m/%Y")}'
                                )

                                # Leitura para armazenar dados obtidos.
                                salvar = Vendas(
                                    Produtos(
                                        list_estoque[i].produto.nome,
                                        list_estoque[i].produto.preco,
                                        list_estoque[i].produto.categoria,
                                    ),
                                    vendedor,
                                    comprador,
                                    quantidade_vendida,
                                )
                                VendasDao.salvar(salvar)

                                quant_final = str(
                                    estoque_quant_prod - quantidade_vendida
                                )

                                estoque_temp.append(
                                    list_estoque[i].produto.nome
                                    + '|'
                                    + list_estoque[i].produto.preco
                                    + '|'
                                    + list_estoque[i].produto.categoria
                                    + '|'
                                    + quant_final
                                    + '\n'
                                )

                                with open(
                                    DATA_BASE + 'estoque.txt', 'w'
                                ) as arq:
                                    arq.writelines(estoque_temp)

                                print(f'Transação efetuada com sucesso')

                            else:
                                print('Saldo insuficiente')

                        else:
                            print('Quantidade excedida')

                    else:
                        estoque_temp.append(
                            list_estoque[i].produto.nome
                            + '|'
                            + list_estoque[i].produto.preco
                            + '|'
                            + list_estoque[i].produto.categoria
                            + '|'
                            + list_estoque[i].quantidade
                        )

                        with open(DATA_BASE + 'estoque.txt', 'w') as arq:
                            arq.writelines(estoque_temp)

            else:
                print(
                    'Produto NÃO existe /ou não cadastrado em nossa base de dados'
                )

        else:
            print('Funcionário NÃO existe em nossa base de dados')


# RELATÓRIOS
class RelatoriosProdController:
    @classmethod
    def mostrar_relat_geral(cls, Solicitar_relatorio):
        # TODO: filtrar relatório de vendas, nome, produto, categoria, quantidade de venda
        x = VendasDao.ler_relatorio_geral()

        lista_tmp = []

        for i in range(len(x)):
            pass
            #DESENVOLVIMENTO


        
