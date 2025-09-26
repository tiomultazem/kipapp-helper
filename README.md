# KiPApp Helper

---
## Pemberitahuan
Per 25 September 2025, aplikasi baru saja mendapatkan penyegaran fungsi penanganan eror. Harap **segera update** aplikasi anda.

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

Jadi, ini berawal dari keresahan pribadi entri SKP tiap akhir bulan ke KiPApp. Yang meresahkan adalah:
entrian puluhan baris SKP setiap bulannya harus dientri satu-satu, dengan formulir 4 string, 1 tanggal dan
1 kotak centang. Lalu, ada 2 string dengan sebagian isian yang identik. Lalu, formulir ini membutuhkan
link bukti dukung kinerja, di mana kita harus meletakkan file bukti dukung di cloud, menyalin link nya,
baru menempelkannya pada formulir KiPApp.

Menurut saya sebagai pengguna KiPApp, bentuk kerja redundan ini cukup merepotkan, setidaknya buat saya dan
beberapa testimoni jujur dari rekan-rekan sesatker dan selindo. Lalu, hal ini akan lebih rumit lagi bilamana
pengguna tidak memakai formulir yang bisa generate link bukti dukungnya otomatis seperti Gform. Pengguna
biasanya meng-upload bukti dukung di Drive BPS yang harus _enable sharing_ setiap file-nya satu-persatu. Bila
seperti ini, maka malah terjadi redundansi di pengisian SKP serta redudansi di pengumpulan link bukti dukung.
Repot pangkat dua.

Jadi saya memikirkan: "Bisa tidak ya, ~saya intervensi Direktorat SIS agar~ pengisian KiPApp menjadi otomatis?" 

...

Hah? Otomatis?

TING 💡 Seketika ada lampu menyala di atas kepala saya. 

Saya akan membuat sebuah alat bantu untuk melakukan hal tersebut.
_**Helping** BPS people enter SKP into KiPApp, so they still can keep their performance up!_

Dan jadilah **KiPApp Helper** ini, atas seizin Allah, mengambil nama dari fungsinya tadi. Membantu. Help. 

Tentu terciptanya KiPApp Helper ini tidak serta merta jadi. Saya harus melalui berbagai tahapan: merancang,
wawancara calon pengguna, menulis kode, _trial-error_ berkali-kali, _testing_, sampai akhirnya jadi.
Alhamdulillah, dengan ini kita bisa mengeliminasi pekerjaan redundan tadi hanya dengan klik beberapa tombol
di KiPApp Helper: login ke KiPApp, navigasi ke halaman pelaksanaan, isi SKP, selesai. Cepat, efisien.

Lalu, perlu diperhatikan juga bahwa ini hanyalah helper. Bukan pengganti KiPApp itu sendiri.
Anda tetap harus mengisi SKP setiap hari, dengan rapi, di spreadsheet/excel, sesuai format agar di akhir
bulan nanti bisa dientri oleh KiPApp Helper. Jadi, jangan malas mencatat SKP harian ya? hehe.  

Tertarik menjadikan entri SKP bulanan anda lebih cepat dan efisien juga?
Anda bisa membuka https://s.bps.go.id/kipapp-helper-panduan-beta untuk mulai menggunakan KiPApp Helper
dengan panduan lengkap, step by step.

Pertanyaan bisa diajukan di QnA yang link nya saya sertakan di sana, ya.

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

