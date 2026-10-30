
import sqlite3
from pathlib import Path
from getpass import getpass
from werkzeug.security import generate_password_hash

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "docenuvem.db"


def criar_tabela():
    with sqlite3.connect(DATABASE) as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                senha_hash TEXT NOT NULL,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


def cadastrar_usuario():
    email = input("E-mail do usuário: ").strip().lower()
    senha = getpass("Crie uma senha: ")
    confirmacao = getpass("Digite a senha novamente: ")

    if not email or "@" not in email:
        print("Digite um e-mail válido.")
        return

    if len(senha) < 8:
        print("A senha precisa ter pelo menos 8 caracteres.")
        return

    if senha != confirmacao:
        print("As senhas não são iguais.")
        return

    senha_hash = generate_password_hash(senha)

    try:
        with sqlite3.connect(DATABASE) as conexao:
            conexao.execute(
                "INSERT INTO usuarios (email, senha_hash) "
                "VALUES (?, ?)",
                (email, senha_hash)
            )

        print("Usuário criado com sucesso!")

    except sqlite3.IntegrityError:
        print("Esse e-mail já está cadastrado.")


if __name__ == "__main__":
    criar_tabela_usuarios = criar_tabela
    criar_tabela_usuarios()
    cadastrar_usuario()
