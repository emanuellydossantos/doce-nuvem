
import os
import sqlite3
from pathlib import Path
from functools import wraps

from flask import (
    Flask, render_template, request,
    redirect, url_for, session, flash
)
from werkzeug.security import check_password_hash

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "docenuvem.db"

app = Flask(__name__)



app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "chave-apenas-para-desenvolvimento-local"
)

app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"


def conectar_banco():
    conexao = sqlite3.connect(DATABASE)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela_usuarios():
    with conectar_banco() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                senha_hash TEXT NOT NULL,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


def criar_tabelas_pedidos():
    with conectar_banco() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                total REAL NOT NULL,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
            )
        """)

        conexao.execute("""
            CREATE TABLE IF NOT EXISTS itens_pedido (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pedido_id INTEGER NOT NULL,
                produto_id TEXT NOT NULL,
                nome_produto TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                preco_unitario REAL NOT NULL,
                subtotal REAL NOT NULL,
                FOREIGN KEY (pedido_id) REFERENCES pedidos(id)
            )
        """)


def login_obrigatorio(funcao):
    @wraps(funcao)
    def verificar_login(*args, **kwargs):
        if "usuario_id" not in session:
            return redirect(url_for("login"))

        return funcao(*args, **kwargs)

    return verificar_login



@app.route("/", methods=["GET"])
def inicio():
    return render_template("inicio.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")

        with conectar_banco() as conexao:
            usuario = conexao.execute(
                "SELECT id, email, senha_hash "
                "FROM usuarios WHERE email = ?",
                (email,)
            ).fetchone()

        if usuario and check_password_hash(
            usuario["senha_hash"], senha
        ):
            session.clear()
            session["usuario_id"] = usuario["id"]
            session["usuario_email"] = usuario["email"]

            return redirect(url_for("painel"))

        flash("E-mail ou senha inválidos.", "erro")

    return render_template("login.html")


@app.route("/painel")
@login_obrigatorio
def painel():
    return render_template(
        "login.html",
        conectado=True,
        email=session.get("usuario_email")
    )


@app.route("/sair", methods=["POST"])
def sair():
    session.clear()
    return redirect(url_for("login"))


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")
        confirmacao = request.form.get("confirmacao", "")

        if not email or "@" not in email:
            flash("Digite um e-mail válido.", "erro")
            return render_template("cadastro.html")

        if len(senha) < 8:
            flash("A senha precisa ter pelo menos 8 caracteres.", "erro")
            return render_template("cadastro.html")

        if senha != confirmacao:
            flash("As senhas não são iguais.", "erro")
            return render_template("cadastro.html")

        from werkzeug.security import generate_password_hash

        senha_hash = generate_password_hash(senha)

        try:
            with conectar_banco() as conexao:
                conexao.execute(
                    "INSERT INTO usuarios (email, senha_hash) VALUES (?, ?)",
                    (email, senha_hash)
                )

            flash("Conta criada! Agora você pode entrar.", "sucesso")
            return redirect(url_for("login"))

        except sqlite3.IntegrityError:
            flash("Este e-mail já está cadastrado.", "erro")

    return render_template("cadastro.html")


criar_tabela_usuarios()
criar_tabelas_pedidos()

# Produtos disponíveis na loja
PRODUTOS = {
    "baunilha": {
        "nome": "Cupcake de Baunilha",
        "preco": 6.00
    },
    "chocolate": {
        "nome": "Cupcake de Chocolate",
        "preco": 6.00
    },
    "morango": {
        "nome": "Cupcake de Morango",
        "preco": 7.00
    },
    "limao-siciliano": {
        "nome": "Cupcake de Limão Siciliano",
        "preco": 7.00
    },
    "red-velvet": {
        "nome": "Cupcake Red Velvet",
        "preco": 8.00
    }
}


# Adicionar um cupcake ao carrinho
@app.route("/adicionar/<produto_id>", methods=["POST"])
@login_obrigatorio
def adicionar_carrinho(produto_id):
    if produto_id not in PRODUTOS:
        flash("Produto não encontrado.", "erro")
        return redirect(url_for("inicio"))

    carrinho = session.get("carrinho", {})
    carrinho[produto_id] = carrinho.get(produto_id, 0) + 1

    session["carrinho"] = carrinho

    flash("Cupcake adicionado ao carrinho!", "sucesso")
    return redirect(url_for("carrinho"))


# Exibir o carrinho
@app.route("/carrinho")
@login_obrigatorio
def carrinho():
    itens = []
    total = 0

    produtos_carrinho = session.get("carrinho", {})

    for produto_id, quantidade in produtos_carrinho.items():
        if produto_id not in PRODUTOS:
            continue

        produto = PRODUTOS[produto_id]
        subtotal = produto["preco"] * quantidade

        itens.append({
            "id": produto_id,
            "nome": produto["nome"],
            "preco": produto["preco"],
            "quantidade": quantidade,
            "subtotal": subtotal
        })

        total += subtotal

    return render_template(
        "carrinho.html",
        itens=itens,
        total=total
    )


# Remover um cupcake do carrinho
@app.route("/remover/<produto_id>", methods=["POST"])
@login_obrigatorio
def remover_carrinho(produto_id):
    carrinho = session.get("carrinho", {})

    if produto_id in carrinho:
        del carrinho[produto_id]
        session["carrinho"] = carrinho
        flash("Item removido do carrinho.", "sucesso")

    return redirect(url_for("carrinho"))


@app.route("/finalizar-pedido", methods=["POST"])
@login_obrigatorio
def finalizar_pedido():
    produtos_carrinho = session.get("carrinho", {})

    if not produtos_carrinho:
        flash("Seu carrinho está vazio.", "erro")
        return redirect(url_for("carrinho"))

    itens = []
    total = 0

    for produto_id, quantidade in produtos_carrinho.items():
        if produto_id not in PRODUTOS:
            continue

        produto = PRODUTOS[produto_id]
        subtotal = produto["preco"] * quantidade

        itens.append({
            "id": produto_id,
            "nome": produto["nome"],
            "quantidade": quantidade,
            "preco": produto["preco"],
            "subtotal": subtotal
        })

        total += subtotal

    if not itens:
        flash("Não há produtos válidos no carrinho.", "erro")
        return redirect(url_for("carrinho"))

    with conectar_banco() as conexao:
        cursor = conexao.execute(
            "INSERT INTO pedidos (usuario_id, total) VALUES (?, ?)",
            (session["usuario_id"], total)
        )

        pedido_id = cursor.lastrowid

        for item in itens:
            conexao.execute("""
                INSERT INTO itens_pedido (
                    pedido_id, produto_id, nome_produto,
                    quantidade, preco_unitario, subtotal
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                pedido_id,
                item["id"],
                item["nome"],
                item["quantidade"],
                item["preco"],
                item["subtotal"]
            ))

    session.pop("carrinho", None)

    return render_template(
        "pedido_confirmado.html",
        pedido_id=pedido_id,
        itens=itens,
        total=total
    )


@app.route("/meus-pedidos")
@login_obrigatorio
def meus_pedidos():
    with conectar_banco() as conexao:
        pedidos = conexao.execute("""
            SELECT id, total, criado_em
            FROM pedidos
            WHERE usuario_id = ?
            ORDER BY id DESC
        """, (session["usuario_id"],)).fetchall()

        pedidos_com_itens = []

        for pedido in pedidos:
            itens = conexao.execute("""
                SELECT nome_produto, quantidade,
                       preco_unitario, subtotal
                FROM itens_pedido
                WHERE pedido_id = ?
                ORDER BY id
            """, (pedido["id"],)).fetchall()

            pedidos_com_itens.append({
                "id": pedido["id"],
                "total": pedido["total"],
                "criado_em": pedido["criado_em"],
                "itens": itens
            })

    return render_template(
        "meus_pedidos.html",
        pedidos=pedidos_com_itens
    )




if __name__ == "__main__":
    app.run(debug=True)