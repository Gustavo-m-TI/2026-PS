public class CalculadoraDesconto {

    static double calcularDesconto(double valor, double percentual) {
        return valor - (valor * percentual / 100.0);
    }

    public static void main(String[] args) {
        System.out.println(calcularDesconto(100, 10)); // 90.0
        System.out.println(calcularDesconto(250, 20)); // 200.0
        System.out.println(calcularDesconto(500, 15)); // 425.0
    }
}