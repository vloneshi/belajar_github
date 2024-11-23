# Membuat set
angka = {1, 2, 3, 2, 1} # Duplikat akan dihilangkan
print (angka) # Output: {1, 2, 3}

# Operasi Himpunan
himpunan_a = {1, 3, 5, 7, 9}
himpunan_a.add(10)
himpunan_b = {2, 4, 6, 8}
print (himpunan_a.union(himpunan_b)) # Gabungan
# Perintah .union itu untuk gabungan
print (himpunan_a.intersection(himpunan_b)) # Irisan
# .intersection itu perintah untuk mencari angka yg sama

# 1 Membuat set kosong
my_set = set()

# 2 Membuat set dengan beberapa elemen
my_set = {1, 2, 3, 4}

# 3 Menambahkan elemen
my_set.add(5)  

# 4 Menghapus elemen
my_set.remove(3)  # Menghapus elemen 3 (akan menimbulkan error jika tidak ada)
my_set.discard(4)  # Menghapus elemen 4 (tidak menimbulkan error jika tidak ada)

# 5 Menampilkan elemen dalam set
print(my_set)  

''' OPERASI SET '''
# Union : menggabungkan dua set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # {1, 2, 3, 4, 5}

# Intersection : mengambil elemen yang ada di kedua set
intersection_set = set1 & set2  # {3}

# Differences : mengambil elemen yang ada di set1 tetapi tidak ada di set2
difference_set = set1 - set2  # {1, 2}

# Symmetric Difference: Mengambil elemen yang ada di salah satu set tetapi tidak di kedua-duanya.
sym_diff_set = set1 ^ set2  # {1, 2, 4, 5}

# 6 Cek Keanggotaan
if 2 in my_set:
    print("2 ada di dalam set")

# 7 Mengubah set menjadi list
my_list = list(my_set)

'''KESIMPULAN NYA'''
# Membuat dan mengelola set
my_set = {1, 2, 3, 4}

# Menambahkan elemen
my_set.add(5)

# Menghapus elemen
my_set.discard(2)

# Menampilkan set
print(my_set)  # Output: {1, 3, 4, 5}

# Operasi set
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a | set_b)  # Union
print(set_a & set_b)  # Intersection
print(set_a - set_b)  # Difference
print(set_a ^ set_b)  # Symmetric Difference
