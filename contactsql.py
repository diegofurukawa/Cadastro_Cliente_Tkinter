from banco import Banco

class ContactClass(object):
    def __init__(self, 
                 idCustomer = 0
                 ,cNameCustomer = ""
                 ,idContact = ""
                 ,cName = ""
                 ,cPhone = ""
                 ,cEmail = ""
                 ,dCreate = ""
                 ):

        self.info = {}
        self.idCustomer = idCustomer
        self.cNameCustomer = cNameCustomer
        self.idContact = idContact
        self.cName = cName
        self.cPhone = cPhone
        self.cEmail = cEmail
        self.dCreate = dCreate


    def Insert(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into tb_Contact (idCustomer, cName, cPhone, cEmail, dCreate) values ('"
                        + self.idCustomer + "', '"
                        + self.cName + "', '" 
                        + self.cPhone + "', '" 
                        + self.cEmail + "', '" 
                        + self.dCreate + "')")

            banco.conexao.commit()
            c.close()

            return ""
        except:
            return "Ocorreu um erro na inserção do usuário"


    def Update(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update tb_Contact set cName = '" + 
                      self.cName 
                        + "', cPhone = '" + self.cPhone 
                        + "', cEmail = '" + self.cEmail 
                    
                        + "' where idCustomer = " + self.idCustomer 
                        + " ")

            banco.conexao.commit()
            c.close()

            return ""
        except:
            return "Ocorreu um erro na alteração do usuário"

    def Delete(self, idContact):
        banco = Banco()
        try:
            c = banco.conexao.cursor()            
            query = ("delete from tb_Contact where idContact = " + idContact)            
            c.execute(query)
            banco.conexao.commit()
            c.close()

            return "delete realizado"
        except:
            return "Ocorreu um erro na exclusão do usuário "
                    

    def SelectId(self, idContact): #idCustomer
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            query = ("SELECT "
                        + "c.idCustomer, "
                        + "c.cName AS cNameCustomer, "
                        + "COALESCE(c2.idContact, '') AS idContact, "
                        + "COALESCE(c2.cName, '') AS cName, "
                        + "COALESCE(c2.cPhone, '') AS cPhone, "
                        + "COALESCE(c2.cEmail, '') AS cEmail, "
                        + "COALESCE(c2.dCreate, '') AS dCreate "
                        + "FROM tb_customer c "
                        + "LEFT JOIN tb_contact c2 ON c2.idCustomer = C.idCustomer "
                        + "WHERE 1=1 "
                        #+ "AND (c.idCustomer = " + idCustomer + " OR " + idCustomer + " = " + idCustomer + ")"
                        + "OR  (c2.idContact = " + idContact + ")"
                        # + "LIMIT 1 "
                    )
            c.execute(query)
                #"select idCustomer,idContact,cName,cPhone,cEmail,dCreate from tb_Contact where idCustomer = " + idCustomer + " ")

            for linha in c:
                self.idCustomer = linha[0]
                self.cNameCustomer = linha[1]
                self.idContact = linha[2]
                self.cName = linha[3]
                self.cPhone = linha[4]
                self.cEmail = linha[5]
                self.dCreate = linha[6]

            c.close()

            return ""
        except:
            return "Ocorreu um erro na SelectId do cliente"
        
        
    def SelectAll(self):
        banco = Banco()
        try:
            selectalldata = []
            with banco.conexao:
                cur = banco.conexao.cursor()
                query = (
                            "SELECT DISTINCT "
                            +"c.idCustomer "
                            +",c.cName AS cNameCustomer "
                            +",COALESCE(c2.idContact, '') AS idContact "
                            +",COALESCE(c2.cName, '') AS cName "
                            +",COALESCE(c2.cPhone, '') AS cPhone "
                            +",COALESCE(c2.cEmail, '') AS cEmail "
                            +",COALESCE(c2.dCreate, '') AS dCreate "
                            +"FROM tb_customer c "
                            +"LEFT JOIN tb_contact c2 "
                            +"ON c2.idCustomer = C.idCustomer"                        
                         )
                cur.execute(query)

                rows = cur.fetchall()
                for row in rows:
                    selectalldata.append(row)

                return selectalldata
                #rows.close()
                #return ""
        except:
            return "Ocorreu um erro na SelectAll do cliente"
        