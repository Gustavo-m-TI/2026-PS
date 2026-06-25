import java.util.Scanner;

public class CalcularMedia {

    static double calcularMedia(double[] notas) {
        double soma = 0;

        for (int i = 0; i < notas.length; i++) {
            soma += notas[i];
        }

        return soma / notas.length;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int quantidade = sc.nextInt();

        double[] notas = new double[quantidade];

        for (int i = 0; i < quantidade; i++) {
            notas[i] = sc.nextDouble();
        }

        double media = calcularMedia(notas);

        System.out.println(media);

        sc.close();
    }
}