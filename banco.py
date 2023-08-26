# Importar SQLite para dentro do Projeto
import sqlite3 as sqlite

class Banco():

    def __init__(self):
        self.conexao = sqlite.connect('database.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists tb_user (
                    idUser integer primary key autoincrement
                    ,cName text
                    ,cPhone text
                    ,cEmail text
                    ,cUser text
                    ,cPassword text
                    )""")
        
        c.execute("""create table if not exists tb_customer (
                    idCustomer INTEGER PRIMARY KEY AUTOINCREMENT
                    ,cName TEXT
                    ,cNameSales TEXT
                    ,cPhone TEXT
                    ,cEmail TEXT
                    ,cDescription TEXT
                    ,dStartOfContract DATE
                    ,nContractDuration TEXT
                    ,dCreate DATE
                    )""")
                
        c.execute("""create table if not exists tb_contact (
                    idContact  INTEGER PRIMARY KEY AUTOINCREMENT
                    ,idCustomer INTEGER
                    ,cName TEXT
                    ,cPhone TEXT
                    ,cEmail TEXT
                    ,dCreate DATE
                    )""")
        
                
        self.conexao.commit()
        
        
        
        c.close()
        
        
#banco = Banco()