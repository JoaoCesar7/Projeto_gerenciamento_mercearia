# é simplesmente uma função Python que recebe uma requisição Web e retorna uma resposta Web.

from controller import (
    CategoriaController,
    EstoqueController,
    FornecedorController,
    ClienteController,
    FuncionarioController,
    VendasController
)
from dao import CategoriaDao, EstoqueDao, FornecedorDao, ClienteDao, FuncionarioDao

print('======================= Gerenciamento de Mercearia =======================')
print()
print()

while True:
    decisao = input('[1]Categoria [2]Produto [3]Fornecedor [4]Cliente [5]Funcionário [6]Caixa [0]Fechar: ')
    decisao = int(decisao)

    print('')
    if decisao == 0:
        break

    # Área de Cadastro/Alteração/Remoção

    if decisao == 1:
        decisao_user = input('[C]adastrar [A]lterar [R]emover [V]oltar: ').lower()

        if decisao_user == 'c':
            mostrar = CategoriaDao.lercategoria()
            for i in mostrar:
                print(i, end='')
            nome_categoria = input('Nome da categoria: ').upper()
            CategoriaController.cadastrarCategoria(nome_categoria)  # Chamando controller      

        elif decisao_user == 'a':
            x = CategoriaDao.lercategoria()
            for i in x:
                print(i, end='')
            alterar_categoria = input('Digite o nome da categoria que deseja alterar: ').upper()
            alterada_categoria = input('Digite o nome da nova categoria alterada: ').upper()
            CategoriaController.alterarCategoria(alterarCategoria=alterar_categoria,
                                                 alteradaCategoria=alterada_categoria)

        elif decisao_user == 'r':
            x = CategoriaDao.lercategoria()
            for i in x:
                print(i, end="")

            indice_categoria = input('Digite o nome da categoria que dejesa remover: ').upper()

            CategoriaController.removerCategoria(indice_categoria)

        elif decisao_user == 'v':
            continue

        else:
            print('')
            print('Desculpe.. Opção inválida. Tente novamente.')
            print('Opções [C] [R] [A] [V]')
            print('')
            continue

    # Área de Produtos
    elif decisao == 2:
        decisao_user2 = input('[C]adastrar [A]lterar [R]emover [V]oltar: ').lower()
        mostrar = EstoqueDao.ler_produto()
        for i in mostrar:
            print(i, end='')

        if decisao_user2 == 'c':

            nome = input('Nome do produto: ').upper()
            preco = input('Valor do produto: R$')
            categoria = input('Categoria do produto: ').upper()
            quantidade = input('Quantidade do produto em estoque: ')
            EstoqueController.cadastrar_produto(nome=nome, preco=preco, categoria=categoria, quantidade=quantidade)

        elif decisao_user2 == 'a':

            nome_alterar = input('Nome do produto que deseja alterar: ').upper()
            print('Dados para alteração')
            nome_alterado = input('Nome do produto: ').upper()
            valor_alterado = input('Valor do produto: R$').upper()
            categoria_alterada = input('Categoria do produto: ').upper()
            quantidade_alterada = input('Digite a quantidade do produto: ').upper()

            EstoqueController.alterar_produto(alterar_produto=nome_alterar, nome=nome_alterado,
                            preco=valor_alterado, categoria=categoria_alterada, quantidade=quantidade_alterada)

        elif decisao_user2 == 'r':
            mostrar = EstoqueDao.ler_produto()
            for i in mostrar:
                print(i, end='')

            produtoRemovido = input('Digite nome do produto que deseja remover: ').upper()
            EstoqueController.remover_produto(nome_produto=produtoRemovido)

        elif decisao_user2 == 'v':
            continue

        else:
            print('')
            print('Desculpe... Opção inválida. Tente novamente.')
            print('Opções [C] [R] [A] [V]')
            print('')
            continue

    # ÁREA DE FORNECEDOR

    elif decisao == 3:
        decisao_user3 = input('[C]adastrar [A]lterar [R]emover [V]oltar: ').lower()
        mostrar = FornecedorDao.ler_fornecedores()
        for i in mostrar:
            print(i, end='')

        if decisao_user3 == 'c':

            nomeForne = input('Nome do fornecedor: ').upper()
            telefone = input('Número de telefone: ')
            cnpj = input('Digite CNPJ da empresa: ')
            categoria = input('DIgite a categoria: ').upper()

            FornecedorController.cadastrar(nome=nomeForne, telefone=telefone, cnpj=cnpj, categoria=categoria)

        elif decisao_user3 == 'r':

            removerFornecedor = input('Nome do fornecedor: ').upper()
            FornecedorController.remover_fornecedor(nome_fornecedor=removerFornecedor)

        elif decisao_user3 == 'a':

            alterar = input('Nome do fornecedor: ').upper()
            print('Informações da alteração do fornecedor')
            nomeAlt = input('Nome do fornecedor: ').upper()
            telAlt = input('Digite o telefone: ')
            cnpjAlt = input('Digite o cnpj: ')
            catAlt = input('Digite a categoria: ').upper()

            FornecedorController.alterarFornecedor(alterarForne=alterar, nome=nomeAlt,
                                                telefone=telAlt, cnpj=cnpjAlt, categoria=catAlt)

        elif decisao_user3 == 'v':
            continue

        else:
            print('')
            print('Desculpe... Opção inválida, tente novamente as opções...')
            print('Digite [C] [R] [A] [V]')
            print('')
            continue

    # ÁREA DE CLIENTES

    elif decisao == 4:
        decisao_user4 = input('[C]adastrar [A]lterar [R]emover [V]oltar: ').lower()
        mostrar = ClienteDao.ler_clientes()
        for i in mostrar:
            print(i, end='')

        if decisao_user4 == 'c':
            nomeClt = input('Nome do cliente: ').upper()
            cpfClt = input('Digite o CPF: ').upper()
            emailClt = input('Digite seu Email: ').lower()
            telefoneClt = input('Telefone de contato: ')
            enderecoclt = input('Digite seu endereço: ').upper()

            ClienteController.cadastrarCliente(nome=nomeClt, cpf=cpfClt, email=emailClt, telefone=telefoneClt,
                                            endereco=enderecoclt)

        elif decisao_user4 == 'r':

            remo_client = input('Digite o nome do cliente que deseja remover: ').upper()
            ClienteController.removerCliente(nome_cliente=remo_client)

        elif decisao_user4 == 'a':

            alterarCLient = input('Nome do cliente: ').upper()

            print('Alterar dados: ')

            nome_cl = input('nome do cliente: ').upper()
            cpf_cl = input('CPF do cliente: ')
            email_cl = input('Email do cliente: ').lower()
            tel_cl = input('Número de telefone: ')
            end_cl = input('Endereço do cliente: ').upper()

            ClienteController.alterarCliente(nomeCliente=alterarCLient, nome=nome_cl,
                                            cpf=cpf_cl, email=email_cl, telefone=tel_cl, endereco=end_cl)

        elif decisao_user4 == 'v':
            continue

        else:
            print('Desculpe, não consegui fazer sua solicitação')

    elif decisao == 5:
        decisao_user5 = input('[C]adastrar [A]lterar [R]emover [V]oltar: ').lower()

        if decisao_user5 == 'c':

            nome_func = input('Nome do funcionário: ').upper()
            cpf_func = input('Digite o CPF: ')
            email_func = input('Digite o email: ').lower()
            tel_func = input('Telefone de contato: ')
            end_func = input('Digite o endereço com Nº: ').upper()
            clt_func = input('Empregado com carteira asssinada: ').upper()

            FuncionarioController.cadastrar_funcionario(nome=nome_func, cpf=cpf_func, email=email_func,
                                                        telefone=tel_func, endereco=end_func, clt=clt_func)

        elif decisao_user5 == 'r':

            nome_funcionario = input('Nome do funcionário: ').upper()
            FuncionarioController.remover_funcionario(remover_func=nome_funcionario)

        elif decisao_user5 == 'a':
            nome_alterar = input('Digite o nome do funcionário que deseja alterar: ').upper()
            print('')
            print('Dados para alteração')
            print('')
            nome_f = input('Digite o nome: ').upper()
            cpf_f = input('Digite o CPF: ')
            email_f = input('Digite Email: ').lower()
            telefone_f = input('Número de telefone: ')
            endereco_f = input('Digite o nome do endereço com número: ').upper()
            clt_f = input('Carteira assinada: [S]im [N]ão: ').upper()

            FuncionarioController.alterar_funcionario(nome_funcionario=nome_alterar, nome=nome_f, cpf=cpf_f,
                                                    email=email_f, telefone=telefone_f, endereco=endereco_f,
                                                    clt=clt_f)
        
        elif decisao_user5 == 'v':
            continue
        
    elif decisao == 6:
        decisao_user6 = input('[1]Venda [2]Sair: ')
        decisao_user6 = int(decisao_user6)


        if decisao_user6 == 1:
            
            itens_vendidos = input('Nome do produto: ').upper()
            vendedor_caixa = input('Nome do funcionário: ').upper()
            comprador = input('CPF do comprador: ').upper()
            quant =input('Quantidade vendida: ') 
            data = input('Data da venda: ')

            VendasController.caixa_controller(itens_vendidos=itens_vendidos,
                                            vendedor=vendedor_caixa, comprador=comprador,
                                            quantidade_vendida=quant, datatime=data)


        elif decisao_user6 == 2:
            pass


        else:
            print('Desculpe... Não consegui concluir sua solicitação')
            continue

    else:
        pass