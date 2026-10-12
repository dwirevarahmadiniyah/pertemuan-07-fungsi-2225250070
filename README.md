# Pertemuan 07 Fungsi Python

Nama: DWI REVA RAHMADINIYAH 
NIM : 2225250070
Kelas: 3E

## Tujuan

Menggunakan fungsi, parameter, nilai kembali (*return value*), dan ruang lingkup variabel (*scope*) untuk membuat program Python yang modular. Dengan menggunakan fungsi, program menjadi lebih terstruktur, mudah dibaca, dan mudah diperbaiki.

## Cara Menjalankan

Program disimpan dengan nama `utilitas_matematika.py` di dalam folder `praktik`.

Jalankan program melalui terminal VS Code menggunakan perintah berikut:

```bash
python3 praktik/utilitas_matematika.py
```

Jika menggunakan Windows dan perintah tersebut tidak bisa dijalankan, gunakan:

```bash
python praktik/utilitas_matematika.py
```

## Struktur Fungsi

| Nama Fungsi | Parameter | Nilai Return | Kegunaan |
|---|---|---|---|
| `luas_persegi_panjang(p, l)` | `p` = panjang, `l` = lebar | `p * l` | Menghitung luas persegi panjang. |
| `luas_segitiga(a, t)` | `a` = alas, `t` = tinggi | `0.5 * a * t` | Menghitung luas segitiga. |
| `jumlah_n(n)` | `n` = batas bilangan | `total` | Menghitung jumlah bilangan dari 1 sampai n. |
| `faktorial(n)` | `n` = bilangan yang dihitung faktorialnya | `hasil` | Menghitung faktorial bilangan menggunakan perulangan. |
| `tampilkan_menu()` | Tidak ada | Tidak ada nilai return khusus (`None`) | Menampilkan pilihan menu aplikasi matematika. |

Fungsi-fungsi tersebut dibuat agar setiap bagian program memiliki tugas masing-masing. Parameter digunakan untuk menerima masukan, sedangkan `return` digunakan untuk mengembalikan hasil perhitungan kepada bagian program yang memanggil fungsi.

## Hasil Pengujian

| No. | Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | Menu 1, panjang = 10, lebar = 5 | Luas = 50 | 50 | Berhasil |
| 2 | Menu 2, alas = 10, tinggi = 6 | Luas = 30 | 30 | Berhasil |
| 3 | Menu 3, n = 5 | Jumlah = 15 | 15 | Berhasil |
| 4 | Menu 4, n = 5 | Faktorial = 120 | 120 | Berhasil |
| 5 | Menu 5 | Program berhenti | Program berhenti | Berhasil |
| 6 | Memasukkan pilihan menu 9 | Pesan pilihan tidak valid | Pesan pilihan tidak valid | Berhasil |

*Catatan: Hasil aktual dan status di atas merupakan hasil yang diharapkan berdasarkan kode program. Sesuaikan dengan hasil yang benar-benar muncul saat program dijalankan.*

## Refleksi

Bagian program yang menjadi lebih sederhana setelah dipisahkan menjadi fungsi adalah perhitungan luas persegi panjang. Perhitungan tersebut dibuat dalam fungsi `luas_persegi_panjang(p, l)`, sehingga rumus luas tidak perlu ditulis ulang setiap kali dibutuhkan. Program cukup memanggil fungsi dengan memasukkan nilai panjang dan lebar.

Selain itu, penggunaan fungsi membuat program lebih rapi dan mudah dipahami. Jika rumus perlu diperbaiki, perubahan dapat dilakukan pada fungsi yang bersangkutan tanpa harus mengubah seluruh program. Dengan demikian, penggunaan fungsi membantu membuat program lebih modular, efisien, dan mudah dikembangkan.
