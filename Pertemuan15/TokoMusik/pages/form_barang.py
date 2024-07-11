from tkinter import Frame, Label, Button, Entry, StringVar, messagebox, ttk
from datetime import datetime
from db.db_barang import Db_Barang

class Form(Frame):
    def __init__(self,parent, username, state):
        super().__init__()
        self.parent = parent
        self.username = username
        self.state = state
        self.render()
        self.config(background='#FFFD8C')

    def render(self):
        container = Frame(self, height=900)
        container.pack(pady=150)

        nama = StringVar()
        harga = StringVar()

        Label(container, text='Input Data Alat Musik', font=('Tahoma', 12, 'bold'), fg='#424769', anchor='e',background='#F3CCF3', padx=200, pady=10).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        Label(container, text='Nama :', font=('Tahoma', 12, 'bold'), fg='#424769', width=15, anchor='e').grid(row=1, column=0, padx=25, pady=15)
        Entry(container, textvariable=nama, width=25, font=('Tahoma', 12, 'bold'), background='#F3CCF3', fg='#424769').grid(row=1, column=1, padx=25, pady=15)

        Label(container, text='Harga :', font=('Tahoma', 12, 'bold'), fg='#424769', width=15, anchor='e').grid(row=2, column=0, padx=25, pady=15)
        Entry(container, textvariable=harga, width=25, font=('Tahoma', 12, 'bold'), background='#F3CCF3', fg='#424769').grid(row=2, column=1, padx=25, pady=15)

        Label(container, text='Tersedia :', font=('Tahoma', 12, 'bold'), fg='#424769', width=15, anchor='e').grid(row=3, column=0, padx=25, pady=15)
        option_box = ttk.Combobox(container, values=['YES', 'NO'], state='readonly', width=25, font=('Tahoma', 12, 'bold'))
        option_box.set('YES')
        option_box.grid(row=3, column=1, padx=25, pady=15)

        Button(container, text='Submit', width=15, font=('Tahoma', 12, 'bold'), command=lambda: self.create((nama,harga, option_box)), background='green', fg='white').grid(row=5, column=0, padx=25, pady=15, sticky='w')
        Button(container, text='Batal', width=15, font=('Tahoma', 12, 'bold'), command=lambda: self.clicked(self.parent, self.username, self.state), background='red', fg='white').grid(row=5, column=1, padx=25, pady=15, sticky='e')

    def clicked(self, parent, username, state):
        from .page_etalase import Etalase
        parent.page.destroy()
        parent.page = Etalase(parent, username, state)
        parent.page.pack(fill='both',expand=True)

    def create(self, value):
        barang = Db_Barang()
        barang.nama = value[0].get()
        barang.harga = value[1].get()
        barang.available = value[2].get()

        if not barang.nama or not barang.harga or not barang.available:
            messagebox.showerror('Error','Semua field harus diisi!')
            return False
        
        validatenama = barang.getOne()
        if (validatenama):
            messagebox.showerror("error", "Barang sudah ada")
            return False
        
        barang.create()
        messagebox.showinfo('Success', 'Barang berhasil ditambahkan')
        self.clicked(self.parent, self.username, self.state)
    
    
    def setDate(self):
        current_cal = datetime.now()
        current = current_cal.strftime('%d-%B-%Y %H:%M')
        return current