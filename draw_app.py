import tkinter as tk
from datetime import datetime

class OtDrawApp:
    def __init__(self, root):
        self.root = root
        self.szinek = ["red", "blue", "green", "black"]
        self.index = 0
        self.radir_mod = False
        self.last_x = None
        self.last_y = None

        self.felsosor = tk.Frame(self.root)
        self.felsosor.pack(fill=tk.X)

        self.ora_label = tk.Label(self.felsosor, text="")
        self.ora_label.pack(side=tk.LEFT, padx=10, pady=5)

        self.szin_gomb = tk.Button(self.felsosor, text="Szín váltás", command=self.ot_valt_szin)
        self.szin_gomb.pack(side=tk.LEFT, padx=10)

        self.torol_gomb = tk.Button(self.felsosor, text="Törlés", command=self.ot_torol)
        self.torol_gomb.pack(side=tk.LEFT, padx=10)

        self.radir_gomb = tk.Button(self.felsosor, text="Radír: ON", command=self.ot_radir_mod)
        self.radir_gomb.pack(side=tk.LEFT, padx=10)

        self.vaszon = tk.Canvas(self.root, width=600, height=400, bg="white")
        self.vaszon.pack(padx=10, pady=10)

        self.vaszon.bind("<Button-1>", self.ot_kor)
        self.vaszon.bind("<Button-1>", self.ot_kezdo_pont, add="+")
        self.vaszon.bind("<B1-Motion>", self.ot_huz)

        self.ot_frissit_ido()

    def ot_aktualis_szin(self):
        return self.szinek[self.index]

    def ot_valt_szin(self):
        self.index = (self.index + 1) % len(self.szinek)

    def ot_torol(self):
        self.vaszon.delete("all")

    def ot_kor(self, event):
        if self.radir_mod:
            r = 10
            szin = "white"
        else:
            r = 3
            szin = self.ot_aktualis_szin()
        x = event.x
        y = event.y
        self.vaszon.create_oval(x - r, y - r, x + r, y + r, fill=szin, outline="")

    def ot_kezdo_pont(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def ot_huz(self, event):
        if self.last_x is not None and self.last_y is not None:
            if self.radir_mod:
                szin = "white"
                vastagsag = 20
            else:
                szin = self.ot_aktualis_szin()
                vastagsag = 6
            self.vaszon.create_line(self.last_x, self.last_y, event.x, event.y, fill=szin, width=vastagsag)
        self.last_x = event.x
        self.last_y = event.y

    def ot_radir_mod(self):
        self.radir_mod = not self.radir_mod
        if self.radir_mod:
            self.radir_gomb.config(text="Radír: OFF")
        else:
            self.radir_gomb.config(text="Radír: ON")

    def ot_frissit_ido(self):
        ido = datetime.now().strftime("%H:%M:%S")
        self.ora_label.config(text=ido)
        self.root.after(1000, self.ot_frissit_ido)
