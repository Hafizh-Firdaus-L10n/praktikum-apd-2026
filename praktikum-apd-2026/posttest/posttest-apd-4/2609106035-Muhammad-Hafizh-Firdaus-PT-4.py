username_benar = "hafizh"
password_benar = "035"
percobaan = 0
login_berhasil = False

while percobaan < 3:
    username = input("Username: ")
    password = input("Password: ")
    if username == username_benar and password == password_benar:
        login_berhasil = True
        break
    else:
        percobaan += 1
        print(f"Salah! Sisa percobaan: {3 - percobaan}")

if login_berhasil:
    data_siswa = []
    kelas_list = []
    lanjut = "ya"

    while lanjut == "ya":
        nama = input("Nama Siswa: ")
        kelas = input("Kelas: ")
        ikut = input("Ikut ujian? (ya/tidak): ")

        if kelas not in kelas_list:
            kelas_list.append(kelas)

        if ikut != "ya":
            data_siswa.append([nama, kelas, "Tidak Ikut", 0, "-"])
            continue

        while True:
            benar = int(input("Jumlah soal benar: "))
            salah = int(input("Jumlah soal salah: "))
            if benar >= 0 and salah >= 0 and benar + salah == 20:
                break
            print("Total benar + salah harus 20. Silahkan ulang.")

        nilai = benar * 5

        if nilai >= 80:
            kategori = "Sangat baik"
        elif nilai >= 60:
            kategori = "Baik"
        elif nilai >= 40:
            kategori = "Cukup"
        else:
            kategori = "Perlu belajar lagi"

        data_siswa.append([nama, kelas, "Ikut", nilai, kategori])
        lanjut = input("Masih ingin input data? (ya/tidak): ")

    print("\n=====DATA NILAI SISWA=====")
    for k in kelas_list:
        print(f"\n=== Kelas {k} ===")
        for siswa in data_siswa:
            if siswa[1] == k:
                print(f"Nama   : {siswa[0]}")
                print(f"Kelas  : {siswa[1]}")
                print(f"Ujian  : {siswa[2]}")
                print(f"Nilai  : {siswa[3]} ({siswa[4]})")
                print("")

else:
    print("Login gagal 3 kali. Program berhenti.")
