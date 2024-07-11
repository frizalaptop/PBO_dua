from tkinter import Frame, Label, Button, Entry, StringVar, messagebox
from db.db_admin import Db_Admin
class Register(Frame):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.render()
        self.config(background='#FEFBD8')

    def render(self):
        container = Frame(self, height=1000, background='#EECEB9')
        container.pack(pady=150, side='bottom')

        username = StringVar()
        password = StringVar()

        Label(container, text='Registrasi User Admin', font=('Tahoma', 12, 'bold'), fg='white', anchor='e',background='#BB9AB1', padx=240, pady=10).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        Label(container, text='Username :', font=('Tahoma', 12, 'bold'), fg='#424769', width=15, background='#EECEB9', anchor='e').grid(row=1, column=0, padx=25, pady=15)
        Entry(container, textvariable=username, width=25, font=('Tahoma', 12, 'bold'), background='white', fg='#424769').grid(row=1, column=1, padx=25, pady=15)

        Label(container, text='Password :', font=('Tahoma', 12, 'bold'), fg='#424769', width=15, background='#EECEB9', anchor='e').grid(row=2, column=0, padx=25, pady=15)
        Entry(container, textvariable=password, width=25, font=('Tahoma', 12, 'bold'), background='white', fg='#424769').grid(row=2, column=1, padx=25, pady=15)

        Button(container, text='Submit', width=25, font=('Tahoma', 12, 'bold'), command=lambda: self.register(username.get(),password.get()), background='green', fg='white').grid(row=5, column=0, columnspan=2, padx=25, pady=15)

    def register(self, username, password):
        _getUser = Db_Admin()
        _getUser.username = username
        _getUser.password = password
        _getUser.hasLogin = 0
        result = _getUser.create()
        messagebox.showinfo("success", "Akun berhasil dibuat")
        self.clicked(self.parent)


    def clicked(self, parent):
        from .navbar import Navbar
        from .form_login import Login

        parent.navbar.destroy()
        parent.navbar = Navbar(parent)
        parent.navbar.pack(fill='both')

        parent.page.destroy()
        parent.page = Login(parent)
        parent.page.pack(fill='both',expand=True)

        



