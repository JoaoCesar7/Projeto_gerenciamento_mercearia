# é simplesmente uma função Python que recebe uma requisição Web e retorna uma resposta Web.

from controller import CategoriaController, ProdutosController
from dao import CategoriaDao

print('======================= Gerenciamento de Mercearia =======================')
print()
print()



while True:
    decisao2 = input('[1]Categoria [2]Produto [3]Fornecedor [4]Cliente [5]Funcionário [0]Fechar: ')
    decisao2 = int(decisao2)

    print('')
    if decisao2 == 0:
        break



# Área de Cadastro/Alteração/Remoção

    if decisao2 == 1:
        categoria = input('[C]adastrar [A]lterar [R]emover [V]oltar: ').lower()

        if categoria == 'c':
            mostrar = CategoriaDao.lercategoria()
            for i in mostrar:
                print(i, end='')
            nome_categoria = input('Nome da categoria: ').upper()
            CategoriaController.cadastrarCategoria(nome_categoria)  # Chamando controller 
        

        if categoria == 'a':
            x = CategoriaDao.lercategoria()
            for i in x:
                print(i, end='')
            alterar_categoria = input('Digite o nome da categoria que deseja alterar: ').upper()
            alterada_categoria = input('Digite o nome da nova categoria alterada: ').upper()
            CategoriaController.alterarCategoria(alterarCategoria=alterar_categoria, alteradaCategoria=alterada_categoria)


        if categoria == 'r':
            x = CategoriaDao.lercategoria()
            for i in x:
                print(i, end="")
    
            indice_categoria = input('Digite o nome da categoria que dejesa remover: ').upper()

            CategoriaController.removerCategoria(indice_categoria)
            

        if categoria == 'v':
            continue



# Área de Produtos

    if decisao2 == 2:
        produtos = input('[C]adastrar [A]lterar [R]emover [V]oltar: ').lower()

        if produtos == 'c':
            nome = input('Nome do produto: ').upper()
            preco = input('Valor do produto: R$')
            categoria = input('Categoria do produto: ').upper()
            ProdutosController.cadastrarProduto(nome=nome, preco=preco, categoria=categoria)

            




   


        if produtos == 'a':
            ...


        if produtos == 'r':
            ...

        if produtos == 'v':
            continue








# Tratamento

    if not decisao2:
        print('Desculpe... Caractere inválido')
        print('Tente novamente..')
        continue
