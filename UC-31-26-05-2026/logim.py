from flask import Flask, render_templete

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_templete(+"inicia.html")

@app.route("/sobre")
def sobre():
    return render_templete("sobre.html")

@app.route("/servicos")
def sobre():
    return render_templete("servicos.html")

if __name__ == "__mani__":
    app.rum(debug=True)
i



