# Criando banco de dados
import sqlite3 as lite

# Criando conexão
con = lite.connect('dados.db')


# Criando tabela
with con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE formulario
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT,
                nome TEXT,
                telefone TEXT,
                dia_em DATE,
                estado TEXT,
                assunto TEXT 
                )''')