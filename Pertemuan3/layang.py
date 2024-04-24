class LayangLayang:
    def __init__(self, diagonal, tinggi):
        self.__diagonal = 0
        self.__tinggi = 0
        self.setDiagonal(diagonal)
        self.setTinggi(tinggi)

    def luas(self):
        L = (self.__diagonal * self.__tinggi) / 2
        return L
    
    def setDiagonal(self, nilai):
        self.__diagonal = nilai
    def setTinggi(self, nilai):
        self.__tinggi = nilai
    def getDiagonal(self):
        return self.__diagonal
    def getTinggi(self):
        return self.__tinggi


try:
    diagonal = float(input('Masukkan panjang diagonal: '))
    tinggi = float(input('Masukkan tinggi layang-layang: '))
    bangun_datar = LayangLayang(diagonal, tinggi)

except ValueError:
    print('Masukan hanya angka')

else:
    print('Luas Layang-layang:', bangun_datar.luas())
