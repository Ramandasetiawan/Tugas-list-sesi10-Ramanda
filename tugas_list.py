# # NO1
# list_input = [8, 3, 12, 4, 7, 2]

# # Menghapus angka yang kurang dari 5 dan menggantinya dengan nilai 0
# list_output = [num if num >= 5 else 0 for num in list_input]

# # Mengurutkan dari nilai terbesar ke terkecil
# list_output.sort(reverse=True)

# print(list_output)





# # NO2
# list_input = [7, 4, 9, 2, 5, 1]

# # Menghapus nilai yang merupakan bilangan ganjil
# list_output = [num for num in list_input if num % 2 == 0]

# # Mengurutkan sisa nilai dari terkecil ke terbesar
# list_output.sort()

# print(list_output)





# # NO3
# kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]

# # Menghapus kata yang memiliki panjang kurang dari lima karakter
# filtered_kata = [word for word in kata if len(word) >= 5]

# # Mengurutkan kata-kata yang tersisa secara alfabetis
# filtered_kata.sort()

# print(filtered_kata)





# # NO4
# list1 = ["apel", "jeruk", "mangga"]
# list2 = ["apel", "anggur", "nanas"]

# # Menggabungkan kedua list
# combined_list = list1 + list2

# # Menghapus semua buah yang memiliki nama yang sama
# unique_fruits = list(set(combined_list))

# # Mengurutkan sisa buah-buahan secara alfabetis
# unique_fruits.sort()

# print(unique_fruits)





# # NO5
# list_input = [105, 20, 8, 150, 30, 5, 200]

# # Menghapus nilai yang kurang dari 10 dan lebih dari 100
# filtered_values = [num for num in list_input if 10 <= num <= 100]

# # Mengurutkan sisa nilai dari terkecil ke terbesar
# filtered_values.sort()

# print(filtered_values)




# # NO6
# buku1 = {"no_isbn": "123-1234-12-0", "judul": "Python ", "pengarang": "Ramanda", "isihalaman": 400, "deskripsi": "Buku panduan pemrograman Python", "stok": 20, "booked": 0}
# buku2 = {"no_isbn": "123-1234-12-1", "judul": "Data base", "pengarang": "Manda", "isihalaman": 370, "deskripsi": "Pengantar ilmu data base", "stok": 9, "booked": 2}
# buku3 = {"no_isbn": "123-1234-12-2", "judul": "Web Development Basics", "pengarang": "Rama", "isihalaman": 300, "deskripsi": "Dasar-dasar pengembangan web", "stok": 7, "booked": 1}

# list_buku = [buku1, buku2, buku3]

# # Data mahasiswa
# buku1 = {"no_isbn": "123-1234-12-0", "judul": "Python ", "pengarang": "Ramanda", "isihalaman": 400, "deskripsi": "Buku panduan pemrograman Python", "stok": 20, "booked": 0}
# buku2 = {"no_isbn": "123-1234-12-1", "judul": "Data base", "pengarang": "Manda", "isihalaman": 370, "deskripsi": "Pengantar ilmu data base", "stok": 9, "booked": 2}
# buku3 = {"no_isbn": "123-1234-12-2", "judul": "Web Development Basics", "pengarang": "Rama", "isihalaman": 300, "deskripsi": "Dasar-dasar pengembangan web", "stok": 7, "booked": 1}

# list_buku = [buku1, buku2, buku3]

# # Data mahasiswa
# mahasiswa1 = {"nama": "agung", "nim": "20230040054", "nomerhp": "085862859225", "alamat": "Jl. Jampangkulon No. 123"}
# mahasiswa2 = {"nama": "lasmi", "nim": "20230040055", "nomerhp": "085872415431", "alamat": "Jl. Cihaur No. 476"}

# list_mahasiswa = [mahasiswa1, mahasiswa2]

# # Data peminjaman
# peminjaman1 = {"nim": "20230040054", "no_isbn": "123-1234-12-0", "tanggalpinjam": "2024-08-26", "tanggal_kembali": "2024-07-07", "status": "Dikembalikan"}
# peminjaman2 = {"nim": "20230040055", "no_isbn": "123-1234-12-1", "tanggalpinjam": "2024-08-29", "tanggal_kembali": "2024-07-19", "status": "Belum dikembalikan"}

# list_peminjaman = [peminjaman1, peminjaman2]

# # Fungsi untuk menampilkan daftar buku
# def tampilkan_buku():
#     for buku in list_buku:
#         print("No ISBN:", buku["no_isbn"])
#         print("Judul:", buku["judul"])
#         print("Pengarang:", buku["pengarang"])
#         print("Isi Halaman:", buku["isihalaman"])
#         print("Deskripsi:", buku["deskripsi"])
#         print("Stok:", buku["stok"])
#         print("Booked:", buku["booked"])
#         print()

# # Fungsi untuk menampilkan daftar mahasiswa
# def tampilkan_mahasiswa():
#     for mahasiswa in list_mahasiswa:
#         print("Nama:", mahasiswa["nama"])
#         print("NIM:", mahasiswa["nim"])
#         print("Nomor HP:", mahasiswa["nomerhp"])
#         print("Alamat:", mahasiswa["alamat"])
#         print()

# # Fungsi untuk menampilkan daftar peminjaman
# def tampilkan_peminjaman():
#     for peminjaman in list_peminjaman:
#         print("NIM:", peminjaman["nim"])
#         print("No ISBN:", peminjaman["no_isbn"])
#         print("Tanggal Pinjam:", peminjaman["tanggalpinjam"])
#         print("Tanggal Kembali:", peminjaman["tanggal_kembali"])
#         print("Status:", peminjaman["status"])
#         print()

# # Contoh pemanggilan fungsi untuk menampilkan data
# print("Daftar Buku:")
# tampilkan_buku()

# print("Daftar Mahasiswa:")
# tampilkan_mahasiswa()

# print("Daftar Peminjaman:")
# tampilkan_peminjaman()




