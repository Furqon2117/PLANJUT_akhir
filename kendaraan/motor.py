from kendaraan.kendaraan import Kendaraan

class Motor(Kendaraan):
    def __init__(self, nama, kecepatan, tipe_motor):
        super().__init__(nama, kecepatan)
        self.tipe_motor = tipe_motor

    def deskripsi(self):
        return f"Motor {self.nama} dengan kecepatan {self.kecepatan} km/h dan tipe {self.tipe_motor}."
