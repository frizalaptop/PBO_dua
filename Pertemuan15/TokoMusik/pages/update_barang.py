from tkinter import Frame, Label, Button, Entry, StringVar, messagebox, ttk
from db.Barang import *
from db.Admin import *

class UpdateBarang(Frame):
    def __init__(self, parent, id, username):
        super().__init__()
        self.id = id
        self.parent = parent
        self.item = self.getOne(self.id)
        [self.user] = self.getOneUser(username)
        self.username = self.user['username']
        self.inLogin = self.user['hasLogin']
        self.render(self.parent)
        self.config(background='#FFFD8C')

    def render(self, parent):
        container = Frame(self, height=900, background='#EECEB9')
        container.pack(pady=150)

        nama = StringVar()
        nama.set(self.item['nama'])
        harga = StringVar()
        harga.set(self.item['harga'])

        Label(container, text='Ubah Data Alat Musik', font=('Tahoma', 12, 'bold'), fg='white', anchor='e',background='#BB9AB1', padx=200, pady=10).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        Label(container, text='Nama :', font=('Tahoma', 12, 'bold'), fg='#424769', width=15 , background='#EECEB9', anchor='e').grid(row=1, column=0, padx=25, pady=15)
        Entry(container, textvariable=nama, width=25, font=('Tahoma', 12, 'bold'), background='white', fg='#424769').grid(row=1, column=1, padx=25, pady=15)

        Label(container, text='Harga :', font=('Tahoma', 12, 'bold'), fg='#424769', width=15 , background='#EECEB9', anchor='e').grid(row=2, column=0, padx=25, pady=15)
        Entry(container, textvariable=harga, width=25, font=('Tahoma', 12, 'bold'), background='white', fg='#424769').grid(row=2, column=1, padx=25, pady=15)
    
        Label(container, text='Tersedia :', font=('Tahoma', 12, 'bold'), fg='#424769', width=15 , background='#EECEB9', anchor='e').grid(row=3, column=0, padx=25, pady=15)
        option_box = ttk.Combobox(container, values=['YES', 'NO'], state='readonly', width=25, font=('Tahoma', 12, 'bold'))
        option_box.set(self.item['available'])
        option_box.grid(row=3, column=1, padx=25, pady=15)

        Button(container, text='Perbarui', width=15, font=('Tahoma', 12, 'bold'), command=lambda: self.update((self.id,nama,harga,option_box, self.username,self.inLogin)), background='green', fg='white').grid(row=4, column=0, padx=25, pady=15, sticky='w')
        Button(container, text='Batalkan', width=15, font=('Tahoma', 12, 'bold'), command=lambda: self.clicked(self.parent, self.username, self.inLogin), background='red', fg='white').grid(row=4, column=1, padx=25, pady=15, sticky='e')

  

    def clicked(self, parent, username, state):
        from .page_etalase import Etalase
        parent.page.destroy()
        parent.page = Etalase(parent, username, state)
        parent.page.pack(fill='both',expand=True)

    def getOne(self, id):
        barang = Barang()
        [result] = barang.getById(id)
        return result
    
    def getOneUser(self, username):
        barang = Admin()
        return barang.getByUsername(username)

    def update(self, value):
        if(not value[1].get() or not value[2].get()):
            messagebox.showerror('Error','Semua field harus diisi!')
            return False

        if not value[2].get().isdigit():
            messagebox.showerror('Error', 'Harga harus berupa angka!')
            return False
        
        if int(value[2].get()) < 1:
            messagebox.showerror('Error', 'Jumlah dan Harga harus di atas 0')
            return False
        
        barang = Barang()
        barang.nama = value[1].get()
        barang.harga = value[2].get()
        barang.available = value[3].get()
        update = barang.updateById(value[0])
        res = json.loads(update)
        messagebox.showinfo(res['status'], res['message'])
        self.clicked(self.parent, value[4], value[5])