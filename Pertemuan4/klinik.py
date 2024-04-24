class Person:
    def __init__(self, NIK, nama, umur, alamat):
        self.NIK = NIK
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def informasi(self):
        print (f"Person: {self.nama}, {self.umur} tahun, {self.alamat}")

class Dokter(Person):
    def __init__(self, NIK, nama, umur, alamat, spesialis):
         super().__init__(NIK, nama, umur, alamat)
         self.spesialis = spesialis
    
    def informasi(self):
        print (f"Dokter {self.nama} spesialis {self.spesialis}")

class  Perawat(Person):
    def __init__(self, NIK, nama, umur, alamat, divisi):
        super().__init__(NIK, nama, umur, alamat)
        self.divisi = divisi

    def informasi(self):
        print (f"Perawat {self.nama} divisi {self.divisi}")

class Karyawan(Person):
    def __init__(self, NIK, nama, umur, alamat, Departemen):
        super().__init__(NIK, nama, umur, alamat)
        self.Departemen = Departemen

    def informasi(self):
        print (f"Karyawan {self.nama} Departemen {self.Departemen}")

    

person = Dokter(32546, 'Hafid', 20, 'Cirebon', 'Hewan')
person.informasi()