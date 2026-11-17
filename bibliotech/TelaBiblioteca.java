
import java.awt.*;
import javax.swing.*;
import javax.swing.border.EmptyBorder;

public class TelaBiblioteca extends JFrame {

    private Biblioteca biblioteca;
    private JTextField campoTitulo;
    private JTextField campoMatricula;
    private JTextArea areaAcervo;

    private final Color FUNDO = new Color(245, 240, 255);
    private final Color ROXO = new Color(109, 40, 217);
    private final Color TEXTO = new Color(59, 35, 90);
    private final Color SELECAO = new Color(216, 180, 254);

    public TelaBiblioteca(Biblioteca biblioteca) {

        this.biblioteca = biblioteca;

        setTitle("BiblioTech - Gerenciamento da Biblioteca");
        setSize(850, 500);
        setLocationRelativeTo(null);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setLayout(new BorderLayout(8, 8));

        getContentPane().setBackground(FUNDO);

        // Painel superior
        JPanel painelSuperior = new JPanel(
                new BorderLayout(8, 8));

        painelSuperior.setBackground(FUNDO);

        painelSuperior.setBorder(
                new EmptyBorder(12, 12, 5, 12));

        // Título da tela
        JLabel tituloTela = new JLabel(
                "Gerenciamento da Biblioteca");

        tituloTela.setFont(
                new Font("SansSerif", Font.BOLD, 20));

        tituloTela.setForeground(ROXO);

        tituloTela.setBorder(
                new EmptyBorder(0, 5, 8, 5));

        painelSuperior.add(
                tituloTela,
                BorderLayout.NORTH);

        // Campos de entrada
        JPanel campos = new JPanel(
                new GridLayout(2, 2, 10, 10));

        campos.setBackground(FUNDO);

        campos.setBorder(
                new EmptyBorder(5, 5, 8, 5));

        campoTitulo = new JTextField(18);
        campoMatricula = new JTextField(18);

        estilizarCampo(campoTitulo);
        estilizarCampo(campoMatricula);

        JLabel labelTitulo = new JLabel("Título do livro:");
        JLabel labelMatricula = new JLabel("Matrícula do leitor:");

        labelTitulo.setFont(
                new Font("SansSerif", Font.BOLD, 13));

        labelMatricula.setFont(
                new Font("SansSerif", Font.BOLD, 13));

        labelTitulo.setForeground(TEXTO);
        labelMatricula.setForeground(TEXTO);

        campos.add(labelTitulo);
        campos.add(campoTitulo);

        campos.add(labelMatricula);
        campos.add(campoMatricula);

        painelSuperior.add(
                campos,
                BorderLayout.CENTER);

        add(painelSuperior, BorderLayout.NORTH);

        // Área do acervo
        areaAcervo = new JTextArea();

        areaAcervo.setEditable(false);
        areaAcervo.setLineWrap(true);
        areaAcervo.setWrapStyleWord(true);

        areaAcervo.setFont(
                new Font("SansSerif", Font.PLAIN, 14));

        areaAcervo.setBackground(FUNDO);
        areaAcervo.setForeground(TEXTO);

        areaAcervo.setMargin(
                new Insets(12, 12, 12, 12));

        JScrollPane painelAcervo = new JScrollPane(areaAcervo);

        painelAcervo.setBorder(
                BorderFactory.createTitledBorder(
                        BorderFactory.createLineBorder(
                                new Color(196, 181, 253)),
                        "Acervo de livros",
                        0,
                        0,
                        new Font("SansSerif", Font.BOLD, 14),
                        ROXO
                )
        );

        painelAcervo.setBackground(FUNDO);

        painelAcervo.getViewport().setBackground(FUNDO);

        painelAcervo.setBorder(
                BorderFactory.createCompoundBorder(
                        BorderFactory.createEmptyBorder(
                                5, 12, 5, 12),
                        painelAcervo.getBorder()
                )
        );

        add(painelAcervo, BorderLayout.CENTER);

        // Painel dos botões
        JPanel botoes = new JPanel(
                new FlowLayout(FlowLayout.CENTER, 12, 12));

        botoes.setBackground(FUNDO);

        JButton botaoEmprestar =
                criarBotao("Emprestar");

        JButton botaoDevolver =
                criarBotao("Devolver");

        JButton botaoAtualizar =
                criarBotao("Atualizar acervo");

        botoes.add(botaoEmprestar);
        botoes.add(botaoDevolver);
        botoes.add(botaoAtualizar);

        add(botoes, BorderLayout.SOUTH);

        // Eventos dos botões
        botaoEmprestar.addActionListener(
                e -> emprestar());

        botaoDevolver.addActionListener(
                e -> devolver());

        botaoAtualizar.addActionListener(
                e -> atualizarAcervo());

        campoTitulo.addActionListener(
                e -> emprestar());

        atualizarAcervo();
    }

    // Estilizar campos de texto
    private void estilizarCampo(JTextField campo) {

        campo.setFont(
                new Font("SansSerif", Font.PLAIN, 14));

        campo.setForeground(TEXTO);
        campo.setBackground(Color.WHITE);

        campo.setCaretColor(ROXO);

        campo.setBorder(
                BorderFactory.createCompoundBorder(
                        BorderFactory.createLineBorder(
                                new Color(196, 181, 253)),
                        BorderFactory.createEmptyBorder(
                                7, 9, 7, 9)
                )
        );
    }

    // Criar botões arredondados
    private JButton criarBotao(String texto) {

        JButton botao = new JButton(texto) {

            @Override
            protected void paintComponent(Graphics g) {

                Graphics2D g2 = (Graphics2D) g.create();

                g2.setRenderingHint(
                        RenderingHints.KEY_ANTIALIASING,
                        RenderingHints.VALUE_ANTIALIAS_ON);

                g2.setColor(getBackground());

                g2.fillRoundRect(
                        0, 0,
                        getWidth(),
                        getHeight(),
                        20, 20);

                g2.dispose();

                super.paintComponent(g);
            }
        };

        botao.setFont(
                new Font("SansSerif", Font.BOLD, 12));

        botao.setBackground(ROXO);
        botao.setForeground(Color.WHITE);

        botao.setFocusPainted(false);
        botao.setBorderPainted(false);
        botao.setContentAreaFilled(false);
        botao.setOpaque(false);

        botao.setCursor(
                new Cursor(Cursor.HAND_CURSOR));

        botao.setBorder(
                BorderFactory.createEmptyBorder(
                        9, 18, 9, 18));

        return botao;
    }

    // Atualizar acervo
    private void atualizarAcervo() {

        areaAcervo.setText(
                biblioteca.obterAcervoComoTexto());

        areaAcervo.setCaretPosition(0);
    }

    // Realizar empréstimo
    private void emprestar() {

        String titulo = campoTitulo.getText().trim();

        String matricula = campoMatricula.getText().trim();

        if (titulo.isEmpty() || matricula.isEmpty()) {

            JOptionPane.showMessageDialog(
                    this,
                    "Preencha o título e a matrícula.",
                    "Campos obrigatórios",
                    JOptionPane.WARNING_MESSAGE);

            return;
        }

        boolean resultado =
                biblioteca.emprestar(titulo, matricula);

        atualizarAcervo();

        if (resultado) {

            JOptionPane.showMessageDialog(
                    this,
                    "Empréstimo realizado.",
                    "Sucesso",
                    JOptionPane.INFORMATION_MESSAGE);

        } else {

            JOptionPane.showMessageDialog(
                    this,
                    "Empréstimo recusado. Confira o título, a matrícula, "
                            + "a disponibilidade e o limite do leitor.",
                    "Empréstimo não realizado",
                    JOptionPane.WARNING_MESSAGE);
        }
    }

    // Realizar devolução
    private void devolver() {

        String titulo = campoTitulo.getText().trim();

        if (titulo.isEmpty()) {

            JOptionPane.showMessageDialog(
                    this,
                    "Preencha o título do livro.",
                    "Campo obrigatório",
                    JOptionPane.WARNING_MESSAGE);

            return;
        }

        boolean resultado =
                biblioteca.devolver(titulo);

        atualizarAcervo();

        if (resultado) {

            JOptionPane.showMessageDialog(
                    this,
                    "Devolução registrada.",
                    "Sucesso",
                    JOptionPane.INFORMATION_MESSAGE);

        } else {

            JOptionPane.showMessageDialog(
                    this,
                    "Nenhum empréstimo ativo encontrado para esse título.",
                    "Devolução não realizada",
                    JOptionPane.WARNING_MESSAGE);
        }
    }

    // Inicialização
    public static void main(String[] args) {

        Biblioteca biblioteca = new Biblioteca();

        biblioteca.cadastrarLivro(
                new Livro("Dom Casmurro", "Machado de Assis", 1899)
        );

        biblioteca.cadastrarLivro(
                new Livro("Capitaes da Areia", "Jorge Amado", 1937)
        );

        biblioteca.cadastrarLeitor(
                new Leitor("Pedro Alves", "2026010", 1)
        );

        biblioteca.cadastrarLeitor(
                new Leitor("Ana Lima", "2026011", 2)
        );

        SwingUtilities.invokeLater(() -> {

            TelaBiblioteca tela =
                    new TelaBiblioteca(biblioteca);

            tela.setVisible(true);
        });
    }
}
