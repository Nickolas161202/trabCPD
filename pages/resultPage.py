import tkinter as tk
from utils.resultCard import resultCard


def resultPage(parent):
    resultFrame = tk.Frame(master=parent)
    resultCard(parent)




    resultFrame.pack()