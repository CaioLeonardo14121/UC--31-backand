from flask import FLask, render_template, request

app = flask(__name__)


@app.route()
def login():
    return render_template('formulario.html')

@app.route('/autenticar', methods={'GET'})
def autenticar():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    return "{} e {}".format(usuario, senha)

if __name__ == '__main__':
    app.rum(debug=True)