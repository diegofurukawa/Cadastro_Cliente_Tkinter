# Importar SQLite para dentro do Projeto
import sqlite3 as sqlite

# Criar uma conexão
con = sqlite.connect('database.db')


# Atualizando Dados na tabela
# updatedata = ['Diego Henrique Silva Furukawa','Cliente do Bruno Furukawa',1]

def fn_update_customer_form(i):
    with con:
        cur = con.cursor()
        query = (
            "UPDATE tb_Customer SET cNameCustomer = ?, cSalesMan = ?, nPhoneNumber = ?, cDescription = ?, dStartOfContract = ?, dCreateCustomer = ? WHERE idCustomer = ?")
        cur.execute(query, i)


def fn_update_contact_form(i):
    with con:
        cur = con.cursor()
        query = (
            "UPDATE tb_Contact SET cNameContact = ?, cPhoneContact = ?, cEmailContact = ?, dCreateContact = ? WHERE idCustomer = ?")
        cur.execute(query, i)