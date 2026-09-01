/*
 * Disciplina: 2026-PS
 * Estudante : [Gustavo Maciel da Silva]
 * Data      : 2026.08.13
 * Projeto   : aula320-projeto-secretaria
 * Arquivo   : Aluno.java
 */

public class Aluno {
    private String nome;
    private String matricula;
    private String curso;
    private String cidade;

    public Aluno(String nome, String matricula, String curso, String cidade) {

        this.nome = nome; 
        this.matricula = matricula;
        this.curso = curso;
        this.cidade = cidade;

    }

    public String getNome() {

        return nome;

    }

    public String getMatricula() {

        return matricula;

    }

    public String getCurso() {

        return curso;
        
    }

    public String getCidade() {

        return cidade;

    }

    public void setNome(String nome) {

        this.nome = nome;

    }

    public void setCurso(String curso) {

        this.curso = curso;

    }

    @Override
    public String toString() {
        return matricula + " | " + nome + " | " + curso + " | " + cidade;
    }

}