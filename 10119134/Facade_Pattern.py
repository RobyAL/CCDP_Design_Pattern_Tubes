class ProdukElektronik:
    def __init__(self, nama, harga):
        self._nama = nama
        self._harga = harga

    def tampilkan_informasi(self):
        return f"{self._nama} - Rp {self._harga}"

class StokProduk:
    def cek_stok(self, produk):
        return f"Stok {produk._nama} tersedia."

class PenawaranDiskon:
    def berlaku_diskon(self, produk):
        return f"Diskon 10% untuk {produk._nama}."

class TokoElektronikFacade:
    def __init__(self):
        self._stok_produk = StokProduk()
        self._penawaran_diskon = PenawaranDiskon()

    def informasi_produk(self, produk):
        info_produk = produk.tampilkan_informasi()
        stok = self._stok_produk.cek_stok(produk)
        diskon = self._penawaran_diskon.berlaku_diskon(produk)
        return f"{info_produk}\n{stok}\n{diskon}"

# Contoh penggunaan Facade Pattern
produk = ProdukElektronik("Laptop Asus", 10000000)
toko_elektronik = TokoElektronikFacade()
informasi_produk = toko_elektronik.informasi_produk(produk)

print(informasi_produk)
# Output:
# Laptop Asus - Rp 10000000
# Stok Laptop Asus tersedia.
# Diskon 10% untuk Laptop Asus.
