import pymysql
from config import DB_CONFIG

def insert_into_db(row_data):
    conn = pymysql.connect(**DB_CONFIG)
    try:
        cursor = conn.cursor()
        sql = """INSERT INTO Besant
                    (DATE, NAME, MOB, ALT_NO, EMAIL, ADDR, COURSE,
                     BATCH, REF_SRC, EXP_or_FSH, CONTACT, COUNSLER, FEES, CMT)
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = list(row_data)
        for idx in (2, 3):
            try:    values[idx] = int(values[idx])
            except: values[idx] = 0
        try:    values[12] = int(values[12])
        except: values[12] = 0

        cursor.execute(sql, values)
        conn.commit()
    finally:
        conn.close()