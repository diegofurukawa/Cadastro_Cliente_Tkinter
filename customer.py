from datetime import date
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Important Biblioteca TKCalendar
from tkcalendar import DateEntry

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
            c_name_customer = self.e_name.get()
            c_sales_man = self.e_salesman.get()
            n_phone_number = self.e_phonenumber.get()
            c_description = self.e_description.get()
            d_start_of_contract = self.e_startcontract.get_date()
            d_create_customer = date.today()

            lista_inserir = [c_name_customer.upper(), c_sales_man.upper(), n_phone_number.upper(), c_description.upper(),
                             d_start_of_contract, d_create_customer]

            if self.e_name.get() == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
            else:
                reply = messagebox.askquestion("Gravar", "Confirma que os dados estão corretos?", icon='warning')
                if reply == 'yes':
                    fn_insert_customer_form(lista_inserir)
                    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
                else:
                    messagebox.showinfo('Sucesso', 'Os dados foram descartados')

                self.e_name.delete(0, 'end')
                self.e_salesman.delete(0, 'end')
                self.e_phonenumber.delete(0, 'end')
                self.e_description.delete(0, 'end')
                self.e_startcontract.delete(0, 'end')
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

                self.e_name.delete(0, 'end')
                self.e_salesman.delete(0, 'end')
                self.e_phonenumber.delete(0, 'end')
                self.e_description.delete(0, 'end')
                self.e_startcontract.delete(0, 'end')
                # e_assunto.delete(0, 'end')

                self.e_name.insert(0, treev_lista[1])
                self.e_salesman.insert(0, treev_lista[2])
                self.e_phonenumber.insert(0, treev_lista[3])
                self.e_description.insert(0, treev_lista[4])
                self.e_startcontract.insert(0, treev_lista[5])

                # e_assunto.insert(0, treev_lista[6])

                def update():
                    c_name_customer = self.e_name.get()
                    c_sales_man = self.e_salesman.get()
                    n_phone_number = self.e_phonenumber.get()
                    c_description = self.e_description.get()
                    d_start_of_contract = self.e_startcontract.get_date()
                    d_create_customer = date.today()

                    lista_atualizar = [c_name_customer.upper(), c_sales_man.upper(), n_phone_number.upper(),
                                       c_description.upper(), d_start_of_contract, d_create_customer,
                                       valor]

                    if self.e_name.get() == '':
                        messagebox.showerror('Erro', 'Preencha todos os campos')
                    else:
                        fn_update_customer_form(lista_atualizar)

                        messagebox.showinfo(
                            'Sucesso', 'Os dados foram atualizados com sucesso')

                        self.e_name.delete(0, 'end')
                        self.e_salesman.delete(0, 'end')
                        self.e_phonenumber.delete(0, 'end')
                        self.e_description.delete(0, 'end')
                        self.e_startcontract.delete(0, 'end')
                        # date.delete(0, 'end')

                        for self.widget in self.frameFooter.winfo_children():
                            self.widget.destroy()

                        fn_mostrar()

                def cancel():
                    self.b_update.destroy()
                    self.b_cancel.destroy()
                    self.e_name.delete(0, 'end')
                    self.e_salesman.delete(0, 'end')
                    self.e_phonenumber.delete(0, 'end')
                    self.e_description.delete(0, 'end')
                    self.e_startcontract.delete(0, 'end')

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
            try:
                self.treev_dados = self.tree.focus()
                treev_dicionario = self.tree.item(self.treev_dados)
                treev_lista = treev_dicionario['values']
                valor = treev_lista[0]

                reply = messagebox.askquestion("Excluir", "Confirma a exclusão?", icon='warning')
                if reply == 'yes':
                    fn_del_customer_form([valor])
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

        # ====================================================================================================================================
        # Funcao DELETE - Fim
        # ====================================================================================================================================

        # Criando Labels
        self.lbl_name = Label(self.frameCenter, text=' Nome Cliente:', height=1, anchor=NW, font=('Ivy 10 bold'),
                              bg=co1, fg=co4)
        self.lbl_name.place(x=10, y=10)

        self.e_name = Entry(self.frameCenter, width=50, justify='left', relief=SOLID)
        self.e_name.place(x=130, y=11)

        # ====================================================================================================================================

        self.lbl_salesman = Label(self.frameCenter, text=' Vendedor:', height=1, anchor=NW, font=('Ivy 10 bold'),
                                  bg=co1, fg=co4)
        self.lbl_salesman.place(x=10, y=40)

        self.e_salesman = Entry(self.frameCenter, width=50, justify='left', relief=SOLID)
        self.e_salesman.place(x=130, y=41)

        # ====================================================================================================================================

        self.lbl_phonenumber = Label(self.frameCenter, text=' Telefone:', height=1, anchor=NW, font=('Ivy 10 bold'),
                                     bg=co1, fg=co4)
        self.lbl_phonenumber.place(x=10, y=70)

        self.e_phonenumber = Entry(self.frameCenter, width=50, justify='left', relief=SOLID)
        self.e_phonenumber.place(x=130, y=71)

        # ====================================================================================================================================

        self.lbl_description = Label(self.frameCenter, text=' Descrição:', height=1, anchor=NW, font=('Ivy 10 bold'),
                                     bg=co1, fg=co4)
        self.lbl_description.place(x=10, y=100)

        self.e_description = Entry(self.frameCenter, width=50, justify='left', relief=SOLID)
        self.e_description.place(x=130, y=101)

        # ====================================================================================================================================

        self.lbl_startcontract = Label(self.frameCenter,
                                       text='Contrato Desde:',
                                       height=1,
                                       anchor=NW,
                                       font=('Ivy 10 bold'),
                                       bg=co1,
                                       fg=co4)

        self.lbl_startcontract.place(x=10, y=130)

        self.e_startcontract = DateEntry(self.frameCenter,
                                         width=12,
                                         Background='darkblue',
                                         bordewidth=2,
                                         year=2023)
        self.e_startcontract.place(x=130, y=131)

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
                                 # command=self.clicked,
                                 image=self.search_img,
                                 width=95,
                                 text=' Busca'.upper(),
                                 compound=LEFT,
                                 anchor=NW,
                                 overrelief=RIDGE,
                                 font='Ivy 8',
                                 bg=co1,
                                 fg=co0)
        self.btn_search.place(x=570, y=8)

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
        self.btn_contact.place(x=570, y=38)

        # Frame Tree
        # funcao para fn_mostrar
        def fn_mostrar():
            # creating a treeview with dual scrollbars
            list_header = [
                'Id',
                'Name Customer',
                'Sales Man',
                'PhoneNumber',
                'Description',
                'Start Contract',
                'Created'
            ]

            df_list = fn_select_all_customer_form()

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

            hd = ["center", "nw", "nw", "center", "nw", "center", "center"]
            h = [30, 210, 130, 110, 200, 100, 100]
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
