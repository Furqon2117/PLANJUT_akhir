class JalankanKendaraan:
    def tampilkan_info(self, kendaraan):
        print(kendaraan.deskripsi())

    def cek_kecepatan(self, kendaraan, kecepatan_maks):
        if kendaraan.kecepatan > kecepatan_maks:
            print(f"Kecepatan {kendaraan.nama} melebihi batas kecepatan maksimal {kecepatan_maks} km/h.")
        else:
            print(f"Kecepatan {kendaraan.nama} masih dalam batas aman.")
