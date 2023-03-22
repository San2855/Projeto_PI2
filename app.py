from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

#tópico 1
conn = sqlite3.connect('agenda.db')
cursor = conn.cursor()

#tópico 2
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
#tópico 3
@app.route('/')
def index():
    return render_template('formulario.html')
#tópico 4
@app.route('/agendar', methods=['POST'])
def agendar():
    data = request.form['data']
    hora = request.form['hora']
    nome = request.form['nome']
    email = request.form['email']
    conn = sqlite3.connect('agendar.db')
    c = conn.cursor

  #tópico 5
    c.execute("""
    INSERT INTO agendamentos (data, hora, nome, email)
    VALUES (?, ?, ?, ?)
    """, (data, hora, nome, email))
    conn.commit()
    conn.close()

    return redirect('/cadastrosucesso.html')

if __name__ == '__main__':
    app.run(debug=True)
