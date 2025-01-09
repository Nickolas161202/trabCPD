import tkinter as tk
from Classes import Card
import urllib.request
from PIL import ImageTk, Image
import io

class WebImage:
    def __init__(self, url):
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()

        image = Image.open(io.BytesIO(raw_data)).resize((200,300))
        self.image = ImageTk.PhotoImage(image)
        
    def get(self):
        return self.image

def resultCard(parent, data: Card, showImages):
    resultFrame = tk.Frame(master=parent)
    nameLabel = tk.Label(resultFrame, text=data.name, font=("Arial", 12))
    if showImages:
        img = WebImage(data.game_absolute_path).get()
    # Store the image directly inside the label to prevent garbage collection
        imgLabel = tk.Label(resultFrame, image=img)
        imgLabel.image = img  # This ensures that the image is kept in memory
        imgLabel.grid(row=2, column= 0)
    nameLabel.grid(row=0, column=0)

    resultFrame.grid(sticky="n")
