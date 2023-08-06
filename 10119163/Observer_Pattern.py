class Pelanggan:
    def __init__(self, nama):
        self._nama = nama
        self._produk_tertawarkan = []

    def terima_notifikasi(self, produk):
        self._produk_tertawarkan.append(produk)
        print(f"{self._nama} menerima notifikasi: {produk} sudah tersedia atau sedang diskon.")

class TokoElektronik:
    def __init__(self):
        self._pelanggan = []

    def tambah_pelanggan(self, pelanggan):
        self._pelanggan.append(pelanggan)

    def hapus_pelanggan(self, pelanggan):
        self._pelanggan.remove(pelanggan)

    def tawarkan_produk(self, produk):
        print(f"Produk {produk} tersedia.")
        for pelanggan in self._pelanggan:
            pelanggan.terima_notifikasi(produk)

# Contoh penggunaan Observer Pattern
toko = TokoElektronik()

pelanggan1 = Pelanggan("John")
pelanggan2 = Pelanggan("Jane")

toko.tambah_pelanggan(pelanggan1)
toko.tambah_pelanggan(pelanggan2)

toko.tawarkan_produk("Laptop Asus")
toko.tawarkan_produk("Smartphone Samsung")
