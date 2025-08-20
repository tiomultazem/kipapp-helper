# KiPApp Helper

**🚨 PERINGATAN!**  
Segala bentuk pelanggaran lisensi akan ditindak **SECARA HUKUM**.  
Silakan gunakan untuk kepentingan pribadi dan sebarkan **dengan menyertakan link repositori ini**.

> **DILARANG KERAS MENYEBARKAN FILE APLIKASI SECARA LANGSUNG TANPA IZIN.**

---

## 💡 Tentang KiPApp Helper

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

Oiya, penjelasannya dibedakan untuk versi 2 dan versi 3 ya. Anda bebas menggunakan yang
mana saja, tapi jelas v3 jauh lebih lengkap (pretty sure Anda akan memilih V3. 99,99% wkwk).
Currently, v2 kutaroh di link https://git.bps.go.id/gilangprasetyo/kipapp-helper.git.

Sekian yapping saya, sekarang masuk ke bagian seriusnya.
Anda bisa membuka https://s.bps.go.id/kipapp-helper-panduan-beta untuk mulai menggunakan v3 dengan
panduan lengkap, step by step. Pertanyaan bisa diajukan di QnA yang saya sertakan di sana, ya.

---

## ⚙️ Versi 2 (V2)

### 🧩 Fitur Utama
- Tanpa GUI
- Via JupyterLab
- Dua fungsi utama: `navigasi()` dan `entri()`

### 📦 Persiapan
1. Google Form dengan kolom:
    - `RK SKP atau keywordnya`
    - `tanggal`
    - `pre-kegiatan`
    - `kegiatan`
    - `jumlah capaian`
    - `jenis capaian`
    - `Upload bukti dukung`
2. Browser **Google Chrome**
3. **JupyterLab**

> ❗ Format kolom harus **persis sama** dan **case-sensitive**

### 🧭 Langkah Penggunaan
1. Entri kegiatan tiap hari ke GForm.
2. Akhir bulan: download Excel dari GForm.
3. Jalankan bagian 1 (install/import package)
4. Jalankan bagian 2.1 dan isi:
    - Username & password SSO
    - Bulan yang mau dikerjakan
    - Lokasi Excel
5. Jalankan bagian 2.2 – 2.4
6. Jalankan bagian 3 untuk login
7. Jalankan `navigasi()`
8. Jalankan `entri()`
9. Hapus RK kosong dan submit
10. Jalankan bagian 5 untuk tutup browser

---

## 🖥️ Versi 3 (V3) — GUI + CMD

### 🌟 Fitur Tambahan
- GUI via `cmd`
- Navigasi, entri, delete SKP, filter bulan, cleaning, auto login SSO, dll.
- Format Excel **bebas** (asalkan urutannya benar)
- Tanpa instalasi manual — cukup klik `runner.bat`

### 📦 Persiapan
1. Excel SKP (dengan format V2 **atau** 5 kolom: `rk skp`, `tanggal`, `kegiatan`, `capaian`, `link`)
2. Chrome browser
3. `credential.txt` berisi:
    - Baris 1: username
    - Baris 2: password
4. Semua file dalam satu folder

### 🧭 Langkah Penggunaan
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

> ☕ Sambil jalanin, siapin kopi juga boleh.

---

## 🤔 FAQ

### FAQ

**Q: Apa itu file .pyc?**  
A: Hasil kompilasi script Python ke bytecode agar bisa
dijalankan lebih cepat oleh interpreter Python. Cara
running nya sama, `python build/gui.pyc` atau `python main.py`

**Q: Apa bisa hapus RK kosong?**  
A: Saat ini belum. Tunggu update terbaru ya.

**Q: Gimana cara stop aplikasi?**  
A: Tekan hentikan proses secara beruntun.

**Q: Aku habis hapus python lokal. Kenapa ga bisa reinstall pake runner?**  
A: Install manual pake python installer yang muncul di foldermu, lalu
jalankan ulang runner.

**Q: Gimana kalo Python udah ada tapi ga terdeteksi di cmd?**  
A: Bila eror di cmd seperti ini,

>'python' is not recognized as an internal or external command operable program or batch file

cari file `python.exe` mu, salin path nya dan tambahkan ke
Environment Variable -> System Variable -> Path

lalu restart cmd mu.

**Q: Gimana cara stop aplikasi?**  
A: Tekan hentikan proses secara beruntun.

---

## 📄 Lisensi (Bahasa Indonesia)

Hak Cipta © 2025 Gilang Wahyu Prasetyo, BPS Kabupaten Tabalong.  
Dilarang mengubah, memodifikasi, mendistribusikan ulang, atau membuat karya turunan tanpa izin tertulis dari pemilik hak cipta.

---

## 📄 License (English)

Copyright © 2025 Gilang Wahyu Prasetyo, BPS Tabalong Regency.  
No modification, redistribution, or derivative works allowed without written permission.

---

