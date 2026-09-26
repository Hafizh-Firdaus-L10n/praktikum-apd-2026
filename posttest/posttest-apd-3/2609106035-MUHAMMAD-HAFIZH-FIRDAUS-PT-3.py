nama = input("Silahkan masukkan nama anda: ")
nim = input("Silahkan masukkan NIM anda: ")

if nama == "hafizh" and nim == "35":
    print("Selamat datang, Hafizh.")

    pertalite = 10000
    pertamax = 12500
    pertamax_turbo = 15000

    print("\nJenis Bensin:")
    print("1. Pertalite: Rp. ", pertalite)
    print("2. Pertamax: Rp. ", pertamax)
    print("3. Pertamax Turbo Rp.: ", pertamax_turbo)
    pilihan_bensin = input("Pilih jenis bensin (1-3): ")

    if pilihan_bensin == "1":
        jenis = "Pertalite"
        harga_per_liter = pertalite
    elif pilihan_bensin == "2":
        jenis = "Pertamax"
        harga_per_liter = pertamax
    elif pilihan_bensin == "3":
        jenis = "Pertamax Turbo"
        harga_per_liter = pertamax_turbo
    else:
        print("Pilihan tidak valid.")

    jumlah_liter = float(input("Masukkan jumlah liter: "))

    total_harga = harga_per_liter * jumlah_liter

    if jumlah_liter >= 10:
        diskon_pembelian = 0.10 * total_harga
    elif jumlah_liter >= 5:
        diskon_pembelian = 0.05 * total_harga
    else:
        diskon_pembelian = 0

    print("Total harga:", total_harga)
    print("Diskon:", diskon_pembelian)
    print("Total bayar:", total_harga - diskon_pembelian)

    member = input("Apakah pembeli member? (ya/tidak)")
    if member == "ya":
        diskon_member = 0.02 * total_harga
    else:
        diskon_member = 0

    total_diskon = diskon_pembelian + diskon_member
    total_bayar = total_harga - total_diskon

    print("\n==============================================")
    print("              STRUK TRANSAKSI SPBU             ")
    print("==============================================")
    print("Nama Pembeli       :", nama)
    print("NIM Pembeli        :", nim)
    print("Jenis BBM          :", jenis)
    print("Jumlah Liter       :", jumlah_liter, "L")
    print("Total Harga        : Rp", total_harga)
    print("Diskon             : Rp", diskon_pembelian + diskon_member)
    print("----------------------------------------------")
    print("TOTAL BAYAR        : Rp", total_bayar)
    print("==============================================")

else:
    print("Login salah. Nama atau NIM salah.")
