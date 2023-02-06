# é simplesmente uma função Python que recebe uma requisição Web e retorna uma resposta Web.

from controller import CategoriaController, ProdutosController
from dao import CategoriaDao, ProdutosDao

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

        elif categoria == 'a':
            x = CategoriaDao.lercategoria()
            for i in x:
                print(i, end='')
            alterar_categoria = input('Digite o nome da categoria que deseja alterar: ').upper()
            alterada_categoria = input('Digite o nome da nova categoria alterada: ').upper()
            CategoriaController.alterarCategoria(alterarCategoria=alterar_categoria, alteradaCategoria=alterada_categoria)

        elif categoria == 'r':
            x = CategoriaDao.lercategoria()
            for i in x:
                print(i, end="")
    
            indice_categoria = input('Digite o nome da categoria que dejesa remover: ').upper()

            CategoriaController.removerCategoria(indice_categoria)

        elif categoria == 'v':
            continue
    
        else:
            print('')
            print('Desculpe.. Opção inválida. Tente novamente.')
            print('Opções [C] [R] [A] [V]')
            print('')
            continue



# Área de Produtos

    elif decisao2 == 2:
        produtos = input('[C]adastrar [A]lterar [R]emover [V]oltar: ').lower()

        if produtos == 'c':
            nome = input('Nome do produto: ').upper()
            preco = input('Valor do produto: R$')
            categoria = input('Categoria do produto: ').upper()
            ProdutosController.cadastrarProduto(nome=nome, preco=preco, categoria=categoria)
   
        elif produtos == 'a':
            # mostrar = Produtos.lerProdutos()
            # for i in mostrar:
            #    print(i, end='')
            
            nome_alterar = input('Nome do produto: ').upper()
            nome_alterado = input('Nome do produto: ').upper()
            valor_alterado = input('Valor do produto: R$').upper()
            categoria_alterada = input('Categoria do produto: ').upper()
            ProdutosController.alterarProduto(alterarProduto=nome_alterar, nome=nome_alterado, 
            preco=valor_alterado, categoria=categoria_alterada)

        elif produtos == 'r':
            # mostrar = ProdutosDao.lerProduto()
            # for i in mostrar:
            #    print(i, end='')

            produtoRemovido = input('Digite nome do produto que deseja remover: ').upper()
            ProdutosController.removerProduto(nomeProduto=produtoRemovido)

        elif produtos == 'v':
            continue

        else:
            print('')
            print('Desculpe... Opção inválida. Tente novamente.')
            print('Opções [C] [R] [A] [V]')
            print('')
            continue

    
    elif decisao2 == 3:
        fornecedor = input('[C]adastrar [A]lterar [R]emover [V]oltar: ').lower()

        if fornecedor == 'c':
            ...

        elif fornecedor == 'r':
            ...
        
        elif fornecedor == 'a':
            ...

        elif fornecedor == 'v':
            continue


        else:
            print('')
            print('Desculpe... Opção inválida, tente novamente as opções...')
            print('Digite [C] [R] [A] [V]')
            print('')
            continue



# Tratamento


    else:
        print('Desculpe... Opção desejava inválida. Por favor...')
        print('Tente novamente')
        print('Opção abaixo.')
        print('')
        continue
