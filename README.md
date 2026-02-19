# Besant_Tech
Xampp



## How They Connect (import flow)
```
main.py
  └── ui/window.py      (builds the form, returns window/entries/exp_var)
  └── ui/buttons.py     (attaches buttons, imports form_handler)
        └── handlers/form_handler.py  (orchestrates saving, imports all 3 writers)
              ├── db/txt_writer.py    (imports config)
              ├── db/excel_writer.py  (imports config)
              └── db/db_writer.py     (imports config)
                    └── config.py     (shared constants, no imports)
