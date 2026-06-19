from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "missao_espacial"

perguntas = [
    {
        "pergunta": "Qual planeta é conhecido como Planeta Vermelho?",
        "opcoes": ["Terra", "Marte", "Júpiter", "Vênus"],
        "resposta": "Marte"
    },
    {
        "pergunta": "Qual é o maior planeta do Sistema Solar?",
        "opcoes": ["Saturno", "Marte", "Júpiter", "Netuno"],
        "resposta": "Júpiter"
    },
    {
        "pergunta": "Qual estrela está no centro do Sistema Solar?",
        "opcoes": ["Lua", "Sol", "Sirius", "Marte"],
        "resposta": "Sol"
    },
    {
        "pergunta": "Quantos planetas existem no Sistema Solar?",
        "opcoes": ["7", "8", "9", "10"],
        "resposta": "8"
    },
    {
        "pergunta": "Quem foi o primeiro ser humano a pisar na Lua?",
        "opcoes": [
            "Yuri Gagarin",
            "Buzz Aldrin",
            "Neil Armstrong",
            "Alan Shepard"
        ],
        "resposta": "Neil Armstrong"
    },
    {
        "pergunta": "Qual planeta é famoso por seus anéis?",
        "opcoes": ["Mercúrio", "Marte", "Saturno", "Vênus"],
        "resposta": "Saturno"
    },
    {
        "pergunta": "Qual é o nome da galáxia onde está localizado o Sistema Solar?",
        "opcoes": [
            "Andrômeda",
            "Via Láctea",
            "Órion",
            "Galáxia do Triângulo"
        ],
        "resposta": "Via Láctea"
    },
    {
        "pergunta": "Qual é o satélite natural da Terra?",
        "opcoes": ["Sol", "Lua", "Marte", "Europa"],
        "resposta": "Lua"
    }
]
@app.route("/")
def inicio():
    return render_template("login.html")

@app.route("/entrar", methods=["POST"])
def entrar():
    nome = request.form["nome"]

    session["nome"] = nome
    session["indice"] = 0
    session["pontos"] = 0

    return redirect(url_for("quiz"))

@app.route("/quiz")
def quiz():

    indice = session.get("indice", 0)

    if indice >= len(perguntas):
        return redirect(url_for("resultado"))

    return render_template(
        "quiz.html",
        pergunta=perguntas[indice],
        numero=indice + 1,
        total=len(perguntas)
    )

@app.route("/responder", methods=["POST"])
def responder():

    resposta = request.form["resposta"]
    indice = session["indice"]

    if resposta == perguntas[indice]["resposta"]:
        session["pontos"] += 1

    session["indice"] += 1

    return redirect(url_for("quiz"))

@app.route("/resultado")
def resultado():

    pontos = session["pontos"]
    nome = session["nome"]

    if pontos == 5:
        classificacao = "Comandante Galáctico"
    elif pontos >= 3:
        classificacao = "Astronauta Experiente"
    else:
        classificacao = "Você é um Betinha Espacial"

    return render_template(
        "resultado.html",
        pontos=pontos,
        nome=nome,
        classificacao=classificacao
    )

if __name__ == "__main__":
    app.run(debug=True)