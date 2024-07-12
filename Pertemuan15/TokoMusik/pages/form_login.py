from tkinter import Frame, Label, Button, Entry, StringVar, messagebox
from db.Admin import *
from .update_user import UpdateUser
class Login(Frame):
    def __init__(self,parent, username = '', state = 0):
        super().__init__()
        self.parent = parent
        self.getUser = Admin()
        self.username = username
        self.inLogin = state
        self.render()
        self.config(background='#FEFBD8')

    def render(self):
        container = Frame(self, height=1000, background='#EECEB9', width=800)
        container.pack(pady=150, side='top')

        if self.inLogin == 0:
            username = StringVar()
            password = StringVar()

            Label(container, text='Login User Admin', font=('Tahoma', 12, 'bold'), fg='white', anchor='e',background='#BB9AB1', padx=240, pady=10).grid(row=0, column=0, columnspan=2, pady=(0, 10))

            Label(container, text='Username :', font=('Tahoma', 12, 'bold'), fg='#424769', width=15, background='#EECEB9', anchor='e').grid(row=1, column=0, padx=25, pady=15)
            Entry(container, textvariable=username, width=25, font=('Tahoma', 12, 'bold'), background='white', fg='#424769').grid(row=1, column=1, padx=25, pady=15)

            Label(container, text='Password :', font=('Tahoma', 12, 'bold'), fg='#424769', width=15, background='#EECEB9', anchor='e').grid(row=2, column=0, padx=25, pady=15)
            Entry(container, textvariable=password, width=25, font=('Tahoma', 12, 'bold'), background='white', fg='#424769').grid(row=2, column=1, padx=25, pady=15)

            Label(container, text='*untuk testing akun yang tersedia:', font=('Tahoma', 10, 'bold'), fg='#424769', background='#EECEB9', anchor='e', padx=200).grid(row=3, column=0, columnspan=2)
            Label(container, text='username : useradmin', font=('Tahoma', 10, 'bold'), fg='#424769', width=20, background='#EECEB9', anchor='center').grid(row=4, column=0, padx=25, pady=15)
            Label(container, text='password : password', font=('Tahoma', 10, 'bold'), fg='#424769', width=20, background='#EECEB9', anchor='center').grid(row=4, column=1, padx=25, pady=15)

            Button(container, text='Submit', width=25, font=('Tahoma', 12, 'bold'), command=lambda: self.login(username.get(),password.get()), background='green', fg='white').grid(row=5, column=0, columnspan=2, padx=25, pady=15)

        else:   
            Label(container, text=f"Selamat Datang Admin {self.username}!", font=('Tahoma', 12, 'bold'), fg='#424769', width=100, anchor='center').grid(row=0, column=0, columnspan=2, padx=25, pady=15)
            Button(container, text='Ubah Profil', width=15, font=('Tahoma', 12, 'bold'), command=lambda: self.update(self.parent, UpdateUser, self.username), background='blue', fg='white').grid(row=1, column=0, padx=25, pady=15, sticky='e')
            Button(container, text='Hapus Akun', width=15, font=('Tahoma', 12, 'bold'), command=lambda: self.delete(self.parent,self.username), background='red', fg='white').grid(row=2, column=0, padx=25, pady=15, sticky='e')
            Button(container, text='Logout', width=15, font=('Tahoma', 12, 'bold'), command=self.logout, background='orange', fg='white').grid(row=3, column=0, padx=25, pady=15, sticky='e')

    def login(self, username, password):
        if not username or not password:
            messagebox.showerror('Error','Semua field harus diisi!')
            return False
        
        self.getUser.username = username
        result = self.getUser.getByUsername(username)
        if result == []:
            messagebox.showerror("error", "username tidak ditemukan")
            return False

        if result[0]['password'] != password:
            messagebox.showerror("error", "Password tidak valid")
            return 
        
        self.username = username
        self.inLogin = 1
        self.getUser.username = self.username
        self.getUser.hasLogin = self.inLogin
        self.getUser.updateHasLogin()
        self.clicked(self.parent, self.username, self.inLogin)
        messagebox.showinfo("success", "Login Berhasil")

    def update(self, parent, page, username):
        parent.page.destroy()
        parent.page = page(parent, username)
        parent.page.pack(fill='both',expand=True)

    def delete(self, parent, username):
        if(messagebox.askyesno('Warning!','Apa anda yakin menghapus akun?')):
            self.getUser.username = username
            self.getUser.deleteByUsername(username)
            self.clicked(parent, '', 0)

    def logout(self):
        self.getUser.username = self.username
        self.getUser.getByUsername(self.username)

        self.getUser.hasLogin = 0
        self.getUser.updateHasLogin()
        self.clicked(self.parent, '', 0)
        messagebox.showinfo("success", "Anda telah Logout")


    def clicked(self, parent, username, state):
        from .navbar import Navbar

        parent.navbar.destroy()
        parent.navbar = Navbar(parent, username)
        parent.navbar.pack(fill='both')

        parent.page.destroy()
        parent.page = Login(parent, username, state)
        parent.page.pack(fill='both',expand=True)

        



