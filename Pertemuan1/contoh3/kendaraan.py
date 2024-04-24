class Kendaraan:
    def __init__(self):
        self._roda = None

    @property
    def roda(self):
        return self._roda
    
    @roda.setter
    def roda(self, value):
        self._roda = value

    def jenisKendaraan(self):
        if self._roda  == 2:
            print('Motor')
        elif self._roda == 4:
            print('Mobil')
        else:
            print("Kendaraan tidak diketahui")

kendaraan = Kendaraan()
roda = input("Masukan jumlah roda : ")
kendaraan.roda = int(roda)
kendaraan.jenisKendaraan()