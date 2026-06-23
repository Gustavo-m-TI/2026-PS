public class VerificadorMaior {

    static int maiorNumero(int a, int b) {
        return (a > b) ? a : b;
    }

    public static void main(String[] args) {
        System.out.println(maiorNumero(10, 20)); // 20
        System.out.println(maiorNumero(50, 5));  // 50
        System.out.println(maiorNumero(30, 30)); // 30
    }
}