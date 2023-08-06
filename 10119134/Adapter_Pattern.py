class PembayaranElektronik:
    def bayar(self, total_harga):
        raise NotImplementedError("Metode bayar harus diimplementasikan dalam subclass.")

class PaymentGateway:
    def bayar_dengan_gateway(self, total_harga):
        print(f"Melakukan pembayaran dengan gateway: {total_harga}")

class AdapterPembayaran(PembayaranElektronik):
    def __init__(self, payment_gateway):
        self._payment_gateway = payment_gateway

    def bayar(self, total_harga):
        self._payment_gateway.bayar_dengan_gateway(total_harga)

# Contoh penggunaan Adapter Pattern
payment_gateway = PaymentGateway()
adapter = AdapterPembayaran(payment_gateway)

total_harga = 1000
adapter.bayar(total_harga)  # Output: Melakukan pembayaran dengan gateway: 1000
