import java.util.Scanner;

public class MaiorValor {

    static int maiorValor(int[] valores) {
        int maior = valores[0];

        for (int i = 1; i < valores.length; i++) {
            if (valores[i] > maior) {
                maior = valores[i];
            }
        }

        return maior;
    }

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.print("Quantos números terá o vetor? ");
        int n = entrada.nextInt();

        int[] vetor = new int[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Digite o número " + (i + 1) + ": ");
            vetor[i] = entrada.nextInt();
        }

        System.out.println("Maior valor do vetor: " + maiorValor(vetor));

        entrada.close();
    }
}