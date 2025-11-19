import tkinter as tk
from draw_app import OtDrawApp

def main():
    root = tk.Tk()
    root.title("Rajz Program")
    app = OtDrawApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
