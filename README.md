## Panduan Instalasi Odoo 16 di Windows

1. **Instal Python 3.8.10**
   - Install Python 3.8.10 dari Microsoft Store.
   - Buka Command Prompt (CMD) dan ketikkan perintah berikut untuk memastikan Python telah terdaftar pada sistem:
     ```
     python --version
     ```

2. **Instal PostgreSQL versi 15**
   - Download dan install PostgreSQL versi 15.
   - Saat instalasi, pilih password yang mudah diingat.
   - Setelah PostgreSQL terinstal, tambahkan folder `bin` PostgreSQL ke Path Environment Variables windows.
   - Untuk memastikan PostgreSQL berhasil terinstal, ketikkan perintah berikut di CMD:
     ```
     postgres --version
     ```

3. **Konfigurasi PostgreSQL**
   - Buka Command Promt atau cmd.
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

5. **Install Git**
   - Download dan install Git dari [Git Downloads](https://git-scm.com/downloads).

6. **Clone Repository Odoo**
   - Buat folder baru bernama `Training`.
   - Buka Command Prompt didalam folder `Training`:
     ```
     cd Training
     ```
   - Clone repository Odoo dari GitHub dengan perintah:
     ```
     git clone --branch 16.0 --depth 1 https://github.com/odoo/odoo.git
     ```

7. **Setup Virtual Environment**
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

- odoo conf
```
[options]
addons_path = C:\Users\firwin\Documents\Training\training_module,C:\Users\firwin\Documents\Training\odoo\addons
admin_passwd = odoo
db_host = localhost
db_name = False
db_password =odoo_user
db_port = 5432
db_user =odoo_user 
dbfilter =
http_port = 8010
xmlrpc_port = 8010
list_db = True
log_db = False
log_db_level = warning
log_handler = :INFO
log_level = info
logfile = 
default_productivity_apps = True
```
---
