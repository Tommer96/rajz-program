import tkinter as tk
from tkinter import messagebox
import random

def dobas(dobasok):
    eredmenyek = [0 for _ in range(7)]
    for _ in range(dobasok):
        szam = random.randint(1, 6)
        eredmenyek[szam] += 1
    eredmeny_cimke_szoveg.set(
        f"1 -- {eredmenyek[1]}\n"
        f"2 -- {eredmenyek[2]}\n"
        f"3 -- {eredmenyek[3]}\n"
        f"4 -- {eredmenyek[4]}\n"
        f"5 -- {eredmenyek[5]}\n"
        f"6 -- {eredmenyek[6]}"
    )

def on_dobas():
    try:
        dobasok_szama = int(dobasok_szama_bemenet.get())
        dobas(dobasok_szama)
    except:
        messagebox.showerror("Hiba", "Rossz értéket adott meg a bodásszámra")


root = tk.Tk()
root.title("Kockadobás statisztika")
root.geometry("600x400")

cim_cimke = tk.Label(root, text="Kockadobások", font=("Arial", 16))
cim_cimke.grid(row=0, column=1, pady=20)

dobasok_szama_bemenet = tk.StringVar(value="10")
dobasszam = tk.Entry(root, textvariable=dobasok_szama_bemenet, width=10)
dobasszam.grid(row=1, column=0, pady=20, padx=50)

eredmeny_cimke_szoveg = tk.StringVar(value="...\n...\n...")
eredmeny_cimke = tk.Label(root, textvariable=eredmeny_cimke_szoveg, font=("Arial", 16))
eredmeny_cimke.grid(row=2, column=1, pady=20)

gomb = tk.Button(root, text="Dobás", command= on_dobas)
gomb.grid(row=1, column=2)

kilepes = tk.Button(root, text="Kilepes", command=root.destroy, bg="red", fg="red")
kilepes.grid(row=1, column=3, padx=50)

tk.mainloop()