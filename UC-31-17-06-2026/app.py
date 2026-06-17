from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "sua_chave_secreta"

@app.route("/")
def inicio():
    return redirect(url_for("contador"))

@app.route("/contador")
def contador():
    if "acessos" not in session:
        session["acessos"] = 0

    session["acessos"] += 1

    return render_template(
        "contador.html",
        acessos=session["acessos"]
    )

@app.route("/zerar")
def zerar():
    session.pop("acessos", None)  # remove apenas o contador
    return redirect(url_for("contador"))

if __name__ == "__main__":
    app.run(debug=True)