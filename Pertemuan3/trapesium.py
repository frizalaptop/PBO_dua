class Trapesium:
    def __init__(self, sisi_a, sisi_b, tinggi):
        self.__sisi_a = 0
        self.__sisi_b = 0
        self.__tinggi = 0
        self.setSisi_a(sisi_a)
        self.setSisi_b(sisi_b)
        self.setTinggi(tinggi)

    
    def luas(self):
        L = ((self.__sisi_a + self.__sisi_b) * self.__tinggi) / 2
        return L
    
    def setSisi_a(self, nilai):
        self.__sisi_a = nilai
    def setSisi_b(self, nilai):
        self.__sisi_b = nilai
    def setTinggi(self, nilai):
        self.__tinggi = nilai
    def getSisi_a(self):
        return self.__sisi_b
    def getSisi_b(self):
        return self.__sisi_b
    def getTinggi(self):
        return self.__tinggi

try:
    sisi_a = float(input('Masukkan sisi a: '))
    sisi_b = float(input('Masukkan sisi b: '))
    tinggi = float(input('Masukkan tinggi : '))
    bangun_datar = Trapesium(sisi_a, sisi_b, tinggi)

except ValueError:
    print('Masukan hanya angka')

else:
    print('Luas Trapesium:', bangun_datar.luas())
