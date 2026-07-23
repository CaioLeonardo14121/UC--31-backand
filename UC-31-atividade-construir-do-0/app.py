from flask import Flask, render_template_string, session
app = Flask(__name__)
app.secret_key = "Lobato123"

@app.route("/")
def inicio():
    return render_template("cantinho.html")

@app.route('/cantinho')
@login_necessario
def cantinho():
    nome = session.get('usuario_nome')

    # Contador de visitas (bônus)
    visitas = session.get('visitas_cantinho', 0)
    visitas += 1
    session['visitas_cantinho'] = visitas

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Meu Cantinho</title>
    </head>
    <body>
        <h1>Meu Cantinho</h1>

        <p>Olá, {{ nome }}! Este é o seu cantinho secreto.</p>

        <h2>Minhas informações</h2>

        <p><strong>Cor favorita:</strong> Azul</p>
        <p><strong>Linguagem favorita:</strong> Python</p>
        <p><strong>Frase:</strong> Nunca pare de aprender!</p>

        <p>Você visitou esse cantinho {{ visitas }} vez(es) hoje.</p>

        <a href="{{ url_for('painel') }}">← Voltar ao painel</a>
    </body>
    </html>
    """, nome=nome, visitas=visitas)