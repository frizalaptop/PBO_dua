from tkinter import Frame, Label, Button, Entry, StringVar, messagebox
from db.db_barang import Db_Barang

class UpdateBarang(Frame):
    def __init__(self, parent, id):
        super().__init__()
        self.id = id
        self.parent = parent
        self.item = self.getOne(self.id)
        self.render(self.parent)
        self.config(background='#FFFD8C')

    def render(self, parent):
        container = Frame(self, height=900)
        container.pack(pady=150)

        nama = StringVar()
        nama.set(self.item[1])
        harga = StringVar()
        harga.set(self.item[2])
        waktu = StringVar()
        waktu.set(self.item[3])
        jumlah = StringVar()
        jumlah.set(self.item[4])
        wakel = StringVar()
        wakel.set(self.item[6])
        jumkel = StringVar()
        jumkel.set(self.item[7])

        Label(container, text='Ubah Data Barang', font=('Tahoma', 12, 'bold'), fg='#424769', anchor='e',background='#F3CCF3', padx=200, pady=10).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        Label(container, text='Nama barang :', font=('Tahoma', 12, 'bold'), fg='#424769', width=15, anchor='e').grid(row=1, column=0, padx=25, pady=15)
        Entry(container, textvariable=nama, width=25, font=('Tahoma', 12, 'bold'), background='#F3CCF3', fg='#424769').grid(row=1, column=1, padx=25, pady=15)

        Label(container, text='Harga /Item :', font=('Tahoma', 12, 'bold'), fg='#424769', width=15, anchor='e').grid(row=2, column=0, padx=25, pady=15)
        Entry(container, textvariable=harga, width=25, font=('Tahoma', 12, 'bold'), background='#F3CCF3', fg='#424769').grid(row=2, column=1, padx=25, pady=15)

        Label(container, text='Waktu :', font=('Tahoma', 12, 'bold'), fg='#424769', width=15, anchor='e').grid(row=3, column=0, padx=25, pady=15)
        Entry(container, textvariable=waktu, state='readonly', width=25, font=('Tahoma', 12, 'bold'), background='#F3CCF3', fg='#424769').grid(row=3, column=1, padx=25, pady=15)
        
        Label(container, text='Jumlah :', font=('Tahoma', 12, 'bold'), fg='#424769', width=15, anchor='e').grid(row=4, column=0, padx=25, pady=15)
        Entry(container, textvariable=jumlah, width=25, font=('Tahoma', 12, 'bold'), background='#F3CCF3', fg='#424769').grid(row=4, column=1, padx=25, pady=15)

        Button(container, text='Simpan', width=15, font=('Tahoma', 12, 'bold'), command=lambda: self.update((nama,harga,waktu,jumlah,wakel,jumkel)), background='green', fg='white').grid(row=5, column=0, padx=25, pady=15, sticky='w')
        Button(container, text='Batalkan', width=15, font=('Tahoma', 12, 'bold'), command=lambda: self.clicked(self.parent), background='red', fg='white').grid(row=5, column=1, padx=25, pady=15, sticky='e')


    def clicked(self, parent):
        from .page_barang import Barang
        parent.page.destroy()
        parent.page = Barang(parent)
        parent.page.pack(fill='both',expand=True)

    def getOne(self, id):
        barang = Db_Barang()
        barang.id = id
        return barang.getOne()

    def update(self, value):
        if(not value[0].get() or not value[1].get() or not value[3]):
            messagebox.showerror('Error','Semua field harus diisi!')
            return False

        if not value[1].get().isdigit() or not value[3].get().isdigit():
            messagebox.showerror('Error', 'Jumlah dan Harga harus berupa angka!')
            return False
        
        if int(value[3].get()) < 1 or int(value[1].get()) < 1:
            messagebox.showerror('Error', 'Jumlah dan Harga harus di atas 0')
            return False
        
        barang = Db_Barang()
        barang.id = self.id
        barang.nama = value[0].get()
        barang.harga = value[1].get()
        barang.waktu = value[2].get()
        barang.jumlah = value[3].get()
        barang.wakel = value[4].get()
        barang.jumkel = value[5].get()
        update = barang.update()

        messagebox.showinfo('Success', 'Berhasil diedit')
        self.clicked(self.parent)