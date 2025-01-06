import tkinter as tk
from utils.resultCard import resultCard



def getSearchData():
    data = []
    return data
def resultPage(parent):
    data = getSearchData()
    resultFrame = tk.Frame(master=parent)
    if len(data) == 0:
        noResult =tk.Label(resultFrame, text="Não há nenhum resultado!")
        noResult.pack()
    else:
        for i in data:
            resultCard(resultFrame, i)




    resultFrame.pack()