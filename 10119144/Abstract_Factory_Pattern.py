from abc import ABC, abstractmethod

class Laptop(ABC):
    @abstractmethod
    def deskripsi(self):
        pass

class Smartphone(ABC):
    @abstractmethod
    def deskripsi(self):
        pass

class LenovoLaptop(Laptop):
    def deskripsi(self):
        return "Ini adalah laptop Lenovo dengan spesifikasi tertentu."

class LenovoSmartphone(Smartphone):
    def deskripsi(self):
        return "Ini adalah smartphone Lenovo dengan spesifikasi tertentu."

class AsusLaptop(Laptop):
    def deskripsi(self):
        return "Ini adalah laptop Asus dengan spesifikasi tertentu."

class AsusSmartphone(Smartphone):
    def deskripsi(self):
        return "Ini adalah smartphone Asus dengan spesifikasi tertentu."

class ElektronikFactory:
    def buat_laptop(self, brand):
        if brand == 'Lenovo':
            return LenovoLaptop()
        elif brand == 'Asus':
            return AsusLaptop()
        else:
            raise ValueError("Brand laptop tidak dikenali.")

    def buat_smartphone(self, brand):
        if brand == 'Lenovo':
            return LenovoSmartphone()
        elif brand == 'Asus':
            return AsusSmartphone()
        else:
            raise ValueError("Brand smartphone tidak dikenali.")

# Contoh penggunaan Abstract Factory
factory = ElektronikFactory()

laptop = factory.buat_laptop('Lenovo')
print(laptop.deskripsi())  # Output: Ini adalah laptop Lenovo dengan spesifikasi tertentu.

smartphone = factory.buat_smartphone('Asus')
print(smartphone.deskripsi())  # Output: Ini adalah smartphone Asus dengan spesifikasi tertentu.
