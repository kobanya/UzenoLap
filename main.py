import tkinter as tk
from tkinter import ttk

def elkuld():
    nev = nev_entry.get()
    email = email_entry.get()
    print("Név:", nev)
    print("Email:", email)
    print("Hol hallottál rólunk?", forras_combobox.get())
    print("Visszalátogatsz a kozlekedes.org oldalra?", ujra_var.get())
    print("Véleményed az oldalról:", velemeny_text.get("1.0", tk.END))
    print("Feliratkozol a hírlevélre?", feliratkozas_var.get())

# Létrehozzuk a fő ablakot
gyoker = tk.Tk()
gyoker.title("Véleményező adatlap")

# kozlekedes.org címke
cimke = tk.Label(gyoker, text="kozlekedes.org")
cimke.pack()

# Személyes adataid keret
szemelyes_frame = tk.LabelFrame(gyoker, text="Személyes adataid")
szemelyes_frame.pack(padx=10, pady=10)

# Név mező
nev_cimke = tk.Label(szemelyes_frame, text="Neved:")
nev_cimke.grid(row=0, column=0, sticky=tk.W)
nev_entry = tk.Entry(szemelyes_frame)
nev_entry.grid(row=0, column=1)

# Email mező
email_cimke = tk.Label(szemelyes_frame, text="Email:")
email_cimke.grid(row=1, column=0, sticky=tk.W)
email_entry = tk.Entry(szemelyes_frame)
email_entry.grid(row=1, column=1)

# Véleményed keret
velemeny_frame = tk.LabelFrame(gyoker, text="Véleményed")
velemeny_frame.pack(padx=10, pady=10)

# Hol hallottál rólunk?
forras_cimke = tk.Label(velemeny_frame, text="Hol hallottál rólunk?")
forras_cimke.grid(row=0, column=0, sticky=tk.W)
forrasok = ["Google", "Barátok", "Facebook", "Reklám"]
forras_combobox = ttk.Combobox(velemeny_frame, values=forrasok)
forras_combobox.current(0)
forras_combobox.grid(row=0, column=1, sticky=tk.W)

# Visszalátogatsz a kozlekedes.org oldalra?
ujra_cimke = tk.Label(velemeny_frame, text="Visszalátogatsz a kozlekedes.org oldalra?")
ujra_cimke.grid(row=1, column=0, sticky=tk.W)
ujra_var = tk.StringVar()

ujra_radio_frame = tk.Frame(velemeny_frame)
ujra_radio_frame.grid(row=1, column=1, sticky=tk.W)

ujra_radio_1 = tk.Radiobutton(ujra_radio_frame, text="Igen", variable=ujra_var, value="Igen")
ujra_radio_1.pack(side=tk.LEFT)

ujra_radio_2 = tk.Radiobutton(ujra_radio_frame, text="Nem", variable=ujra_var, value="Nem")
ujra_radio_2.pack(side=tk.LEFT)

ujra_radio_3 = tk.Radiobutton(ujra_radio_frame, text="Lehet", variable=ujra_var, value="Lehet")
ujra_radio_3.pack(side=tk.LEFT)

# Elválasztó vonal
elvalaszto = ttk.Separator(velemeny_frame, orient=tk.HORIZONTAL)
elvalaszto.grid(row=2, column=0, columnspan=2, sticky="ew", pady=10)

# Véleményed az oldalról:
velemeny_cimke = tk.Label(velemeny_frame, text="Véleményed az oldalról:")
velemeny_cimke.grid(row=4, column=0, sticky=tk.W)
velemeny_text = tk.Text(velemeny_frame, height=6)
velemeny_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)

# Feliratkozol a hírlevélre?
feliratkozas_var = tk.IntVar()
feliratkozas_checkbox = tk.Checkbutton(velemeny_frame, text="Feliratkozol a hírlevélre", variable=feliratkozas_var)
feliratkozas_checkbox.grid(row=7, column=0, columnspan=2, sticky=tk.W)

# Küldés gomb
kuld_button = tk.Button(gyoker, text="Küldés", command=elkuld)
kuld_button.pack(pady=10)

# Fő ablak indítása
gyoker.mainloop()
