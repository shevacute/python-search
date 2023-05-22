def sequential_search_phonebook(phonebook, name):
    for entry in phonebook:
        if entry['Nama'] == name:
            return entry['No. Telepon']
    return None

# Tabel buku telepon
phonebook = [
    {'Nama': 'John Doe', 'No. Telepon': '081234567890'},
    {'Nama': 'Jane Smith', 'No. Telepon': '089876543210'},
    {'Nama': 'Michael Johnson', 'No. Telepon': '087811223344'},
    {'Nama': 'Emily Davis', 'No. Telepon': '082122232425'}
]

# Mencari nomor telepon Jane menggunakan sequential search
name = 'Jane Smith'
phone_number = sequential_search_phonebook(phonebook, name)

# Menampilkan nomor telepon Jane jika ditemukan
if phone_number:
    print(f"Nomor telepon Jane adalah: {phone_number}")
else:
    print(f"Tidak ditemukan nomor telepon untuk {name}")
