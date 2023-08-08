# pip install pillow
# pip install tkcalendar

# Importando Biblioteca Pillow
from PIL import Image, ImageTk


# ============= Imagem Form =============
def img_form_customer():
    img_customer_header = Image.open('icons/ico_customer_202308.png')
    img_customer_header = img_customer_header.resize((45, 45))
    img_customer_header = ImageTk.PhotoImage(img_customer_header)

    return img_customer_header

# ============= Imagem Form =============
def img_form_contact():
    img_contact_header = Image.open('icons/livro-de-enderecos.png')
    img_contact_header = img_contact_header.resize((45, 45))
    img_contact_header = ImageTk.PhotoImage(img_contact_header)

    return img_contact_header


# ============= Imagem Form =============
def img_customer():
    app_img_customer = Image.open('icons/customer.png')
    app_img_customer = app_img_customer.resize((17, 17))
    app_img_customer = ImageTk.PhotoImage(app_img_customer)

    return app_img_customer


# ============= Botao Delete =============
def img_delete():
    img_del = Image.open('icons/icon_customer.png')
    img_del = img_del.resize((17, 17))
    img_del = ImageTk.PhotoImage(img_del)

    return img_del


# ============= Botao Refresh =============
def img_refresh():
    img_ref = Image.open('icons/updated.png')
    img_ref = img_ref.resize((17, 17))
    img_ref = ImageTk.PhotoImage(img_ref)

    return img_ref


# ============= Botao Inserir =============
def img_insert():
    img_add = Image.open('icons/save-file.png')
    img_add = img_add.resize((17, 17))
    img_add = ImageTk.PhotoImage(img_add)

    return img_add


# ============= Botao Buscar =============
def img_search():
    img_search_ico = Image.open('icons/search (1).png')
    img_search_ico = img_search_ico.resize((17, 17))
    img_search_ico = ImageTk.PhotoImage(img_search_ico)

    return img_search_ico


# ============= Botao Salvar =============
def img_save():
    img_save_ico = Image.open('icons/search (1).png')
    img_save_ico = img_save_ico.resize((17, 17))
    img_save_ico = ImageTk.PhotoImage(img_save_ico)

    return img_save_ico


# ============= Botao Contatos =============
def img_contact():
    img_contact_ico = Image.open('icons/contact.png')
    img_contact_ico = img_contact_ico.resize((17, 17))
    img_contact_ico = ImageTk.PhotoImage(img_contact_ico)

    return img_contact_ico
