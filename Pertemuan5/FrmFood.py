import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Food import Food

class FormMahasiswa:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label

        Label(mainFrame, text='Nama:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Level Pedas:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtLevel = Entry(mainFrame) 
        self.txtLevel.grid(row=2, column=1, padx=5, pady=5)   
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('id', 'nama', 'lv_pedas')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('nama', text='Nama')
        self.tree.column('nama', width="60")
        self.tree.heading('lv_pedas', text='Level Pedas')
        self.tree.column('lv_pedas', width="200")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtLevel.delete(0,END)
        self.txtLevel.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")       
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        mhs = Food()
        result = mhs.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        nim = self.txtNIM.get()
        mhs = Food()
        res = mhs.getByNIM(nim)
        rec = mhs.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNama.focus()
        return res
        
    def TampilkanData(self, event=None):
        nim = self.txtNIM.get()
        mhs = Food()
        res = mhs.getByNIM(nim)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,mhs.nama)
        jk = mhs.jk
        if(jk=="P"):
            self.P.select()
        else:
            self.L.select()
        self.txtKodeProdi.set(mhs.kode_prodi)   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        nama = self.txtNama.get()
        lv_pedas = self.txtLevel.get()
        
        food = Food()
        food.nama = nama
        food.lv_pedas = lv_pedas
        if(self.ditemukan==True):
            res = food.updateByNIM(id)
            ket = 'Diperbarui'
        else:
            res = food.simpan()
            ket = 'Disimpan'
            
        rec = food.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        nim = self.txtNIM.get()
        mhs = Food()
        mhs.nim = nim
        if(self.ditemukan==True):
            res = mhs.deleteByNIM(nim)
            rec = mhs.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormMahasiswa(root, "Aplikasi Data Mahasiswa")
    root.mainloop() 