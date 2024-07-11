import tkinter as tk
import json

from tkinter import Frame,Label,Entry,Button,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Tokoroti import *

class FrmTokoroti:
     
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = False
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='Kode Produk:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Nama:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Stok:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        
        # Textbox
        self.txtKd_produk = Entry(mainFrame) 
        self.txtKd_produk.grid(row=0, column=1, padx=5, pady=5) 
        self.txtKd_produk.bind("<Return>",self.onCari) # menambahkan event Enter key
        
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5) 
        self.txtStok = Entry(mainFrame) 
        self.txtStok.grid(row=2, column=1, padx=5, pady=5) 
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('id', 'kd_produk', 'nama','stok')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('kd_produk', text='KODE')
        self.tree.column('kd_produk', width="60")
        self.tree.heading('nama', text='NAMA')
        self.tree.column('nama', width="200")
        self.tree.heading('stok', text='STOK')
        self.tree.column('stok', width="60")
        
        # set tree position
        self.tree.place(x=0, y=200)

    def onClear(self, event=None):
        self.txtKd_produk.delete(0,END)
        self.txtKd_produk.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")       
        self.txtStok.delete(0,END)
        self.txtStok.insert(END,"")       
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        tokoRoti = Tokoroti()
        result = tokoRoti.getAllData()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"], d["kd_produk"], d["nama"], d["stok"]))
    
    def onCari(self, event=None):
        kode = self.txtKd_produk.get()
        tokoRoti = Tokoroti()
        a = tokoRoti.getByKd_produk(kode)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
        
        
    def TampilkanData(self, event=None):
        kd_produk = self.txtKd_produk.get()
        tokoRoti = Tokoroti()
        res = tokoRoti.getByKd_produk(kd_produk)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,tokoRoti.nama)
        self.txtStok.delete(0,END)
        self.txtStok.insert(END,tokoRoti.stok)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from textbox
        kd_produk = self.txtKd_produk.get()
        nama = self.txtNama.get()
        stok = self.txtStok.get()
        
        # create new Object
        tokoRoti = Tokoroti()
        
        # set the atribute
        tokoRoti.kd_produk = kd_produk
        tokoRoti.nama = nama
        tokoRoti.stok = stok
        
        if(self.ditemukan==False):
            # save the record
            res = tokoRoti.simpan()
        else:
            # update the record
            res = tokoRoti.updateByKd_produk(kd_produk)
        
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()

    def onDelete(self, event=None):
        kd_produk = self.txtKd_produk.get()
        tokoRoti = Tokoroti()
        tokoRoti.kd_produk = kd_produk
        if(self.ditemukan==True):
            res = tokoRoti.deleteByKd_produk(kd_produk)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

root2 = tk.Tk()
aplikasi = FrmTokoroti(root2, "Aplikasi Toko Roti")
root2.mainloop() 
