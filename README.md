# KiPApp Helper

**PERINGATAN!**  
Segala bentuk pelanggaran lisensi akan ditindak **SECARA HUKUM**.  
Silakan gunakan untuk kepentingan pribadi dan sebarkan **dengan menyertakan link repositori ini**.

> **DILARANG KERAS MENYEBARKAN FILE APLIKASI SECARA LANGSUNG TANPA IZIN.**

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
Anda bisa membuka https://s.bps.go.id/kipapp-helper-panduan-beta untuk mulai menggunakan v3 dengan
panduan lengkap, step by step. Pertanyaan bisa diajukan di QnA yang saya sertakan di sana, ya.

---

### Persiapan
1. Excel SKP (dengan format V2 **atau** 5 kolom: `rk skp`, `tanggal`, `kegiatan`, `capaian`, `link`)
2. Chrome browser
3. `credential.txt` berisi:
    - Baris 1: username
    - Baris 2: password
4. Semua file dalam satu folder

### Langkah Penggunaan
1. Entri kegiatan ke GForm/Excel tiap hari
2. Akhir bulan: siapkan Excel
3. Bila belum ada Python/Anaconda/Miniconda terinstal, jalankan `runner.bat`.
Python akan otomatis terinstal di direktori tersebut dan langsung membuka
KiPApp Helper. Bila sudah menginstal, maka jalankan `main.py` melalui bash.
4. Klik **Isi Otomatis SSO**, pilih Excel, uncheck "Aktifkan Cleaning" bila pakai format bebas
5. Klik **Inisialisasi**, masukkan OTP dan tutup popup
6. Klik **Ke halaman pelaksanaan**
7. Klik **Mulai entri SKP**
8. Hapus RK kosong dan **submit**
9. Klik **Tutup aplikasi**

---

## QnA

Anda bisa mengakses https://s.bps.go.id/kipapp-helper-qna untuk mengakses QnA

---

## 📄 Lisensi (Bahasa Indonesia)

Hak Cipta © 2025 Gilang Wahyu Prasetyo, BPS Kabupaten Tabalong.  
Dilarang mengubah, memodifikasi, mendistribusikan ulang, atau membuat karya turunan tanpa izin tertulis dari pemilik hak cipta.

---

## 📄 License (English)

Copyright © 2025 Gilang Wahyu Prasetyo, BPS Tabalong Regency.  
No modification, redistribution, or derivative works allowed without written permission.

---

