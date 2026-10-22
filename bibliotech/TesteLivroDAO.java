public class TesteLivroDAO {

    public static void main(String[] args) {

        LivroDAO dao = new LivroDAO();

        boolean resultado = dao.excluirLivro(1);

        System.out.println(
            "Livro excluído: " + resultado
        );
    }
}