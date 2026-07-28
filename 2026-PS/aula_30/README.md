# Trabalho de POO - Classe Chamado

## Aluno

- Nome: Gustavo
- Turma: 2º Informatica

## Descrição

Este projeto implementa a classe `Chamado` em Java, representando um chamado de suporte técnico.

## Arquivos

- `Chamado.java`
- `Main.java`

## Como compilar

```bash
javac *.java
```

## Como executar

```bash
java Main
```

## Funcionalidades

- Criar chamados;
- Alterar descrição;
- Alterar prioridade;
- Fechar chamado;
- Reabrir chamado;
- Exibir informações do chamado.

## Validações

- Número do chamado deve ser maior que zero;
- Descrição não pode ser vazia;
- Prioridade deve estar entre 1 e 3.

## Opções extras escolhidas

Foram implementadas as seguintes funcionalidades extras:

1. **Método `resumo()`**
   - Retorna um resumo contendo número, descrição, prioridade e situação do chamado.

2. **Método `prioridadeMaiorQue(Chamado outro)`**
   - Compara a prioridade de dois chamados e retorna `true` quando o chamado atual possui prioridade maior que o outro.

## Observações

O programa cria três objetos da classe `Chamado`, realiza testes de operações válidas e inválidas e exibe o estado final dos objetos utilizando o método `toString()`.
