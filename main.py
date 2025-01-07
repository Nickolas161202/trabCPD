import tkinter as tk
from pages.advanced import AdvancedScreen
from utils.navigationFunctions import switchPage
from pages.mainpage import mainPage
from pages.filePage import filePage

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(sticky= "nsew")

def backToMain(a, b):
    print(a.winfo_children())
    for frames in a.winfo_children():
        frames.destroy()
    b(a)

def main():
    root = tk.Tk()
    root.minsize(1000, 700)
    root.configure(bg="#0000FF")  # Define the background color of the root window (optional)
    
    btn =  tk.Button(root, command= lambda: backToMain(main_frame, filePage), text="Voltar à página inicial")
    btn.grid(column=0, row=0)
    
    main_frame = tk.Frame(root ,bg="#0000FF")  # Red background for main_frame
    main_frame.rowconfigure(0, weight=1)
    main_frame.columnconfigure(0, weight=1)
    filePage(main_frame)
    main_frame.grid(row=1, column=2, sticky="nsew")  # Stretch main_frame to fill the root window
    
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    
    root.mainloop()

if __name__ == "__main__":
    main()
