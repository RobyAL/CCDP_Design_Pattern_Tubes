from abc import ABC, abstractmethod

# Component
class KomponenProduk(ABC):
    @abstractmethod
    def tampilkan_informasi(self):
        pass

# Leaf
class ProdukElektronik(KomponenProduk):
    def __init__(self, nama, harga):
        self._nama = nama
        self._harga = harga

    def tampilkan_informasi(self):
        return f"{self._nama} - Rp {self._harga}"

# Composite
class KategoriProduk(KomponenProduk):
    def __init__(self, nama):
        self._nama = nama
        self._produk = []

    def tambah_produk(self, produk):
        self._produk.append(produk)

    def hapus_produk(self, produk):
        self._produk.remove(produk)

    def tampilkan_informasi(self):
        info_kategori = f"{self._nama}:"
        for produk in self._produk:
            info_kategori += f"\n  {produk.tampilkan_informasi()}"
        return info_kategori

# Contoh penggunaan Composite Pattern
# Membuat beberapa produk elektronik
produk1 = ProdukElektronik("Laptop Asus", 10000000)
produk2 = ProdukElektronik("Smartphone Samsung", 8000000)
produk3 = ProdukElektronik("Kamera Sony", 5000000)

# Membuat kategori produk dan menambahkan produk elektronik ke dalamnya
kategori_laptop = KategoriProduk("Laptop")
kategori_laptop.tambah_produk(produk1)

kategori_smartphone = KategoriProduk("Smartphone")
kategori_smartphone.tambah_produk(produk2)

kategori_kamera = KategoriProduk("Kamera")
kategori_kamera.tambah_produk(produk3)

# Menampilkan informasi kategori dan produk elektronik
print(kategori_laptop.tampilkan_informasi())
print(kategori_smartphone.tampilkan_informasi())
print(kategori_kamera.tampilkan_informasi())
