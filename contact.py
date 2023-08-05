# Importando Biblioteca TKCalendar
# from tkcalendar import Calendar, DateEntry
from datetime import date
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from delete import *
from icons import *
from insert import *
from update import *
from view import *

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

class Contact_Page:
    def __init__(self, parent, window):
        
        self.tree = None
        self.parent = parent
        
        self.frameHeader = Frame(window, width=899, height=50, bg=co1, relief=FLAT)
        self.frameHeader.grid(row=0, column=0)
        #self.frameCenter.pack()

        self.app_logo = img_form_contact()
        self.app_logo = Label(self.frameHeader, 
                              image=self.app_logo,
                              text=" Contatos", 
                              width=900, compound=LEFT,
                              relief=RAISED,
                              anchor=NW, 
                              font=('Verdana 20 bold'), 
                              bg=co1, 
                              fg=co4)
        self.app_logo.place(x=0, y=0)
    
              
        self.frameCenter = Frame(window, width=899, height=265, bg=co1, pady=20, relief=FLAT)
        self.frameCenter.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)
        #self.frameCenter.pack()
        
        self.frameFooter = Frame(window, width=899, height=700, bg=co1, pady=20, relief=FLAT)
        self.frameFooter.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

        # Funcoes

# ====================================================================================================================================
# funcao INSERT - Inicio
# ====================================================================================================================================

        # funcao inserir
        def insert():
            idCustomer = self.e_idcustomer.get()
            cNameContact = self.e_namecontact.get()
            nPhoneNumber = self.e_phonenumber.get()
            cEmail = self.e_email.get()
            dCreateContact = date.today()

            lista_inserir = [idCustomer, cNameContact.upper(), nPhoneNumber.upper(), cEmail.lower(), dCreateContact]

            if self.e_namecontact.get() == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
            else:
                reply = messagebox.askquestion("Gravar", "Confirma que os dados estão corretos?", icon='warning')
                if reply == 'yes':
                    # self.e_idcustomer.delete(0, 'end')
                    # self.e_namecustomer.delete(0, 'end')
                    fn_insert_contact_form(lista_inserir)
                    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
                else:
                    messagebox.showinfo('Sucesso', 'Os dados foram descartados')

                self.e_idcustomer.delete(0, 'end')
                self.e_namecustomer.delete(0, 'end')
                self.e_namecontact.delete(0, 'end')
                self.e_phonenumber.delete(0, 'end')
                self.e_email.delete(0, 'end')
                # e_assunto.delete(0, 'end')

                for self.widget in self.frameFooter.winfo_children():
                    self.widget.destroy()
                    
            mostrar()
                
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
                idCustomer = treev_lista[0]

                self.e_namecontact.delete(0, 'end')
                self.e_phonenumber.delete(0, 'end')
                self.e_email.delete(0, 'end')
                # e_assunto.delete(0, 'end')

                self.e_idcustomer.insert(0, treev_lista[0])
                self.e_namecustomer.insert(0, treev_lista[1])

                self.e_namecontact.insert(0, treev_lista[3])
                self.e_phonenumber.insert(0, treev_lista[4])
                self.e_email.insert(0, treev_lista[5])

                # e_assunto.insert(0, treev_lista[6])

                def update():
                    cNameContact = self.e_namecontact.get()
                    cPhoneContact = self.e_phonenumber.get()
                    cEmailContact = self.e_email.get()
                    dCreateContact = date.today()

                    lista_atualizar = [cNameContact.upper(), cPhoneContact.upper(), cEmailContact.lower(), dCreateContact, idCustomer]

                    if self.e_namecontact.get() == '':
                        messagebox.showerror('Erro', 'Preencha todos os campos')
                    else:
                        fn_update_contact_form(lista_atualizar)

                        messagebox.showinfo(
                            'Sucesso', 'Os dados foram atualizados com sucesso')

                        self.e_idcustomer.delete(0, 'end')
                        self.e_namecustomer.delete(0, 'end')
                        self.e_namecontact.delete(0, 'end')
                        self.e_phonenumber.delete(0, 'end')
                        self.e_email.delete(0, 'end')
                        # date.delete(0, 'end')
                        
                        for self.widget in self.frameFooter.winfo_children():
                            self.widget.destroy()
                    
                        mostrar()

                def cancel():
                    self.btn_update.destroy()
                    self.btn_cancel.destroy()
                    
                    self.e_idcustomer.delete(0, 'end')
                    self.e_namecustomer.delete(0, 'end')
                    self.e_namecontact.delete(0, 'end')
                    self.e_phonenumber.delete(0, 'end')
                    self.e_email.delete(0, 'end')
                    
                    # for self.widget in self.frameFooter.winfo_children():
                    #     self.widget.destroy()

                    for self.widget in self.frameFooter.winfo_children():
                        self.widget.destroy()                        
                    
                    mostrar()      

                # ============= Botao Update =============
                self.btn_update = Button(self.frameCenter, command=update, text="Confirmar".upper(), width=13, height=1, bg=co2, fg=co1,
                                font=('ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
                self.btn_update.place(x=450, y=102)                

                self.btn_cancel = Button(self.frameCenter, command=cancel, text="Cancelar".upper(), width=13, height=1, bg=co7, fg=co1,
                                    font=('ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
                self.btn_cancel.place(x=450, y=132)
            
            except IndexError:
                messagebox.showerror(
                    'Erro', 'Seleciona um dos dados na tabela')
                     
            mostrar()
# ====================================================================================================================================
# Funcao UPDATE - Fim
# ====================================================================================================================================

# ====================================================================================================================================
# Funcao DELETE - Inicio
# ====================================================================================================================================
        # funcao deletar
        def delete():
            try:
                self.treev_dados = self.tree.focus()
                treev_dicionario = self.tree.item(self.treev_dados)
                treev_lista = treev_dicionario['values']
                valor = treev_lista[0]

                reply = messagebox.askquestion("Excluir", "Confirma a exclusão?", icon='warning')
                if reply == 'yes':
                    fn_del_contact_form([valor])
                    # print(valor)
                    messagebox.showinfo(
                        'Sucesso', 'Os dados foram deletados com sucesso!')
                else:
                    messagebox.showinfo(
                        'Sucesso', 'Os dados foram mantidos.')

                for self.widget in self.frameFooter.winfo_children():
                    self.widget.destroy()

                mostrar()

            except IndexError:
                messagebox.showerror(
                    'Erro', 'Seleciona um dos dados na tabela')

# ====================================================================================================================================
# Funcao DELETE - Fim
# ====================================================================================================================================

          
        # Criando Labels
        self.lbl_idcustomer = Label(self.frameCenter, 
                                    text=' Id Cliente', 
                                    height=1, 
                                    anchor=NW, 
                                    font=('Ivy 10 bold'),
                                    bg=co1, 
                                    #fg=co4
                                    )
        self.lbl_idcustomer.place(x=10, y=10)

        self.e_idcustomer = Entry(self.frameCenter, width=50, justify='left', relief=SOLID)
        self.e_idcustomer.place(x=130, y=11)

        # ====================================================================================================================================

        self.lbl_namecustomer = Label(self.frameCenter, text=' Nome Cliente:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        self.lbl_namecustomer.place(x=10, y=40)

        self.e_namecustomer = Entry(self.frameCenter, width=50, justify='left', relief=SOLID)
        self.e_namecustomer.place(x=130, y=41)

        # ====================================================================================================================================

        self.lbl_namecontact = Label(self.frameCenter, text=' Nome Contato:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        self.lbl_namecontact.place(x=10, y=70)

        self.e_namecontact = Entry(self.frameCenter, width=50, justify='left', relief=SOLID)
        self.e_namecontact.place(x=130, y=71)

        # ====================================================================================================================================

        self.lbl_phonenumber = Label(self.frameCenter, text=' Tel. Contato:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        self.lbl_phonenumber.place(x=10, y=100)

        self.e_phonenumber = Entry(self.frameCenter, width=50, justify='left', relief=SOLID)
        self.e_phonenumber.place(x=130, y=101)

        # ====================================================================================================================================

        self.lbl_email = Label(self.frameCenter, text=' E-mail Contato:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        self.lbl_email.place(x=10, y=130)

        self.e_email = Entry(self.frameCenter, width=50, justify='left', relief=SOLID)
        self.e_email.place(x=130, y=131)

        # ============= Botao Inserir =============

        self.img_add = img_insert()
        self.btn_insert = Button(self.frameCenter, 
                                 command=insert,
                                 image=self.img_add, width=95, text=' Adicionar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font='Ivy 8', bg=co1, fg=co0)
        self.btn_insert.place(x=450, y=8)

        # # ============= Botao Refresh =============

        self.ref_img = img_refresh()
        self.btn_refresh = Button(self.frameCenter, 
                                  command=refresh,
                                  image=self.ref_img, width=95, text=' Carregar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font='Ivy 8', bg=co1, fg=co0)
        self.btn_refresh.place(x=450, y=38)


        # ============= Botao Delete =============
        self.del_img = img_delete()
        self.btn_delete = Button(self.frameCenter, 
                                 command=delete,
                                 image=self.del_img, width=95, text=' Excluir'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font='Ivy 8', bg=co1, fg=co0)
        self.btn_delete.place(x=450, y=70)


        # ============= Botao Pesquisa =============
        self.search_img = img_search()
        self.btn_search = Button(self.frameCenter, 
                                 #command=self.clicked, 
                                 image=self.search_img, width=95, text=' Busca'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font='Ivy 8', bg=co1, fg=co0)
        self.btn_search.place(x=570, y=8)

        # ============= Botao Pesquisa =============
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
        self.btn_customer.place(x=570, y=38)
        
        
        # self.welcm_lbl = Label(self.frameCenter, text='Customer Page')
        # self.welcm_lbl.grid(row=0, column=1)

        # self.name_lbl = Label(self.frameCenter, text='name:')
        # self.name_lbl.grid(row=1, column=0)

        # self.name_entry = Entry(self.frameCenter)
        # self.name_entry.grid(row=1, column=1)

        # self.sbt = Button(self.frameCenter, text='login', command=self.clicked)
        # self.sbt.grid(row=2, column=1)
        

        # Frame Tree
        # funcao para mostrar
        def mostrar():
            # creating a treeview with dual scrollbars
            list_header = [
                            'Id', 
                           'Customer', 
                           'Contact', 
                           'Name Contact', 
                           'PhoneNumber', 
                           'Email', 
                           'Created'
                           ]

            df_list = fn_select_all_contact_form()

            global tree

            self.tree = ttk.Treeview(self.frameFooter, 
                                selectmode="extended",
                                columns=list_header, 
                                show="headings")
            
            # vertical scrollbar
            self.vsb = ttk.Scrollbar(
                self.frameFooter, orient="vertical", command= self.tree.yview)
            # horizontal scrollbar
            self.hsb = ttk.Scrollbar(
                self.frameFooter, orient="horizontal", command= self.tree.xview)

            self.tree.configure(yscrollcommand= self.vsb.set, xscrollcommand= self.hsb.set)

            self.tree.grid(column=0, row=0, sticky='nsew')
            self.vsb.grid(column=1, row=0, sticky='ns')
            self.hsb.grid(column=0, row=1, sticky='ew')
            self.frameFooter.grid_rowconfigure(0, weight=12)
            
            
            hd = ["center", "nw", "nw", "nw", "nw", "center", "center"]
            h = [30, 200, 60, 200, 100, 200, 80]
            n = 0

            for col in list_header:
                self.tree.heading(col, text=col.title(), anchor=CENTER)
                # adjust the column's width to the header string
                self.tree.column(col, width= h[n], anchor= hd[n])

                n += 1

            for item in df_list:
                self.tree.insert('', 'end', values=item)
                
        mostrar()

    def clicked(self):
        self.frameHeader.destroy()
        self.frameCenter.destroy()
        self.frameFooter.destroy()
        self.parent.changepage(0)