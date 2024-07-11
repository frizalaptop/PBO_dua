import tkinter as tk
from tkinter import Frame, Label, Button
from FrmBarang import FrmBarang
from FrmCustomer import FrmCustomer

class FrmHome:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("300x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=tk.BOTH, expand=tk.YES)

        Label(mainFrame, text='Laporan apa yang ingin Anda lihat?').pack(pady=10)

        self.btnCustomer = Button(mainFrame, text='Customer', command=self.openCustomer, width=20)
        self.btnCustomer.pack(pady=5)

        self.btnBarang = Button(mainFrame, text='Barang', command=self.openBarang, width=20)
        self.btnBarang.pack(pady=5)

    def openCustomer(self):
        newWindow = tk.Toplevel(self.parent)
        app = FrmCustomer(newWindow, "Aplikasi Data Customer")

    def openBarang(self):
        newWindow = tk.Toplevel(self.parent)
        app = FrmBarang(newWindow, "Aplikasi Data Barang")

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FrmHome(root, "Menu Utama Laporan")
    root.mainloop()
