from abc import ABC, abstractmethod

class ProdukElektronik(ABC):
    @abstractmethod
    def deskripsi(self):
        pass

class Laptop(ProdukElektronik):
    def deskripsi(self):
        return "Ini adalah laptop dengan spesifikasi tertentu."

class Smartphone(ProdukElektronik):
    def deskripsi(self):
        return "Ini adalah smartphone dengan spesifikasi tertentu."

class Kamera(ProdukElektronik):
    def deskripsi(self):
        return "Ini adalah kamera dengan spesifikasi tertentu."

class ElektronikFactory:
    def buat_produk(self, jenis):
        if jenis == 'laptop':
            return Laptop()
        elif jenis == 'smartphone':
            return Smartphone()
        elif jenis == 'kamera':
            return Kamera()
        else:
            raise ValueError("Jenis produk elektronik tidak dikenali.")

# Contoh penggunaan Factory Method
factory = ElektronikFactory()

laptop = factory.buat_produk('laptop')
print(laptop.deskripsi())  # Output: Ini adalah laptop dengan spesifikasi tertentu.

smartphone = factory.buat_produk('smartphone')
print(smartphone.deskripsi())  # Output: Ini adalah smartphone dengan spesifikasi tertentu.

kamera = factory.buat_produk('kamera')
print(kamera.deskripsi())  # Output: Ini adalah kamera dengan spesifikasi tertentu.
