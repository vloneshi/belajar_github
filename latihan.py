''' Soal ke 1, Periksa apakah nilai variable umur lebih besar dari 18.
umur = 20'''

# Jawab 
umur1 = 20
umur2 = 18
print(umur1 > umur2)

# Cara lain
umur = 20
is_dewasa = umur > 18
print(is_dewasa) # Output True


'''Soal ke 2, Periksa apakah nilai variable nama sama dengan "Andi"
nama = "Budi'''

#Jawab
nama1 = "Andi"
nama2 = "Budi"
print(nama1 == nama2 )

# Cara lain
nama = "Budi"
is_andi = nama == "Andi"
print(is_andi)

''' Soal ke 3, Buatlah program yang meminta input nomor hari (1-7)
lalu menampilkan nama hari-hari'''

# Jawab
hari = {
    1: "Senin",
    2: "Selasa",
    3: "Rabu",
    4: "Kamis",
    5: "Jumat",
    6: "Sabtu",
    7: "Minggu"
}

nomor_hari = int(input("Masukkan nomor hari (1-7): "))
if nomor_hari in hari:
    print(f"Hari ke-{nomor_hari} adalah {hari[nomor_hari]}.")
else:
    print("Input tidak valid! Silakan masukkan nomor antara 1 sampai 7.")


# Cara lain
nomor_hari = int(input("Masukkan nomor hari (1-7): "))
if nomor_hari == 1:
    print("Hari Senin")
elif nomor_hari == 2:
    print("Hari Selasa")
elif nomor_hari == 3:
    print("Hari Rabu")
elif nomor_hari == 4:
    print("Hari Kamis")
elif nomor_hari == 5:
    print("Hari Jumat")
elif nomor_hari == 6:
    print("Hari Sabtu")
elif nomor_hari == 7:
    print("Hari Minggu")
else:
    print("Nomor hari tidak valid")

'''Soal ke 4, Buat fungsi bernama hitung_luas_persegi_panjang yang menerima 2 parameter
yaitu panjang dan lebar. Fungsi ini akan menghitung dan mengembalikan luas persegi panjang
dengan simbol * 
panjang = 10 dan lebar = 5'''

def hitung_luas_persegi_panjang(panjang, lebar):
    hasil = (panjang * lebar)
    return hasil

jumlah = hitung_luas_persegi_panjang(10, 5)   
print("Hasil nya adalah",jumlah) # Output nya "Hasilnya adalah 50"


#Soal ke 5, Buatlah sebuah list yg berisi buah-buahan, lalu rubahlah menjadi tuple.
buah = ["Apel", "Pisang", "Mangga"]
buah_tuple = tuple(buah)
print(buah_tuple) # Output: ('Apel', 'Pisang', 'Mangga')

# Soal ke 6, Tampilkan daftar buah indeks ke 0 dan ke 2
print(buah_tuple[0])  # Output: Apel
print(buah_tuple[2])  # Output: Mangga

