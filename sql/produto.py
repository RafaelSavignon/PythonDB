SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS produto(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT NOT NULL,
        estoque INTEGER NOT NULL,
        preco FLOAT NOT NULL
    )
"""

SQL_INSERIR = """
    INSERT INTO produto(nome, descricao, estoque, preco)
    VALUES (?, ?, ?, ?)
"""

SQL_OBTER_TODOS = """
    SELECT id, nome, descricao, estoque, preco
    FROM produto
    ORDER BY nome
"""

SQL_ALTERAR = """
    UPDATE produto
    SET nome=?, descricao=?, estoque=?, preco=?
    WHERE id=?
"""

SQL_DELETAR = """
    DELETE FROM produto
    WHERE id=?
"""

SQL_OBTER_UM = """
    SELECT id, nome, descricao, estoque, preco
    FROM produto
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*) FROM produto
"""