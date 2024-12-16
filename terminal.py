def hitung_biaya_parkir(durasi):
    # Tarif untuk 2 jam pertama
    dua_jam_pertama = 3000
    # Tarif per jam setelah 2 jam pertama
    lebih_dari_2_jam = 1500
    # Biaya tambahan jika parkir lebih dari 24 jam
    biaya_tambahan = 10000

    # Kondisi jika durasi parkir kurang dari atau sama dengan 2 jam
    if durasi <= 2:
        # Biaya parkir hanya untuk dua jam pertama
        biaya = dua_jam_pertama
    # Kondisi jika durasi parkir lebih dari 2 jam
    elif durasi > 2:
        # Biaya parkir setelah dua jam pertama dihitung berdasarkan durasi
        biaya = lebih_dari_2_jam * (durasi - 2) + dua_jam_pertama

    # Kondisi jika durasi parkir lebih dari 24 jam
    if durasi > 24:
        # Biaya tambahan berlaku jika parkir lebih dari 24 jam
        biaya = biaya_tambahan + (lebih_dari_2_jam * durasi) + dua_jam_pertama

    # Mengembalikan biaya yang telah dihitung
    return biaya

try:
    # Meminta input dari pengguna untuk durasi parkir
    durasi = int(input("Masukkan jam parkir: "))
    # Memeriksa apakah durasi yang dimasukkan negatif
    if durasi < 0:
        print("Jam parkir tidak valid.")
    else:
        # Menghitung biaya parkir menggunakan fungsi hitung_biaya_parkir
        biaya = hitung_biaya_parkir(durasi)
        # Menampilkan hasil perhitungan biaya parkir
        print(f"Biaya parkir untuk {durasi} jam adalah Rp{biaya}")
except ValueError:
    # Menangani kesalahan input jika yang dimasukkan bukan angka
    print("Harap masukkan durasi yang valid.")
