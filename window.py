from tkinter import Tk
from contact import ContactPage
from customer import CustomerPage
from janela import ConfigWindow

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

class MainGui:
    def __init__(self, root, title, geometry):

        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        self.PageShow = CustomerPage(self, self.root)

    def changepage(self, page):
        self.page = page

        if self.page == 0:
            # del self.pageshow
            self.PageShow = CustomerPage(self, self.root)

        if self.page == 1:
            # del self.pageshow
            self.PageShow = ContactPage(self, self.root)

        
        
def main():
    root = Tk()
    w = ConfigWindow()
    MainGui(root, w.title, w.width+'x'+w.height)
    root.mainloop()