# 📋 Besant Technologies — Enquiry Form

> A clean, modular **Python Tkinter** desktop application to capture student enquiry data and persist it across **TXT**, **Excel (.xlsx)**, and **MySQL** — all from one sleek GUI form.

---

## 🖼️ Overview

This app provides a simple desktop form for Besant Technologies staff to log student enquiry details. On submission, data is automatically saved to three destinations simultaneously — a flat text file, an Excel workbook, and a MySQL database.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🖥️ **GUI Form** | Built with Python's native `tkinter` — no browser needed |
| 📝 **TXT Export** | Appends each submission as a comma-separated row |
| 📊 **Excel Export** | Auto-creates & appends to `user_details.xlsx` via `openpyxl` |
| 🗄️ **MySQL Insert** | Persists to a `Besant` table via `pymysql` |
| 🔘 **Radio Buttons** | Experience / Fresher selection baked in |
| ⚠️ **Error Handling** | DB failures show a dialog — form stays open, data isn't lost |

---

## 🗂️ Project Structure

```
besant_enquiry/
│
├── main.py                   # 🚀 Entry point — run this file
│
├── config.py                 # ⚙️  Shared constants (labels, filenames, DB creds)
│
├── ui/
│   ├── __init__.py
│   ├── window.py             # 🪟 Builds the Tkinter window & form fields
│   └── buttons.py            # 🔘 Submit & Quit buttons
│
├── handlers/
│   ├── __init__.py
│   └── form_handler.py       # 🧠 Orchestrates data collection & saving
│
└── db/
    ├── __init__.py
    ├── txt_writer.py          # 📝 Writes to user_details.txt
    ├── excel_writer.py        # 📊 Writes to user_details.xlsx
    └── db_writer.py           # 🗄️  Inserts into MySQL
```

---

## 🔁 Module Connection Flow

```
main.py
  ├── ui/window.py        →  builds form, returns (window, entries, exp_var)
  └── ui/buttons.py       →  attaches buttons
        └── handlers/form_handler.py   →  collects & routes data
              ├── db/txt_writer.py     →  saves to .txt
              ├── db/excel_writer.py   →  saves to .xlsx
              └── db/db_writer.py      →  inserts into MySQL
                    └── config.py      →  DB credentials & constants
```

> 💡 Data flows **top-down**. Only `main.py` touches `ui/`. The `db/` layer is completely independent and reusable.

---

## 📦 Installation

### 1. Clone the repo
```bash
git clone https://github.com/your-username/besant-enquiry-form.git
cd besant-enquiry-form
```

### 2. Install dependencies
```bash
pip install openpyxl pymysql
```

> `tkinter` comes pre-installed with standard Python. If missing: `sudo apt install python3-tk`

### 3. Set up MySQL
```sql
CREATE DATABASE tkinterdb;

USE tkinterdb;

CREATE TABLE Besant (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    DATE      VARCHAR(50),
    NAME      VARCHAR(100),
    MOB       BIGINT,
    ALT_NO    BIGINT,
    EMAIL     VARCHAR(100),
    ADDR      TEXT,
    COURSE    VARCHAR(100),
    BATCH     VARCHAR(50),
    REF_SRC   VARCHAR(100),
    EXP_or_FSH VARCHAR(20),
    CONTACT   VARCHAR(100),
    COUNSLER  VARCHAR(100),
    FEES      INT,
    CMT       TEXT
);
```

### 4. Configure credentials
Edit `config.py`:
```python
DB_CONFIG = {
    "host":     "localhost",
    "user":     "root",
    "password": "your_password",   # 👈 update this
    "database": "tkinterdb"
}
```

### 5. Run the app
```bash
python main.py
```

---

## 🖥️ Form Fields

| # | Field | Type |
|---|---|---|
| 1 | Date | Text Entry |
| 2 | Name | Text Entry |
| 3 | Mobile No | Text Entry |
| 4 | Alternate No | Text Entry |
| 5 | Email Id | Text Entry |
| 6 | Address | Text Entry |
| 7 | Course Interested | Text Entry |
| 8 | Batch Preferred | Text Entry |
| 9 | How You Came To Know Us | Text Entry |
| 10 | Experience or Fresher | 🔘 Radio Button |
| 11 | Contact Person from Besant | Text Entry |
| 12 | Counselor | Text Entry |
| 13 | Fees | Text Entry |
| 14 | Comment | Text Entry |

---

## 📤 Output Files

| File | Location | Format |
|---|---|---|
| `user_details.txt` | Project root | CSV-style plain text |
| `user_details.xlsx` | Project root | Excel workbook |
| MySQL table | `tkinterdb.Besant` | Relational DB rows |

> 📌 Both `txt` and `xlsx` files are auto-created on first submission if they don't exist.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **tkinter** — GUI framework
- **openpyxl** — Excel read/write
- **pymysql** — MySQL connector

---

---

## 🤝 Contributing

Pull requests are welcome!

---



---

<div align="center">
  Made with ❤️ for Besant Technologies
</div>
