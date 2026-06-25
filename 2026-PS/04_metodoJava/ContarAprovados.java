import java.util.Scanner;

public class ContarAprovados {

    static int contarAprovados(double[] notas) {
        int aprovados = 0;

        for (int i = 0; i < notas.length; i++) {
            if (notas[i] >= 6.0) {
                aprovados++;
            }
        }

        return aprovados;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int quantidade = sc.nextInt();

        double[] notas = new double[quantidade];

        for (int i = 0; i < quantidade; i++) {
            notas[i] = sc.nextDouble();
        }

        System.out.println(contarAprovados(notas));

        sc.close();
    }
}