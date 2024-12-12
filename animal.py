class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.nama = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    
    def info_animal(self):
        print("Nama Hewan \t\t\t :", self.nama +
              "\nmakanan \t\t\t :", self.makanan +
              "\nhidup \t\t\t\t :", self.hidup +
              "\nberkembang_biak \t\t\ :", self.berkembang_biak)

hewan = Animal('kucing garong', 'cimol', 'udara', 'bertelur')  
hewan.info_animal()

