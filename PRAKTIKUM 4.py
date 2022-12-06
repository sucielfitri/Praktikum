import random

#Daftar ini memberikan gambaran tentang waktu acara.
Kalimat_starter = random.randint(1, 3)
if Kalimat_starter == 1 :
    kalimat_1 = ("Di malam sepi, ")
if Kalimat_starter == 2 :
    kalimat_1 = ("seorang gadis merenung kembali, ")
if Kalimat_starter == 3 :
    kalimat_1 = ("kejadian masa lampau, ")

#Daftar ini menceritakan tentang karakter utama dari cerita ini.
karakter = random.randint(1, 3)
if karakter == 1 :
    kalimat_2 = ("Gadis itu menyimpan sejuta derita ")
if karakter == 2 :
    kalimat_2 = ("yang tak pernah ia ceritakan pada siapa pun, ")
if karakter == 3 :
    kalimat_2 = ("karena pribadinya yang pemalu ")

#Daftar ini menentukan hari yang tepat di mana beberapa insiden telah terjadi.
waktu = random.randint(1, 3)
if waktu == 1 :
    kalimat_3 = ("Senyumnya hilang sejak kepergian ayahnya")
if waktu == 2 :
    kalimat_3 = ("tepat pada hari ulang tahunnya ")
if waktu == 3 :
    kalimat_3 = ("ke- 7 tahun ")

#Daftar ini mendefinisikan plot cerita.
story_plot = random.randint(1, 3)
if story_plot == 1 :
    kalimat_4 = (" Kejadian yang benar-benar menusuk batin, ")
if story_plot == 2 :
    kalimat_4 = ("seorang gadis kecil, ")
if story_plot == 3 :
    kalimat_4 = ("tepat di depan matanya, ")

#Daftar ini mendefinisikan tempat di mana insiden itu terjadi.
tempat = random.randint(1, 3)
if tempat == 1 :
    kalimat_5 = ("Sebuah truk tronton menerjang sosok ayah dari gadis manis, ")
if tempat == 2 :
    kalimat_5 = ("tepat di depan rumah, ")
if tempat == 3 :
    kalimat_5 = ("seketika berlumuran darah dengan kado impian di tangannya, ")

#Daftar ini mendefinisikan karakter kedua dari cerita.
second_character = random.randint(1, 3)
if second_character == 1 :
    kalimat_6 = ("Setelah kepergian ayah, ibu jadi mudah marah ")
if second_character == 2 :
    kalimat_6 = ("dan melampiaskan emosinya ")
if second_character == 3 :
    kalimat_6 = ("dengan menyerang secara fisik hingga mentalnya ")

#Daftar ini mendefinisikan usia karakter kedua.
usia = random.randint(1, 3)
if usia == 1 :
    kalimat_7 = ("Mungkin karena usia ibu masih terbilang sangat muda ")
if usia == 2 :
    kalimat_7 = ("dan belum siap ")
if usia == 3 :
    kalimat_7 = ("secara emosional dalam mengurus anak ")

#Daftar ini menceritakan tentang pekerjaan yang dilakukan karakter kedua.
pekerjaan = random.randint(1, 3)
if pekerjaan == 1 :
    kalimat_8 = ("Sejak itu ibu semakin tidak terkendali ")
if pekerjaan == 2 :
    kalimat_8 = ("dan selalu pulang ")
if pekerjaan == 3 :
    kalimat_8 = ("dalam keadaan mabuk ")

print (kalimat_1, kalimat_2, kalimat_3, kalimat_4, kalimat_5, kalimat_6, kalimat_7, kalimat_8)