import tkinter as tk
def switchPage(actualFrame, nextFrame, parent): 
    actualFrame.destroy()
    nextFrame(parent)
