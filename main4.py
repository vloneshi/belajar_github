# Materi Perulangan menggunakan "for"
# for untuk materi yang ditentukan

for i in range(1, 20):
    if i == 6 :
        break
    print("Princesssss")

# Perulangan menggunakan "while"
# while untuk perulangan nya tidak ditentukan

angka = 1
while angka <= 20:
    print(angka)
    angka += 1

    

Percabangan if
nilai = 60
if nilai >= 75:
    print("Anda lulus ujian.")
else :
    print("Anda belum lulus ujian.")

nilai = 75
if nilai >= 75:
    print("Anda lulus ujian.")
else :
    print("Anda belum lulus ujian.")

# Challenge
nilai = [80,75,56,45]
for i in nilai:
    if i >= 80:
        status = "Baik Sekali"
    elif i >= 75:
        status = "Baik"
    elif i >= 56:
        status = "Cukup"
    elif i >= 45:
        status = "Kurang"
    else:
        status = "Tidak Lulus"

    print(f"Nilai: {i}, status: {status}")

# Latihan
for princess in range(1, 20):
    if princess == 6:
        break
    print("Sedang belajar python")

'''
elif = ngasi kategori (banyak opsi)
else = tidak ada diopsi 
if = jika 

'''

# Latihan Princess
nilai = [73]
for c in nilai: 
    if c >= 85:
        grade = "A"
    elif c >= 80:
        grade = "B"
    elif c >= 70:
        grade = "C"
    else:
        grade : "D"
    print(f"Nilai: {c}, Grade: {grade}")