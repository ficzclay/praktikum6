# Inisialisasi daftar kamus
list_of_dicts = [
    {'Nama': 'Ari', 'Nomor Telepon': '081267888'},
    {'Nama': 'Riko', 'Nomor Telepon': '087654544'}
]

# Menentukan lebar kolom
column_width = max(len(key) for d in list_of_dicts for key in d) + 2

# Cetak header tabel
print("|".join([key.ljust(column_width) for key in list_of_dicts[0]]))

# Cetak garis pembatas
print("|".join(["=" * column_width] * len(list_of_dicts[0])))

# Cetak data
for entry in list_of_dicts:
    print("|".join([entry[key].ljust(column_width) for key in entry]))
