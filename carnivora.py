# Parent Class
class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name, self.makanan, self.hidup, self.berkembang_biak = name, makanan, hidup, berkembang_biak

    def tampilkan_info(self):
        return f"Nama: {self.name}, Makanan: {self.makanan}, Hidup: {self.hidup}, Berkembang Biak: {self.berkembang_biak}"

# Child Class 1: Amphibi
class Amphibi(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, habitat):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.habitat = habitat
    def tampilkan_habitat(self):
        return f"Habitat: {self.habitat}"

# Child Class 2: Mamalia
class Mamalia(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jumlah_keturunan):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jumlah_keturunan = jumlah_keturunan
    def tampilkan_jumlah_keturunan(self):
        return f"Jumlah Keturunan: {self.jumlah_keturunan}"

# Child Class 3: Burung
class Burung(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, warna_bulu):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.warna_bulu = warna_bulu
    def tampilkan_warna_bulu(self):
        return f"Warna Bulu: {self.warna_bulu}"

# Child Class 4: Carnivora
class Carnivora(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_daging):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_daging = jenis_daging
    def berburu(self):
        return f"{self.name} berburu dengan cara menyerang mangsanya."
    def tampilkan_jenis_daging(self):
        return f"Jenis Daging: {self.jenis_daging}"
    


# Membuat Objek
print("===== Carnivora =====")
amphibi1 = Amphibi("Kodok", "Serangga", "Di darat dan air", "Bertelur", "Kolam")
mamalia1 = Mamalia("Singa", "Daging", "Di darat", "Melahirkan", "1")
burung1 = Burung("Elang", "Daging", "Di udara dan darat", "Bertelur", "Cokelat dengan putih")
carnivora1 = Carnivora("Harimau", "Daging", "Di darat", "Melahirkan", "Daging besar")

# Menampilkan Info
print(amphibi1.tampilkan_info(), amphibi1.tampilkan_habitat())
print(mamalia1.tampilkan_info(), mamalia1.tampilkan_jumlah_keturunan())
print(burung1.tampilkan_info(), burung1.tampilkan_warna_bulu())
print(carnivora1.tampilkan_info(), carnivora1.berburu(), carnivora1.tampilkan_jenis_daging())
