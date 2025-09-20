# KiPApp Helper

---
## Fitur Baru
- Siap bekerja dengan rentang tanggal? KiPApp Helper sekarang sudah bisa menangani rentang tanggal!
Ayo, gunakan KiPApp Helper untuk input SKP anda yang memuat rentang tanggal itu 🥳
- Masih _kekeuh_ menggunakan Drive BPS untuk menyimpan bukti dukung, meskipun harus enable link satu-
persatu? Tenang. KiPApp Helper akan mengklik link-link tersebut untuk anda, cukup dengan 1 tombol!
## Riwayat Update

| Waktu                  | Lokasi Update | Rincian Update                                                                 |
|------------------------|---------------|--------------------------------------------------------------------------------|
| 29 Juli 2025 11:38 WITA | Git, GDrive   | Perbaikan fungsi entri SKP dengan format bebas                                 |
| 31 Juli 2025 10:20 WITA | Git           | Menyesuaikan beberapa log                                                       |
| 31 Juli 2025 14:30 WITA | Git, GDrive   | Penambahan fungsi atur delay di 8 titik                                         |
| 31 Juli 2025 14:49 WITA | Git           | Ubah sistem threading biar ga ngefreeze                                         |
| 31 Juli 2025 15:02 WITA | Git           | Kunci inisialisasi bila ada browser terbuka                                     |
| 1 Agustus 2025 14:00 WITA | Git         | Pembaruan log dan peningkatan UX, memotong loop bila terdapat error input       |
| 1 Agustus 2025 14:44 WITA | Git         | Sinkronisasi tabel SKP yang di-view dan dientri                                 |
| 6 Agustus 2025 11:40 WITA | Git, GDrive | Pembaruan tampilan dan tata letak                                               |
| 7 Agustus 2025 13:09 WITA | Git         | Optimisasi dark mode dan beberapa log                                           |
| 12 Agustus 2025      | Git         | Penambahan fitur import dari link spreadsheet langsung                          |
| 17 Agustus 2025      | Git, Drive  | Penambahan fitur import dari Excel Drive BPS Langsung                           |
| 20 Agustus 2025      | Github      | Mengubah tempat update menjadi di Github, menyederhanakan tampilan              |
| 29 Agustus 2025      | Github      | Memperbaiki auto close untuk pengguna yang login menggunakan OTP                |
| 3 September 2025     | Github      | Menambahkan fitur baru: Handling file di Drive BPS                |
| 15 September 2025     | Github      | Menambahkan fitur baru: Handling Rentang Tanggal                |

---

## Tentang KiPApp Helper

jadi, ini berawal dari emosiku kudu entri SKP tiap akhir bulan ke KiPApp. ya gimana engga,
entrian puluhan harus dientri satu-satu, mana isiannya ada 4 string, 1 tanggal dan
1 kotak centang. lalu 2 di antara string tersebut isinya sama, cuma dibedakan header dan footer
aja. lalu butuh file bukti, di mana KiPApp mintanya cuma link buktinya aja. buktinya taroh di
mana? ya gatau, pokoknya saia (KiPApp) butuhnya cuma link bukti weeek 🤪

saya (dev) tau, bahwa bentuk kerja 3x ini (satu: mencatat kerjaan dan bukti di tempat lain,
kemudian dua: mengentrinya ke KiPApp, tiga: SATU-PERSATU) cukup menyebalkan
(setidaknya buat saya dan beberapa testimoni jujur dari rekan-rekan selindo)
lalu akan lebih rumit lagi kalo ga pake form yang generate link bukti dukungnya otomatis,
kek cuma nyimpen bukti di drive BPS misalkan. kamu harus _enable sharing_ gambarnya (kerjaan
keempat) dan lagi: ENABLE NYA SATU PERSATU!!! (ok ini kerjaan kelima, jadi kalo kamu pake
cara ini kuhitung jadi 5x kerja lah)

jadi saya memikirkan: bisa ga sih,entri ke KiPApp kubuat otomatis aja?

hah? otomatis?

seketika ada lampu menyala di atas kepala saya. ting 💡

lalu jadilah **KiPApp Helper** ini, atas seizin Allah. 

yaa ngga serta merta jadi dong. ngoding dulu, trial error beberapa kali, sampai akhirnya
ditemukanlah kodingan yang solutif ini. alhamdulillah, dengan ini kita bisa mengeliminasi
kerjaan kedua dan ketiga tadi (atau yang kerja hingga 5x), menjadi setidaknya setengah 
kerjaan lah. jadi yea, kerjaan kita tinggal 1.5x dari yang seharusnya. 
mencatat tiap hari, login ke KiPApp, kemudian ngentri deh. uhuy.

Sekian yapping saya, sekarang masuk ke bagian seriusnya.
Anda bisa membuka https://s.bps.go.id/kipapp-helper-panduan-beta untuk mulai menggunakan KiPApp Helper
dengan panduan lengkap, step by step. Pertanyaan bisa diajukan di QnA yang link nya saya sertakan di sana, ya.

---

### Penjelasan Fitur

#### Jendela Utama
1. Checkbox `Advanced Mode`: Menampilkan menu advanced yang tidak tercakup dalam fungsi utama entri SKP.
2. Checkbox `Tampilkan Log`: Menampilkan/Menyembunyikan Log Aktivitas di bawah.
3. Lampu: kiri, akan menyala kuning bila aplikasi sibuk, dan abu-abu bila idle. kanan, akan menyala hijau bila
sebuah fungsi berhasil dijalankan, merah bila gagal dijalankan, dan abu-abu bila sibuk.
4. Tombol `Opsi`: Untuk memunculkan Pop Up Opsi mengatur beberapa behavior aplikasi.
5. Isian `Username SSO BPS`: Kolom isian username SSO.
6. Isian `Password SSO BPS`: Kolom isian password SSO.
7. Isian `Bulan`: Kolom isian bulan (otomatis, mengambil dari bulan sekarang di PC pengguna).
8. Dropdown `Excel Lokal`/`Gsheet`: Pemilihan mode import SKP. Bila file lokal maka tombol di sebelah
kanan isian akan bertuliskan `Browse` untuk mencari file SKP di file explorer PC pengguna, dan kolom isian akan terisi
direktori file nya setelah pengguna memilih file. Bila dropdown link dipilih, maka pengguna bisa drop link spreadsheet
nya langsung ke isian, dan tombol di sebelah kanan akan berubah tulisan menjadi `Import`.
9. Tombol `Browse`/`Import`: Untuk mencari file di lokal/import dari spreadsheet setelah drop link nya di isian.
10. Checkbox `Cleaning`: Untuk cleaning file sesuai format KiPApp Helper. Uncheck bila tidak menggunakan format tersebut.
11. Checkbox `Filter Bulan`: Untuk memfilter baris SKP sesuai bulan yang tertulis di isian. 
12. Tombol `Isi Otomatis SSO`: Untuk mengisi SSO otomatis dari credential.txt yang sudah disiapkan pengguna.
13. Tombol `Lihat Tabel`: Untuk memunculkan Pop Up tampilan tabel data SKP.
14. Tab `Main Control`: Memuat 3 tombol fitur utama entri SKP.

_to be continued_

---

## QnA

Anda bisa mengakses https://s.bps.go.id/kipapp-helper-qna untuk mengakses QnA

---

**PERINGATAN!**  
Segala bentuk pelanggaran lisensi akan ditindak **SECARA HUKUM**.  
Silakan sebarkan **hanya dengan cara menyertakan link repositori ini**.

## 📄 Lisensi (Bahasa Indonesia)

Hak Cipta © 2025 Gilang Wahyu Prasetyo, BPS Kabupaten Tabalong.  
Dilarang mengubah, memodifikasi, mendistribusikan ulang, atau membuat karya turunan tanpa izin tertulis dari pemilik hak cipta.

---

## 📄 License (English)

Copyright © 2025 Gilang Wahyu Prasetyo, BPS Tabalong Regency.  
No modification, redistribution, or derivative works allowed without written permission.

---

