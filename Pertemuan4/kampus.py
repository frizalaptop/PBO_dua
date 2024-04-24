class Person:
    def __init__(self, NIK, nama, umur, alamat):
        self.NIK = NIK
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def informasi(self):
        print (f"Person: {self.nama}, {self.umur} tahun, {self.alamat}")

class Dosen(Person):
    def __init__(self, NIK, nama, umur, alamat, gelar):
         super().__init__(NIK, nama, umur, alamat)
         self.gelar = gelar
    
    def informasi(self):
        print (f"Dosen {self.nama}, {self.gelar}")

class  Mahasiswa(Person):
    def __init__(self, NIK, nama, umur, alamat, jurusan):
        super().__init__(NIK, nama, umur, alamat)
        self.jurusan = jurusan

    def informasi(self):
        print (f"Nama {self.nama}, Mahasiswa {self.jurusan}")

class Staff(Person):
    def __init__(self, NIK, nama, umur, alamat, Departemen):
        super().__init__(NIK, nama, umur, alamat)
        self.Departemen = Departemen

    def informasi(self):
        print (f"Staff {self.nama} Departemen {self.Departemen}")

class Satpam(Person):
    def __init__(self, NIK, nama, umur, alamat):
        super().__init__(NIK, nama, umur, alamat)
        self.jabatan = "Satpam"

    def informasi(self):
        print (f"Satpam {self.nama} Jabatan {self.jabatan}")

class Ob(Person):
    def __init__(self, NIK, nama, umur, alamat):
        super().__init__(NIK, nama, umur, alamat)
        self.jabatan = "OB"

    def informasi(self):
        print (f"Satpam {self.nama} Jabatan {self.jabatan}")

    

person = Satpam(32546, 'Sopyan', 20, 'Jakarta')
person.informasi()