class Kendaraan:
    def __init__(self, roda):
        self.roda = roda

    def jenisKendaraan(self):
        if self.roda  == 2:
            print('Motor')
        elif self.roda == 4:
            print('Mobil')
        else:
            print("Kendaraan tidak diketahui")

kendaraan = Kendaraan(4) #integer required
kendaraan.jenisKendaraan() 