from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastro", methods=["POST"])
def cadastro():

    nome = request.form["nome"].strip().title()
    email = request.form["email"].strip().lower()
    telefone = request.form["telefone"].strip()
    cpf = request.form["cpf"].strip()
    cidade = request.form["cidade"].strip().title()
    estado = request.form["estado"].strip().upper()
    curso = request.form["curso"].strip()
    idade = request.form["idade"].strip()
    senha = request.form["senha"].strip()

    if len(nome) < 8:
        return "Nome inválido."

    if "@" not in email or ".com" not in email:
        return "E-mail inválido."

    if telefone == "":
        return "Telefone inválido."

    if cpf == "":
        return "CPF inválido."

    if len(cidade) < 3:
        return "Cidade inválida."

    if len(estado) != 2:
        return "Estado inválido."

    if curso == "":
        return "Curso inválido."

    if not idade.isdigit() or int(idade) < 16:
        return "Idade inválida."

    if len(senha) < 8:
        return "Senha muito fraca."

    return f"""
    <h2>Cadastro realizado com sucesso!</h2>

    <p><b>Nome:</b> {nome}</p>
    <p><b>E-mail:</b> {email}</p>
    <p><b>Telefone:</b> {telefone}</p>
    <p><b>CPF:</b> {cpf}</p>
    <p><b>Cidade:</b> {cidade}</p>
    <p><b>Estado:</b> {estado}</p>
    <p><b>Curso:</b> {curso}</p>
    <p><b>Idade:</b> {idade}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)