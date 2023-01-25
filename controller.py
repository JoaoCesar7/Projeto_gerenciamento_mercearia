# Controller onde fica as validações do nosso algoritimo.

from model import Categoria, Produtos, Estoque, Vendas, Fornecedor, Pessoas
from dao import CategoriaDao



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
        cate = list(map(lambda x: x.categoria.replace('\n', '') == removerCategoria, x))
        if len(cate) == 0:
            print('Categoria não existe em nossa base de dados')
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
        cat = list(filter(lambda x: x.categoria.replace('\n', '') == alterarCategoria, y))
        if len(cat) > 0:
            alt = list(filter(lambda x: x.categoria.replace('\n', '') == alteradaCategoria, y))
            if len(alt) == 0:
                try:
                    y = list(filter(lambda x: x.catergoria(alteradaCategoria)))
                    if y.categoria == alterarCategoria:
                        ...
                except:
                    ...
        else:
            ...



# CLASSES DA ÁREA DE PRODUTOS








# CLASSES DA ÁREA DE ESTOQUE



            