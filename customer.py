from datetime import date
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Important Biblioteca TKCalendar
from tkcalendar import DateEntry

from icons import img_form_customer, img_form_contact, img_customer, img_delete, img_refresh, img_insert, img_search, img_save, img_contact
#from delete import *
# from insert import *
# from update import *
# from view import *

from customersql import cCustomerClass

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


class customer_page:
    
    def __init__(self, parent, window):
                
        self.tree = None
        self.parent = parent

        self.frameHeader = Frame(window, width=899, height=50, bg=co1, relief=FLAT)
        self.frameHeader.grid(row=0, column=0)
        # self.frameCenter.pack()

        self.app_logo = img_form_customer()
        self.app_logo = Label(self.frameHeader,
                              image=self.app_logo,
                              text=" Cadastro de Cliente",
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
            customer = cCustomerClass()
            
            customer.idCustomer = self.txt_idcustomer.get()
            customer.cName = self.txt_name.get()
            customer.cNameSales = self.txt_salesman.get()
            customer.cPhone = self.txt_phonenumber.get()
            customer.cEmail = ""
            customer.cDescription = self.txt_description.get()
            customer.dStartOfContract = self.txt_startcontract.get()
            customer.dCreate = str(date.today())

            if (self.txt_name.get() == ''
                or self.txt_salesman.get() == ''
                or self.txt_phonenumber.get() == ''
                or self.txt_startcontract.get() == ''):
                messagebox.showerror('Erro', 'Preencha todos os campos')
            else:
                reply = messagebox.askquestion("Gravar", "Confirma que os dados estão corretos?", icon='warning')
                if reply == 'yes':
                    #fn_insert_customer_form(lista_inserir)
                    customer.InsertCustomer()
                    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
                else:
                    messagebox.showinfo('Sucesso', 'Os dados foram descartados')

                self.txt_idcustomer.delete(0, 'end')
                self.txt_name.delete(0, 'end')
                self.txt_salesman.delete(0, 'end')
                self.txt_phonenumber.delete(0, 'end')
                self.txt_description.delete(0, 'end')
                self.txt_startcontract.delete(0, 'end')
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

                self.txt_idcustomer.delete(0, 'end')
                self.txt_name.delete(0, 'end')
                self.txt_salesman.delete(0, 'end')
                self.txt_phonenumber.delete(0, 'end')
                self.txt_description.delete(0, 'end')
                self.txt_startcontract.delete(0, 'end')
                # e_assunto.delete(0, 'end')

                
                self.txt_idcustomer.insert(0, treev_lista[0])
                self.txt_name.insert(0, treev_lista[1])
                self.txt_salesman.insert(0, treev_lista[2])
                self.txt_phonenumber.insert(0, treev_lista[3])
                #self.txt_email.insert(0, treev_lista[3])
                self.txt_description.insert(0, treev_lista[5])
                self.txt_startcontract.insert(0, treev_lista[6])

                # e_assunto.insert(0, treev_lista[6])

                def update():
                    customer = cCustomerClass()
                    
                    customer.idCustomer = self.txt_idcustomer.get()
                    customer.cName = self.txt_name.get()
                    customer.cNameSales = self.txt_salesman.get()
                    customer.cPhone = self.txt_phonenumber.get()
                    customer.cEmail = ""
                    customer.cDescription = self.txt_description.get()
                    customer.dStartOfContract = self.txt_startcontract.get()
                    customer.dCreate = str(date.today())

                    if self.txt_name.get() == '':
                        messagebox.showerror('Erro', 'Preencha todos os campos')
                    else:
                        #fn_update_customer_form(lista_atualizar)
                        customer.UpdateCustomer()

                        messagebox.showinfo(
                            'Sucesso', 'Os dados foram atualizados com sucesso')

                        self.txt_name.delete(0, 'end')
                        self.txt_salesman.delete(0, 'end')
                        self.txt_phonenumber.delete(0, 'end')
                        self.txt_description.delete(0, 'end')
                        self.txt_startcontract.delete(0, 'end')
                        # date.delete(0, 'end')

                        for self.widget in self.frameFooter.winfo_children():
                            self.widget.destroy()

                        fn_mostrar()

                def cancel():
                    self.b_update.destroy()
                    self.b_cancel.destroy()
                    self.txt_name.delete(0, 'end')
                    self.txt_salesman.delete(0, 'end')
                    self.txt_phonenumber.delete(0, 'end')
                    self.txt_description.delete(0, 'end')
                    self.txt_startcontract.delete(0, 'end')

                    for self.widget in self.frameFooter.winfo_children():
                        self.widget.destroy()

                    fn_mostrar()

                fn_mostrar()

                # ============= Botao Update =============
                self.b_update = Button(self.frameCenter, command=update, text="Confirmar".upper(), width=13, height=1,
                                       bg=co2, fg=co1,
                                       font=('ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
                self.b_update.place(x=450, y=102)

                self.b_cancel = Button(self.frameCenter, command=cancel, text="Cancelar".upper(), width=13, height=1,
                                       bg=co7, fg=co1,
                                       font=('ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
                self.b_cancel.place(x=450, y=132)

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
            customer = cCustomerClass()
            try:
                self.treev_dados = self.tree.focus()
                treev_dicionario = self.tree.item(self.treev_dados)
                treev_lista = treev_dicionario['values']
                valor = treev_lista[0]

                reply = messagebox.askquestion("Excluir", "Confirma a exclusão?", icon='warning')
                if reply == 'yes':
                    #fn_del_customer_form([valor])
                    customer.DeleteCustomer()
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
            customer = cCustomerClass()

            idCustomer = self.txt_idcustomer.get()

            customer.SelectCustomerId(idCustomer)

            self.txt_idcustomer.delete(0, END)
            self.txt_idcustomer.insert(INSERT, customer.idCustomer)

            self.txt_idcustomer.delete(0, 'end')
            self.txt_name.delete(0, 'end')
            self.txt_salesman.delete(0, 'end')
            self.txt_phonenumber.delete(0, 'end')
            self.txt_description.delete(0, 'end')
            self.txt_startcontract.delete(0, 'end')


            self.txt_idcustomer.insert(INSERT, customer.idCustomer)
            self.txt_name.insert(INSERT, customer.cName)
            self.txt_salesman.insert(INSERT, customer.cNameSales)
            self.txt_phonenumber.insert(INSERT, customer.cPhone)
            #self.txt_email.insert(0, treev_lista[3])
            self.txt_description.insert(INSERT, customer.cDescription)
            self.txt_startcontract.insert(INSERT, customer.dStartOfContract)
                        
            
            

        # ====================================================================================================================================
        # Funcao DELETE - Fim
        # ====================================================================================================================================

        # Criando Labels
        # ====================================================================================================================================

        self.lbl_idcustomer = Label(self.frameCenter, text=' Id Cliente:', height=1, anchor=NW, font='Ivy 10 bold',
                                    bg=co1, fg=co4)
        self.lbl_idcustomer.place(x=10, y=10)

        self.txt_idcustomer = Entry(self.frameCenter, width=25, justify='left', relief=SOLID)
        self.txt_idcustomer.place(x=130, y=11)
        
        # ====================================================================================================================================
        
        self.lbl_name = Label(self.frameCenter, text=' Nome Cliente:', height=1, anchor=NW, font='Ivy 10 bold',
                              bg=co1, fg=co4)
        self.lbl_name.place(x=10, y=40)

        self.txt_name = Entry(self.frameCenter, width=50, justify='left', relief=SOLID)
        self.txt_name.place(x=130, y=41)

        # ====================================================================================================================================

        self.lbl_salesman = Label(self.frameCenter, text=' Vendedor:', height=1, anchor=NW, font='Ivy 10 bold',
                                  bg=co1, fg=co4)
        self.lbl_salesman.place(x=10, y=70)

        self.txt_salesman = Entry(self.frameCenter, width=50, justify='left', relief=SOLID)
        self.txt_salesman.place(x=130, y=71)

        # ====================================================================================================================================

        self.lbl_phonenumber = Label(self.frameCenter, text=' Telefone:', height=1, anchor=NW, font='Ivy 10 bold',
                                     bg=co1, fg=co4)
        self.lbl_phonenumber.place(x=10, y=100)

        self.txt_phonenumber = Entry(self.frameCenter, width=50, justify='left', relief=SOLID)
        self.txt_phonenumber.place(x=130, y=101)

        # ====================================================================================================================================

        self.lbl_description = Label(self.frameCenter, text=' Descrição:', height=1, anchor=NW, font='Ivy 10 bold',
                                     bg=co1, fg=co4)
        self.lbl_description.place(x=10, y=130)

        self.txt_description = Entry(self.frameCenter, width=50, justify='left', relief=SOLID)
        self.txt_description.place(x=130, y=131)

        # ====================================================================================================================================

        self.lbl_startcontract = Label(self.frameCenter,
                                       text='Contrato Desde:',
                                       height=1,
                                       anchor=NW,
                                       font=('Ivy 10 bold'),
                                       bg=co1,
                                       fg=co4)

        self.lbl_startcontract.place(x=10, y=160)

        self.txt_startcontract = DateEntry(self.frameCenter,
                                         width=12,
                                         Background='darkblue',
                                         bordewidth=2,
                                         year=2023)
        self.txt_startcontract.place(x=130, y=161)


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
        self.contact_img = img_contact()
        self.btn_contact = Button(self.frameCenter,
                                  command=self.clicked,
                                  image=self.contact_img,
                                  width=95,
                                  text=' Contatos'.upper(),
                                  compound=LEFT,
                                  anchor=NW,
                                  overrelief=RIDGE,
                                  font='Ivy 8',
                                  bg=co1,
                                  fg=co0)
        self.btn_contact.place(x=570, y=8)

        # Frame Tree
        # funcao para fn_mostrar
        def fn_mostrar():
            customer = cCustomerClass()
            # creating a treeview with dual scrollbars
            list_header = [
                'Id',
                'Name Customer',
                'Sales Man',
                'PhoneNumber',
                'E-mail',
                'Description',
                'Start Contract',
                'Created'
            ]

            #df_list = fn_select_all_customer_form()
            df_list = customer.SelectCustomerAll()
            
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

            hd = ["center", "nw", "nw", "center", "nw", "center", "center", "center"]
            h = [30, 200, 110, 100, 170, 100, 80, 70]
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
        self.parent.changepage(1)
