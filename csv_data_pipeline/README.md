# CSV Automation and Oracle Database Loader

This project automates the following tasks:

1. **Cleaning** old `.csv` files from a target directory
2. **Copying** new `.csv` files from a source folder
3. **Renaming** the copied file to today's date
4. **Counting** rows in the final `.csv` file with a Windows popup
5. **Loading** CSV data into an Oracle database (via SQL*Loader and `cx_Oracle`)

---

## 📁 Project Structure

```
csv_data_pipeline/
├── All.py                       # Full automation pipeline
├── copy.py                      # Copy CSVs from source to destination
├── count.py                     # Count rows in a CSV file (Windows-only popup)
├── File.py                      # Check if CSV exists in a directory
├── database.py                  # Oracle DB connection and SELECT
├── sqlldr.py                    # Trigger SQL*Loader and archive file
│
├── scripts/
│   ├── csv_to_db_loader.py      # Loads CSV rows into DB via cx_Oracle
│   ├── connect_db_sample.py     # Demo for Oracle SELECT query
│   └── remove_csv.py            # Deletes old `.csv` files
│
├── data/
│   ├── dataset.csv
│   ├── dataset_new.csv
│   ├── Most-Recent-Cohorts-Scorecard-Elements.csv
│   └── streamline.xlsx
│
├── bat_scripts/
│   ├── copy.bat
│   └── count.bat
│
├── config/
│   └── control.ctl              # Control file for SQL*Loader
│
├── README.md
├── .gitignore
└── requirements.txt
```

---

## 🚀 How to Run

### ✅ Full automation (copy, rename, count):
```bash
python All.py
```

### ✅ Copy only:
```bash
python copy.py
```

### ✅ Count only:
```bash
python count.py
```

### ✅ Load CSV into Oracle DB (via cx_Oracle):
```bash
python scripts/csv_to_db_loader.py
```

### ✅ Trigger SQL*Loader:
```bash
python sqlldr.py
```

> 🔔 Make sure Oracle client and SQL*Loader are configured in your PATH.

---

## 🛠 Setup

1. Install requirements:
```bash
pip install cx_Oracle
```

2. Ensure Oracle DB connection string is properly configured inside `database.py`, `sqlldr.py`, and `csv_to_db_loader.py`.

---

## ⚠️ Notes

- **Windows Only**: GUI popups via `ctypes.windll` only work on Windows.
- **Environment Security**: It's recommended to store credentials in environment variables or a `.env` file.

---

## 📃 License

MIT License (or your preferred license)
