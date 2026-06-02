import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {

        // Criando o Scanner para ler dados do teclado
        Scanner entrada = new Scanner(System.in);

        // Variáveis para armazenar o nome do item e o valor
        String item = "";
        double valor = 0;

        // Exibindo o nome do restaurante
        System.out.println("=================================");
        System.out.println("     RESTAURANTE SABOR CASEIRO");
        System.out.println("=================================");

        // Exibindo o cardápio
        System.out.println("1 - X-Burguer .......... R$ 18,00");
        System.out.println("2 - Pizza .............. R$ 35,00");
        System.out.println("3 - Suco Natural ....... R$ 8,00");
        System.out.println("4 - Café ............... R$ 5,00");
        System.out.println("5 - Lasanha ............ R$ 28,00");
        System.out.println("=================================");

        // Pedindo ao usuário para escolher uma opção
        System.out.print("Escolha uma opção: ");
        int opcao = entrada.nextInt();

        // Verificando qual item foi escolhido
        if (opcao == 1) {
            item = "X-Burguer";
            valor = 18.00;

        } else if (opcao == 2) {
            item = "Pizza";
            valor = 35.00;

        } else if (opcao == 3) {
            item = "Suco Natural";
            valor = 8.00;

        } else if (opcao == 4) {
            item = "Café";
            valor = 5.00;

        } else if (opcao == 5) {
            item = "Lasanha";
            valor = 28.00;

        } else {

            // Caso o usuário digite uma opção inválida
            System.out.println("Opção inválida. Escolha uma das opções acima.");

            // Fechando o Scanner
            entrada.close();

            // Encerrando o programa
            return;
        }

        // Perguntando a quantidade desejada
        System.out.print("Digite a quantidade desejada: ");
        int quantidade = entrada.nextInt();

        // Calculando o valor total do pedido
        double total = valor * quantidade;

        // Exibindo o resumo final do pedido
        System.out.println("\n========= RESUMO DO PEDIDO =========");
        System.out.println("Item escolhido: " + item);
        System.out.println("Valor unitário: R$ " + valor);
        System.out.println("Quantidade: " + quantidade);
        System.out.println("Valor total: R$ " + total);
        System.out.println("====================================");

        // Fechando o Scanner
        entrada.close();
    }
}