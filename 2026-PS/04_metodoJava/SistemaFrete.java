public class SistemaFrete {

    static double calcularFrete(double peso) {
        if (peso <= 1) {
            return 10.0;
        } else if (peso <= 5) {
            return 20.0;
        } else {
            return 35.0;
        }
    }

    public static void main(String[] args) {
        System.out.println(calcularFrete(0.5)); // 10.0
        System.out.println(calcularFrete(3));   // 20.0
        System.out.println(calcularFrete(8));   // 35.0
    }
}