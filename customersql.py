from banco import Banco

class CustomerClass(object):
    def __init__(self, 
                 idCustomer = 0
                 ,cName = ""
                 ,cNameSales = ""
                 ,cPhone = ""
                 ,cEmail = ""
                 ,cDescription = ""
                 ,dStartOfContract = ""
                 ,dCreate = ""
                 ,cSearch = ""
                 ):

        self.info = {}
        self.idCustomer = idCustomer
        self.cName = cName
        self.cNameSales = cNameSales
        self.cPhone = cPhone
        self.cEmail = cEmail
        self.cDescription = cDescription
        self.dStartOfContract = dStartOfContract
        self.cSearch = cSearch


    def InsertCustomer(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into tb_Customer (cName, cNameSales, cPhone, cEmail, cDescription, dStartOfContract, dCreate) values ('"
                        + self.cName + "', '" 
                        + self.cNameSales + "', '" 
                        + self.cPhone + "', '" 
                        + self.cEmail + "', '" 
                        + self.cDescription + "', '" 
                        + self.dStartOfContract + "', '" 
                        + self.dCreate + "')")

            banco.conexao.commit()
            c.close()

            return ""
        except:
            return "Ocorreu um erro na inserção do usuário"


    def UpdateCustomer(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update tb_Customer set cName = '" + self.cName
                    + "',cNameSales = '" + self.cNameSales 
                    + "', cPhone = '" + self.cPhone 
                    + "', cEmail = '" + self.cEmail 
                    + "', cDescription = '" + self.cDescription 
                    + "', dStartOfContract = '" + self.dStartOfContract 
                   
                    + "' where idCustomer = " + self.idCustomer 
                    + " ")

            banco.conexao.commit()
            c.close()

            return ""
        except:
            return "Ocorreu um erro na alteração do usuário"

    def DeleteCustomer(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from tb_customer where idCustomer = " + self.idCustomer + " ")

            banco.conexao.commit()
            c.close()

            return ""
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def SelectCustomerId(self, idCustomer):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute(
                "select idCustomer,cName,cNameSales,cPhone,cEmail,cDescription,dStartOfContract,dCreate from tb_Customer where idCustomer = " + idCustomer + " ")

            for linha in c:
                self.idCustomer = linha[0]
                self.cName = linha[1]
                self.cNameSales = linha[2]
                self.cPhone = linha[3]
                self.cEmail = linha[4]
                self.cDescription = linha[5]
                self.dStartOfContract = linha[6]
                self.dCreate = linha[7]

            c.close()

            return ""
        except:
            return "Ocorreu um erro na busca do cliente"
        
    def SelectCustomerAllSearch(self):
        banco = Banco()
        try:
            selectalldata = []
            with banco.conexao:
                cur = banco.conexao.cursor()
                query = (
                            "SELECT * FROM tb_Customer "
                            + "WHERE (idCustomer ||'-'|| cName ||'-'|| cNameSales) LIKE "
                            + "'%"
                            + self.cSearch
                            + "%'"
                         )
                cur.execute(query)

                rows = cur.fetchall()
                for row in rows:
                    selectalldata.append(row)

                return selectalldata
                #rows.close()
                #return ""
        except:
            return "Ocorreu um erro na busca do cliente"
                
        
    def SelectCustomerAll(self):
        banco = Banco()
        try:
            selectalldata = []
            with banco.conexao:
                cur = banco.conexao.cursor()
                query = ("SELECT * FROM tb_Customer")
                cur.execute(query)

                rows = cur.fetchall()
                for row in rows:
                    selectalldata.append(row)

                return selectalldata
                #rows.close()
                #return ""
        except:
            return "Ocorreu um erro na busca do cliente"