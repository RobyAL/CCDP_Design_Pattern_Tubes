class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConnection, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self):
        # Implementasi koneksi ke database
        return "Berhasil terhubung ke database."

# Contoh penggunaan Singleton Pattern
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)  # Output: True, kedua objek merupakan objek yang sama

result = db1.connect()
print(result)  # Output: Berhasil terhubung ke database.

result = db2.connect()
print(result)  # Output: Berhasil terhubung ke database.
