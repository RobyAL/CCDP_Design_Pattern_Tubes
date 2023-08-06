from abc import ABC, abstractmethod

# Abstract Class dengan metode Template
class TemplatePenjualan(ABC):
    def pesan_produk(self):
        self.pilih_produk()
        self.konfirmasi_pesanan()
        self.pembayaran()
        self.kirim_pesanan()

    @abstractmethod
    def pilih_produk(self):
        pass

    @abstractmethod
    def konfirmasi_pesanan(self):
        pass

    def pembayaran(self):
        print("Pembayaran dilakukan secara online.")

    def kirim_pesanan(self):
        print("Pesanan akan segera dikirim.")

# Subclass yang mengimplementasikan metode-metode abstrak
class PenjualanElektronik(TemplatePenjualan):
    def pilih_produk(self):
        print("Pilih produk elektronik yang ingin dibeli.")

    def konfirmasi_pesanan(self):
        print("Konfirmasi pesanan produk elektronik.")

# Subclass yang mengimplementasikan metode-metode abstrak
class PenjualanPakaian(TemplatePenjualan):
    def pilih_produk(self):
        print("Pilih pakaian yang ingin dibeli.")

    def konfirmasi_pesanan(self):
        print("Konfirmasi pesanan pakaian.")

    def pembayaran(self):
        print("Pembayaran dilakukan saat barang diterima.")

# Contoh penggunaan Template Method Pattern
print("Penjualan Produk Elektronik:")
penjualan_elektronik = PenjualanElektronik()
penjualan_elektronik.pesan_produk()

print("\nPenjualan Pakaian:")
penjualan_pakaian = PenjualanPakaian()
penjualan_pakaian.pesan_produk()
