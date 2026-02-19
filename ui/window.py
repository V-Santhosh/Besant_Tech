from tkinter import *
from config import LABELS

def build_window():
    window = Tk()
    window.title("Besant Technologies Enquiry Form")
    window.geometry("700x520")

    Label(window, text="Besant Technologies Enquiry Form",
          fg="red", font=("Arial", 14, "bold"),
          relief="ridge", bd=3, padx=10, pady=5)\
        .grid(row=0, column=0, columnspan=2, pady=10)

    entries = []
    exp_var = StringVar(value="Fresher")

    for i, text in enumerate(LABELS):
        Label(window, text=text, anchor="w", width=35)\
            .grid(row=i+1, column=0, padx=10, pady=4)

        if i == 9:
            frame = Frame(window)
            frame.grid(row=i+1, column=1, padx=10, pady=4, sticky="w")
            Radiobutton(frame, text="Experience", variable=exp_var, value="Experience").pack(side=LEFT)
            Radiobutton(frame, text="Fresher",    variable=exp_var, value="Fresher").pack(side=LEFT)
            entries.append(None)
        else:
            e = Entry(window, width=45)
            e.grid(row=i+1, column=1, padx=10, pady=4)
            entries.append(e)

    return window, entries, exp_var