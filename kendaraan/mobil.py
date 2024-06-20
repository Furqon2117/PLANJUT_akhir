from kendaraan.kendaraan import Kendaraan

class Mobil(Kendaraan):
    def __init__(self, nama, kecepatan, jumlah_roda):
        super().__init__(nama, kecepatan)
        self.jumlah_roda = jumlah_roda

    def deskripsi(self):
        return f"Mobil {self.nama} dengan kecepatan {self.kecepatan} km/h dan memiliki {self.jumlah_roda} roda."
