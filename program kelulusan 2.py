import re
pattern = "[0-9]{9}"  # perintah untuk menentukan input NIM dengan ketentuan validasi panjangnnya 9 dan hanya angka
nim = input ("NIM : ")
if (re.search(pattern, nim)):
   print("NIM BENAR")
else:
    print("NIM SALAH")

pattern = "[a-zA-Z]" # perintah untuk menentukan input Nama hanya menggunakan huruf besar dan kecil 
nama = input ("Nama : ") 
if (re.search(pattern, nama)):
   print("NAMA BENAR")
else:
    print("NAMA SALAH")
kehadiran=float (input("Kehadiran :"))#perintah untuk input kehadiran
tugas=float (input("Tugas :"))#perintah untuk input tugas
uts=float (input("UTS :"))#perintah untuk input uts
uas=float (input("UAS :"))#perintah untuk input uas



#Rumus untuk mencari nilai akhir(rata-rata) dan jumlah nilai
Jumlah_nilai = kehadiran+tugas+uas+uts # menghitung jumlah nilai
NA=(0.1*kehadiran)+(0.2*tugas)+(0.3*uts)+(0.4*uas) # menghitung NA dengan ketentuan

print("jumlah_nilai:",Jumlah_nilai) #perintah untuk menampilkan output jumlah nilai
print("Rata-Rata:",str(NA))#perintah untuk menampilkan output NA


#menentukan nilai Grade
if (NA >= 00 and NA < 30): # jika nilai akhir lebih dari atau sama dengan 0 dan kurang dari 30, maka gradenya E
    print("Grade:E")
elif (NA >= 31 and NA < 50):# jika nilai akhir lebih dari atau sama dengan 31 dan kurang dari 50, maka gradenya D
    print("Grade:D")
elif (NA >= 51 and NA < 70):# jika nilai akhir lebih dari atau sama dengan 51 dan kurang dari 70, maka gradenya C
    print("Grade:C") 
elif (NA >= 80 and NA < 90):# jika nilai akhir lebih dari atau sama dengan 80 dan kurang dari 90, maka gradenya B
    print("Grade:B")
elif (NA >= 91 and NA < 100):# jika nilai akhir lebih dari atau sama dengan 91 dan kurang dari 100, maka gradenya A
    print("Grade:A")

#perintah menentukan lulus atau tidak lulus
if NA >=51: # jika nilai lebih dari atau sama dengan 51 maka keterangannya L
    print("Keterangan:L")
else:
    print("Keterangan:TL")

