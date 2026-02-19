from ui.window  import build_window
from ui.buttons import build_buttons

def main():
    window, entries, exp_var = build_window()
    build_buttons(window, entries, exp_var)
    window.mainloop()

if __name__ == "__main__":
    main()

    