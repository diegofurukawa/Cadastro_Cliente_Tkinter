# Importar SQLite para dentro do Projeto
import sqlite3 as sqlite

# Criar uma conexão
con = sqlite.connect('database.db')


# Selecionando todos Dados na tabela
# selectalldata = []

def fn_select_all_customer_form():
    selectalldata = []
    with con:
        cur = con.cursor()
        query = ("SELECT * FROM customer")
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            selectalldata.append(row)

        return selectalldata


# Selecionando Dado Especifico na tabela
def fn_select_id_customer_form(id):
    selectdata = []
    with con:
        cur = con.cursor()
        query = ("SELECT * FROM customer WHERE idCustomer = ?")
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            selectdata.append(row)

    return selectdata


def fn_select_all_contact_form():
    selectalldata = []
    with con:
        cur = con.cursor()
        query = (
            "SELECT DISTINCT c.idCustomer ,c.cNameCustomer,COALESCE(c2.idContact, '') AS idContact,COALESCE(c2.cNameContact, '') AS cNameContact,COALESCE(c2.cPhoneContact, '') AS cPhoneContact,COALESCE(c2.cEmailContact, '') AS  cEmailContact,COALESCE(c2.dCreateContact, '') AS  dCreateContact FROM customer c LEFT JOIN contact c2 ON c2.idCustomer = C.idCustomer")
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            selectalldata.append(row)

        return selectalldata


# Selecionando Dado Especifico na tabela
def fn_select_id_contact_form(id):
    selectdata = []
    with con:
        cur = con.cursor()
        query = ("SELECT * FROM customer WHERE idCustomer = ?")
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            selectdata.append(row)

    return selectdata