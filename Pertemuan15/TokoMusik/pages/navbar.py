from tkinter import Frame, Button, messagebox
from .form_register import Register
from .page_etalase import Etalase
from .form_login import Login
from db.Admin import Admin


class Navbar(Frame):
    def __init__(self,parent, username = ''):
        super().__init__()
        self.getUser = Admin()
        if username == '':
            self.currentUser = []
            self.inLogin = 0
            self.username = ''
        else:
            [self.currentUser] = self.getUser.getByUsername(username)
            self.inLogin = self.currentUser['hasLogin']
            self.username = self.currentUser['username']
        
        self.render(parent)
        self.config(background='#EECEB9')
        self.config(pady=20)

    def render(self, parent):
        container = Frame(self)
        container.config(background='#EECEB9')

        Button(container, text='Login' if self.inLogin == 0 else 'Dashboard', width=25, font=('Tahoma', 12, 'bold'), command=lambda: self.clicked(parent, Login, self.username, self.inLogin), background='#BB9AB1', fg='white').grid(row=1, column=1, padx=25)
        Button(container, text='Etalase', width=25, font=('Tahoma', 12, 'bold'), command=lambda: self.clicked(parent, Etalase, self.username, self.inLogin), background='#BB9AB1', fg='white').grid(row=1, column=2, padx=25)
        Button(container, text='Registrasi', width=25, font=('Tahoma', 12, 'bold'), command=lambda: self.clicked(parent, Register, self.username, self.inLogin), background='#BB9AB1', fg='white').grid(row=1, column=4, padx=25)

        container.pack()

    def clicked(self, parent, page, user='', state=0):
        if (page.__name__ == 'Etalase'):
            if(self.inLogin == 0):
                messagebox.showwarning("warning", "Anda belum login")
                return False
            else:
                pass
        if (page.__name__ == 'Register'):
            if(self.inLogin == '1'):
                messagebox.showwarning("warning", "Anda sudah Login")
                return False
            else:
                pass
            
        parent.navbar.destroy()
        parent.navbar = Navbar(parent, user)
        parent.navbar.pack(fill='both')
        parent.page.destroy()
        if page == Register:
            parent.page = page(parent) 
        else:
            parent.page = page(parent, user, state)
        
        parent.page.pack(fill='both',expand=True)



