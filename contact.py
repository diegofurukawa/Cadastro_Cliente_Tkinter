from datetime import date
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Important Biblioteca TKCalendar
from tkcalendar import DateEntry

from icons import img_form_customer, img_form_contact, img_customer, img_delete, img_refresh, img_insert, img_search, img_save, img_contact
from contactsql import ContactClass

#from delete import *
# from insert import *
# from update import *
# from view import *



################# cores ###############
co0 = "#000000"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # - profit
co6 = "#038cfc"  # azul
co7 = "#ef5350"  # vermelha
co8 = "#263238"  # + verde
co9 = "#F8F8FF"  # GhostWhite
co10 = "#696969"  # DimGray


class ContactPage:
    
    def __init__(self, parent, window):
                
        self.tree = None
        self.parent = parent

        self.frameHeader = Frame(window, width=899, height=50, bg=co1, relief=FLAT)
        self.frameHeader.grid(row=0, column=0)
        # self.frameCenter.pack()

        self.app_logo = img_form_contact()
        self.app_logo = Label(self.frameHeader,
                              image=self.app_logo,
                              text=" Cadastro de Contato",
                              width=900, compound=LEFT,
                              relief=RAISED,
                              anchor=NW,
                              font=('Verdana 20 bold'),
                              bg=co1,
                              fg=co4)
        self.app_logo.place(x=0, y=0)

        self.frameCenter = Frame(window, width=899, height=265, bg=co1, pady=20, relief=FLAT)
        self.frameCenter.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)
        # self.frameCenter.pack()

        self.frameFooter = Frame(window, width=899, height=700, bg=co1, pady=20, relief=FLAT)
        self.frameFooter.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

        # Funcoes

        # ====================================================================================================================================
        # funcao INSERT - Inicio
        # ====================================================================================================================================

        # funcao inserir
        def insert():
            var = ContactClass()
            
            var.idCustomer = self.txt_idCustomer.get()
            var.cName = self.txt_NameContact.get()
            var.cPhone = self.txt_PhoneNumber.get()
            var.cEmail = self.txt_Email.get()
            var.dCreate = str(date.today())

            if (self.txt_NameContact.get() == ''
                or self.txt_PhoneNumber.get() == ''
                or self.txt_Email.get() == ''):
                messagebox.showerror('Erro', 'Preencha todos os campos')
            else:
                reply = messagebox.askquestion("Gravar", "Confirma que os dados estão corretos?", icon='warning')
                if reply == 'yes':
                    #fn_insert_customer_form(lista_inserir)
                    self.lblmsg["text"] = var.Insert()
                    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
                else:
                    messagebox.showinfo('Sucesso', 'Os dados foram descartados')

                self.txt_idCustomer.delete(0, 'end')
                self.txt_NameCustomer.delete(0, 'end')
                self.txt_NameContact.delete(0, 'end')
                self.txt_PhoneNumber.delete(0, 'end')
                self.txt_Email.delete(0, 'end')
                # e_assunto.delete(0, 'end')

                for self.widget in self.frameFooter.winfo_children():
                    self.widget.destroy()

            fn_mostrar()

        # ====================================================================================================================================
        # funcao INSERT - Fim
        # ====================================================================================================================================

        # ====================================================================================================================================
        # funcao UPDATE - Inicio
        # ====================================================================================================================================
        def refresh():
            try:
                self.treev_dados = self.tree.focus()
                treev_dicionario = self.tree.item(self.treev_dados)
                treev_lista = treev_dicionario['values']
                valor = treev_lista[0]

                self.txt_idCustomer.delete(0, 'end')
                self.txt_NameCustomer.delete(0, 'end')
                
                self.txt_idContact.delete(0, 'end')
                self.txt_NameContact.delete(0, 'end')
                self.txt_Email.delete(0, 'end')
                self.txt_PhoneNumber.delete(0, 'end')
                # e_assunto.delete(0, 'end')

                
                self.txt_idCustomer.insert(0, treev_lista[0])
                self.txt_NameCustomer.insert(0, treev_lista[1])
                
                self.txt_idContact.insert(0, treev_lista[2])
                self.txt_NameContact.insert(0, treev_lista[3])
                self.txt_Email.insert(0, treev_lista[4])
                self.txt_PhoneNumber.insert(0, treev_lista[5])


                # e_assunto.insert(0, treev_lista[6])

                def update():
                    var = ContactClass()
                    
                    var.idCustomer = self.txt_idCustomer.get()
                    var.cNameCustomer = self.txt_NameCustomer.get()
                    
                    var.idContact = self.txt_idContact.get()
                    var.cName = self.txt_NameContact.get()
                    var.cPhone = self.txt_PhoneNumber.get()
                    var.cEmail = self.txt_Email.get()                                    

                    if (self.txt_NameContact.get() == ''
                        or self.txt_PhoneNumber.get() == ''
                        or self.txt_Email.get() == ''):
                        messagebox.showerror('Erro', 'Preencha todos os campos')
                    else:
                        #fn_update_customer_form(lista_atualizar)
                        self.lblmsg["text"] = var.Update()

                        messagebox.showinfo(
                            'Sucesso', 'Os dados foram atualizados com sucesso')

                        self.txt_idCustomer.delete(0, 'end')
                        self.txt_NameCustomer.delete(0, 'end')
                        
                        self.txt_idContact.delete(0, 'end')
                        self.txt_NameContact.delete(0, 'end')
                        self.txt_Email.delete(0, 'end')
                        self.txt_PhoneNumber.delete(0, 'end')

                        for self.widget in self.frameFooter.winfo_children():
                            self.widget.destroy()

                        fn_mostrar()

                def cancel():
                    self.btn_update.destroy()
                    self.btn_cancel.destroy()
                    
                    self.txt_idCustomer.delete(0, 'end')
                    self.txt_NameCustomer.delete(0, 'end')
                    
                    self.txt_idContact.delete(0, 'end')
                    self.txt_NameContact.delete(0, 'end')
                    self.txt_Email.delete(0, 'end')
                    self.txt_PhoneNumber.delete(0, 'end')

                    for self.widget in self.frameFooter.winfo_children():
                        self.widget.destroy()

                    fn_mostrar()

                fn_mostrar()

                # ============= Botao Update =============
                self.btn_update = Button(self.frameCenter, command=update, text="Confirmar".upper(), width=13, height=1,
                                       bg=co2, fg=co1,
                                       font=('ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
                self.btn_update.place(x=450, y=102)

                self.btn_cancel = Button(self.frameCenter, command=cancel, text="Cancelar".upper(), width=13, height=1,
                                       bg=co7, fg=co1,
                                       font=('ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
                self.btn_cancel.place(x=450, y=132)

            except IndexError:
                messagebox.showerror(
                    'Erro', 'Seleciona um dos dados na tabela')

            fn_mostrar()

        # ====================================================================================================================================
        # Funcao UPDATE - Fim
        # ====================================================================================================================================

        # ====================================================================================================================================
        # Funcao DELETE - Inicio
        # ====================================================================================================================================
        # funcao deletar
        def delete():
            var = ContactClass()
            try:
                self.treev_dados = self.tree.focus()
                treev_dicionario = self.tree.item(self.treev_dados)
                treev_lista = treev_dicionario['values']
                #valor = treev_lista[0] #idCustomer
                #valor = treev_lista[1] #cNameCustomer
                valor = treev_lista[2]
                
                #self.lblmsg["text"] = valor
                            
                idContact = self.txt_idContact.get()
                if idContact == '':
                    idContact = valor
                else:
                    idContact
                
                self.lblmsg["text"] = idContact
                
                reply = messagebox.askquestion("Excluir", "Confirma a exclusão?", icon='warning')
                if reply == 'yes':
                    #fn_del_customer_form([valor])
                    self.lblmsg["text"] = var.Delete(idContact)
                    
                    # print(valor)
                    messagebox.showinfo(
                        'Sucesso', 'Os dados foram deletados com sucesso!')
                else:
                    messagebox.showinfo(
                        'Sucesso', 'Os dados foram mantidos.')

                for self.widget in self.frameFooter.winfo_children():
                    self.widget.destroy()

                fn_mostrar()

            except IndexError:
                messagebox.showerror(
                    'Erro', 'Seleciona um dos dados na tabela')
                

                            
        def searchcustomer():
            var = ContactClass()

            #idCustomer = self.txt_idCustomer.get()
            idContact = self.txt_idContact.get()

            self.lblmsg["text"] = var.SelectId(idContact) #idCustomer

            self.txt_idCustomer.delete(0, END)
            self.txt_idCustomer.insert(INSERT, var.idCustomer)
            
            self.txt_idContact.delete(0, END)
            self.txt_idContact.insert(INSERT, var.idContact)

            self.txt_idCustomer.delete(0, 'end')
            self.txt_NameCustomer.delete(0, 'end')
            self.txt_idContact.delete(0, 'end')
            self.txt_NameContact.delete(0, 'end')
            self.txt_Email.delete(0, 'end')
            self.txt_PhoneNumber.delete(0, 'end')


            self.txt_idCustomer.insert(INSERT, var.idCustomer)
            self.txt_NameCustomer.insert(INSERT, var.cNameCustomer)
            self.txt_idContact.insert(INSERT, var.idContact)
            self.txt_NameContact.insert(INSERT, var.cName)
            self.txt_PhoneNumber.insert(INSERT, var.cPhone)
            self.txt_Email.insert(INSERT, var.cEmail)


        # ====================================================================================================================================
        # Funcao DELETE - Fim
        # ====================================================================================================================================

        # Criando Labels
        # ====================================================================================================================================

        self.lbl_idcustomer = Label(self.frameCenter, text=' Id Cliente:', height=1, anchor=NW, font='Ivy 10 bold',
                                    bg=co1, fg=co4)
        self.lbl_idcustomer.place(x=10, y=10)

        self.txt_idCustomer = Entry(self.frameCenter, width=15, justify='left', relief=SOLID)
        self.txt_idCustomer.place(x=130, y=11)
        
        self.txt_idContact = Entry(self.frameCenter, width=15, justify='left', relief=SOLID)
        self.txt_idContact.place(x=230, y=11)


        
        # ====================================================================================================================================
        
        self.lbl_namecustomer = Label(self.frameCenter, text=' Nome Cliente:', height=1, anchor=NW, font='Ivy 10 bold',
                              bg=co1, fg=co4)
        self.lbl_namecustomer.place(x=10, y=40)

        self.txt_NameCustomer = Entry(self.frameCenter, width=50, justify='left', relief=SOLID)
        self.txt_NameCustomer.place(x=130, y=41)

        # ====================================================================================================================================

        self.lbl_namecontact = Label(self.frameCenter, text=' Nome Contato:', height=1, anchor=NW, font='Ivy 10 bold',
                                  bg=co1, fg=co4)
        self.lbl_namecontact.place(x=10, y=70)

        self.txt_NameContact = Entry(self.frameCenter, width=50, justify='left', relief=SOLID)
        self.txt_NameContact.place(x=130, y=71)

        # ====================================================================================================================================

        self.lbl_phonenumber = Label(self.frameCenter, text=' Telefone:', height=1, anchor=NW, font='Ivy 10 bold',
                                     bg=co1, fg=co4)
        self.lbl_phonenumber.place(x=10, y=100)

        self.txt_PhoneNumber = Entry(self.frameCenter, width=50, justify='left', relief=SOLID)
        self.txt_PhoneNumber.place(x=130, y=101)

        # ====================================================================================================================================

        self.lbl_email = Label(self.frameCenter, text=' E-mail:', height=1, anchor=NW, font='Ivy 10 bold',
                                     bg=co1, fg=co4)
        self.lbl_email.place(x=10, y=130)

        self.txt_Email = Entry(self.frameCenter, width=50, justify='left', relief=SOLID)
        self.txt_Email.place(x=130, y=131)


        self.lblmsg = Label(self.frameCenter, text='', height=1, anchor=NW, bg=co1, fg=co4)
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.place(x=130, y=200)
        

        # ============= Botao Inserir =============

        self.img_add = img_insert()
        self.btn_insert = Button(self.frameCenter,
                                 command=insert,
                                 image=self.img_add,
                                 width=95,
                                 text=' Adicionar'.upper(),
                                 compound=LEFT,
                                 anchor=NW,
                                 overrelief=RIDGE,
                                 font='Ivy 8',
                                 bg=co1,
                                 fg=co0)
        self.btn_insert.place(x=450, y=8)

        # # ============= Botao Refresh =============

        self.ref_img = img_refresh()
        self.btn_refresh = Button(self.frameCenter,
                                  command=refresh,
                                  image=self.ref_img,
                                  width=95,
                                  text=' Carregar'.upper(),
                                  compound=LEFT,
                                  anchor=NW,
                                  overrelief=RIDGE,
                                  font='Ivy 8',
                                  bg=co1,
                                  fg=co0)
        self.btn_refresh.place(x=450, y=38)

        # ============= Botao Delete =============
        self.del_img = img_delete()
        self.btn_delete = Button(self.frameCenter,
                                 command=delete,
                                 image=self.del_img,
                                 width=95,
                                 text=' Excluir'.upper(),
                                 compound=LEFT,
                                 anchor=NW,
                                 overrelief=RIDGE,
                                 font='Ivy 8',
                                 bg=co1,
                                 fg=co0)

        self.btn_delete.place(x=450, y=70)

        # ============= Botao Pesquisa =============
        self.search_img = img_search()
        self.btn_search = Button(self.frameCenter,
                                 command=searchcustomer,
                                 image=self.search_img,
                                 width=95,
                                 text=' Busca'.upper(),
                                 compound=LEFT,
                                 anchor=NW,
                                 overrelief=RIDGE,
                                 font='Ivy 8',
                                 bg=co1,
                                 fg=co0)
        self.btn_search.place(x=331, y=8)

        # ============= Botao Contact =============
        self.customer_img = img_customer()
        self.btn_customer = Button(self.frameCenter,
                                  command=self.clicked,
                                  image=self.customer_img,
                                  width=95,
                                  text=' Clientes'.upper(),
                                  compound=LEFT,
                                  anchor=NW,
                                  overrelief=RIDGE,
                                  font='Ivy 8',
                                  bg=co1,
                                  fg=co0)
        self.btn_customer.place(x=570, y=8)

        # Frame Tree
        # funcao para fn_mostrar
        def fn_mostrar():
            var = ContactClass()
            # creating a treeview with dual scrollbars
            list_header =   [
                            'Id', #idCustomer
                            'Customer', #cNameCustomer
                            'Contact', #idContact
                            'Name Contact', #cName
                            'PhoneNumber', #cPhone
                            'Email', #cEmail
                            'dCreate' 
                            ]

            #df_list = fn_select_all_customer_form()
            df_list = var.SelectAll()
            
            global tree

            self.tree = ttk.Treeview(self.frameFooter,
                                     selectmode="extended",
                                     columns=list_header,
                                     show="headings")

            # vertical scrollbar
            self.vsb = ttk.Scrollbar(
                self.frameFooter, orient="vertical", command=self.tree.yview)
            # horizontal scrollbar
            self.hsb = ttk.Scrollbar(
                self.frameFooter, orient="horizontal", command=self.tree.xview)

            self.tree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)

            self.tree.grid(column=0, row=0, sticky='nsew')
            self.vsb.grid(column=1, row=0, sticky='ns')
            self.hsb.grid(column=0, row=1, sticky='ew')
            self.frameFooter.grid_rowconfigure(0, weight=12)

            hd = [
                    "center"    #idCustomer
                    ,"nw"       #cNameCustomer
                    ,"nw"       #idContact
                    ,"nw"       #cName
                    ,"nw"       #cPhone
                    ,"center"   #cEmail
                    ,"center"   #dCreate
                ]
            h = [30, 200, 60, 200, 100, 200, 80]
            n = 0

            for col in list_header:
                self.tree.heading(col, text=col.title(), anchor=CENTER)
                # adjust the column's width to the header string
                self.tree.column(col, width=h[n], anchor=hd[n])

                n += 1

            for item in df_list:
                self.tree.insert('', 'end', values=item)

        fn_mostrar()

    def clicked(self):
        self.frameHeader.destroy()
        self.frameCenter.destroy()
        self.frameFooter.destroy()
        self.parent.changepage(0)
