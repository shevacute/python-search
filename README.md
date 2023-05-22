1.Sequential Search
  adalah algoritma pencarian yang sederhana dan langsung. Algoritma ini memeriksa setiap elemen dalam urutan secara berurutan sampai elemen yang dicari ditemukan atau sampai seluruh urutan selesai diperiksa. Jika elemen ditemukan, algoritma mengembalikan indeksnya; jika tidak ditemukan, algoritma mengembalikan nilai yang menunjukkan bahwa elemen tidak ada dalam urutan.
2.Binary Search
  algoritma pencarian yang efisien digunakan pada urutan data yang telah diurutkan. Algoritma ini membagi urutan data menjadi setengah pada setiap iterasi, dengan membandingkan elemen tengah urutan dengan elemen yang dicari. Jika elemen tengah sama dengan elemen yang dicari, algoritma mengembalikan indeksnya. Jika elemen tengah lebih kecil dari elemen yang dicari, algoritma melanjutkan pencarian hanya pada setengah kanan urutan. Jika elemen tengah lebih besar dari elemen yang dicari, algoritma melanjutkan pencarian hanya pada setengah kiri urutan. Proses ini berlanjut hingga elemen ditemukan atau setengah urutan tidak dapat dibagi lagi.
  
PENJELASAN PERCOBAAN 10,11,12
10.(binary_search_rotation.py)
  Menemukan rotasi terkecil dari sebuah list yang sudah dirotasi 
  jika list = [6,7,8,9,1,2,3,4,5], maka outputnya adalah 4
11.(binary_search_most_frequent.py)
   Menentukan elemen yang paling sering banyak muncul dari list yang diurutkan
   jika listnya = [2,2,2,4,4,6,6,6,6,8,8,8,8,8], maka seharusnya output yang dihasilkan ialah 8
   KENDALA : tetapi berdasarkan percobaan yang saya kerjakan output dari elemen yang paling sering        banyak muncul yaitu 6
12.(binary_search_name_list.py)
   Mencari data dalam list terurut, dari list yang disediakan kita dapat menginputkan elemen yang          dimana output nya akan menghasilkan elemen tersedia atau tidak mengacu dari list yang ada.
