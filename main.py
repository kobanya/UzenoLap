import tkinter as tk
from tkinter import ttk
import csv

def elkuld():
    nev = nev_entry.get()
    email = email_entry.get()
    hallott = forras_combobox.get()
    visszalatogat = ujra_var.get()
    velemeny = velemeny_text.get("1.0", tk.END).strip()
    feliratkozas = feliratkozas_var.get()

    feliratkozas = "IGEN" if feliratkozas_var.get() == 1 else "NEM"
    adatok = [nev, email, hallott, visszalatogat, velemeny, feliratkozas]

    with open('kozlekedes.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(adatok)

    # Beviteli mezők törlése
    nev_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    velemeny_text.delete("1.0", tk.END)
    feliratkozas_checkbox.deselect()

    # Frissítsük a válaszok táblázatot
    frissit_vaszontablazat()

def frissit_vaszontablazat():
    # Töröljük a táblázat tartalmát
    for i in tablazat.get_children():
        tablazat.delete(i)

    # Beolvassuk a kozlekedes.csv adatokat és hozzáadjuk a táblázathoz
    with open('kozlekedes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            tablazat.insert("", "end", values=row)
# Létrehozzuk a fő ablakot
ablak = tk.Tk()
ablak.title("kozlekedes.org")

# kozlekedes.org címke
cimke = tk.Label(ablak, text="Mond el a véleményed bátran!", font=("Arial", 18), bg="yellow")
cimke.pack(fill='x')

# Személyes adataid keret
szemelyes_frame = tk.LabelFrame(ablak, text="Személyes adataid", fg="green")
szemelyes_frame.pack(padx=10, pady=10, anchor="w")

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
velemeny_frame = tk.LabelFrame(ablak, text="Véleményed", fg="green")
velemeny_frame.pack(padx=10, pady=10)

# Hol hallottál rólunk?
forras_cimke = tk.Label(velemeny_frame, text="Hol hallottál rólunk?")
forras_cimke.grid(row=0, column=0, sticky=tk.W)
forrasok = ["Google", "Barátok", "Facebook", "Reklám"]
forras_combobox = ttk.Combobox(velemeny_frame, values=forrasok)
forras_combobox.current(0)
forras_combobox.grid(row=0, column=1, sticky=tk.W)

# Elválasztó vonal
elvalaszto = ttk.Separator(velemeny_frame, orient=tk.HORIZONTAL)
elvalaszto.grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)

# Visszalátogatsz a kozlekedes.org oldalra?
ujra_cimke = tk.Label(velemeny_frame, text="Visszalátogatsz a kozlekedes.org oldalra?")
ujra_cimke.grid(row=2, column=0, sticky=tk.W)
ujra_var = tk.StringVar()

ujra_radio_frame = tk.Frame(velemeny_frame)
ujra_radio_frame.grid(row=3, column=0, sticky=tk.W)

ujra_radio_1 = tk.Radiobutton(ujra_radio_frame, text="Igen", variable=ujra_var, value="Igen")
ujra_radio_1.pack(side=tk.LEFT)

ujra_radio_2 = tk.Radiobutton(ujra_radio_frame, text="Nem", variable=ujra_var, value="Nem")
ujra_radio_2.pack(side=tk.LEFT)

ujra_radio_3 = tk.Radiobutton(ujra_radio_frame, text="Lehet", variable=ujra_var, value="Lehet")
ujra_radio_3.pack(side=tk.LEFT)

# Elválasztó vonal
elvalaszto = ttk.Separator(velemeny_frame, orient=tk.HORIZONTAL)
elvalaszto.grid(row=4, column=0, columnspan=2, sticky="ew", pady=10)

# Üres label
ures_label = tk.Label(velemeny_frame)
ures_label.grid(row=5, column=0)

# Véleményed az oldalról:
velemeny_cimke = tk.Label(velemeny_frame, text="Véleményed az oldalról:")
velemeny_cimke.grid(row=6, column=0, sticky=tk.W)
velemeny_text = tk.Text(velemeny_frame, height=6)
velemeny_text.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)

# Feliratkozol a hírlevélre?
feliratkozas_var = tk.IntVar()
feliratkozas_checkbox = tk.Checkbutton(velemeny_frame, text="Feliratkozom a hírlevélre", variable=feliratkozas_var)
feliratkozas_checkbox.grid(row=8, column=0, columnspan=2, sticky=tk.W)

# Küldés gomb
kuld_button = tk.Button(ablak, text="Küldés", command=elkuld)
kuld_button.pack(pady=10)
# kozlekedes.org címke
cimke2 = tk.Label(ablak, text="A beküldött válaszok", font=("Arial", 18), bg="yellow")
cimke2.pack(fill='x')
# Válaszok keret
valaszok_frame = tk.LabelFrame(ablak, text="Válaszok", fg="blue")
valaszok_frame.pack(padx=10, pady=10, anchor="w")

# Válaszok táblázat
tablazat = ttk.Treeview(valaszok_frame, columns=["Név", "Email", "Hallott", "Visszalátogat", "Vélemény", "Feliratkozás"], show="headings")
tablazat.heading("Név", text="Név")
tablazat.column("Név", width=200)
tablazat.heading("Email", text="Email")
tablazat.column("Email", width=310)
tablazat.heading("Hallott", text="Hol hallottál?")
tablazat.heading("Visszalátogat", text="Visszajösz?")
tablazat.heading("Vélemény", text="Vélemény")
tablazat.heading("Feliratkozás", text="Hírlrvél")
tablazat.grid(row=0, column=0, sticky="nsew")
style = ttk.Style()
style.configure("Treeview", rowheight=35)

valaszok_frame.grid_columnconfigure(0, weight=1)

# Fő ablak indítása
frissit_vaszontablazat()
ablak.mainloop()

