import os

# clear terminal (cls buat windows, clear buat mac/linux)
clear = "cls" if os.name == "nt" else "clear"

# data awal
# dictionary user: key = username, value = dictionary (password, role)
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "hafizh": {"password": "hafizh123", "role": "user"},
}

# dictionary barang: key = ID barang, value = dictionary (nama, lokasi, jumlah, kondisi)
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

# id untuk barang baru (terus bertambah, gak dipakai ulang walau ada yang dihapus)
id_berikutnya = 5

# dictionary kondisi: key = pilihan menu, value = nama kondisi
daftar_kondisi = {"1": "Baik", "2": "Rusak Ringan", "3": "Rusak Berat"}

# program utama
while True:
    os.system(clear)
    print("=" * 45)
    print("   SISTEM INVENTARIS BARANG KOS")
    print("=" * 45)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu_awal = input("Pilih menu (1-3): ").strip()

    # login
    if menu_awal == "1":
        percobaan = 0
        user_login = None

        while percobaan < 3:
            os.system(clear)
            print("=== LOGIN ===")
            username = input("Username: ").strip()
            password = input("Password: ").strip()

            if username in users and users[username]["password"] == password:
                user_login = username
                break

            percobaan += 1
            print(f"Username atau password salah! Sisa percobaan: {3 - percobaan}")
            input("Tekan Enter untuk lanjut...")

        if user_login is None:
            print("Terlalu banyak percobaan gagal. Kembali ke menu awal.")
            input("Tekan Enter untuk lanjut...")
            continue

        # menu admin
        if users[user_login]["role"] == "admin":
            while True:
                os.system(clear)
                print("=" * 45)
                print(f"   MENU ADMIN - Halo, {user_login}!")
                print("=" * 45)
                print("1. Tambah Barang (Create)")
                print("2. Lihat Daftar Barang (Read)")
                print("3. Ubah Data Barang (Update)")
                print("4. Hapus Barang (Delete)")
                print("5. Logout")
                menu_admin = input("Pilih menu (1-5): ").strip()

                # menambahkan barang (create)
                if menu_admin == "1":
                    os.system(clear)
                    print("=== TAMBAH BARANG ===")

                    while True:
                        nama = input("Nama barang      : ").strip()
                        if nama == "":
                            print("Nama barang tidak boleh kosong!")
                        else:
                            break

                    while True:
                        lokasi = input("Lokasi (mis. Kamar 3, Dapur): ").strip()
                        if lokasi == "":
                            print("Lokasi tidak boleh kosong!")
                        else:
                            break

                    while True:
                        jumlah = input("Jumlah           : ").strip()
                        if not jumlah.isdigit():
                            print("Jumlah harus berupa angka bulat positif!")
                        elif int(jumlah) < 1:
                            print("Jumlah minimal 1!")
                        else:
                            jumlah = int(jumlah)
                            break

                    print("Kondisi: 1. Baik  2. Rusak Ringan  3. Rusak Berat")
                    while True:
                        pilih_kondisi = input("Pilih kondisi (1-3): ").strip()
                        if pilih_kondisi in daftar_kondisi:
                            kondisi = daftar_kondisi[pilih_kondisi]
                            break
                        else:
                            print("Pilihan harus 1, 2, atau 3!")

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
                    os.system(clear)
                    print("=== DAFTAR BARANG KOS ===")
                    if len(barang) == 0:
                        print("Belum ada data barang.")
                    else:
                        print(
                            f"{'ID':<4}{'Nama':<20}{'Lokasi':<18}{'Jml':<6}{'Kondisi':<14}"
                        )
                        print("-" * 62)
                        for kode, b in barang.items():
                            print(
                                f"{kode:<4}{b['nama']:<20}{b['lokasi']:<18}{b['jumlah']:<6}{b['kondisi']:<14}"
                            )
                    input("\nTekan Enter untuk kembali...")

                # memperbarui data barang (update)
                elif menu_admin == "3":
                    os.system(clear)
                    print("=== UBAH DATA BARANG ===")
                    if len(barang) == 0:
                        print("Belum ada data barang.")
                        input("Tekan Enter untuk kembali...")
                        continue

                    print(
                        f"{'ID':<4}{'Nama':<20}{'Lokasi':<18}{'Jml':<6}{'Kondisi':<14}"
                    )
                    print("-" * 62)
                    for kode, b in barang.items():
                        print(
                            f"{kode:<4}{b['nama']:<20}{b['lokasi']:<18}{b['jumlah']:<6}{b['kondisi']:<14}"
                        )

                    kode_input = input("\nPilih ID barang yang diubah: ").strip()
                    if not kode_input.isdigit() or int(kode_input) not in barang:
                        print("ID barang tidak valid!")
                        input("Tekan Enter untuk kembali...")
                        continue

                    kode = int(kode_input)
                    print(f"\nBarang dipilih: {barang[kode]['nama']}")
                    print("1. Ubah nama")
                    print("2. Ubah lokasi")
                    print("3. Ubah jumlah")
                    print("4. Ubah kondisi")
                    print("5. Batal")
                    ubah = input("Pilih data yang diubah (1-5): ").strip()

                    if ubah == "1":
                        baru = input("Nama baru: ").strip()
                        if baru == "":
                            print("Nama tidak boleh kosong! Perubahan dibatalkan.")
                        else:
                            barang[kode]["nama"] = baru
                            print("Nama berhasil diubah!")
                    elif ubah == "2":
                        baru = input("Lokasi baru: ").strip()
                        if baru == "":
                            print("Lokasi tidak boleh kosong! Perubahan dibatalkan.")
                        else:
                            barang[kode]["lokasi"] = baru
                            print("Lokasi berhasil diubah!")
                    elif ubah == "3":
                        baru = input("Jumlah baru: ").strip()
                        if not baru.isdigit() or int(baru) < 1:
                            print(
                                "Jumlah harus angka bulat minimal 1! Perubahan dibatalkan."
                            )
                        else:
                            barang[kode]["jumlah"] = int(baru)
                            print("Jumlah berhasil diubah!")
                    elif ubah == "4":
                        print("1. Baik  2. Rusak Ringan  3. Rusak Berat")
                        baru = input("Pilih kondisi baru (1-3): ").strip()
                        if baru in daftar_kondisi:
                            barang[kode]["kondisi"] = daftar_kondisi[baru]
                            print("Kondisi berhasil diubah!")
                        else:
                            print("Pilihan tidak valid! Perubahan dibatalkan.")
                    elif ubah == "5":
                        print("Perubahan dibatalkan.")
                    else:
                        print("Pilihan tidak valid!")
                    input("Tekan Enter untuk kembali...")

                # menghapus data barang (delete)
                elif menu_admin == "4":
                    os.system(clear)
                    print("=== HAPUS BARANG ===")
                    if len(barang) == 0:
                        print("Belum ada data barang.")
                        input("Tekan Enter untuk kembali...")
                        continue

                    print(
                        f"{'ID':<4}{'Nama':<20}{'Lokasi':<18}{'Jml':<6}{'Kondisi':<14}"
                    )
                    print("-" * 62)
                    for kode, b in barang.items():
                        print(
                            f"{kode:<4}{b['nama']:<20}{b['lokasi']:<18}{b['jumlah']:<6}{b['kondisi']:<14}"
                        )

                    kode_input = input("\nPilih ID barang yang dihapus: ").strip()
                    if not kode_input.isdigit() or int(kode_input) not in barang:
                        print("ID barang tidak valid!")
                    else:
                        kode = int(kode_input)
                        yakin = (
                            input(f"Yakin hapus '{barang[kode]['nama']}'? (y/n): ")
                            .strip()
                            .lower()
                        )
                        if yakin == "y":
                            del barang[kode]
                            print("Barang berhasil dihapus!")
                        else:
                            print("Penghapusan dibatalkan.")
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
                os.system(clear)
                print("=" * 45)
                print(f"   MENU PENGGUNA - Halo, {user_login}!")
                print("=" * 45)
                print("1. Lihat Daftar Barang")
                print("2. Logout")
                menu_user = input("Pilih menu (1-2): ").strip()

                if menu_user == "1":
                    os.system(clear)
                    print("=== DAFTAR BARANG KOS ===")
                    if len(barang) == 0:
                        print("Belum ada data barang.")
                    else:
                        print(
                            f"{'ID':<4}{'Nama':<20}{'Lokasi':<18}{'Jml':<6}{'Kondisi':<14}"
                        )
                        print("-" * 62)
                        for kode, b in barang.items():
                            print(
                                f"{kode:<4}{b['nama']:<20}{b['lokasi']:<18}{b['jumlah']:<6}{b['kondisi']:<14}"
                            )
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
        os.system(clear)
        print("=== REGISTER ===")
        username_baru = input("Username baru: ").strip()

        if username_baru == "" or " " in username_baru:
            print("Username tidak boleh kosong atau mengandung spasi!")
        elif username_baru in users:
            print("Username sudah dipakai!")
        else:
            password_baru = input("Password baru (min. 6 karakter): ").strip()
            if len(password_baru) < 6:
                print("Password minimal 6 karakter!")
            else:
                users[username_baru] = {"password": password_baru, "role": "user"}
                print("Registrasi berhasil! Silakan login.")
        input("Tekan Enter untuk kembali...")

    # keluar dari program
    elif menu_awal == "3":
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut...")
