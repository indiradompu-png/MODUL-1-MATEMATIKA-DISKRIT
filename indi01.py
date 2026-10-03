prestasi = True
ekonomi_kurang = False

# Model logika
beasiswa = prestasi or ekonomi_kurang

# Output hasil seleksi
if beasiswa:
    print("Mahasiswa mendapatkan BEASISWA")
else:
    print("Mahasiswa TIDAK mendapatkan beasiswa")