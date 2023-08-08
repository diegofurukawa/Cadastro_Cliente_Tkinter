# Importar SQLite para dentro do Projeto
import sqlite3 as sqlite

# Criar uma conexão
con = sqlite.connect('database.db')

# Criar uma tabela
with con:
    cur = con.cursor()
    cur.execute("""create table if not exists tb_user (
                        idUser integer primary key autoincrement
                        ,cName text
                        ,cPhone text
                        ,cEmail text
                        ,cUser text
                        ,cPassword text
                        )""")
    
    cur.execute("""create table if not exists customer (
            idCustomer INTEGER PRIMARY KEY AUTOINCREMENT
            ,cName TEXT
            ,cNameSales TEXT
            ,cPhone TEXT
            ,cDescription TEXT
            ,dStartOfContract DATE
            ,dCreate DATE
            )""")    
       
    cur.execute("""create table if not exists tb_customer (
                idCustomer INTEGER PRIMARY KEY AUTOINCREMENT
                ,cName TEXT
                ,cNameSales TEXT
                ,cPhone TEXT
                ,cEmail TEXT
                ,cDescription TEXT
                ,dStartOfContract DATE
                ,dCreate DATE
                )""")
                
    cur.execute("""create table if not exists tb_contact (
                idContact  INTEGER PRIMARY KEY AUTOINCREMENT
                ,idCustomer INTEGER
                ,cName TEXT
                ,cPhone TEXT
                ,cEmail TEXT
                ,dCreate DATE
                )""")