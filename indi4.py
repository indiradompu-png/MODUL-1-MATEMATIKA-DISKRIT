kartu_mahasiswa = True
jas_lab = True

# Model logika 
boleh_masuk = kartu_mahasiswa and jas_lab

# Output hasil 
if boleh_masuk:
   print("Mahasiswa BOLEH masuk laboratorium")
else:
   print("Mahasiswa TIDAK BOLEH masuk laboratorium")