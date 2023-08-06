from copy import deepcopy

class ProdukElektronik:
    def __init__(self, nama, harga, spesifikasi):
        self._nama = nama
        self._harga = harga
        self._spesifikasi = spesifikasi

    def clone(self):
        return deepcopy(self)

    def tampilkan_informasi(self):
        return f"{self._nama} - Rp {self._harga}\nSpesifikasi: {self._spesifikasi}"

# Contoh penggunaan Prototype Pattern
produk_asli = ProdukElektronik("Laptop Asus", 10000000, "Intel Core i5, 8GB RAM, 256GB SSD")
print("Produk Asli:")
print(produk_asli.tampilkan_informasi())

# Kloning produk_asli untuk membuat produk baru dengan harga diskon
produk_diskon = produk_asli.clone()
produk_diskon._harga -= 2000000
print("\nProduk Diskon:")
print(produk_diskon.tampilkan_informasi())
