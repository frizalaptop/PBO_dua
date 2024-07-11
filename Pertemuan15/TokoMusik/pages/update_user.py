from tkinter import Frame, Label, Button, Entry, StringVar, messagebox
from db.db_admin import Db_Admin

class UpdateUser(Frame):
    def __init__(self, parent, username):
        super().__init__()
        self.username = username
        self.parent = parent
        self.user = self.getOne(self.username)
        self.userId = self.user[0]
        self.render(self.parent)
        self.config(background='#FEFBD8')

    def render(self, parent):
        container = Frame(self, height=900, background='#EECEB9')
        container.pack(pady=150)

        username = StringVar()
        username.set(self.user[1])
        password = StringVar()
        password.set(self.user[2])

        Label(container, text='Ubah Data Admin', font=('Tahoma', 12, 'bold'), fg='white', anchor='e',background='#BB9AB1', padx=200, pady=10).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        Label(container, text='Username :', font=('Tahoma', 12, 'bold'), fg='#424769', width=15, background='#EECEB9', anchor='e').grid(row=1, column=0, padx=25, pady=15)
        Entry(container, textvariable=username, width=25, font=('Tahoma', 12, 'bold'), background='white', fg='#424769').grid(row=1, column=1, padx=25, pady=15)

        Label(container, text='Password :', font=('Tahoma', 12, 'bold'), fg='#424769', width=15, background='#EECEB9', anchor='e').grid(row=2, column=0, padx=25, pady=15)
        Entry(container, textvariable=password, width=25, font=('Tahoma', 12, 'bold'), background='white', fg='#424769').grid(row=2, column=1, padx=25, pady=15)

        Button(container, text='Perbarui', width=15, font=('Tahoma', 12, 'bold'), command=lambda: self.update((self.userId,username,password)), background='green', fg='white').grid(row=5, column=0, padx=25, pady=15, sticky='w')
        Button(container, text='Batalkan', width=15, font=('Tahoma', 12, 'bold'), command=lambda: self.clicked(self.parent, self.username, self.user[3]), background='red', fg='white').grid(row=5, column=1, padx=25, pady=15, sticky='e')


    def clicked(self, parent, username, state):
        from .navbar import Navbar
        from .form_login import Login

        parent.navbar.destroy()
        parent.navbar = Navbar(parent, username)
        parent.navbar.pack(fill='both')

        parent.page.destroy()
        parent.page = Login(parent, username, state)
        parent.page.pack(fill='both',expand=True)

    def getOne(self, username):
        user = Db_Admin()
        user.username = username
        return user.getOne()

    def update(self, value):
        if(not value[1].get() or not value[2].get()):
            messagebox.showerror('Error','Semua field harus diisi!')
            return False
        
        user = Db_Admin()
        user.id = value[0]
        user.username = value[1].get()
        user.password = value[2].get()
        update = user.updateUser()

        messagebox.showinfo('Success', 'Berhasil diperbarui')
        self.clicked(self.parent, user.username, user.hasLogin)