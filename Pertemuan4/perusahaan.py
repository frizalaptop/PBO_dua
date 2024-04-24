class Person:
    def __init__(self, NIK, nama, umur, alamat):
        self.NIK = NIK
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def informasi(self):
        print (f"Person: {self.nama}, {self.umur} tahun, {self.alamat}")

class Manager(Person):
    def __init__(self, NIK, nama, umur, alamat, proyek):
         super().__init__(NIK, nama, umur, alamat)
         self.proyek = proyek
    
    def informasi(self):
        print (f"Manager {self.nama} memimpin proyek {self.proyek}")

class  Programmer(Person):
    def __init__(self, NIK, nama, umur, alamat, task):
        super().__init__(NIK, nama, umur, alamat)
        self.task = task

    def informasi(self):
        print (f"Nama {self.nama}, dalam tugas {self.task}")

class Teknisi(Person):
    def __init__(self, NIK, nama, umur, alamat, shift):
        super().__init__(NIK, nama, umur, alamat)
        self.shift = shift

    def informasi(self):
        print (f"Teknisi {self.nama} shift {self.shift}")

class Staff(Person):
    def __init__(self, NIK, nama, umur, alamat, divisi):
        super().__init__(NIK, nama, umur, alamat)
        self.divisi = divisi

    def informasi(self):
        print (f"Staff {self.nama} Divisi {self.divisi}")


    

person = Programmer(32546, 'Friza', 20, 'Cirebon', 'Back-End Dev')
person.informasi()