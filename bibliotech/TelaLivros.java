
import javax.swing.*;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.util.List;

public class TelaLivros extends JFrame {

        private final LivroDAO dao = new LivroDAO();

        private final DefaultTableModel modelo;
        private final JTable tabela;

        private final JTextField campoId = new JTextField(8);
        private final JLabel status = new JLabel("Pronto.");
        private final JTextField campoTitulo = new JTextField(18);

        public TelaLivros() {

                setTitle("BiblioTech - Consulta de Livros");
                setSize(850, 450);
                setLocationRelativeTo(null);

                setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

                setLayout(new BorderLayout(8, 8));

                getContentPane().setBackground(
                                new Color(245, 240, 255));

                modelo = new DefaultTableModel(
                                new Object[] { "ID", "Capa", "Título", "Autor", "Ano" }, 0) {

                        @Override
                        public boolean isCellEditable(int linha, int coluna) {
                                return false;
                        }
                };

                tabela = new JTable(modelo);
                tabela.setRowHeight(95);

                tabela.setFont(new Font("SansSerif", Font.PLAIN, 14));
                tabela.setBackground(new Color(245, 240, 255));
                tabela.setForeground(new Color(59, 35, 90));
                tabela.setSelectionBackground(new Color(216, 180, 254));

                tabela.getTableHeader().setFont(
                                new Font("SansSerif", Font.BOLD, 14));

                tabela.getTableHeader().setBackground(
                                new Color(109, 40, 217));

                tabela.getTableHeader().setForeground(Color.WHITE);

                tabela.setFillsViewportHeight(true);

                DefaultTableCellRenderer centralizar = new DefaultTableCellRenderer();

                centralizar.setHorizontalAlignment(SwingConstants.CENTER);

                for (int i = 0; i < tabela.getColumnCount(); i++) {
                        tabela.getColumnModel()
                                        .getColumn(i)
                                        .setCellRenderer(centralizar);
                }

                DefaultTableCellRenderer rendererSemCapa = new DefaultTableCellRenderer();

                rendererSemCapa.setHorizontalAlignment(
                                SwingConstants.CENTER);

                rendererSemCapa.setForeground(new Color(124, 108, 145));

                rendererSemCapa.setFont(
                                new Font("SansSerif", Font.ITALIC, 12));

                tabela.getColumnModel()
                                .getColumn(1)
                                .setCellRenderer(rendererSemCapa);

                DefaultTableCellRenderer centralizarCabecalho = new DefaultTableCellRenderer();

                centralizarCabecalho.setHorizontalAlignment(
                                SwingConstants.CENTER);

                centralizarCabecalho.setFont(
                                new Font("SansSerif", Font.BOLD, 14));

                centralizarCabecalho.setBackground(
                                new Color(109, 40, 217));

                centralizarCabecalho.setForeground(Color.WHITE);

                tabela.getTableHeader().setDefaultRenderer(
                                centralizarCabecalho);

                tabela.setRowHeight(85);

                tabela.getColumnModel().getColumn(1).setPreferredWidth(90);

                tabela.getColumnModel()
                    .getColumn(1)
                    .setCellRenderer(
                        new javax.swing.table.DefaultTableCellRenderer() {

                                @Override
                                public java.awt.Component getTableCellRendererComponent(
                                                                        JTable tabela,
                                                                        Object valor,
                                                                        boolean selecionada,
                                                                        boolean foco,
                                                                        int linha,
                                                                        int coluna) {

                                                                JLabel label = new JLabel();

                                                                label.setHorizontalAlignment(
                                                                                JLabel.CENTER);

                                                                label.setOpaque(true);

                                                                label.setBackground(
                                                                                selecionada
                                                                                                ? tabela.getSelectionBackground()
                                                                                                : tabela.getBackground());

                                                                if (valor instanceof ImageIcon) {
                                                                        label.setIcon((ImageIcon) valor);
                                                                } else {
                                                                        label.setText("Sem capa");
                                                                }

                                                                return label;
                                                        }
                                                });

                // Botões
                JButton atualizar = criarBotao("Atualizar listagem");
                JButton buscar = criarBotao("Buscar por ID");
                JButton mostrarTodos = criarBotao("Mostrar todos");
                JButton botaoConsultar = criarBotao("Consultar livros");
                JButton botaoBuscarTitulo = criarBotao("Buscar por título");

                JButton botaoCapa = criarBotao("Selecionar capa");

                // Pesquisa por título
                JPanel controles_busca = new JPanel(
                                new FlowLayout(FlowLayout.LEFT, 8, 8));

                controles_busca.setBackground(new Color(245, 240, 255));

                controles_busca.add(new JLabel("Título:"));
                controles_busca.add(campoTitulo);
                controles_busca.add(botaoBuscarTitulo);

                // Pesquisa por ID
                JPanel controles = new JPanel(
                                new FlowLayout(FlowLayout.LEFT, 8, 8));

                controles.setBackground(new Color(245, 240, 255));

                controles.add(new JLabel("ID do livro:"));
                controles.add(campoId);
                controles.add(buscar);
                controles.add(botaoCapa);

                // Ações
                JPanel acoes = new JPanel(
                                new FlowLayout(FlowLayout.LEFT, 8, 8));

                acoes.setBackground(new Color(245, 240, 255));

                acoes.add(atualizar);
                acoes.add(mostrarTodos);
                acoes.add(botaoConsultar);

                // Organização vertical
                JPanel vertical_align = new JPanel();

                vertical_align.setLayout(
                                new BoxLayout(vertical_align, BoxLayout.Y_AXIS));

                vertical_align.setBackground(new Color(245, 240, 255));

                vertical_align.add(controles_busca);
                vertical_align.add(controles);
                vertical_align.add(acoes);

                // Tabela
                JScrollPane painelTabela = new JScrollPane(tabela);

                painelTabela.setBackground(new Color(245, 240, 255));

                painelTabela.getViewport().setBackground(
                                new Color(245, 240, 255));

                // Rodapé
                status.setOpaque(true);
                status.setBackground(new Color(245, 240, 255));
                status.setForeground(new Color(59, 35, 90));

                add(vertical_align, BorderLayout.NORTH);
                add(painelTabela, BorderLayout.CENTER);
                add(status, BorderLayout.SOUTH);

                // Eventos dos botões
                atualizar.addActionListener(e -> carregarLivros());

                mostrarTodos.addActionListener(e -> carregarLivros());

                buscar.addActionListener(e -> buscarLivro());

                botaoConsultar.addActionListener(e -> {
                        new TelaLivros().setVisible(true);
                });

                botaoBuscarTitulo.addActionListener(
                                e -> buscarPorTitulo());

                botaoCapa.addActionListener(
                                e -> selecionarCapa());

                campoTitulo.addActionListener(
                                e -> buscarPorTitulo());

                campoId.addActionListener(
                                e -> buscarLivro());

                carregarLivros();
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

                botao.setFont(new Font("SansSerif", Font.BOLD, 12));
                botao.setBackground(new Color(109, 40, 217));
                botao.setForeground(Color.WHITE);

                botao.setFocusPainted(false);
                botao.setBorderPainted(false);
                botao.setContentAreaFilled(false);
                botao.setOpaque(false);

                botao.setCursor(new Cursor(Cursor.HAND_CURSOR));

                botao.setBorder(
                                BorderFactory.createEmptyBorder(9, 16, 9, 16));

                return botao;
        }

        // Carregar todos os livros
        private void carregarLivros() {

                modelo.setRowCount(0);

                List<Livro> livros = dao.listarLivros();

                for (Livro livro : livros) {
                        adicionarLinha(livro);
                }

                status.setText("Livros apresentados: " + livros.size());
        }

        // Adicionar livro na tabela
        private void adicionarLinha(Livro livro) {

                modelo.addRow(new Object[] {
                                livro.getId(),
                                carregarMiniatura(livro.getCapa()),
                                livro.getTitulo(),
                                livro.getAutor(),
                                livro.getAno()
                });
        }

        // Buscar livro pelo ID
        private void buscarLivro() {

                String texto = campoId.getText().trim();

                int id;

                try {

                        id = Integer.parseInt(texto);

                        if (id <= 0) {
                                throw new NumberFormatException();
                        }

                } catch (NumberFormatException ex) {

                        JOptionPane.showMessageDialog(
                                        this,
                                        "Informe um ID inteiro positivo.",
                                        "Entrada inválida",
                                        JOptionPane.WARNING_MESSAGE);

                        return;
                }

                Livro livro = dao.buscarLivroPorId(id);

                modelo.setRowCount(0);

                if (livro == null) {

                        status.setText(
                                        "Nenhum livro encontrado para o ID " + id);

                        JOptionPane.showMessageDialog(
                                        this,
                                        "Livro não encontrado.");

                } else {

                        adicionarLinha(livro);

                        status.setText(
                                        "Livro encontrado: " + livro.getTitulo());
                }

                campoId.setText("");
        }

        // Buscar livros pelo título
        private void buscarPorTitulo() {

                String titulo = campoTitulo.getText().trim();

                if (titulo.isEmpty()) {

                        JOptionPane.showMessageDialog(
                                        this,
                                        "Informe o título do livro.",
                                        "Campo obrigatório",
                                        JOptionPane.WARNING_MESSAGE);

                        return;
                }

                List<Livro> livros = dao.buscarLivrosPorTitulo(titulo);

                modelo.setRowCount(0);

                for (Livro livro : livros) {
                        adicionarLinha(livro);
                }

                status.setText(
                                "Livros encontrados: " + livros.size());

                if (livros.isEmpty()) {

                        JOptionPane.showMessageDialog(
                                        this,
                                        "Nenhum livro encontrado.");
                }

                campoTitulo.setText("");
        }

        // Selecionar e salvar capa do livro
        private void selecionarCapa() {

                int linha = tabela.getSelectedRow();

                if (linha == -1) {

                        JOptionPane.showMessageDialog(
                                        this,
                                        "Selecione um livro na tabela.");

                        return;
                }

                int linhaModelo = tabela.convertRowIndexToModel(linha);

                int id = (int) modelo.getValueAt(
                                linhaModelo, 0);

                JFileChooser seletor = new JFileChooser();

                seletor.setDialogTitle(
                                "Selecione a capa do livro");

                seletor.setFileFilter(
                                new javax.swing.filechooser.FileNameExtensionFilter(
                                                "Imagens JPG e PNG", "jpg", "jpeg", "png"));

                if (seletor.showOpenDialog(this) != JFileChooser.APPROVE_OPTION) {
                        return;
                }

                java.nio.file.Path destino = null;

                try {

                        destino = java.nio.file.Path.of(
                                        ImagemLivro.salvar(
                                                        seletor.getSelectedFile().toPath(),
                                                        id));

                        boolean atualizado = dao.atualizarCapa(
                                        id, destino.toString().replace('\\', '/'));

                        if (!atualizado) {

                                java.nio.file.Files.deleteIfExists(destino);

                                JOptionPane.showMessageDialog(
                                                this,
                                                "Não foi possível atualizar o livro.");

                                return;
                        }

                        carregarLivros();

                        JOptionPane.showMessageDialog(
                                        this,
                                        "Capa salva com sucesso!");

                } catch (Exception ex) {

                        if (destino != null) {

                                try {
                                        java.nio.file.Files.deleteIfExists(destino);

                                } catch (java.io.IOException ignorado) {
                                }
                        }

                        JOptionPane.showMessageDialog(
                                        this,
                                        "Erro ao salvar capa: " +
                                                        ex.getMessage());
                }
        }

        private ImageIcon carregarMiniatura(
                        String caminho) {

                if (caminho == null || caminho.isBlank()) {
                        return null;
                }

                java.io.File arquivo = new java.io.File(caminho);

                if (!arquivo.isFile()) {
                        return null;
                }

                try {

                        java.awt.image.BufferedImage imagem = javax.imageio.ImageIO.read(arquivo);

                        if (imagem == null) {
                                return null;
                        }

                        Image reduzida = imagem.getScaledInstance(
                                        55, 75, Image.SCALE_SMOOTH);

                        return new ImageIcon(reduzida);

                } catch (java.io.IOException e) {
                        return null;
                }
        }

        // Inicialização
        public static void main(String[] args) {

                SwingUtilities.invokeLater(() -> {
                        new TelaLivros().setVisible(true);
                });
        }
}
