"""
Clear Glass - Banco de Dados SQLite
Operações CRUD para todas as tabelas do sistema.
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "clearglass.db")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")
SEED_PATH = os.path.join(os.path.dirname(__file__), "seed.sql")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(with_seed=False):
    conn = get_connection()
    with open(SCHEMA_PATH, "r") as f:
        conn.executescript(f.read())
    if with_seed:
        with open(SEED_PATH, "r") as f:
            conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Banco de dados inicializado com sucesso.")


# ---------- CLIENTES ----------

def listar_clientes():
    with get_connection() as conn:
        return [dict(r) for r in conn.execute("SELECT * FROM clientes").fetchall()]


def buscar_cliente(cliente_id):
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM clientes WHERE id = ?", (cliente_id,)).fetchone()
        return dict(row) if row else None


def criar_cliente(nome, email, telefone=None, empresa=None):
    with get_connection() as conn:
        cur = conn.execute(
            "INSERT INTO clientes (nome, email, telefone, empresa) VALUES (?, ?, ?, ?)",
            (nome, email, telefone, empresa),
        )
        conn.commit()
        return cur.lastrowid


def atualizar_cliente(cliente_id, **campos):
    allowed = {"nome", "email", "telefone", "empresa"}
    updates = {k: v for k, v in campos.items() if k in allowed}
    if not updates:
        return
    set_clause = ", ".join(f"{k} = ?" for k in updates)
    with get_connection() as conn:
        conn.execute(
            f"UPDATE clientes SET {set_clause} WHERE id = ?",
            (*updates.values(), cliente_id),
        )
        conn.commit()


def deletar_cliente(cliente_id):
    with get_connection() as conn:
        conn.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
        conn.commit()


# ---------- SERVIÇOS ----------

def listar_servicos(apenas_disponiveis=False):
    query = "SELECT * FROM servicos"
    if apenas_disponiveis:
        query += " WHERE disponivel = 1"
    with get_connection() as conn:
        return [dict(r) for r in conn.execute(query).fetchall()]


def criar_servico(nome, descricao, preco, disponivel=True):
    with get_connection() as conn:
        cur = conn.execute(
            "INSERT INTO servicos (nome, descricao, preco, disponivel) VALUES (?, ?, ?, ?)",
            (nome, descricao, preco, int(disponivel)),
        )
        conn.commit()
        return cur.lastrowid


# ---------- DEPOIMENTOS ----------

def listar_depoimentos():
    query = """
        SELECT d.id, c.nome AS cliente, d.texto, d.avaliacao, d.data
        FROM depoimentos d
        JOIN clientes c ON c.id = d.cliente_id
        ORDER BY d.data DESC
    """
    with get_connection() as conn:
        return [dict(r) for r in conn.execute(query).fetchall()]


def criar_depoimento(cliente_id, texto, avaliacao):
    with get_connection() as conn:
        cur = conn.execute(
            "INSERT INTO depoimentos (cliente_id, texto, avaliacao) VALUES (?, ?, ?)",
            (cliente_id, texto, avaliacao),
        )
        conn.commit()
        return cur.lastrowid


# ---------- CONTATOS ----------

def listar_contatos():
    with get_connection() as conn:
        return [dict(r) for r in conn.execute("SELECT * FROM contatos ORDER BY data_envio DESC").fetchall()]


def registrar_contato(nome, email, mensagem):
    with get_connection() as conn:
        cur = conn.execute(
            "INSERT INTO contatos (nome, email, mensagem) VALUES (?, ?, ?)",
            (nome, email, mensagem),
        )
        conn.commit()
        return cur.lastrowid


# ---------- ESCRITÓRIOS ----------

def listar_escritorios():
    with get_connection() as conn:
        return [dict(r) for r in conn.execute("SELECT * FROM escritorios").fetchall()]


# ---------- FUNCIONÁRIOS ----------

def listar_funcionarios():
    with get_connection() as conn:
        return [dict(r) for r in conn.execute("SELECT * FROM funcionarios").fetchall()]


def buscar_funcionario(funcionario_id):
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM funcionarios WHERE id = ?", (funcionario_id,)).fetchone()
        return dict(row) if row else None


# ---------- DEMO ----------

if __name__ == "__main__":
    init_db(with_seed=True)

    print("\n=== CLIENTES ===")
    for c in listar_clientes():
        print(f"  [{c['id']}] {c['nome']} | {c['email']} | {c['empresa'] or '-'}")

    print("\n=== SERVIÇOS DISPONÍVEIS ===")
    for s in listar_servicos(apenas_disponiveis=True):
        print(f"  [{s['id']}] {s['nome']} - R$ {s['preco']:.2f}")

    print("\n=== DEPOIMENTOS ===")
    for d in listar_depoimentos():
        print(f"  {d['cliente']} ({d['avaliacao']}★): {d['texto'][:60]}...")

    print("\n=== ESCRITÓRIOS ===")
    for e in listar_escritorios():
        print(f"  {e['cidade']}, {e['pais']} | {e['endereco']}")

    print("\n=== FUNCIONÁRIOS ===")
    for f in listar_funcionarios():
        print(f"  {f['nome']} | {f['cargo']} | {f['departamento']}")

    print("\n=== CONTATOS RECEBIDOS ===")
    for ct in listar_contatos():
        print(f"  {ct['nome']} <{ct['email']}> em {ct['data_envio']}")
