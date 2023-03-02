# modelagem dos dados


from datetime import date


class Categoria:


    def __init__(self, categoria):
        self.categoria = categoria


class Produtos:


    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria


class Estoque:


    def __init__(self, produtos: Produtos, quantidade):
        self.produtos = produtos
        self.quantidade = quantidade


class Vendas:


    def __init__(self, itens_vendidos: Produtos, vendedor, comprador, quantidade_vendida, datatime: date):
        self.itens_vendidos = itens_vendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidade_vendida = quantidade_vendida
        datatime = datatime


class Fornecedor:


    def __init__(self, nome, telefone, cnpj, categoria):
        self.nome = nome
        self.telefone = telefone
        self.cnpj = cnpj
        self.categoria = categoria


class Cliente:


    def __init__(self, nome, cpf, email, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco



class Funcionario(Cliente):


    def __init__(self, nome, cpf, email, telefone, endereco, clt):
        self.clt = clt
        super(Funcionario, self).__init__(nome, cpf, email, telefone, endereco)



