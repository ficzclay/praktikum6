# Inisialisasi dictionary untuk menyimpan data mahasiswa
data_mahasiswa = {}

# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(tugas, uts, uas):
    return 0.3 * tugas + 0.35 * uts + 0.35 * uas

# Fungsi untuk menghapus data mahasiswa berdasarkan NIM
def hapus_data_mahasiswa():
    if not data_mahasiswa:
        print("\nTidak ada data mahasiswa untuk dihapus.")
    else:
        nim_hapus = int(input("\nMasukkan NIM mahasiswa yang akan dihapus: "))
        if nim_hapus in data_mahasiswa:
            del data_mahasiswa[nim_hapus]
            print(f"Data mahasiswa dengan NIM {nim_hapus} berhasil dihapus.")
        else:
            print(f"Tidak ada data mahasiswa dengan NIM {nim_hapus}.")

# Fungsi untuk mengubah data mahasiswa berdasarkan NIM
def ubah_data_mahasiswa():
    if not data_mahasiswa:
        print("\nTidak ada data mahasiswa untuk diubah.")
    else:
        nim_ubah = int(input("\nMasukkan NIM mahasiswa yang akan diubah: "))
        if nim_ubah in data_mahasiswa:
            print(f"\nData Mahasiswa dengan NIM {nim_ubah}:")
            print("Nama   :", data_mahasiswa[nim_ubah]['Nama'])
            print("Tugas  :", data_mahasiswa[nim_ubah]['Tugas'])
            print("UTS    :", data_mahasiswa[nim_ubah]['UTS'])
            print("UAS    :", data_mahasiswa[nim_ubah]['UAS'])

            # Meminta input baru untuk data yang akan diubah
            data_mahasiswa[nim_ubah]['Nama'] = input("Nama baru   : ")
            data_mahasiswa[nim_ubah]['Tugas'] = int(input("Nilai Tugas baru : "))
            data_mahasiswa[nim_ubah]['UTS'] = int(input("Nilai UTS baru   : "))
            data_mahasiswa[nim_ubah]['UAS'] = int(input("Nilai UAS baru   : "))
            
            # Menghitung nilai akhir setelah perubahan
            data_mahasiswa[nim_ubah]['Akhir'] = hitung_nilai_akhir(
                data_mahasiswa[nim_ubah]['Tugas'],
                data_mahasiswa[nim_ubah]['UTS'],
                data_mahasiswa[nim_ubah]['UAS']
            )

            print("\nData mahasiswa berhasil diubah.")
        else:
            print(f"Tidak ada data mahasiswa dengan NIM {nim_ubah}.")

# Fungsi untuk mencari data mahasiswa berdasarkan NIM
def cari_data_mahasiswa():
    if not data_mahasiswa:
        print("\nTidak ada data mahasiswa untuk dicari.")
    else:
        nim_cari = int(input("\nMasukkan NIM mahasiswa yang akan dicari: "))
        if nim_cari in data_mahasiswa:
            print("\nData Mahasiswa dengan NIM", nim_cari, ":")
            print("Nama   :", data_mahasiswa[nim_cari]['Nama'])
            print("Tugas  :", data_mahasiswa[nim_cari]['Tugas'])
            print("UTS    :", data_mahasiswa[nim_cari]['UTS'])
            print("UAS    :", data_mahasiswa[nim_cari]['UAS'])
            print("Akhir  :", data_mahasiswa[nim_cari]['Akhir'])
        else:
            print(f"Tidak ada data mahasiswa dengan NIM {nim_cari}.")

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\nProgram Input Nilai")
    print("===================")
    print("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari (K)eluar]:", end=" ")

# Fungsi untuk menampilkan daftar nilai
def tampilkan_daftar_nilai():
    if not data_mahasiswa:
        print("\nDaftar Nilai")
        print("==========================================================")
        print("| NO |  NIM   |    NAMA    | TUGAS | UTS  | UAS  | AKHIR |")
        print("==========================================================")
        print("|                    TIDAK ADA DATA                      |")
        print("==========================================================")
    else:
        print("\nDaftar Nilai")
        print("============================================================")
        print("|  NO  |  NIM   |    NAMA    | TUGAS | UTS  | UAS  | AKHIR |")
        print("============================================================")
        no = 1
        for nim, data in data_mahasiswa.items():
            print(f"| {no:^4} | {nim:^6} | {data['Nama']:^10} | {data['Tugas']:^5} | {data['UTS']:^4} | {data['UAS']:^4} | {data['Akhir']:^5.1f} |")
            no += 1
        print("============================================================")

# Fungsi untuk menambah data mahasiswa
def tambah_data_mahasiswa():
    print("\nTambah Data")
    nim = int(input("NIM : "))
    nama = input("Nama : ")
    uts = int(input("Nilai UTS: "))
    uas = int(input("Nilai UAS : "))
    tugas = int(input("Nilai Tugas: "))
    
    # Hitung nilai akhir
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

    # Simpan data mahasiswa ke dalam dictionary
    data_mahasiswa[nim] = {'Nama': nama, 'Tugas': tugas, 'UTS': uts, 'UAS': uas, 'Akhir': nilai_akhir}
    print("\nData mahasiswa berhasil ditambahkan!")

# Program utama
while True:
    tampilkan_menu()
    pilihan = input().upper()

    if pilihan == 'L':
        tampilkan_daftar_nilai()
    elif pilihan == 'T':
        try:
            tambah_data_mahasiswa()
        except ValueError:
            print("\nInput tidak valid. Silakan coba lagi.")
    elif pilihan == 'H':
        hapus_data_mahasiswa()
    elif pilihan == 'U':
        ubah_data_mahasiswa()
    elif pilihan == 'C':
        cari_data_mahasiswa()
    elif pilihan == 'K':
        print("Keluar dari program. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
