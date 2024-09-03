# PT-Subang-Autocomp-Training

## How to Install and Setup Odoo from Scratch (Local and Linux Env)

1. First of All, make sure that Python installed on your system. Check the version with command :

```bash
# Check Python Version
python3 --version
```

2. Next, you need to Install Postgresql and create Odoo User in Postgresql with the command :

```bash
# Install the Postgres
sudo apt install postgresql

# Create Odoo User in Postgresql
sudo -u postgres psql
CREATE USER odoo_user WITH CREATEDB CREATEROLE LOGIN PASSWORD 'odoo_user';
```

3. Next, Install wkthmltopdf on Your System with command :

```bash
# Install wkhtmltopdf
sudo apt install wkhtmltopdf

# Check the Version
wkhtmltopdf --version
```

4. Next, Install Odoo on Your System and make sure that you installed Git first with Command :

```bash
# Install Git
sudo apt-get install git

# Create Odoo Folder that has 3 Folder inside it
mkdir Odoo16
cd Odoo16
mkdir Conf
mkdir Project
mkdir -p Project/custom-addons
git clone https://www.github.com/odoo/odoo -b 16.0

```

5. Next, create Virtual Env inside Folder Odoo16 with command :

```bash
# Create Python Virtual End
python3 -m venv odoo16-env

```

6. Now, you have 4 Folder inside Folder Odoo16 : 
- Conf, 
- Project, 
- odoo, 
- odoo16-env

7. Next, you can activate the Virtual Env with command (Assume that your active Directory is Odoo16) :

```bash
# Activate Python Virtual Env
source odoo16-env/bin/activate

# Example Result:
(odoo16-env) root@ubuntu:~$

```

8. Now, you can Install the Library Requirements for Odoo with Command (Assume that your active Directory is Odoo16) :

```bash
# Install Wheel
python3 -m pip install wheel

# Install Odoo Requirements
python3 -m pip install -r odoo/requirements.txt

```

9. Next, you can create an Odoo Config File inside Folder Conf with Detail like this :

```bash
[options]
addons_path = Path for Odoo Addons and Customization, like /home/user/odoo16/odoo/addons, /home/user/odoo16/Project/custom-addons
admin_passwd = odoo
db_host = localhost
db_name = False
db_password = odoo_user # Password that we make in Postgresql (Ref. Number 2)
db_port = 5432
db_user = odoo_user # User that we make in Postgresql (Ref. Number 2)
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

10. After that, you can try to running Odoo with Command (Assume that Virtual Env is active and your current Directory in Odoo16) :

```bash
# Running Odoo from Terminal / Command
python odoo/odoo-bin -c Conf/your_config_filename.conf --dev xml
```

11. Then, Open your browser and go to : localhost:8010 . If the anything is going fine, you will be direct to Your Odoo Web

## How to Setup Launch JSON on VS Code for Odoo Env

1. Open your VS Code

2. Next, click Run and Debug Icon (4 Position from Top) on Left Side Menu

3. Next, click Create Launch JSON File

4. Next, you can create Launch JSON File with Detail like this :

```bash
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Arkana Training",
            "type": "python",
            "request": "launch",
            "stopOnEntry": false,
            "console": "integratedTerminal",
            "python": "/home/user/odoo16/odoo16-env/bin/python",
            "program": "/home/user/odoo16/odoo/odoo-bin",
            "args": [
                "--config=/home/user/odoo16/Conf/your_config_filename.conf",
                "--dev=xml",
                # "--database=odoo16_arkana_training",
            ]
        },
    ]
}

```

5. Next, Save the File and try to Run with Click Start (>) Button on Run and Debug

6. Then, Open your browser and go to : localhost:8010 . If the anything is going fine, you will be direct to Your Odoo Web

## Notes for Github Branch and Commit Policy

1. Remember to make Branch with Detail like this :
- [To Do]/Date_What_You_Do

```bash
# Create Feature
features/20240225_purchase_down_payment_feature

# Fixing Code / Flow
fix/20240225_fix_amount_on_invoice_prinout
patch/20240225_fix_amount_on_invoice_printout

# Improvement Code / Flow
imp/20240227_imp_register_payment_for_invoice

```

2. Remember to make Commit with Detail like this :
- [To Do] Message

```bash
# Add Feature
[ADD] Purchase Down Payment Feature

# Fix Code 
[FIX] Fix Amount in Invoice Prinout

# Imp Code
[IMP] Imp Register Payment for Invoice

# Del Code / Feature / Other
]DEL] Delete some File / Code / Flow in Folder

```
