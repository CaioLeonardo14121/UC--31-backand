from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    nome = request.args.get('nome')
    curso = request.args.get('curso')
    cidade = request.args.get('cidade')
    idade = request.args.get('idade')

    return render_template(
        'resultado.html',
        nome=nome,
        curso=curso,
        cidade=cidade,
        idade=idade
    )

app.run(debug=True)