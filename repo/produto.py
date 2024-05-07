import sqlite3
from typing import List, Optional
from model.produto import Produto
from sql.produto import *
from util.database import obter_conexao


class ProdutoRepo():

    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @classmethod
    def inserir(cls, produto: Produto) -> Optional[Produto]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_INSERIR, (
                    produto.nome,
                    produto.descricao,
                    produto.estoque,
                    produto.preco
                ))
                if cursor.rowcount > 0:
                    produto.id = cursor.lastrowid
                    return produto
        except sqlite3.Error as ex:
            print(ex)
            return None
        
    @classmethod
    def obter_todos(cls) -> List[Produto]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(SQL_OBTER_TODOS).fetchall()
                produtos = [Produto(*t) for t in tuplas]
                return produtos
        except sqlite3.Error as ex:
            print(ex)
            return None
        
    @classmethod
    def alterar(cls, produto: Produto) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_ALTERAR, (
                    produto.nome,
                    produto.descricao,
                    produto.estoque,
                    produto.preco,
                    produto.id
                ))
                if cursor.rowcount > 0:
                    return True
        except sqlite3.Error as ex:
            print(ex)
            return False
        
    @classmethod
    def excluir(cls, id: int) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_DELETAR, (id,))
                return (cursor.rowcount > 0)
        except sqlite3.Error as ex:
            print(ex)
            return False
        
    @classmethod
    def obter_um(cls, id: int) -> Optional[Produto]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_UM, (id,)).fetchone()
                produto = Produto(*tupla)
                return produto
        except sqlite3.Error as ex:
            print(ex)
            return None
        
    @classmethod
    def quantidade(cls) -> Optional[int]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_QUANTIDADE).fetchone()
                return int(tupla[0])
        except sqlite3.Error as ex:
            print(ex)
            return None