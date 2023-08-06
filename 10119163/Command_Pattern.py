from abc import ABC, abstractmethod

class PerintahPembelian(ABC):
    @abstractmethod
    def eksekusi(self):
        pass

class PembelianProduk(PerintahPembelian):
    def __init__(self, produk):
        self._produk = produk

    def eksekusi(self):
        return f"Produk {self._produk} telah berhasil dibeli."

class Pelanggan:
    def __init__(self):
        self._perintah_pembelian = []

    def tambah_perintah_pembelian(self, perintah):
        self._perintah_pembelian.append(perintah)

    def beli_produk(self):
        hasil_pembelian = []
        for perintah in self._perintah_pembelian:
            hasil_pembelian.append(perintah.eksekusi())
        return hasil_pembelian

# Contoh penggunaan Command Pattern
pelanggan = Pelanggan()

perintah1 = PembelianProduk("Laptop Asus")
perintah2 = PembelianProduk("Smartphone Samsung")

pelanggan.tambah_perintah_pembelian(perintah1)
pelanggan.tambah_perintah_pembelian(perintah2)

hasil_pembelian = pelanggan.beli_produk()
for hasil in hasil_pembelian:
    print(hasil)
# Output:
# Produk Laptop Asus telah berhasil dibeli.
# Produk Smartphone Samsung telah berhasil dibeli.
