from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)

app.secret_key = '123'

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        senha = request.form.get('senha')

        if not email or not senha:

            flash('Preencha todos os campos.', 'erro')
            return redirect(url_for('login'))

    if email != 'admin@email.com' or senha != '123':

         flash('E-mail ou senha inválidos.', 'erro')
         return redirect(url_for('login'))
    
    flash('Login realizado com sucesso!', 'sucesso')
    return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/panel')
def panel():
    return render_template('panel.html')

if __name__ == '__main__':
    app.run(debug=True)
