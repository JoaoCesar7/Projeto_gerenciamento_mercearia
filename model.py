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


    def __init__(self, itensVendidos: Produtos, vendedor, comprador, quantidadeVendida, datatime: date):
        self.itensVendidos = itensVendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
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


    def __init__(self, clt, nome, cpf, email, telefone, endereco, numeroClt, serieClt, emissaoClt):
        self.clt = clt
        self.numeroClt = numeroClt
        self.serieClt = serieClt
        self.emissaoClt = emissaoClt
        super(Funcionario, self).__init__(nome, cpf, email, telefone, endereco)



