class Jajargenjang:
    def __init__(self, alas, tinggi):
        self.__alas = 0
        self.__tinggi = 0
        self.setAlas(alas)
        self.setTinggi(tinggi)

    
    def luas(self):
        L = self.__alas * self.__tinggi
        return L
    
    def setAlas(self, nilai):
        self.__alas = nilai
    def setTinggi(self, nilai):
        self.__tinggi = nilai
    def getAlas(self):
        return self.__alas
    def getTinggi(self):
        return self.__tinggi

try:
    alas = float(input('Masukkan panjang alas: '))
    tinggi = float(input('Masukkan tinggi jajargenjang: '))
    bangun_datar = Jajargenjang(alas, tinggi)

except ValueError:
    print('Masukan hanya angka')

else:
    print('Luas Jajargenjang:', bangun_datar.luas())
