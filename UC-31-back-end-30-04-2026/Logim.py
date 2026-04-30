from flask import Flask, render_template_string

app = Flask(__name__)

# HTML do login
login_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>

    <h2>Login</h2>

    <form>
        <label>Usuário:</label><br>
        <input type="text" name="usuario"><br><br>

        <label>Senha:</label><br>
        <input type="password" name="senha"><br><br>

        <button type="submit">Entrar</button>
    </form>

</body>
</html>
"""

# HTML dos alunos
alunos_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Alunos</title>
</head>
<body>

    <h2>Lista de Alunos</h2>

    <table border="1">
        <tr>
            <th>Nome</th>
            <th>Matrícula</th>
        </tr>

        {% for aluno in alunos %}
        <tr>
            <td>{{ aluno.nome }}</td>
            <td>{{ aluno.matricula }}</td>
        </tr>
        {% endfor %}

    </table>

</body>
</html>
"""

# Rota login
@app.route('/login')
def login():
    return render_template_string(login_html)

# Rota alunos
@app.route('/alunos')
def alunos():
    lista_alunos = [
        {"nome": "Carlos", "matricula": "112233"},
        {"nome": "Fernanda", "matricula": "223344"},
        {"nome": "João", "matricula": "334455"},
        {"nome": "Beatriz", "matricula": "445566"},
        {"nome": "Rafael", "matricula": "556677"}
    ]
    return render_template_string(alunos_html, alunos=lista_alunos)

if __name__ == '__main__':
    app.run(debug=True)