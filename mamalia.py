# Parent Class
class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name, self.makanan, self.hidup, self.berkembang_biak = name, makanan, hidup, berkembang_biak

    def tampilkan_info(self):
        return f"Nama: {self.name}, Makanan: {self.makanan}, Hidup: {self.hidup}, Berkembang Biak: {self.berkembang_biak}"

# Child Class 1: Mamalia
class Mamalia(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jumlah_keturunan, jenis_habitat):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jumlah_keturunan = jumlah_keturunan
        self.jenis_habitat = jenis_habitat

    def tampilkan_jumlah_keturunan(self):
        return f"Jumlah Keturunan: {self.jumlah_keturunan}"
    
    def tampilkan_jenis_habitat(self):
        return f"Habitat: {self.jenis_habitat}"

# Membuat Objek
print("===== Mamalia =====")
mamalia1 = Mamalia("Singa", "Daging", "Di darat", "Melahirkan", "1", "Padang rumput")
mamalia2 = Mamalia("Gajah", "Tumbuhan", "Di darat", "Melahirkan", "1", "Hutan")
mamalia3 = Mamalia("Kelinci", "Tumbuhan", "Di darat", "Melahirkan", "3", "Padang rumput")

# Menampilkan Info
print(mamalia1.tampilkan_info(), mamalia1.tampilkan_jumlah_keturunan(), mamalia1.tampilkan_jenis_habitat())
print(mamalia2.tampilkan_info(), mamalia2.tampilkan_jumlah_keturunan(), mamalia2.tampilkan_jenis_habitat())
print(mamalia3.tampilkan_info(), mamalia3.tampilkan_jumlah_keturunan(), mamalia3.tampilkan_jenis_habitat())
