public class Produto {

    private int codigo;
    private String nome;
    private double preco;

    public Produto(int codigo, String nome, double preco) {
        this.codigo = codigo;
        this.nome = nome;
        this.preco = preco;
    }

    // Getters

    public int getCodigo() {
        return codigo;
    }

    public String getNome() {
        return nome;
    }

    public double getPreco() {
        return preco;
    }

    // Setters

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    // Alterar preço normalmente

    public void alterarPreco(double preco) {
        this.preco = preco;
    }

    // Sobrecarga: alterar preço aplicando desconto

    public void alterarPreco(double preco, double desconto) {
        this.preco = preco - (preco * desconto / 100);
    }

    // toString

    @Override
    public String toString() {
        return codigo + " - " + nome + " - R$ " + preco;
    }
}
