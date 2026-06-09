import java.util.Random;
import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        Random rand = new Random();

        String[] produtos = {"X-Burguer", "Pizza", "Batata Frita", "Refrigerante", "Sorvete", "Frango Frito", "Nuggets", "Suco", "Água", "Pudim", "Bolo", "Torta"};
        double[] precos = {18.00, 35.00, 18.00, 8.00, 6.00, 22.00, 12.00, 7.00, 3.00, 10.00, 12.00, 14.00};
        int[] quantidades = new int[produtos.length];

        // categorias por índices no array produtos
        int[] idxComidas = {0, 1, 2, 5, 6};
        int[] idxBebidas = {3, 7, 8};
        int[] idxSobremesas = {4, 9, 10, 11};

        boolean finalizado = false;

        while (!finalizado) {
            System.out.println("===========================");
            System.out.println("FAST FOOD IFPR");
            System.out.println("===========================\n");

            System.out.println("1 - Comidas");
            System.out.println("2 - Bebidas");
            System.out.println("3 - Sobremesas");
            System.out.println("4 - Finalizar Pedido\n");

            System.out.print("Escolha: ");
            int escolhaMain = readInt(entrada);

            switch (escolhaMain) {
                case 1:
                    // Comidas
                    if (handleCategory(entrada, produtos, precos, quantidades, idxComidas)) {
                        if (showSummaryAndPayment(entrada, produtos, precos, quantidades, rand)) {
                            finalizado = true;
                        }
                    }
                    break;
                case 2:
                    // Bebidas
                    if (handleCategory(entrada, produtos, precos, quantidades, idxBebidas)) {
                        if (showSummaryAndPayment(entrada, produtos, precos, quantidades, rand)) {
                            finalizado = true;
                        }
                    }
                    break;
                case 3:
                    // Sobremesas
                    if (handleCategory(entrada, produtos, precos, quantidades, idxSobremesas)) {
                        if (showSummaryAndPayment(entrada, produtos, precos, quantidades, rand)) {
                            finalizado = true;
                        }
                    }
                    break;
                case 4:
                    // Finalizar pedido: se não houver itens, volta ao menu
                    if (sum(quantidades) == 0) {
                        System.out.println("Nenhum item no pedido. Escolha algo antes de finalizar.\n");
                        break;
                    }
                    if (showSummaryAndPayment(entrada, produtos, precos, quantidades, rand)) {
                        finalizado = true;
                    }
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.\n");
            }
        }

        entrada.close();
    }

    private static boolean handleCategory(Scanner entrada, String[] produtos, double[] precos, int[] quantidades, int[] indices) {
        int menuWidth = 25;
        while (true) {
            System.out.println("\n---------------------------");
            System.out.println("Escolha um item (0 - Voltar):");
            for (int i = 0; i < indices.length; i++) {
                int idx = indices[i];
                String left = (i + 1) + " - " + produtos[idx];
                int dots = menuWidth - left.length();
                if (dots < 3) dots = 3;
                String fill = new String(new char[dots]).replace('\0', '.');
                System.out.println(left + " " + fill + " " + format(precos[idx]));
            }
            System.out.println("0 - Voltar\n");

            System.out.print("Escolha: ");
            int escolha = readInt(entrada);

            if (escolha == 0) return false;
            if (escolha < 0 || escolha > indices.length) {
                System.out.println("Opção inválida. Tente novamente.\n");
                continue;
            }

            int prodIdx = indices[escolha - 1];
            System.out.println();
            System.out.print("Quantidade: ");
            int q = readInt(entrada);
            if (q <= 0) {
                System.out.println("Quantidade inválida. Item não adicionado.\n");
                continue;
            }
            quantidades[prodIdx] += q;
            System.out.println();
            System.out.println("Item adicionado ao pedido!\n");
            System.out.println("Deseja continuar comprando?");
            System.out.println("1 - Sim");
            System.out.println("2 - Finalizar\n");
            System.out.print("Escolha: ");
            int cont = readInt(entrada);
            System.out.println();
            if (cont == 2) {
                return true; // finalizar pedido
            }
            return false; // voltar ao menu principal
        }
    }

    private static int sum(int[] arr) {
        int s = 0;
        for (int v : arr) s += v;
        return s;
    }

    private static boolean showSummaryAndPayment(Scanner entrada, String[] produtos, double[] precos, int[] quantidades, Random rand) {
        System.out.println("\n===========================");
        System.out.println("RESUMO DO PEDIDO");
        System.out.println("===========================\n");
        double total = 0.0;
        int columnWidth = 25;
        for (int i = 0; i < produtos.length; i++) {
            if (quantidades[i] > 0) {
                double sub = quantidades[i] * precos[i];
                total += sub;
                String left = quantidades[i] + "x " + produtos[i];
                int dots = columnWidth - left.length();
                if (dots < 3) dots = 3;
                String fill = new String(new char[dots]).replace('\0', '.');
                System.out.println(left + " " + fill + " " + format(sub));
            }
        }
        System.out.println();
        System.out.println("TOTAL: " + format(total) + "\n");
        boolean pagamentoConcluido = false;
        while (!pagamentoConcluido) {
            System.out.println("Forma de pagamento:\n");
            System.out.println("1 - Dinheiro");
            System.out.println("2 - Cartão");
            System.out.println("3 - PIX");
            System.out.println("4 - Voltar ao menu\n");

            System.out.print("Escolha: ");
            int pag = readInt(entrada);
            if (pag == 4) {
                pagamentoConcluido = true;
                return false;
            } else if (pag >= 1 && pag <= 3) {
                System.out.println();
                System.out.println("Pagamento realizado com sucesso!\n");
                int numeroPedido = rand.nextInt(900) + 100;
                System.out.println("Pedido Nº " + numeroPedido + "\n");
                System.out.println("Aguarde a chamada do seu pedido.");
                pagamentoConcluido = true;
                return true;
            } else {
                System.out.println("Opção de pagamento inválida. Tente novamente.\n");
            }
        }
        return false;
    }

    private static String format(double valor) {
        String s = String.format("R$ %.2f", valor);
        return s.replace('.', ',');
    }

    private static int readInt(Scanner sc) {
        while (!sc.hasNextInt()) {
            sc.next();
            System.out.print("Entrada inválida. Digite um número: ");
        }
        return sc.nextInt();
    }
}