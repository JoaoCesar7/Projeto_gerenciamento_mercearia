# Padrão MVC

Esse projeto faz parte do curso Python Full e foi desenvolvido para treinar e compreender melhor o padrão MVC (Model, View, Controller)

O padrão MVC é uma arquitetura de Software muito utilizada. É um padrão muito completo, muito organizado e fácil de se trabalhar em equipe. Uma das vantagens de trabalhar com ele é a facilidade de trabalhar com várias pessoas e cada pessoa ser responsável por uma parte. Cada parte tem uma atribuição específica, o que facilita na organização e na hora de localizar possíveis problemas que venham a surgir, por exemplo, um problema na Controller não vai prejudicar o que já foi desenvolvido na Model e na View. Ou seja, eles são unidades únicas de código que fazem relações com as outras.

<h3>View:</h3>
parte do projeto responsável pela interface gráfica, é o que o usuário vai ver;

<h3>Dal:</h3>
faz o acesso ao banco de dados ou arquivo. Define como que vai ser salvo no banco de dados ou no arquivo texto, como que vai ser feita a leitura dos dados

<h3>Controller:</h3>
responsável pela lógica do problema, pelas verificações. Por exemplo validação de cpf, o usuário insere o cpf na View e esse cpf é enviado para a Controller que vai verificar esse cpf, se tiver tudo certo ele passa para a Model, se tiver algum erro ele devolve para a View indicando que há um erro.

<h3>Model:</h3>
armazenamento e estrutura dos dados, modelagem dos dados 

# Proposta

Desenvlver gerenciamento mercearia. O projeto tem que Cadastrar, Alterar, Remover; Categoria, Produtos, Fornecedor, Funcionário entre outros.
