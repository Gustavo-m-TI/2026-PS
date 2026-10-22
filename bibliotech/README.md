# Bibliotech

Sistema de emprestimo de livros para a biblioteca do campus.
​
## 1. O projeto
​
O cliente é a Dona Marli, bibliotecária do campus. O sistema resolve problemas de controle de empréstimos, devoluções e disponibilidade dos livros, que atualmente são anotados em um caderno. Ele atende tanto a bibliotecária, facilitando a organização, quanto os alunos, que podem consultar a disponibilidade dos livros sem ir ao balcão.

## 2. Historias de usuario
​
| # | Historia de usuario |
|---|---|
| HU01 | Como leitor, quero consultar a disponibilidade de um livro, para saber se posso pega-lo emprestado sem ir ate o balcao. |
| HU02 | Como leitor, quero devolver um livro, para nao ficar com pendencia na biblioteca. |
| HU03 | Como bibliotecaria, quero registrar um emprestimo, para saber quem esta com cada exemplar. |
| HU04 | Como bibliotecaria, quero cadastrar um livro novo, para que ele possa ser encontrado no sistema. |
| HU05 | Como bibliotecaria, quero ver os emprestimos atrasados, para cobrar a devolucao. |
| HU06 | Como leitor, quero reservar um livro que esteja emprestado, para garantir que eu possa pegá-lo quando estiver disponível. |

## 3. Requisitos
​
### Requisitos funcionais
​
| # | Requisito funcional | Veio da |
|---|---|---|
| RF01 | O sistema deve permitir que a bibliotecaria cadastre um livro no acervo. | HU04 |
| RF02 | O sistema deve permitir que a bibliotecaria cadastre um leitor. | regra de acesso: so quem tem cadastro leva livro |
| RF03 | O sistema deve permitir que o leitor consulte a disponibilidade de um livro. | HU01 |
| RF04 | O sistema deve permitir que a bibliotecaria registre a devolucao de um livro. | HU02 |
| RF05 | O sistema deve permitir que a bibliotecaria registre o emprestimo de um livro. | HU03 |
| RF06 | O sistema deve permitir o leitor reservar um livro que esteja emprestado | HU06 - nosso caderno |
​
### Requisitos nao funcionais
​
| # | Requisito nao funcional |
|---|---|
| RNF01 | A consulta de disponibilidade deve responder em menos de 3 segundos. |
| RNF02 | Somente usuarios identificados como bibliotecarios podem alterar o acervo. |

## 4. Diagramas (feitos em APS)
​
### Casos de uso
​
![Diagrama de casos de uso do BiblioTech](docs/casos-de-uso.svg)
​
### Classes
​
![Diagrama de classes do BiblioTech](docs/classes.svg)

## 5. O que o codigo devolveu ao diagrama (Aula 37)

 - Livro ganhou o atributo disponivel: boolean, porque estaDisponivel() precisa guardar o estado.
 - Leitor ganhou livrosEmMaos: int, podePegarEmprestado(), compara com o limite.

 ## 6. Como executar

 No Codespace, dentro da pasta "bilbiotech":

```
javac *.java
java TesteRequisitos
java TelaBiblioteca
```


`TesteRequisitos` confere os requisitos no terminal. `TelaBiblioteca` abre a j


## 7. Requisitos e verificacoes

| # | Onde esta no codigo | Como verifico |
|---|---|---|
| RF01 | `Biblioteca.cadastrarLivro()` | TesteRequisitos: 1 verificacao RF01 |
| RF02 | `Biblioteca.cadastrarLeitor()` | TesteRequisitos: 1 verificacao RF02 |
| RF03 | `Biblioteca.buscarLivro()` e `Livro.estaDisponivel()`; area do acervo na janela | TesteRequisitos: 2 verificacoes R03 |
| RF04 | `Biblioteca.devolver()`, que chama `Emprestimo.registrarDevolucao()`; botao Devolver | TesteRequisitos: 3 verificacoes Rf04 |
| RF05 | `Biblioteca.emprestar()`, que chama `Emprestimo.realizarEmprestimo()`; botao Emprestar | TesteRequisitos: 5 verificacoes RF05 |
| RF06 | (o seu RF: onde esta, ou "ainda nao implementado") | (a verificacao, ou "sem verificacao" |


## 8. O que o BiblioTech ainda nao faz

- HU05: ver os emprestimos atrasados. O emprestimo ainda nao tem prazo.
- RNF02: qualquer pessoa que abre a janela pode emprestar e devolver; nao ha login de bibliotecario.
- Cadastrar livro e leitor pela janela: hoje o cadastro esta no `main` de `Telabiblioteca`.
- Guardar os dados: ao fechar o programa, os emprestimos se perdem.

## 9. Persistência de Dados

### Banco de dados utilizado

O BiblioTech utiliza o MariaDB como sistema gerenciador de banco de dados (SGBD). O banco utilizado pela aplicação chama-se bibliotech, e a tabela livros armazena as informações dos livros cadastrados.

A conexão é realizada por meio do JDBC, utilizando o driver do MariaDB.

### Classe Conexao

A classe Conexao é responsável por estabelecer a conexão entre a aplicação Java e o banco de dados MariaDB.

O método conectar() obtém as credenciais por meio das variáveis de ambiente DB_USER e DB_PASSWORD e utiliza o DriverManager para abrir a conexão com o banco.

Caso as variáveis não estejam configuradas, o método lança uma exceção SQLException informando que as credenciais precisam ser definidas.

### Classe LivroDAO

A classe LivroDAO é responsável pela persistência dos dados dos livros, utilizando o padrão DAO (Data Access Object). Ela executa comandos SQL para inserir, atualizar e excluir registros na tabela livros.

A classe utiliza PreparedStatement para executar os comandos SQL com parâmetros e fecha automaticamente os recursos utilizados por meio do try-with-resources.

### Métodos implementados
| Método |	Funcionalidade |
| --- | --- |
| adicionarLivro(String titulo, String autor, int ano) |	Insere um novo livro na tabela livros. Retorna true se alguma linha for inserida e false se ocorrer um erro ou nenhuma linha for afetada. |
| atualizarLivro(int id, String titulo, String autor, int ano)	| Atualiza o título, o autor e o ano de um livro identificado pelo seu id. Retorna true se alguma linha for alterada e false caso contrário. |
| excluirLivro(int id)	| Exclui o livro identificado pelo id. Retorna true se alguma linha for removida e false caso contrário. |

Em caso de erro de SQL, os métodos exibem uma mensagem no terminal e retornam false.

### Configuração das variáveis de ambiente

A aplicação utiliza as variáveis de ambiente DB_USER e DB_PASSWORD para acessar o banco de dados. Essa abordagem evita armazenar as credenciais diretamente no código-fonte.

No terminal Bash do Codespace ou Linux, configure as variáveis antes de executar a aplicação:

export DB_USER="seu_usuario"
export DB_PASSWORD="sua_senha"


Substitua os valores pelos dados do seu ambiente MariaDB. Não coloque a senha real neste README nem em arquivos versionados do repositório.

Para verificar se as variáveis estão configuradas sem exibir a senha:

test -n "$DB_USER" && echo "DB_USER configurada" || echo "DB_USER não configurada"
test -n "$DB_PASSWORD" && echo "DB_PASSWORD configurada" || echo "DB_PASSWORD não configurada"


As variáveis definidas com export ficam disponíveis no terminal atual e nos processos iniciados por ele. Se abrir outro terminal, poderá ser necessário configurá-las novamente.

Antes de executar os testes, certifique-se de que o MariaDB está em execução, que o banco bibliotech existe, que a tabela livros foi criada e que o driver JDBC do MariaDB está disponível no classpath.

### Como executar o teste de conexão

Execute a classe de teste de conexão existente no projeto. Se ela se chamar TesteConexao, por exemplo, compile os arquivos e execute:

javac *.java
java TesteConexao


O teste deve chamar Conexao.conectar() para verificar se a aplicação consegue estabelecer uma conexão com o MariaDB utilizando as credenciais configuradas.

O nome TesteConexao é apenas um exemplo: utilize o nome real da classe de teste existente no repositório.

### Como executar os testes de persistência

Execute a classe de teste de persistência existente no projeto. Se ela se chamar TesteLivroDAO, por exemplo:

javac *.java
java TesteLivroDAO


Os testes devem verificar os métodos implementados em LivroDAO, validando a inserção, a atualização e a exclusão de livros.

Recomenda-se utilizar registros de teste e conferir o resultado das operações no banco de dados. Para evitar alterações acidentais, prefira executar os testes em um banco de dados separado do ambiente utilizado pela aplicação.

Os nomes TesteLivroDAO e TesteConexao são ilustrativos. Caso essas classes ainda não existam, será necessário criá-las antes de executar os testes.
