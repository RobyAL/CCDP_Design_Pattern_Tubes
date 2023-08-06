from abc import ABC, abstractmethod

class MetodePembayaran(ABC):
    @abstractmethod
    def bayar(self, total_harga):
        pass

class TransferBank(MetodePembayaran):
    def bayar(self, total_harga):
        return f"Melakukan pembayaran via transfer bank: {total_harga}"

class KartuKredit(MetodePembayaran):
    def bayar(self, total_harga):
        return f"Melakukan pembayaran via kartu kredit: {total_harga}"

class Pelanggan:
    def __init__(self, nama, metode_pembayaran):
        self._nama = nama
        self._metode_pembayaran = metode_pembayaran

    def bayar(self, total_harga):
        return self._metode_pembayaran.bayar(total_harga)

# Contoh penggunaan Strategy Pattern
metode_transfer = TransferBank()
metode_kartu_kredit = KartuKredit()

pelanggan1 = Pelanggan("John", metode_transfer)
pelanggan2 = Pelanggan("Jane", metode_kartu_kredit)

total_harga = 1000
print(pelanggan1.bayar(total_harga))  # Output: Melakukan pembayaran via transfer bank: 1000
print(pelanggan2.bayar(total_harga))  # Output: Melakukan pembayaran via kartu kredit: 1000
