from tkinter import *
from handlers.form_handler import get_details_to_txt

def build_buttons(window, entries, exp_var):
    Button(window, text="Submit", bg="gray", fg="white", width=10,
           command=lambda: get_details_to_txt(entries, exp_var, window))\
        .grid(row=16, column=1, sticky="w", pady=10)

    Button(window, text="Quit", bg="red", fg="white", width=10,
           command=window.quit)\
        .grid(row=16, column=1, sticky="e", pady=10)