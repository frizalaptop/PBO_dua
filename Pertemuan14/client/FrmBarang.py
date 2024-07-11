import tkinter as tk
import json

from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Barang import *

class FrmBarang:
    
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
        Label(mainFrame, text='Kode:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Barang:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Harga:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        
        # Textbox
        self.txtKode = Entry(mainFrame) 
        self.txtKode.grid(row=0, column=1, padx=5, pady=5) 
        self.txtKode.bind("<Return>",self.onCari) # menambahkan event Enter key
        
        self.txtBarang = Entry(mainFrame) 
        self.txtBarang.grid(row=1, column=1, padx=5, pady=5) 
        
        self.txtHarga = Entry(mainFrame) 
        self.txtHarga.grid(row=2, column=1, padx=5, pady=5) 
     
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('id', 'kode', 'barang','harga')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('kode', text='Kode')
        self.tree.column('kode', width="60")
        self.tree.heading('barang', text='Barang')
        self.tree.column('barang', width="200")
        self.tree.heading('harga', text='Harga')
        self.tree.column('harga', width="30")
        
        # set tree position
        self.tree.place(x=0, y=200)

    def onClear(self, event=None):
        self.txtKode.delete(0,END)
        self.txtKode.insert(END,"")
        self.txtBarang.delete(0,END)
        self.txtBarang.insert(END,"")       
        self.txtHarga.delete(0,END)
        self.txtHarga.insert(END,"")       
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        barang = Barang()
        result = barang.getAllData()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"], d["kode"], d["nama_barang"], d["harga"]))
    
    def onCari(self, event=None):
        kode = self.txtKode.get()
        barang = Barang()
        a = barang.getByKode(kode)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
        
        
    def TampilkanData(self, event=None):
        kode = self.txtKode.get()
        barang = Barang()
        res = barang.getByKode(kode)
        self.txtBarang.delete(0,END)
        self.txtBarang.insert(END,barang.nama_barang)
        self.txtHarga.delete(0,END)
        self.txtHarga.insert(END,barang.harga)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from textbox
        kode = self.txtKode.get()
        nama_barang = self.txtBarang.get()
        harga = self.txtHarga.get()
        
        # create new Object
        barang = Barang()
        
        # set the atribute
        barang.kode = kode
        barang.nama_barang = nama_barang
        barang.harga = harga
        
        if(self.ditemukan==False):
            # save the record
            res = barang.simpan()
        else:
            # update the record
            res = barang.updateByKode(kode)
        
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        #clear the form input
        self.onClear()

    def onDelete(self, event=None):
        kode = self.txtKode.get()
        barang = Barang()
        barang.kode = kode
        if(self.ditemukan==True):
            res = barang.deleteByKode(kode)
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

if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmBarang(root2, "Aplikasi Data Barang")
    root2.mainloop() 