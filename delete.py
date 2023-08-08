# Importar SQLite para dentro do Projeto
import sqlite3 as sqlite

# Criar uma conexão
con = sqlite.connect('database.db')


# Deletando Dados na tabela
def fn_del_customer_form(id):
    with con:
        cur = con.cursor()
        query = ("DELETE FROM tb_Customer WHERE idCustomer = ?")
        cur.execute(query, id)


# Deletando Dados na tabela
def fn_del_contact_form(id):
    with con:
        cur = con.cursor()
        query = ("DELETE FROM tb_Contact WHERE idCustomer = ?")
        cur.execute(query, id)