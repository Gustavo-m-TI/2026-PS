import java.util.ArrayList;
import java.util.Scanner;

public class CatalogoProdutos {

    static void adicionarProduto(ArrayList<String> lista, String nome) {
        lista.add(nome);
    }

    static void listarProdutos(ArrayList<String> lista) {
        for (int i = 0; i < lista.size(); i++) {
            System.out.println((i + 1) + " - " + lista.get(i));
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> produtos = new ArrayList<>();

        int quantidade = sc.nextInt();
        sc.nextLine(); // consumir a quebra de linha

        for (int i = 0; i < quantidade; i++) {
            String produto = sc.nextLine();
            adicionarProduto(produtos, produto);
        }

        listarProdutos(produtos);

        sc.close();
    }
}