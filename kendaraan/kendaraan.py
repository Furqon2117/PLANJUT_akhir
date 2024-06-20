from abc import ABC, abstractmethod

class Kendaraan(ABC):
    def __init__(self, nama, kecepatan):
        self.nama = nama
        self.kecepatan = kecepatan

    @abstractmethod
    def deskripsi(self):
        pass
