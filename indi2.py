kartu_mahasiswa = False
kartu_perpustakaan = True

# Model logika 
boleh_pinjam = kartu_mahasiswa or kartu_perpustakaan

# Output hasil 
if boleh_pinjam:
   print("Mahasiswa BOLEH meminjam buku")
else:
   print("Mahasiswa TIDAK BOLEH meminjam buku")