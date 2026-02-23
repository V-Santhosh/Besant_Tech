# Besant Technologies – Student Enquiry Form (Tkinter)

This is a simple desktop application built using Python Tkinter to capture student enquiry details at Besant Technologies.

Normally, enquiry details are written down manually and later entered into Excel or some internal system. The idea behind this project was to avoid doing the same data entry multiple times.

Using this form, staff can enter the student details once — and the data will automatically be stored in:

- a .txt file  
- an Excel sheet  
- a MySQL database  

So basically, one-time entry → saved in all 3 places.

---

## What happens on submission?

When the user fills out the form and clicks submit:

- Data gets appended into a text file (user_details.txt)
- Same data is written into an Excel file (user_details.xlsx)
- It is also inserted into a MySQL table named Besant

If the Excel file or txt file does not already exist, the application will create it during the first entry itself.

Also, in case the database connection fails for some reason, the form will remain open so that the entered data is not lost.

---

## Project structure (rough idea)

```
besant_enquiry/
│
├── main.py          -> starts the application
├── config.py        -> DB credentials & shared constants
│
├── ui/
│   ├── window.py    -> form layout
│   └── buttons.py   -> submit / quit buttons
│
├── handlers/
│   └── form_handler.py -> collects form data
│
└── db/
    ├── txt_writer.py
    ├── excel_writer.py
    └── db_writer.py
```

main.py loads the UI → UI passes values to the handler → handler sends the data to txt / Excel / MySQL modules.

---

## Installation

Clone the repository:

```
git clone https://github.com/your-username/besant-enquiry-form.git
cd besant-enquiry-form
```

Install required libraries:

```
pip install openpyxl pymysql
```

Tkinter usually comes pre-installed with Python.

If you're on Linux and it's missing:

```
sudo apt install python3-tk
```

---

## MySQL Setup

Create a database and table using the following:

```sql
CREATE DATABASE tkinterdb;
USE tkinterdb;

CREATE TABLE Besant (
    id INT AUTO_INCREMENT PRIMARY KEY,
    DATE VARCHAR(50),
    NAME VARCHAR(100),
    MOB BIGINT,
    ALT_NO BIGINT,
    EMAIL VARCHAR(100),
    ADDR TEXT,
    COURSE VARCHAR(100),
    BATCH VARCHAR(50),
    REF_SRC VARCHAR(100),
    EXP_or_FSH VARCHAR(20),
    CONTACT VARCHAR(100),
    COUNSLER VARCHAR(100),
    FEES INT,
    CMT TEXT
);
```

---

## Update DB Credentials

Inside config.py, update your MySQL credentials:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "tkinterdb"
}
```

---

## Run the application

```
python main.py
```

---

## Form fields included

The form currently captures:

- Date  
- Name  
- Mobile Number  
- Alternate Number  
- Email  
- Address  
- Course Interested  
- Preferred Batch  
- Reference Source  
- Experience / Fresher  
- Contact Person  
- Counselor  
- Fees  
- Comments  

---

## Output

After submission, the data will be stored in:

- user_details.txt (plain text format)
- user_details.xlsx (Excel format)
- tkinterdb.Besant (MySQL table)

Both txt and Excel files are auto-created during the first submission if they are not already present.

---

## Tech Stack

- Python  
- Tkinter  
- openpyxl  
- pymysql  

---

This project was mainly built to reduce duplicate data entry and keep enquiry records stored in both file system and database at the same time.
