# # # # # # # # # # kartu = {"merah", "merah", "biru", "hijau"}

# # # # # # # # # # print(kartu)

# # # # # # # # # # matkul = ["apd", "orsikom", "apd", "kalkulus"]
# # # # # # # # # # sks = set(matkul)
# # # # # # # # # # print(sks)

# # # # # # # # # kartu = {"merah", "merah", "biru", "hijau"}

# # # # # # # # # kartu.discard("merah")
# # # # # # # # # print(kartu)


# # # # # # # # # aslab1 = {"fina", "shasha", "risma"}
# # # # # # # # # aslab2 = {"larry", "attar", "haekal"}
# # # # # # # # # gabung = aslab1.union(aslab2)
# # # # # # # # # print(gabung)


# # # # # # # # # Matkul = {
# # # # # # # # #     "Matkul_ganjil" : "kalkulus",
# # # # # # # # # "Matkul_genap" : "statistik"
# # # # # # # # # }

# # # # # # # # # print(Matkul["Matkul_ganjil"])
# # # # # # # # # print(Matkul)


# # # # # # # # # Biodata = {
# # # # # # # # #     "Nama": "Siti Julpa",
# # # # # # # # #     "NIM": 25091060,
# # # # # # # # #     "KRS": ["Struktur Data", "Basis Data"],
# # # # # # # # #     "Mahasiswa_Aktif": True,
# # # # # # # # #     "Instagram": "julpatarr",
# # # # # # # # # }
# # # # # # # # # print(Biodata["Instagram"])
# # # # # # # # # print(Biodata["KRS"][0])

# # # # # # # # Biodata = {
# # # # # # # #     "Nama": "Siti Julpa",
# # # # # # # #     "NIM": 25091060,
# # # # # # # #     "KRS": ["Struktur Data", "Basis Data"],
# # # # # # # #     "Mahasiswa_Aktif": True,
# # # # # # # #     "Instagram": "julpatarr",
# # # # # # # # }
# # # # # # # # print(f"Nama saya adalah {Biodata.get('Nama')}")
# # # # # # # # print(Biodata.get("Nama"))
# # # # # # # # print(Biodata.get("Alamat"))
# # # # # # # # print(Biodata.get("Alamat", "Key untuk alamat tidak ada"))

# # # # # # # game = {
# # # # # # #     "pou": "chill",
# # # # # # #     "genshin impact": "action",
# # # # # # #     "valorant": "fps",
# # # # # # #     "minecraft": "sandbox",
# # # # # # #     "mobile legend": "moba",
# # # # # # # }
# # # # # # # for i in game:
# # # # # # #     print(i)
# # # # # # # for i in game.keys():
# # # # # # #     print(i)


# # # # # # game = {
# # # # # #     "pou": "chill",
# # # # # #     "genshin impact": "action",
# # # # # #     "valorant": "fps",
# # # # # #     "minecraft": "sandbox",
# # # # # #     "mobile legend": "moba",
# # # # # # }
# # # # # # for i in game.values():
# # # # # #     print(i)

# # # # # game = {
# # # # # "pou" : "chill",
# # # # # "genshin impact" : "action",
# # # # # "valorant" : "fps",
# # # # # "minecraft" : "sandbox",
# # # # # "mobile legend" : "moba"
# # # # # }
# # # # # for keys, value in game.items():
# # # # #     print(f"{keys} adalah jenis game {value}")


# # # # game = {
# # # #     "pou": "chill",
# # # #     "genshin impact": "action",
# # # #     "valorant": "fps",
# # # #     "minecraft": "sandbox",
# # # #     "mobile legend": "moba",
# # # # }
# # # # game["resident evil"] = "horror"
# # # # print(game)

# # # game = {
# # # "pou" : "chill",
# # # "genshin impact" : "action",
# # # "valorant" : "fps",
# # # "minecraft" : "sandbox",
# # # "mobile legend" : "moba"
# # # }
# # # game.update({"resident evil" : "horror"})
# # # print(game)

# # key = (
# #     "ayam geprek",
# #     "ayam goreng",
# #     "ayam bakar",
# # )
# # value = 12000
# # menu = dict.fromkeys(key, value)
# # print(menu)

# menu = {
#     "ayam": ["ayam geprek", "ayam goreng", "ayam bakar"],
#     "nasi": ["nasi goreng", "nasi uduk"],
#     "mie": ["mie goreng rendang", "mie goreng aceh"],
#     "kuah": ["soto", "rawon", "sop iga"],
# }
# for i, j in menu.items():
#     print(f"Kategori {i} memiliki menu :")
# for kategori in j:
#     print(kategori)
# print("")


data_siswa = {
    "siswa1": {"nama": "Johan", "kelas": "A2", "nilai": 95},
    "siswa2": {"nama": "Hafizh", "kelas": "A2", "nilai": 100},
    "siswa3": {"nama": "Son", "kelas": "A2", "nilai": 99},
}
