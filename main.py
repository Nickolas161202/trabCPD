
import tkinter as tk
from pages.advanced import AdvancedScreen
from utils.navigationFunctions import switchPage

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()



def main():
    root = App()
    w = tk.Label(root, text='Bem Vindo ao LoR Finder!')
    inp = tk.Entry(root)
    btn = tk.Button(root, text="Busca Avançada", command=lambda: switchPage(AdvancedScreen))
    root.master.minsize(1000, 700)
    w.pack()
    inp.pack()
    btn.pack()

    root.mainloop()


if __name__ == "__main__":
    main()