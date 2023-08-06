from abc import ABC, abstractmethod

class ProdukElektronik(ABC):
    @abstractmethod
    def deskripsi(self):
        pass

class Laptop(ProdukElektronik):
    def deskripsi(self):
        return "Ini adalah laptop dengan spesifikasi tertentu."

class TambahanGaransi(ProdukElektronik):
    def __init__(self, produk):
        self._produk = produk

    def deskripsi(self):
        return f"{self._produk.deskripsi()} Ditambahkan garansi ekstra."

# Contoh penggunaan Decorator Pattern
laptop = Laptop()
laptop_dengan_garansi = TambahanGaransi(laptop)

print(laptop.deskripsi())  # Output: Ini adalah laptop dengan spesifikasi tertentu.
print(laptop_dengan_garansi.deskripsi())  # Output: Ini adalah laptop dengan spesifikasi tertentu. Ditambahkan garansi ekstra.
