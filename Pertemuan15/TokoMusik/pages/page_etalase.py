from tkinter import Frame, Label, Canvas, Scrollbar, Button, messagebox
from datetime import datetime
from .form_barang import Form
from .update_barang import UpdateBarang
from db.db_barang import Db_Barang
from db.db_admin import Db_Admin

class Etalase(Frame):
    def __init__(self, parent, username, state):
        super().__init__()
        self.parent = parent
        self.getUser = Db_Admin()
        self.username = username
        self.state = state
        self.render()
        self.config(background='white')

    def render(self):
        items = sorted(self.getAll(), key=lambda item: item[1])
        Button(self, text='Tambah Barang', width=15, font=('Tahoma', 12, 'bold'), background='blue', fg='white', command=lambda: self.clicked(self.parent, Form, self.username, self.state)).pack(side='bottom', pady=10)
        
        canvas = Canvas(self, bg='#9EB8D9')
        canvas.pack(side='left', fill='both', expand=True)

        scrollbar = Scrollbar(self, orient='vertical', command=canvas.yview)
        scrollbar.pack(side='right', fill='y')

        canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = Frame(canvas, bg='#9EB8D9')
        canvas.create_window((50, 10), window=content_frame, anchor='nw')

        container = Frame(content_frame, background='#EBD9B4')
        container.pack(pady=5, fill='both', expand=True)
        Label(container, bg='#EBD9B4', text="Nama Barang", width=40, font=('Tahoma', 10, 'bold'),anchor='w').grid(row=0, column=0)
        Label(container,  bg='#EBD9B4', text="Harga", width=40, font=('Tahoma', 10, 'bold'), anchor='center', justify='center').grid(row=0, column=1)
        Label(container, bg='#EBD9B4', text="Tersedia", width=20, font=('Tahoma', 10, 'bold'),anchor='w').grid(row=0, column=2)

        for item in items:
            container = Frame(content_frame)
            container.pack(pady=5, fill='both', expand=True)
            Label(container, text=f"{item[1]}", width=40, font=('Tahoma', 10, 'bold'), fg='#424769',anchor='w').grid(row=0, column=0)
            Label(container, text=f"{item[2]:,.0f}", width=40, font=('Tahoma', 10, 'bold'), fg='#424769', anchor='center', justify='center').grid(row=0, column=1)
            Label(container, text=f"{item[3]}", width=20, font=('Tahoma', 10, 'bold'), fg='#424769',anchor='w').grid(row=0, column=2)
            
            Button(container, command=lambda id=item[0]: self.updatePage(self.parent, UpdateBarang, id), text='Ubah', width=15, font=('Tahoma', 8, 'bold'), background='orange', fg='white').grid(row=0, column=3)
            Button(container, command=lambda id=item[0]: self.delete(id), text='Hapus', width=15, font=('Tahoma', 8, 'bold'), background='red', fg='white').grid(row=0, column=4)

            content_frame.update_idletasks()

        canvas.bind('<Configure>', lambda event, canvas=canvas: self.on_canvas_configure(canvas))

    def on_canvas_configure(self, canvas):
        canvas.configure(scrollregion=canvas.bbox('all'))
    
    def clicked(self, parent, page, username, state):
        parent.page.destroy()
        parent.page = page(parent, username, state)
        parent.page.pack(fill='both',expand=True)

    def getAll(self):
        src = Db_Barang().getAll()
        return src
    
    def delete(self, id):
        if messagebox.askyesno('Hapus Barang', 'Apakah anda yakin ingin menghapus?' , icon='warning'):
            src = Db_Barang()
            src.id = id
            src.deleteOne()
            messagebox.showinfo('Hapus Barang', 'Berhasil menghapus data', icon='info')
            self.clicked(self.parent, Etalase, self.username, self.state)
        
    
    def updatePage(self, parent, page, id):
        parent.page.destroy()
        parent.page = page(parent, id)
        parent.page.pack(fill='both',expand=True)
        
    def keluar(self, id_barang):
        barang = Db_Barang()
        barang.id = id_barang
        result = barang.getOne()
        if result[4] == 0:
            messagebox.showinfo('warning', 'Stok barang habis')
            return False
        barang.nama = result[1]
        barang.harga = result[2]
        barang.waktu = result[3]
        barang.jumlah = result[4] - 1
        barang.jumkel = result[7] + 1
        barang.keluar = 1
        barang.wakel = self.setDate()
        barang.update()
        self.clicked(self.parent, Etalase, '')
        messagebox.showinfo('Success', 'Barang telah keluar')
        
    def setDate(self):
        current_cal = datetime.now()
        current = current_cal.strftime('%d-%B-%Y %H:%M')
        return current
