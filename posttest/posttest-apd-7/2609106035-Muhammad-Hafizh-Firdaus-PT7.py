import os

# ===================== VARIABEL GLOBAL =====================
# (dibuat di luar fungsi biar bisa dibaca semua fungsi/prosedur)

# global 1: clear terminal (cls buat windows, clear buat mac/linux)
clear = "cls" if os.name == "nt" else "clear"

# global 2: dictionary user, key = username, value = dictionary (password, role)
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "hafizh": {"password": "hafizh123", "role": "user"},
}

# global 3: dictionary barang, key = ID barang, value = dictionary (nama, lokasi, jumlah, kondisi)
barang = {
    1: {"nama": "Setrika", "lokasi": "Ruang Jemur", "jumlah": 2, "kondisi": "Baik"},
    2: {"nama": "Kulkas", "lokasi": "Dapur Bersama", "jumlah": 1, "kondisi": "Baik"},
    3: {
        "nama": "Mesin Cuci",
        "lokasi": "Ruang Jemur",
        "jumlah": 1,
        "kondisi": "Rusak Ringan",
    },
    4: {"nama": "Sapu", "lokasi": "Gudang", "jumlah": 5, "kondisi": "Baik"},
}

# global 4: id untuk barang baru (terus bertambah, gak dipakai ulang walau ada yang dihapus)
id_berikutnya = 5

# global 5: dictionary kondisi, key = pilihan menu, value = nama kondisi
daftar_kondisi = {"1": "Baik", "2": "Rusak Ringan", "3": "Rusak Berat"}


# ===================== FUNGSI (pakai return) =====================


# fungsi TANPA parameter 1: minta jumlah barang sampai valid, lalu return angkanya
def input_jumlah():
    while True:
        try:
            teks = input("Jumlah: ").strip()  # variabel lokal
            if not teks.isdigit():
                raise ValueError("Jumlah harus berupa angka bulat positif!")
            jumlah = int(teks)  # variabel lokal
            if jumlah < 1:
                raise ValueError("Jumlah minimal 1!")
        except ValueError as pesan_error:
            print(pesan_error)
        else:
            return jumlah


# fungsi TANPA parameter 2: minta pilihan kondisi sampai valid, lalu return nama kondisinya
def pilih_kondisi():
    print("Kondisi: 1. Baik  2. Rusak Ringan  3. Rusak Berat")
    while True:
        try:
            pilihan = input("Pilih kondisi (1-3): ").strip()  # variabel lokal
            kondisi = daftar_kondisi[pilihan]  # KeyError kalau key tidak ada
        except KeyError:
            print("Pilihan harus 1, 2, atau 3!")
        else:
            return kondisi


# fungsi DENGAN parameter 1: minta input teks (label = parameter) sampai tidak kosong
def input_teks(label):
    while True:
        try:
            teks = input(f"{label}: ").strip()  # variabel lokal
            if teks == "":
                raise ValueError(f"{label} tidak boleh kosong!")
        except ValueError as pesan_error:
            print(pesan_error)
        else:
            return teks


# fungsi DENGAN parameter 2 (REKURSIF): menjumlahkan stok semua barang
# daftar_id = list ID barang, indeks = posisi ID yang sedang dihitung
def hitung_total_unit(daftar_id, indeks):
    # base case: semua ID sudah dihitung, berhenti
    if indeks == len(daftar_id):
        return 0
    jumlah_ini = barang[daftar_id[indeks]]["jumlah"]  # variabel lokal
    # recursive case: jumlah barang ini + total sisanya
    return jumlah_ini + hitung_total_unit(daftar_id, indeks + 1)


# ===================== PROSEDUR (tanpa return) =====================


# prosedur DENGAN parameter: bersihkan layar lalu cetak judul
def tampilkan_banner(judul):
    os.system(clear)
    print("=" * 45)
    print(f"   {judul}")
    print("=" * 45)


# prosedur TANPA parameter: cetak tabel barang (membaca variabel global barang)
def tampilkan_tabel():
    if len(barang) == 0:
        print("Belum ada data barang.")
    else:
        print(f"{'ID':<4}{'Nama':<20}{'Lokasi':<18}{'Jml':<6}{'Kondisi':<14}")
        print("-" * 62)
        for kode, b in barang.items():
            print(
                f"{kode:<4}{b['nama']:<20}{b['lokasi']:<18}{b['jumlah']:<6}{b['kondisi']:<14}"
            )
        print("-" * 62)
        total = hitung_total_unit(list(barang), 0)  # variabel lokal
        print(f"Total unit barang: {total}")


# ===================== PROGRAM UTAMA =====================
while True:
    tampilkan_banner("SISTEM INVENTARIS BARANG KOS")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu_awal = input("Pilih menu (1-3): ").strip()

    # login
    if menu_awal == "1":
        percobaan = 0
        user_login = None

        while percobaan < 3:
            tampilkan_banner("LOGIN")
            username = input("Username: ").strip()
            password = input("Password: ").strip()

            try:
                if users[username]["password"] != password:
                    raise ValueError("Password salah!")
            except (KeyError, ValueError):
                # username tidak ada (KeyError) atau password salah (ValueError)
                percobaan += 1
                print(f"Username atau password salah! Sisa percobaan: {3 - percobaan}")
                input("Tekan Enter untuk lanjut...")
            else:
                user_login = username
                break

        if user_login is None:
            print("Terlalu banyak percobaan gagal. Kembali ke menu awal.")
            input("Tekan Enter untuk lanjut...")
            continue

        # menu admin
        if users[user_login]["role"] == "admin":
            while True:
                tampilkan_banner(f"MENU ADMIN - Halo, {user_login}!")
                print("1. Tambah Barang (Create)")
                print("2. Lihat Daftar Barang (Read)")
                print("3. Ubah Data Barang (Update)")
                print("4. Hapus Barang (Delete)")
                print("5. Logout")
                menu_admin = input("Pilih menu (1-5): ").strip()

                # menambahkan barang (create)
                if menu_admin == "1":
                    tampilkan_banner("TAMBAH BARANG")
                    nama = input_teks("Nama barang")
                    lokasi = input_teks("Lokasi (mis. Kamar 3, Dapur)")
                    jumlah = input_jumlah()
                    kondisi = pilih_kondisi()

                    barang[id_berikutnya] = {
                        "nama": nama,
                        "lokasi": lokasi,
                        "jumlah": jumlah,
                        "kondisi": kondisi,
                    }
                    print(f"Barang berhasil ditambahkan dengan ID {id_berikutnya}!")
                    id_berikutnya += 1
                    input("Tekan Enter untuk kembali...")

                # membaca daftar barang (read)
                elif menu_admin == "2":
                    tampilkan_banner("DAFTAR BARANG KOS")
                    tampilkan_tabel()
                    input("\nTekan Enter untuk kembali...")

                # memperbarui data barang (update)
                elif menu_admin == "3":
                    tampilkan_banner("UBAH DATA BARANG")
                    tampilkan_tabel()

                    try:
                        if len(barang) == 0:
                            raise ValueError("Tidak ada barang yang bisa diubah!")
                        kode_input = input("\nPilih ID barang yang diubah: ").strip()
                        if not kode_input.isdigit():
                            raise ValueError("ID harus berupa angka!")
                        kode = int(kode_input)
                        data = barang[kode]  # KeyError kalau ID tidak ada
                    except ValueError as pesan_error:
                        print(pesan_error)
                    except KeyError:
                        print("ID barang tidak ditemukan!")
                    else:
                        print(f"\nBarang dipilih: {data['nama']}")
                        print("1. Ubah nama")
                        print("2. Ubah lokasi")
                        print("3. Ubah jumlah")
                        print("4. Ubah kondisi")
                        print("5. Batal")
                        ubah = input("Pilih data yang diubah (1-5): ").strip()

                        if ubah == "1":
                            barang[kode]["nama"] = input_teks("Nama baru")
                            print("Nama berhasil diubah!")
                        elif ubah == "2":
                            barang[kode]["lokasi"] = input_teks("Lokasi baru")
                            print("Lokasi berhasil diubah!")
                        elif ubah == "3":
                            barang[kode]["jumlah"] = input_jumlah()
                            print("Jumlah berhasil diubah!")
                        elif ubah == "4":
                            barang[kode]["kondisi"] = pilih_kondisi()
                            print("Kondisi berhasil diubah!")
                        elif ubah == "5":
                            print("Perubahan dibatalkan.")
                        else:
                            print("Pilihan tidak valid!")
                    finally:
                        input("Tekan Enter untuk kembali...")

                # menghapus data barang (delete)
                elif menu_admin == "4":
                    tampilkan_banner("HAPUS BARANG")
                    tampilkan_tabel()

                    try:
                        if len(barang) == 0:
                            raise ValueError("Tidak ada barang yang bisa dihapus!")
                        kode_input = input("\nPilih ID barang yang dihapus: ").strip()
                        if not kode_input.isdigit():
                            raise ValueError("ID harus berupa angka!")
                        kode = int(kode_input)
                        data = barang[kode]  # KeyError kalau ID tidak ada
                    except ValueError as pesan_error:
                        print(pesan_error)
                    except KeyError:
                        print("ID barang tidak ditemukan!")
                    else:
                        yakin = (
                            input(f"Yakin hapus '{data['nama']}'? (y/n): ")
                            .strip()
                            .lower()
                        )
                        if yakin == "y":
                            del barang[kode]
                            print("Barang berhasil dihapus!")
                        else:
                            print("Penghapusan dibatalkan.")
                    finally:
                        input("Tekan Enter untuk kembali...")

                # log out
                elif menu_admin == "5":
                    print("Logout berhasil.")
                    input("Tekan Enter untuk lanjut...")
                    break

                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk lanjut...")

        # menu user biasa
        else:
            while True:
                tampilkan_banner(f"MENU PENGGUNA - Halo, {user_login}!")
                print("1. Lihat Daftar Barang")
                print("2. Logout")
                menu_user = input("Pilih menu (1-2): ").strip()

                if menu_user == "1":
                    tampilkan_banner("DAFTAR BARANG KOS")
                    tampilkan_tabel()
                    input("\nTekan Enter untuk kembali...")

                elif menu_user == "2":
                    print("Logout berhasil.")
                    input("Tekan Enter untuk lanjut...")
                    break

                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk lanjut...")

    # register
    elif menu_awal == "2":
        tampilkan_banner("REGISTER")

        try:
            username_baru = input("Username baru: ").strip()
            if username_baru == "" or " " in username_baru:
                raise ValueError("Username tidak boleh kosong atau mengandung spasi!")
            if username_baru in users:
                raise ValueError("Username sudah dipakai!")

            password_baru = input("Password baru (min. 6 karakter): ").strip()
            if len(password_baru) < 6:
                raise ValueError("Password minimal 6 karakter!")
        except ValueError as pesan_error:
            print(pesan_error)
        else:
            users[username_baru] = {"password": password_baru, "role": "user"}
            print("Registrasi berhasil! Silakan login.")
        finally:
            input("Tekan Enter untuk kembali...")

    # keluar dari program
    elif menu_awal == "3":
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut...")
