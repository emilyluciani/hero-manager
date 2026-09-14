# app.py
from flask import Flask, render_template, request, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from config import get_db
from mysql.connector.errors import IntegrityError
from models import (
    buscar_usuario_por_email, criar_usuario, buscar_usuario,
    buscar_herois_por_nome_ou_id, atualizar_usuario, listar_herois,
    buscar_heroi, contar_equipe, adicionar_heroi_usuario,
    listar_equipe, listar_base, atualizar_local, remover_heroi_usuario
)
import os
app = Flask(__name__)
app.secret_key = "chave_super_secreta"

UPLOAD_FOLDER = 'static/img/usuarios'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# -----------------------------
# LOGIN
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def login():
    # Se já estiver logado → manda para Home
    if "usuario_id" in session:
        return redirect("/home")

    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        usuario = buscar_usuario_por_email(email)
        if not usuario or not check_password_hash(usuario["senha"], senha):
            return render_template("login.html", erro="Email ou senha inválidos")

        session["usuario_id"] = usuario["id"]
        return redirect("/home")

    # GET → apenas carrega a página
    return render_template("login.html")

# -----------------------------
# CADASTRO
# -----------------------------
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if "usuario_id" in session:
        return redirect("/home")

    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        cpf = request.form["cpf"]
        senha = generate_password_hash(request.form["senha"])
        planeta = request.form["planeta"]

        try:
            criar_usuario(nome, email, cpf, senha, planeta)
            flash("Conta criada com sucesso! Faça login.")
            return redirect("/")

        except IntegrityError:
            flash("Email ou CPF já cadastrado!")
            return redirect("/cadastro")

    return render_template("cadastro.html")

# -----------------------------
# HOME
# -----------------------------
@app.route("/home")
def home():
    if "usuario_id" not in session:
        return redirect("/")
    
    usuario = buscar_usuario(session["usuario_id"])
    return render_template("home.html", user=usuario)

@app.get("/buscar")
def buscar():
    termo = request.args.get("q", "")
    if termo.strip() == "":
        return redirect("/herois")
    resultados = buscar_herois_por_nome_ou_id(termo)
    return render_template("resultados.html", herois=resultados, termo=termo)

@app.get("/autocomplete")
def autocomplete():
    termo = request.args.get("q", "").strip()
    if termo == "":
        return []
    resultados = buscar_herois_por_nome_ou_id(termo)
    nomes = [h["nome"] for h in resultados]
    return nomes

# -----------------------------
# PERFIL
# -----------------------------
@app.route("/perfil")
def perfil():
    if "usuario_id" not in session:
        return redirect("/")
    usuario = buscar_usuario(session["usuario_id"])
    equipe = listar_equipe(session["usuario_id"])
    return render_template("perfil.html", user=usuario, equipe=equipe)

@app.post("/perfil")
def perfil_post():
    id = session["usuario_id"]
    nome = request.form["nome"]
    email = request.form["email"]
    planeta = request.form["planeta"]
    atualizar_usuario(id, nome, email, planeta)
    return redirect("/perfil")

@app.post("/perfil/upload_foto")
def perfil_upload_foto():
    if "usuario_id" not in session:
        return redirect("/")

    if "foto" not in request.files:
        flash("Nenhum arquivo selecionado")
        return redirect("/perfil")

    file = request.files["foto"]

    if file.filename == "":
        flash("Nenhum arquivo selecionado")
        return redirect("/perfil")

    if file and allowed_file(file.filename):
        # Mantém a extensão original
        ext = file.filename.rsplit('.', 1)[1].lower()
        filename = f"user_{session['usuario_id']}.{ext}"
        caminho = os.path.join(UPLOAD_FOLDER, filename)

        # Cria a pasta se não existir
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        file.save(caminho)

        # Atualiza o banco de dados
        con = get_db()
        cur = con.cursor()
        cur.execute("UPDATE usuario SET foto=%s WHERE id=%s", (filename, session["usuario_id"]))
        con.commit()
        cur.close()

        flash("Foto enviada com sucesso!")
        return redirect("/perfil")
    else:
        flash("Formato inválido. Use png, jpg, jpeg ou gif.")
        return redirect("/perfil")

# -----------------------------
# LISTAR HERÓIS
# -----------------------------
@app.get("/herois")
def herois():
    dados = listar_herois()
    return render_template("herois.html", herois=dados)

# -----------------------------
# DETALHES
# -----------------------------
@app.get("/heroi/<int:id>")
def heroi(id):
    h = buscar_heroi(id)
    return render_template("heroi_detalhes.html", h=h)

# -----------------------------
# ADICIONAR HERÓI
# -----------------------------
@app.post("/adicionar")
def adicionar():
    usuario_id = session["usuario_id"]
    heroi_id = request.form["heroi_id"]

    total = contar_equipe(usuario_id)
    local = "equipe" if total < 5 else "base"

    adicionar_heroi_usuario(usuario_id, heroi_id, local)
    return redirect("/equipe")


# -----------------------------
# EQUIPE / BASE
# -----------------------------
@app.get("/equipe")
def equipe():
    usuario_id = session["usuario_id"]
    equipe = listar_equipe(usuario_id)
    base = listar_base(usuario_id)
    return render_template("equipe.html", equipe=equipe, base=base)

# -----------------------------
# TROCAR EQUIPE <-> BASE
# -----------------------------
@app.post("/trocar")
def trocar():
    uh_id = request.form["uh_id"]
    local = request.form["local"]
    usuario_id = session["usuario_id"]

    con = get_db()
    cur = con.cursor(dictionary=True)

    cur.execute("""
        SELECT COUNT(*) AS total
        FROM usuario_heroi
        WHERE usuario_id = %s AND local = 'equipe'
    """, (usuario_id,))
    qtd_equipe = cur.fetchone()["total"]

    if local == "equipe" and qtd_equipe >= 5:
        flash("Sua equipe já tem 5 heróis! Mova alguém para a base antes.")
        return redirect("/equipe")

    cur.execute("UPDATE usuario_heroi SET local = %s WHERE id = %s", (local, uh_id))
    con.commit()
    return redirect("/equipe")

# -----------------------------
# REMOVER
# -----------------------------
@app.post("/remover")
def remover():
    uh_id = request.form["uh_id"]
    remover_heroi_usuario(uh_id)
    return redirect("/equipe")

# -----------------------------
# LOGOUT
# -----------------------------
@app.get("/logout")
def logout():
    session.clear()
    return redirect("/")

# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)