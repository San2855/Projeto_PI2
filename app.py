from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('agendar.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS agendamentos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    hora TEXT NOT NULL,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
);
""")
conn.commit()

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/agendar', methods=['POST'])
def agendar():
    data = request.form['data']
    hora = request.form['hora']
    nome = request.form['nome']
    email = request.form['email']
    conn = sqlite3.connect('agendar.db')
    c = conn.cursor()
    c.execute("""
    INSERT INTO agendamentos (data, hora, nome, email)
    VALUES (?, ?, ?, ?)
    """, (data, hora, nome, email))
    conn.commit()
    conn.close()

    return redirect('/sucesso.html')

@app.route ('/sucesso.html')
def cadastradosucesso():
    return render_template('sucesso.html')


if __name__ == '__main__':
    app.run(debug=True)
