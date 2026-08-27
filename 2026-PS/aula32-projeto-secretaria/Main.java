/*
 * Disciplina: 2026-PS
 * Estudante : [Gustavo Maciel da Silva]
 * Data      : 2026.08.13
 * Projeto   : aula320-projeto-secretaria
 * Arquivo   : Main.java
 */

// import: ArrayList = a lista que cresce (o gaveteiro).
// Scanner = a leitura do teclado.
import java.util.ArrayList;
import java.util.Scanner;

/*
 * O BALCAO DA SECRETARIA: no guarda ficha nenhuma, ele atende.
 * Mostra o menu, le a escolha e chama o metodo que resolve.
 */
public class Main {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        // O GAVETEIRO TIPADO: o <Aluno> diz que so entra ficha de aluno aqui.
        ArrayList<Aluno> lista = new ArrayList<Aluno>();

        // while (true) = repete para sempre. A unica saida e o break da opcao 0.
        while (true) {
            System.out.println("========================================");
            System.out.println("     SECRETARIA DO GUSTAVO MACIEL ");
            System.out.println("========================================");
            System.out.println("[1] Cadastrar aluno");
            System.out.println("[2] Listar alunos");
            System.out.println("[3] Buscar por matricula");
            System.out.println("[4] Atualizar curso");
            System.out.println("[5] Remover aluno");
            System.out.println("[0] Sair");
            System.out.print("Sua escolha: ");
            String opcao = teclado.nextLine().trim();

            // Texto se compara com .equals, nunca com == (isso vale ouro em Java).
            if (opcao.equals("0")) {
                System.out.println("Secretaria fechada. Ate a proxima!");
                break;
            } else if (opcao.equals("1")) {
                cadastrar(lista, teclado);
            } else if (opcao.equals("2")) {
                listar(lista);
            } else if (opcao.equals("3")){
                buscar(lista, teclado);
            } else if (opcao.equals("4")){
                atualizar(lista, teclado); 
            } else if (opcao.equals("5")){
                remover(lista, teclado);
            } else {
                System.out.println("Opcao invalida! Vale 0, 1, 2, 3, 4 ou 5.");
            }
        }
    }

    // Le os dados no balcao, carimba a ficha e guarda no gaveteiro.
    static void cadastrar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Nome: ");
        String nome = teclado.nextLine().trim();

        // LACUNA GUIADA: Leia matricula e curso do mesmo jeito,
        // crie a ficha com new Aluno(...), guarde com lista.add(...)
        // e avise: "Ficha de " + nome + " arquivada!"

        System.out.print("Matricula: ");
        String matricula = teclado.nextLine().trim();

        Aluno existente = buscarPorMatricula(lista, matricula);
        if (existente != null) {
            System.out.println("Ja existe ficha com a matricula " + matricula + "!");
            return;
        }

        System.out.print("Curso: ");
        String curso = teclado.nextLine().trim();

        System.out.print("Cidade: ");
        String cidade = teclado.nextLine().trim();

        Aluno aluno = new Aluno(nome, matricula, curso, cidade);
        lista.add(aluno);

        System.out.println("Ficha de " + nome + " arquivada!");
    }

    // Percorre o gaveteiro e imprime ficha por ficha (padrao da Aula 29).
    static void listar(ArrayList<Aluno> lista) {
        // LACUNA AUTONOMA: se lista.size() == 0, avise "Nenhuma ficha...";
        // senao, imprima "--- FICHAS NO GAVETEIRO: N ---" com lista.size()
        // e percorra com for.
        // imprimindo matricula + " | " + nome + " | " + curso pelos getters

        if (lista.size() == 0) {
            System.out.println("Nenhuma ficha...");
        } else {
            System.out.println("--- FICHAS NO GAVETEIRO: " + lista.size() + " ---");

            for (Aluno aluno : lista) {
                System.out.println(aluno.getMatricula() + " | " + aluno.getNome() + " | " + aluno.getCurso() + " | " + aluno.getCidade());
            }
        }
    }

    static Aluno buscarPorMatricula (ArrayList<Aluno> lista, String matricula) {
        for (int i = 0; i < lista.size(); i++) {
            Aluno a = lista.get(i);

            if (a.getMatricula().equals(matricula)) {
                return a;
            }
        }
        return null;
    }

    // O balcao pergunta a matricula e usa a busca para responder.
    static void buscar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matricula procurada: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);

        // GUARDA: confere o null NATES de usar o resultado.
        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula " + matricula + ".");
        } else {
            System.out.println("Achei: " + a.getMatricula() + " | " + a.getNome() + " | " + a.getCurso());
        }
    }
    // Atualizar reusa a busca: escrever uma vez, chamar quantas vezes precisar.
    static void atualizar (ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matricula da ficha a atualizar: ");
        String matricula = teclado.nextLine().trim();
        Aluno a =  buscarPorMatricula(lista, matricula);
        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula "  + matricula + ".");
            return;
        }
        System.out.print("Novo curso de " + a.getNome() + ": ");
        String novoCurso = teclado.nextLine().trim();

        // a variavel a segura a MESMA ficha que esta na lista: mudar por
        // aqui muda o que a listagem mostra depois. Nao precisa reinserir.
        a.setCurso(novoCurso);
        System.out.println("Ficha atualizada: " + a.getMatricula() + " | " + a.getNome() + " | " + a.getCurso());
    }

    // Acao destrutiva pede confirmacao. Padrao de sistema de verdade.
    static void remover(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Matricula da ficha a remover: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);
        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula " + matricula + ".");
            return;
        }
        System.out.print("Tem certeza que quer remover " + a.getNome() + "? (s/n): ");
        String resposta = teclado.nextLine().trim();
        if (resposta.equals("s")) {
            lista.remove(a);
            System.out.println("Ficha removida.");
        } else {
            System.out.println("Remocao cancelada.");
        }
    }

} 