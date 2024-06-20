from kendaraan.mobil import Mobil
from kendaraan.motor import Motor
from jalankan.jalankan_kendaraan import JalankanKendaraan

def tes():
    
    nama_mobil = input("Masukkan nama mobil: ")
    kecepatan_mobil = int(input("Masukkan kecepatan mobil (km/h): "))
    jumlah_roda = int(input("Masukkan jumlah roda mobil: "))
    print("-----------------------------------------------")
    
    nama_motor = input("Masukkan nama motor: ")
    kecepatan_motor = int(input("Masukkan kecepatan motor (km/h): "))
    tipe_motor = input("Masukkan tipe motor: ")
    print("-----------------------------------------------")

    mobil1 = Mobil(nama_mobil, kecepatan_mobil, jumlah_roda)
    motor1 = Motor(nama_motor, kecepatan_motor, tipe_motor)
   
    interface_kendaraan = JalankanKendaraan()

   
    kendaraan_list = [mobil1, motor1]
    for kendaraan in kendaraan_list:
        interface_kendaraan.tampilkan_info(kendaraan)

    print("-----------------------------------------------")
    kecepatan_maks = int(input("Masukkan batas kecepatan maksimal (km/h): "))
    print("-----------------------------------------------")
    for kendaraan in kendaraan_list:
        interface_kendaraan.cek_kecepatan(kendaraan, kecepatan_maks)

if __name__ == "__main__":
    tes()
