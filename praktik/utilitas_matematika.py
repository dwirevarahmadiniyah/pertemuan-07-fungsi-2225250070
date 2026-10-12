def luas_persegi_panjang(p, l):
    return p * l

def luas_segitiga(a, t):
    return 0.5 * a * t

def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

def tampilkan_menu():
    print("\n--- APLIKASI MATEMATIKA ---")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("5. Keluar")

# Program Utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")
    
    if pilihan == "1":
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        print(f"Hasil Luas Persegi Panjang: {luas_persegi_panjang(panjang, lebar)}")
        
    elif pilihan == "2":
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        print(f"Hasil Luas Segitiga: {luas_segitiga(alas, tinggi)}")
        
    elif pilihan == "3":
        n = int(input("Masukkan nilai n: "))
        print(f"Hasil Jumlah 1 sampai {n}: {jumlah_n(n)}")
        
    elif pilihan == "4":
        n = int(input("Masukkan nilai n: "))
        print(f"Hasil Faktorial {n}: {faktorial(n)}")
        
    elif pilihan == "5":
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1-5.")