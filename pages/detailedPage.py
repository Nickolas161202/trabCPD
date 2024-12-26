import tkinter as tk


def detailedCard(parent):
    detailedFrame = tk.Frame(master=parent)
    nameLabel = tk.Label(detailedFrame, text="nome")


    nameLabel.pack()
    detailedFrame.pack()