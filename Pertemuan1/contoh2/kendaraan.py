class Kendaraan:
    def __init__(self):
        self.roda = None

    def getData(self, roda):
        self.roda = roda

    def jenisKendaraan(self):
        if self.roda  == 2:
            print('Motor')
        elif self.roda == 4:
            print('Mobil')
        else:
            print("Kendaraan tidak diketahui")

kendaraan = Kendaraan()
roda = input("Masukan jumlah roda : ")

kendaraan.getData(int(roda)) # integer Require
kendaraan.jenisKendaraan()