import tkinter as tk
from utils.resultCard import resultCard
from Classes import *
from pages.detailedPage import detailedCard



def pagination(end, start, data, parent, grandParent):
    for frames in parent.winfo_children():
        frames.destroy()
        
    resultCard(parent, data[start], grandParent)
    dtbtn = tk.Button(parent, text= "Detalhes", command= lambda: switchToDetail(grandParent, detailedCard, data[start]))
    dtbtn.grid()
    resultCard(parent, data[end], grandParent)
    dtbtn1 = tk.Button(parent, text= "Detalhes", command= lambda: switchToDetail(grandParent, detailedCard, data[end]))
    dtbtn1.grid()
    prevEnd = end - 2
    prevStart = start - 2
    start = end+1 
    end =  end +2
    
    if end <= len(data):    
        nextbtn = tk.Button(parent, text="next", command=lambda: pagination(end, start, data, parent, grandParent))
        nextbtn.grid()
        prevbtn = tk.Button(parent, text="prev", command=lambda: pagination(prevEnd, prevStart, data, parent, grandParent))
        prevbtn.grid()
    else:
        prevbtn = tk.Button(parent, text="prev", command=lambda: pagination(prevEnd, prevStart, data, parent, grandParent))
        prevbtn.grid()


    
    
def switchToDetail(parent, nextFrame, data):
    print(parent.winfo_children())
    for frames in parent.winfo_children():
        frames.destroy()
    nextFrame(parent, data)

def resultPage(parent, data:ColecaoDeCartas):
   
    data = data.retorna_colecao()
    print(data)
    resultFrame = tk.Frame(master=parent)
    resultFrame.grid(row=0, column=0, sticky="nsew")  
    
    canvas = tk.Canvas(resultFrame)
    canvas.grid(row=0, column=0, sticky="nsew")  # Canvas inside the frame
    scr = tk.Scrollbar(resultFrame, orient="vertical", command=canvas.yview)
    scr.grid(row=0, column=1, sticky="ns")  # Scrollbar alongside the canvas
    
    canvas.configure(yscrollcommand=scr.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    secondFrame = tk.Frame(canvas, background='blue')
    canvas.create_window((300, 0), window=secondFrame, anchor="nw")
    if len(data) == 0:
        noResult = tk.Label(secondFrame, text="Não há nenhum resultado!")
        noResult.pack()
    elif(len(data) <=2):
        for item in data:
            resultCard(secondFrame, item, parent)
    else:

         pagination(1, 0, data, secondFrame, parent)


        
    
    resultFrame.grid_rowconfigure(0, weight=1)
    resultFrame.grid_columnconfigure(0, weight=1)
