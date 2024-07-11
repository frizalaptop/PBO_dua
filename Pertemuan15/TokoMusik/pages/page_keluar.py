from tkinter import Frame, Label, Canvas, Scrollbar, Button, messagebox
from db.db_barang import Db_Barang
from datetime import datetime


class BarangKeluar(Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.render(self.parent)
        self.config(background='white')

    def render(self, parent):
        items = sorted(self.getAll(), key=lambda item: item[1])        
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
        Label(container, bg='#EBD9B4', text="harga", width=30, font=('Tahoma', 10, 'bold'),anchor='w').grid(row=0, column=1)
        Label(container, bg='#EBD9B4', text="Jumlah", width=10, font=('Tahoma', 10, 'bold'),anchor='w').grid(row=0, column=2)
        Label(container, bg='#EBD9B4', text="Tanggal keluar", width=45, font=('Tahoma', 10, 'bold'),anchor='w').grid(row=0, column=3)

        for item in items:
            container = Frame(content_frame)
            container.pack(pady=5, fill='both', expand=True)
            Label(container, text=f"{item[1]}", width=40, font=('Tahoma', 10, 'bold'), fg='#424769',anchor='w').grid(row=0, column=0)
            Label(container, text=f"{item[2]:,.0f}", width=30, font=('Tahoma', 10, 'bold'), fg='#424769',anchor='w').grid(row=0, column=1)
            Label(container, text=f"{item[7]}", width=10, font=('Tahoma', 10, 'bold'), fg='#424769',anchor='w').grid(row=0, column=2)
            Label(container, text=f"{item[6]}", width=45, font=('Tahoma', 10, 'bold'), fg='#424769',anchor='w').grid(row=0, column=3)
            Button(container, command=lambda id=item[0]: self.bersihkan(id), text='Bersihkan',width=15, font=('Tahoma', 8, 'bold'), background='orange', fg='white').grid(row=0,column=5)
            Button(container, command=lambda id=item[0]: self.deleteOne(id, self.parent),text='Hapus', width=15, font=('Tahoma', 8, 'bold'), background='red', fg='white').grid(row=0, column=6)

            content_frame.update_idletasks()

        canvas.bind('<Configure>', lambda event, canvas=canvas: self.on_canvas_configure(canvas))

    def on_canvas_configure(self, canvas):
        canvas.configure(scrollregion=canvas.bbox('all'))
    
    def clicked(self, parent, page):
        parent.page.destroy()
        parent.page = page(parent)
        parent.page.pack(fill='both',expand=True)

    def getAll(self):
        src = Db_Barang().getAll()
        return src
    
    def updatePage(self, parent, page, id):
        parent.page.destroy()
        parent.page = page(parent, id)
        parent.page.pack(fill='both',expand=True)

    def bersihkan(self, id_barang):
        barang = Db_Barang()
        barang.id = id_barang
        result = barang.getOne()
        barang.nama = result[1]
        barang.harga = result[2]
        barang.waktu = result[3]
        barang.jumlah = result[4]
        barang.keluar = 0
        barang.wakel = '-'
        barang.update()
        self.clicked(self.parent, BarangKeluar)
        messagebox.showinfo('Success', 'Barang diurungkan')
    
    def setDate(self):
        current_cal = datetime.now()
        current = current_cal.strftime('%d-%B-%Y %H:%M')
        return current

        
    def deleteOne(self, id, parent):
        src = Db_Barang()
        src.id = id
        src.deleteOne()

        messagebox.showinfo('Success', 'Berhasil dihapus')
        self.clicked(parent, BarangKeluar)
        
        
