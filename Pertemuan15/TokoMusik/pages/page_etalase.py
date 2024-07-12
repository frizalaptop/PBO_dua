from tkinter import Frame, Label, Canvas, Scrollbar, Button, messagebox
import json
from .form_barang import Form
from .update_barang import UpdateBarang
from db.Barang import *
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
        items = sorted(self.getAll(), key=lambda item: item['nama'])
        Button(self, text='Tambah Barang', width=15, font=('Tahoma', 12, 'bold'), background='blue', fg='white', command=lambda: self.clicked(self.parent, Form, self.username, self.state)).pack(side='bottom', pady=10)
        
        canvas = Canvas(self, bg='#FEFBD8')
        canvas.pack(side='left', fill='both', expand=True)

        scrollbar = Scrollbar(self, orient='vertical', command=canvas.yview)
        scrollbar.pack(side='right', fill='y')

        canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = Frame(canvas, bg='#FEFBD8')
        canvas.create_window((50, 10), window=content_frame, anchor='nw')

        container = Frame(content_frame, background='#EECEB9')
        container.pack(pady=5, fill='both', expand=True)
        Label(container, bg='#EECEB9', text="Nama Barang", width=50, font=('Tahoma', 10, 'bold'),anchor='w').grid(row=0, column=0)
        Label(container,  bg='#EECEB9', text="Harga", width=50, font=('Tahoma', 10, 'bold'), anchor='center', justify='center').grid(row=0, column=1)
        Label(container, bg='#EECEB9', text="Tersedia", width=20, font=('Tahoma', 10, 'bold'),anchor='center').grid(row=0, column=2)

        for item in items:
            container = Frame(content_frame)
            container.pack(pady=5, fill='both', expand=True)
            Label(container, text=f"{item['nama']}", width=50, font=('Tahoma', 10, 'bold'), fg='#424769', background='#E7D4B5',anchor='w').grid(row=0, column=0)
            Label(container, text=f"{int(item['harga']):,.0f}", width=50, font=('Tahoma', 10, 'bold'), fg='#424769', background='#E7D4B5', anchor='center', justify='center').grid(row=0, column=1)
            Label(container, text=f"{item['available']}", width=20, font=('Tahoma', 10, 'bold'), fg='#424769', background='#E7D4B5',anchor='center', justify='center').grid(row=0, column=2)
            
            Button(container, command=lambda id=item['id']: self.updatePage(self.parent, UpdateBarang, id, self.username), text='Ubah', width=15, font=('Tahoma', 8, 'bold'), background='orange', fg='white').grid(row=0, column=3)
            Button(container, command=lambda id=item['id']: self.delete(id), text='Hapus', width=15, font=('Tahoma', 8, 'bold'), background='red', fg='white').grid(row=0, column=4)

            content_frame.update_idletasks()

        canvas.bind('<Configure>', lambda event, canvas=canvas: self.on_canvas_configure(canvas))

    def on_canvas_configure(self, canvas):
        canvas.configure(scrollregion=canvas.bbox('all'))
    
    def clicked(self, parent, page, username, state):
        parent.page.destroy()
        parent.page = page(parent, username, state)
        parent.page.pack(fill='both',expand=True)

    def getAll(self):
        barang = Barang()
        result = barang.getAllData()
        parse_data = json.loads(result)
        return parse_data
    
    def delete(self, id):
        if messagebox.askyesno('Hapus Barang', 'Apakah anda yakin ingin menghapus?' , icon='warning'):
            src = Barang()
            delete = src.deleteById(id)
            res = json.loads(delete)
            messagebox.showinfo(res['status'], res['message'], icon='info')
            self.clicked(self.parent, Etalase, self.username, self.state)
        
    
    def updatePage(self, parent, page, id, username):
        parent.page.destroy()
        parent.page = page(parent, id, username)
        parent.page.pack(fill='both',expand=True)
        