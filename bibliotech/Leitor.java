/*
 * Disciplina: 2026-PS
 * Projeto    : bibliotech
 * Arquivo    : Leitor.java
 * Autor      : Gustavo Maciel da Silva
 * Descricao  : Leitor E UM TIPO DE Usuario: herda nome, matricula e entrar().
 */
public class Leitor extends Usuario {
    private int limiteEmprestimos;
    private int livrosEmMaos;

    public Leitor(String nome, String matricula, int limiteEmprestimos) {
        super(nome, matricula);
        this.limiteEmprestimos = limiteEmprestimos;
        this.livrosEmMaos = 0;
    }
    
    public int getLimiteEmprestimos() {
        return limiteEmprestimos;
    }

    public int getLivrosEmMaos() {
        return livrosEmMaos;
    }

    // OPERACAO DA CAIXA: podePegarEmprestado().
    public boolean podePegarEmprestado() {
        return livrosEmMaos < limiteEmprestimos;
    }

    // Os dois metodos que o emprestimo vai usar na Aula 38.
    public void pegouLivro() {
        this.livrosEmMaos = this.livrosEmMaos + 1;
    }

    public void devolveuLivro() {
        this.livrosEmMaos = this.livrosEmMaos - 1;
    }

    public String toString() {
        return "Leitor " + getNome() + " (" + getMatricula() + ") - "
                + livrosEmMaos + " de " + limiteEmprestimos + " livros";
    }

}