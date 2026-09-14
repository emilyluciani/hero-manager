# models.py
from config import get_db

# ---------------------------
# USUÁRIO
# ---------------------------
def buscar_usuario_por_email(email):
    con = get_db()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM usuario WHERE email=%s", (email,))
    return cur.fetchone()

def criar_usuario(nome, email, cpf, senha, planeta):
    con = get_db()
    cur = con.cursor()
    cur.execute("""
        INSERT INTO usuario (nome, email, cpf, senha, planeta)
        VALUES (%s, %s, %s, %s, %s)
    """, (nome, email, cpf, senha, planeta))
    con.commit()

def buscar_usuario(id):
    con = get_db()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM usuario WHERE id=%s", (id,))
    return cur.fetchone()

def atualizar_usuario(id, nome, email, planeta):
    con = get_db()
    cur = con.cursor()
    cur.execute("""
        UPDATE usuario SET nome=%s, email=%s, planeta=%s
        WHERE id=%s
    """, (nome, email, planeta, id))
    con.commit()

# ---------------------------
# HERÓIS
# ---------------------------
def listar_herois():
    con = get_db()
    cur = con.cursor(dictionary=True)
    cur.execute("""
        SELECT h.*, c.nome AS classe
        FROM heroi h
        JOIN classe c ON c.id = h.classe_id
    """)
    return cur.fetchall()

def buscar_heroi(id):
    con = get_db()
    cur = con.cursor(dictionary=True)
    cur.execute("""
        SELECT h.*, c.nome AS classe
        FROM heroi h
        JOIN classe c ON c.id = h.classe_id
        WHERE h.id = %s
    """, (id,))
    return cur.fetchone()

def buscar_herois_por_nome_ou_id(termo):
    con = get_db()
    cur = con.cursor(dictionary=True)

    # Se for número → busca por ID também
    try:
        numero = int(termo)
    except:
        numero = None

    if numero:
        cur.execute("""
            SELECT h.*, c.nome AS classe
            FROM heroi h
            JOIN classe c ON c.id = h.classe_id
            WHERE h.id = %s OR h.nome LIKE %s
        """, (numero, f"%{termo}%"))
    else:
        cur.execute("""
            SELECT h.*, c.nome AS classe
            FROM heroi h
            JOIN classe c ON c.id = h.classe_id
            WHERE h.nome LIKE %s
        """, (f"%{termo}%",))

    return cur.fetchall()

# ---------------------------
# EQUIPE / BASE
# ---------------------------
def contar_equipe(usuario_id):
    con = get_db()
    cur = con.cursor(dictionary=True)
    cur.execute("""
        SELECT COUNT(*) AS total
        FROM usuario_heroi
        WHERE usuario_id=%s AND local='equipe'
    """, (usuario_id,))
    return cur.fetchone()["total"]

def adicionar_heroi_usuario(usuario_id, heroi_id, local):
    con = get_db()
    cur = con.cursor()

    # segurança: impedir adicionar na equipe se já tiver 5
    if local == "equipe":
        cur.execute("""
            SELECT COUNT(*) FROM usuario_heroi
            WHERE usuario_id=%s AND local='equipe'
        """, (usuario_id,))
        total = cur.fetchone()[0]

        if total >= 5:
            local = "base"

    cur.execute("""
        INSERT INTO usuario_heroi (usuario_id, heroi_id, local)
        VALUES (%s, %s, %s)
    """, (usuario_id, heroi_id, local))

    con.commit()
    cur.close()

def listar_equipe(usuario_id):
    con = get_db()
    cur = con.cursor(dictionary=True)
    cur.execute("""
        SELECT uh.id AS uh_id, h.*, c.nome AS classe
        FROM usuario_heroi uh
        JOIN heroi h ON h.id = uh.heroi_id
        JOIN classe c ON c.id = h.classe_id
        WHERE uh.usuario_id=%s AND uh.local='equipe'
    """, (usuario_id,))
    return cur.fetchall()

def listar_base(usuario_id):
    con = get_db()
    cur = con.cursor(dictionary=True)
    cur.execute("""
        SELECT uh.id AS uh_id, h.*, c.nome AS classe
        FROM usuario_heroi uh
        JOIN heroi h ON h.id = uh.heroi_id
        JOIN classe c ON c.id = h.classe_id
        WHERE uh.usuario_id=%s AND uh.local='base'
    """, (usuario_id,))
    return cur.fetchall()

def atualizar_local(uh_id, local):
    con = get_db()
    cur = con.cursor()
    cur.execute("UPDATE usuario_heroi SET local=%s WHERE id=%s", (local, uh_id))
    con.commit()

def remover_heroi_usuario(uh_id):
    con = get_db()
    cur = con.cursor()
    cur.execute("DELETE FROM usuario_heroi WHERE id=%s", (uh_id,))
    con.commit()