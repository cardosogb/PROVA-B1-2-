-- Clear Glass - Schema do Banco de Dados

CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    telefone TEXT,
    empresa TEXT,
    data_cadastro TEXT DEFAULT (date('now'))
);

CREATE TABLE IF NOT EXISTS servicos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    preco REAL NOT NULL,
    disponivel INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS depoimentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    texto TEXT NOT NULL,
    avaliacao INTEGER CHECK(avaliacao BETWEEN 1 AND 5),
    data TEXT DEFAULT (date('now')),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

CREATE TABLE IF NOT EXISTS contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    mensagem TEXT NOT NULL,
    data_envio TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS escritorios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cidade TEXT NOT NULL,
    estado TEXT,
    pais TEXT NOT NULL,
    endereco TEXT
);

CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    departamento TEXT,
    email TEXT UNIQUE NOT NULL
);
