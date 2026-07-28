public class Chamado {

    private int numero;
    private String descricao;
    private int prioridade;
    private boolean aberto;

    public Chamado(int numero, String descricao, int prioridade, boolean aberto) {

        if (numero <= 0) {
            throw new IllegalArgumentException("Número deve ser positivo.");
        }

        if (descricao == null || descricao.trim().isEmpty()) {
            throw new IllegalArgumentException("Descrição obrigatória.");
        }

        if (prioridade < 1 || prioridade > 3) {
            throw new IllegalArgumentException("Prioridade deve ser entre 1 e 3.");
        }

        this.numero = numero;
        this.descricao = descricao;
        this.prioridade = prioridade;
        this.aberto = aberto;
    }

    public int getNumero() {
        return numero;
    }

    public String getDescricao() {
        return descricao;
    }

    public int getPrioridade() {
        return prioridade;
    }

    public boolean isAberto() {
        return aberto;
    }

    public boolean setDescricao(String descricao) {
        if (descricao == null || descricao.trim().isEmpty()) {
            return false;
        }

        this.descricao = descricao;
        return true;
    }

    public boolean fechar() {
        if (!aberto) {
            return false;
        }

        aberto = false;
        return true;
    }

    public boolean reabrir() {
        if (aberto) {
            return false;
        }

        aberto = true;
        return true;
    }

    public boolean alterarPrioridade(int novaPrioridade) {
        if (novaPrioridade < 1 || novaPrioridade > 3) {
            return false;
        }

        prioridade = novaPrioridade;
        return true;
    }

    public String resumo() {
        return "Chamado #" + numero +
                " | " + descricao +
                " | Prioridade: " + prioridade +
                " | " + (aberto ? "Aberto" : "Fechado");
    }

    public boolean prioridadeMaiorQue(Chamado outro) {
        return this.prioridade > outro.prioridade;
    }

    @Override
    public String toString() {
        return "Chamado{" +
                "numero=" + numero +
                ", descricao='" + descricao + '\'' +
                ", prioridade=" + prioridade +
                ", aberto=" + aberto +
                '}';
    }
}
