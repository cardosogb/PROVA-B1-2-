-- Clear Glass - Dados Iniciais

INSERT INTO funcionarios (nome, cargo, departamento, email) VALUES
    ('Alanah Rodriguez', 'CEO', 'Diretoria', 'alanah.rodriguez@clearglass.com'),
    ('Carlos Mendes', 'Gerente de Vendas', 'Comercial', 'carlos.mendes@clearglass.com'),
    ('Fernanda Lima', 'Engenheira de Produto', 'Produção', 'fernanda.lima@clearglass.com'),
    ('Rafael Souza', 'Analista Financeiro', 'Financeiro', 'rafael.souza@clearglass.com'),
    ('Priya Nair', 'Designer', 'Marketing', 'priya.nair@clearglass.com');

INSERT INTO escritorios (cidade, estado, pais, endereco) VALUES
    ('São Paulo', 'SP', 'Brasil', 'Av. Paulista, 1000'),
    ('Rio de Janeiro', 'RJ', 'Brasil', 'Rua da Assembleia, 200'),
    ('Lisboa', NULL, 'Portugal', 'Avenida da Liberdade, 50'),
    ('Miami', 'FL', 'EUA', '1200 Brickell Ave');

INSERT INTO servicos (nome, descricao, preco, disponivel) VALUES
    ('Vidro Temperado', 'Vidro com resistência a arranhões melhorada em 60%', 350.00, 1),
    ('Vidro Laminado', 'Alta segurança para ambientes comerciais', 480.00, 1),
    ('Consultoria de Projeto', 'Avaliação e especificação de vidros para obras', 200.00, 1),
    ('Manutenção Preventiva', 'Inspeção e cuidados periódicos', 150.00, 1),
    ('Vidro Acústico', 'Isolamento sonoro para ambientes internos', 620.00, 0);

INSERT INTO clientes (nome, email, telefone, empresa, data_cadastro) VALUES
    ('João Pereira', 'joao.pereira@construtora.com', '11999990001', 'Construtora Alpha', '2025-01-10'),
    ('Maria Silva', 'maria.silva@arqdesign.com', '21999990002', 'Arq & Design', '2025-02-15'),
    ('Roberto Alves', 'roberto.alves@gmail.com', '11988880003', NULL, '2025-03-01'),
    ('Lucia Fernandes', 'lucia@vidrosul.com.br', '47977770004', 'VidroSul', '2025-03-20'),
    ('Thomas Green', 'thomas.green@buildcorp.us', NULL, 'BuildCorp USA', '2025-04-05');

INSERT INTO depoimentos (cliente_id, texto, avaliacao, data) VALUES
    (1, 'Produto de altíssima qualidade. Redução de manutenção notável desde que adotamos a Clear Glass.', 5, '2025-04-01'),
    (2, 'Equipe muito profissional. O vidro laminado superou as expectativas do projeto.', 5, '2025-04-10'),
    (3, 'Bom custo-benefício. Atendimento rápido e entrega no prazo.', 4, '2025-04-18'),
    (4, 'Parceria excelente. Recomendo a linha de vidro temperado para qualquer obra.', 5, '2025-04-25');

INSERT INTO contatos (nome, email, mensagem, data_envio) VALUES
    ('Ana Costa', 'ana.costa@email.com', 'Gostaria de um orçamento para 200m² de vidro temperado.', '2025-05-01 09:00:00'),
    ('Pedro Rocha', 'pedro.rocha@email.com', 'Tenho interesse na consultoria de projeto.', '2025-05-03 14:30:00');
