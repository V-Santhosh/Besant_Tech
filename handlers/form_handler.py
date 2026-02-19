from tkinter import messagebox
from config import LABELS
from db.excel_writer import write_to_excel
from db.txt_writer   import write_to_txt
from db.db_writer    import insert_into_db

def get_details_to_txt(entries, exp_var, window):
    row_data = []
    for i, e in enumerate(entries):
        value = exp_var.get() if i == 9 else e.get()
        print(LABELS[i], value)
        row_data.append(value)

    write_to_txt(LABELS, row_data)
    write_to_excel(LABELS, row_data)

    try:
        insert_into_db(row_data)
    except Exception as exc:
        messagebox.showerror("DB Error", f"Database insert failed:\n{exc}")
        return

    messagebox.showinfo("Success", "Successfully Submitted")
    window.destroy()