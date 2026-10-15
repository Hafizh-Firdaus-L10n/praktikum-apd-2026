# # # nama1 = "hafizh"
# # # # nama2 = "son"
# # # # nama3 = "kane"

# # # # # print(nama1, nama2, nama3)

# # list_nama = ["dele", "son", "kane"]
# # # # # print(list_nama)
# # # # # for i in list_nama:
# # # # #     print(i)

# # list_nama.append("eriksen")
# # list_nama.extend(["rose", "vertonghen"])
# # list_nama.insert(2, "alderweireld")
# # list_nama[0:3] = ["lloris", "dembele", "modric"]

# # # # for i in list_nama:
# # # #     print(i)


# poin1 = [1, 2, 3, 4, 5, 6, 7]
# poin2 = [8, 9, 10]
# poin = poin1 + poin2
# print(poin)
# # # # del list_nama[1:4]
# # # # print(list_nama)

# # # list_nama.remove("rose")
# # print(list_nama)

# list_nama = ["Hafizh", "Johann", "Azka"]
# ambil_nama = list_nama.pop(1)
# print(list_nama)

# line_up = [
#     ["Ferrari", "Leclerc", 16],
#     ["Mercedes", "Hamilton", 44],
#     ["Red Bull", "Verstappen", 1],
#     ["McLaren", "Norris", 4],
# ]
# for i in line_up:
#     for j in i:
#         print(j)


buah = ("apel", "mangga", "nanas")
listbuah = list(buah)
listbuah.append("pisang")
buah = tuple(listbuah)

print(buah)

game = ("ml", "genshin")
(moba, open_world) = game
print(moba)
print(open_world)
