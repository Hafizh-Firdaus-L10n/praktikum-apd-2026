# urutan pengerjaan biar ga bolak balik classroom
# 1. buat list bagasi
# 2. hitung berat akhir tanpa menggunakan sum(harus hitung manual) dan simpan dalam variabel berat_akhir
# 3. hitung total bayar dengan cara mengalikan berat akhir dengan 0.05 dan simpan dalam variabel total_bayar
# 4. hitung rata rata berat bagasi menggunakan variabel bernama rata_rata yang berisi variabel berat_akhir dibagi dengan banyak data, boleh pakai len(bagasi)
# 5. buat variabel bernama nim yang diisi dengan 2 digit terakhir nim
# 6. buat variabel bernama bolean yang isinya nim < rata_rata
# 7. list slicing untuk mengambil dan menampilkan data penumpang yang di tengah yaitu indeks ke-2 hingga indeks ke-4
# 8. konversi total berat akhir ke satuan gram
# 9. tampilkan semua nilai variabel yang ada menggunakan print


bagasi_1 = 12
bagasi_2 = 18
bagasi_3 = 7
bagasi_4 = 15
bagasi_5 = 20
bagasi_6 = 10

list_bagasi = [bagasi_1, bagasi_2, bagasi_3, bagasi_4, bagasi_5, bagasi_6]

berat_akhir = bagasi_1 + bagasi_2 + bagasi_3 + bagasi_4 + bagasi_5 + bagasi_6
total_bayar = berat_akhir * 0.05
berat_akhir_gram = berat_akhir * 1000

rata_rata = berat_akhir / len(list_bagasi)

nim = 35
bolean = nim < rata_rata

bagasi_tengah = list_bagasi[2:5]

print("Bagasi 1:", bagasi_1)
print("Bagasi 2:", bagasi_2)
print("Bagasi 3:", bagasi_3)
print("Bagasi 4:", bagasi_4)
print("Bagasi 5:", bagasi_5)
print("Bagasi 6:", bagasi_6)
print("Berat Akhir:", berat_akhir)
print("Total Bayar:", total_bayar)
print("Rata-rata Berat Bagasi:", rata_rata)
print("NIM:", nim)
print("Bolean:", bolean)
print("Bagasi Tengah:", bagasi_tengah)
print("Berat Akhir dalam Gram:", berat_akhir_gram)
