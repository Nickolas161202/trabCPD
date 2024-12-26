
import tkinter as tk
from pages.advanced import AdvancedScreen
from utils.navigationFunctions import switchPage
from pages.mainpage import mainPage
class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

def backToMain(a, b):
    print(a.winfo_children())
    for frames in a.winfo_children():
        frames.destroy()
    b(a)

def main():
    root = tk.Tk()
    root.minsize(1000, 700)
    btn =  tk.Button(root, command= lambda: backToMain(main_frame, mainPage), text="voltar a página inicial")
    btn.pack()
    main_frame = tk.Frame(root)
    mainPage(main_frame)
    main_frame.pack()
    root.mainloop()


if __name__ == "__main__":
    main()