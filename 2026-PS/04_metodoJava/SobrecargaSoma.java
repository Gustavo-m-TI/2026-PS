public class SobrecargaSoma { 

    // Método para somar inteiros
    static int somar(int a, int b) {

        return a + b;

    }

    // Método para somar números decimais
    static double somar(double a, double b) {

        return a + b;

    }

    public static void main(String[] args) {

        System.out.println(somar(5, 3));         // 8

        System.out.println(somar(2.5, 3.5));     // 6.0

        System.out.println(somar(100, 50));      // 150

    }

}