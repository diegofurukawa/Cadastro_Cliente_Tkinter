# Importar SQLite para dentro do Projeto
import sqlite3 as sqlite

# Criar uma conexão
con = sqlite.connect('database.db')


# Inserindo Dados na tabela
# insertdata = ['Mari Afonso','Diego','(11)994329402','Cliente do Diego', '17/07/2013' ,'17/07/2023']
# insertdata = [1, 'Nome do Contato','(11)994329402', 'email@email.com','17/07/2023']

def fn_insert_customer_form(i):
    with con:
        cur = con.cursor()
        query = (
            "INSERT INTO tb_Customer (cName, cNameSales, cPhone, cEmail, cDescription, dStartOfContract, dCreate) VALUES (?, ?, ?, ?, ?, ?, ?)")
        cur.execute(query, i)


def fn_insert_contact_form(i):
    with con:
        cur = con.cursor()
        query = (
            "INSERT INTO tb_Contact (idCustomer, cNameContact, cPhoneContact, cEmailContact, dCreateContact) VALUES (?, ?, ?, ?, ?)")
        cur.execute(query, i)