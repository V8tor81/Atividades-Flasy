# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Página inicial
@app.route("/")
def inicial():
    return "<h1>Olá, Flasky!!!</h1>"

# Página do formulário de login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        # Usuário e senha corretos
        if username == "usuario" and password == "senha123":
            return render_template("success.html")
        else:
            return render_template("error.html")
    
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
