print("\n==Belajar Function==\n")

# Mengisi nilai parameter
def sapa(nama):
    print("Halo,", nama, "!")
# Format string tanpa jarak spasi
    print(f"Halo, {nama}!") # Menampilkan function

# Mengisi nilai fungsi dengan tipe data string yaitu ochie
sapa("Ochie") # Output nya : Halo, Ochie!

# Contoh function kedua
def tambah(a, b, c):
    hasil = (a + b) / c
    return hasil
 

jumlah = tambah(3,5,2)
print("Hasil nya adalah",jumlah) # Output nya 4 (3+5:2)

print("\n==Perintah List==\n")

# Membuat list
buah = ["apel", "pisang", "mangga"]

# Mengakses elemen
(buah[0]) # Output : apel, karna python dimulai dari 0 bukan 1

# Jika ingin mengubah elemen
buah[1] = "jeruk"
print(buah) # Outputnya berubah jadi ['apel, 'jeruk', 'mangga']

''' Challenge menambahkan 2 buah bebas
lalu hapus mangga'''

fruit = ["apple", "banana", "mango"]

# Menambahkan 2 buah
fruit.extend(["melon", "watermelon"])

'''
cara lain bisa menggunakan :
buah.append("melon")
buah.append("watermelon")
'''

# Cara kalo mau nambahin fruit tapi taro diurutan awal

fruit.insert(0, "strawberry")


# Menghapus salah satu buah
fruit.remove("mango")

'''
cara lain kalo mau menghapus :
del fruit [2]
'''

print(fruit)

print("\n==Perintah Tuple==\n")
# gabisa dirubah, dan menggunakan nya memakai tanda kurung biasa

# Struktur data Tuple

angka1 = (1, 2, 3)
angka2 = (4, 5, 6)
angka3 = angka1 + angka2

print(angka3)