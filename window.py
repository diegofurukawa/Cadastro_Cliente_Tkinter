from contact import *
from customer import *

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
        self.PageShow = customer_page(self, self.root)

    def changepage(self, page):
        self.page = page

        if self.page == 0:
            # del self.pageshow
            self.PageShow = customer_page(self, self.root)

        if self.page == 1:
            # del self.pageshow
            self.PageShow = Contact_Page(self, self.root)


def main():
    root = Tk()
    MainGui(root, "Main Window", "900x600")
    root.mainloop()


if __name__ == '__main__':
    main()
