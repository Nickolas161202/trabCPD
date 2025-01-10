import tkinter as tk
from utils.resultCard import resultCard
from Classes import *
from pages.detailedPage import detailedCard



def pagination(end, start, data, parent, grandParent, useImg):
    for frames in parent.winfo_children():
        frames.destroy()
    
    first = tk.Frame(parent)
    first.grid_rowconfigure(0, weight=1)
    first.grid_columnconfigure(0, weight=1)
    resultCard(first, data[start], useImg)
    first.grid(row=1, column=0, sticky="nw", padx=20)
    dtbtn = tk.Button(parent, text= "Detalhes", command= lambda: switchToDetail(grandParent, detailedCard, data[start]))
    dtbtn.grid(row=1, column=0, sticky="sw", padx=20 )
    try:
        second = tk.Frame(parent)
        resultCard(second, data[end],  useImg)
        second.grid(row=1, column=1, sticky="ne")
        dtbtn1 = tk.Button(parent, text= "Detalhes", command= lambda: switchToDetail(grandParent, detailedCard, data[end]))
        dtbtn1.grid(row=1, column=1, sticky="se")
    except Exception:
        pass

    if len(data) >2:
        prevEnd = end - 2
        prevStart = start - 2
        start = end+1 
        end =  end +2
    
        if prevStart < 0:
            nextbtn = tk.Button(parent, text="Próximo", command=lambda: pagination(end, start, data, parent, grandParent, useImg))
            nextbtn.grid(column=1, row=2)

        elif end <= len(data):

            nextbtn = tk.Button(parent, text="Próximo", command=lambda: pagination(end, start, data, parent, grandParent, useImg))
            nextbtn.grid(column=1, row=2)
            prevbtn = tk.Button(parent, text="Anterior", command=lambda: pagination(prevEnd, prevStart, data, parent, grandParent, useImg))
            prevbtn.grid(column=1, row=2, sticky="w")
        else:
            prevbtn = tk.Button(parent, text="Anterior", command=lambda: pagination(prevEnd, prevStart, data, parent, grandParent, useImg))
            prevbtn.grid(column=1, row=2, sticky="w")


    
    
def switchToDetail(parent, nextFrame, data):
    print(parent.winfo_children())
    for frames in parent.winfo_children():
        frames.destroy()
    nextFrame(parent, data)

def resultPage(parent, data:list):
    useImg = data[1].get()
    data = data[0].cartas
    print(data)

    resultFrame = tk.Frame(master=parent)
    resultFrame.grid(row=0, column=0, sticky="nsew")  
    resultFrame.columnconfigure((0,1,2), weight=1, uniform= 'a')
    resultFrame.rowconfigure(1,weight=2, uniform= 'a')
    resultFrame.rowconfigure((0,2),weight=1, uniform= 'a')
    
    if len(data) == 0:
        noResult = tk.Label(resultFrame, text="Não há nenhum resultado!", font=("Arial Black", 20))
        noResult.grid(column=1, row=1,  columnspan=2, sticky="n")

    else:
        pagination(1, 0, data, resultFrame, parent, useImg)


        
    
    resultFrame.grid_rowconfigure(0, weight=1)
    resultFrame.grid_columnconfigure(0, weight=1)
