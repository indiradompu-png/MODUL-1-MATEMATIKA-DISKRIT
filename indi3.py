sudah_bayar = False
izin_khusus = True

# Model logika
boleh_ujian = sudah_bayar or izin_khusus

# Output hasil
if boleh_ujian:
   print("Mahasiswa BOLEH mengikuti ujian")
else:
   ptint("Mahasiswa TIDAK  BOLEH mengikuti ujian")
