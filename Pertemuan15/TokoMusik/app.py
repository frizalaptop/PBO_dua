from tkinter import Tk
from pages.navbar import Navbar
from pages.form_login import Login

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title('Toko Musik Berkah')
        self.minsize(700, 300)
        self.state('zoomed')

        self.navbar = Navbar(self)
        self.page = Login(self)

        self.navbar.pack(fill='both')
        self.page.pack(fill='both',expand=True)

root = Window()
root.mainloop()