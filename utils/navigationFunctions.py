import tkinter as tk
def switchPage(actualFrame, nextFrame, parent): 
    actualFrame.destroy()
    nextFrame(parent)

def goToDetailedPage(actualFrame, nextFrame, parent, data): 
    actualFrame.destroy()
    nextFrame(parent, data)
