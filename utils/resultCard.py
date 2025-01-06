import tkinter as tk
from utils.navigationFunctions import switchPageWithData
from pages.detailedPage import detailedCard
from Classes import Card
import urllib.request
from PIL import ImageTk, Image
import io

class WebImage:
    def __init__(self, url):
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()

        image = Image.open(io.BytesIO(raw_data))
        self.image = ImageTk.PhotoImage(image)

    def get(self):
        return self.image

def resultCard(parent, data: Card):
    resultFrame = tk.Frame(master=parent)

    nameLabel = tk.Label(resultFrame, text=data.name)
    img = WebImage(data.game_absolute_path).get()

    # Store the image directly inside the label to prevent garbage collection
    imgLabel = tk.Label(resultFrame, image=img)
    imgLabel.image = img  # This ensures that the image is kept in memory

    btn = tk.Button(resultFrame, text="detalhes", command=lambda: switchPageWithData(resultFrame, detailedCard, parent, data))

    nameLabel.grid(row=0, column=0)
    btn.grid(row=1, column=0)
    imgLabel.grid(row=2, column= 0)

    resultFrame.pack()
