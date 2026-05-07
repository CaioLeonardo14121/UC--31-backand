from flask import Flask, render_template

app = Flask(__name__)

@app.route('/filme/<genero>')
def filme(genero):

    if genero == "acao":
        return render_template("acao.html")

    elif genero == "comedia":
        return render_template("comedia.html")

    elif genero == "terror":
        return render_template("terror.html")

    elif genero == "romance":
        return render_template("romance.html")

    else:
        return render_template("erro.html")


app.run(debug=True)