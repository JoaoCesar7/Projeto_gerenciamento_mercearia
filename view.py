# é simplesmente uma função Python que recebe uma requisição Web e retorna uma resposta Web.

from controller import CategoriaController
from dao import CategoriaDao

print('======================= Gerenciamento de Mercearia =======================')
print()
print()



while True:
    decisao2 = input('[1]Categoria [2]Produto [3]Fornecedor [4]Cliente [5]Funcionário [0]Sair: ')
    decisao2 = int(decisao2)
    print('')
    if decisao2 == 0:
        break



# Área de Cadastro/Alteração/Remoção

    if decisao2 == 1:
        categoria = input('[C]adastrar [A]lterar [R]emover: ').lower()

        if categoria == 'c':
            nome_categoria = input('Nome da categoria: ').upper()
            CategoriaController.cadastrarCategoria(nome_categoria)  # Chamando controller 
        

        if categoria == 'a':
            CategoriaDao.lercategoria()

            alterar_categoria = input('Digite o nome da categoria que deseja alterar: ')
            CategoriaController.alterarCategoria(alterar_categoria)



        if categoria == 'r':
            CategoriaDao.lercategoria()
    
            indice_categoria = input('Digite o nome da categoria que dejesa remover: ').upper()

            CategoriaController.removerCategoria(indice_categoria)
            

            