## Panduan Instalasi Odoo 16 di Windows

1. **Instal Python 3.8.10**
   - Install Python 3.8.10 dari Microsoft Store.
   - Buka Command Prompt (CMD) dan ketikkan perintah berikut untuk memastikan Python telah terdaftar pada sistem:
     ```
     python --version
     ```

2. **Instal PostgreSQL versi 16**
   - Download dan install PostgreSQL versi 15.
   - Saat instalasi, pilih password yang mudah diingat.
   - Setelah PostgreSQL terinstal, tambahkan folder `bin` PostgreSQL ke Environment Variables.
   - Untuk memastikan PostgreSQL berhasil terinstal, ketikkan perintah berikut di CMD:
     ```
     postgres --version
     ```

3. **Konfigurasi PostgreSQL**
   - Masuk ke PostgreSQL dengan perintah:
     ```
     psql -U postgres
     ```
   - Masukkan password PostgreSQL yang telah Anda setup selama instalasi.
   - Setelah berhasil masuk, buat user baru dengan perintah berikut:
     ```
     CREATE USER odoo_user WITH PASSWORD 'odoo_user' CREATEDB CREATEROLE LOGIN;
     ```
   - Untuk memastikan user telah dibuat dengan role yang benar, ketikkan perintah:
     ```
     \du
     ```

4. **Install Git**
   - Download dan install Git dari [Git Downloads](https://git-scm.com/downloads).

5. **Clone Repository Odoo**
   - Buat folder baru bernama `Training`.
   - Buka CMD dan navigasikan ke folder `Training`:
     ```
     cd Training
     ```
   - Clone repository Odoo dari GitHub dengan perintah:
     ```
     git clone --branch 16.0 --depth 1 https://github.com/odoo/odoo.git
     ```

6. **Setup Virtual Environment**
   - Buat virtual environment dengan Python:
     ```
     python -m venv env-odoo16
     ```
   - Aktifkan virtual environment:
     ```
     env-odoo16\Scripts\activate
     ```
   - Masuk ke folder `odoo`:
     ```
     cd odoo
     ```
   - Install dependencies `setuptools` dan `wheel`:
     ```
     pip install setuptools wheel
     ```
   - Install dependencies dari `requirements.txt`:
     ```
     pip install -r requirements.txt
     ```

---
