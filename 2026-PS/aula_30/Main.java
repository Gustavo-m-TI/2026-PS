public class Main {

    public static void main(String[] args) {

        int diaNascimento = 14;
        String iniciais = "Gu";

        Chamado c1 = new Chamado(
                diaNascimento,
                "Problema " + iniciais,
                2,
                true
        );

        Chamado c2 = new Chamado(
                diaNascimento + 1,
                "Internet lenta",
                1,
                true
        );

        Chamado c3 = new Chamado(
                diaNascimento + 2,
                "Computador não liga",
                3,
                false
        );

        System.out.println("=== Objetos criados ===");
        System.out.println(c1);
        System.out.println(c2);
        System.out.println(c3);

        System.out.println("\nTentando descrição vazia:");
        System.out.println(c1.setDescricao(""));

        System.out.println("\nTentando prioridade inválida:");
        System.out.println(c1.alterarPrioridade(5));

        System.out.println("\nFechando chamado:");
        System.out.println(c1.fechar());

        System.out.println("\nTentando fechar novamente:");
        System.out.println(c1.fechar());

        System.out.println("\nReabrindo:");
        System.out.println(c1.reabrir());

        System.out.println("\nAlterando prioridade:");
        System.out.println(c1.alterarPrioridade(3));

        System.out.println("\nResumo:");
        System.out.println(c1.resumo());

        System.out.println("\nComparação de prioridade:");
        System.out.println(c1.prioridadeMaiorQue(c2));

        System.out.println("\n=== Estado final ===");
        System.out.println(c1);
        System.out.println(c2);
        System.out.println(c3);
    }
}
