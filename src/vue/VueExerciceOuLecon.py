import tkinter as Tk
from src.modele.StructureData import *
from PIL import Image,ImageTk



class VueExerciceOuLecon:


    def __init__(self,cours_or_exo):


        if type(cours_or_exo)==Cours:
            azer=cours_or_exo.lecon[0].version[0]
            if len(azer)<38:
                vue_courant = Tk.Tk()
                canvas3 = Tk.Canvas(vue_courant, background="white", width=1000, height=1000)

                image = Image.open("/home/quince-art/PycharmProjects/Projet_long/"+"data/"+azer)
                photo2 = ImageTk.PhotoImage(image)

                canvas3.create_image(500, 500, image=photo2)
                canvas3.pack()
                vue_courant.mainloop()
            else:

                vue_courant = Tk.Tk()
                canvas3 = Tk.Canvas(vue_courant, background="white", width=1000, height=1000)

                image = Image.open("/home/quince-art/PycharmProjects/Projet_long/"+"data/"+"No_image.png")
                photo2 = ImageTk.PhotoImage(image)

                canvas3.create_image(500, 500, image=photo2)
                canvas3.pack()
                vue_courant.mainloop()


        elif type(cours_or_exo)==Exercice:
            azer =cours_or_exo.version[0].data
            if len(azer)<38:
                vue_courant = Tk.Tk()
                canvas3 = Tk.Canvas(vue_courant, background="white", width=1000, height=1000)

                image = Image.open("data/"+azer)
                photo2 = ImageTk.PhotoImage(image)

                canvas3.create_image(500, 500, image=photo2)
                canvas3.pack()
                vue_courant.mainloop()
            else:
                vue_courant = Tk.Toplevel()
                canvas3 = Tk.Canvas(vue_courant, background="white", width=1000, height=1000)

                image = Image.open("/home/quince-art/PycharmProjects/Projet_long/"+"data/"+"No_image.png")
                photo2 = ImageTk.PhotoImage(image)

                canvas3.create_image(500, 500, image=photo2)
                canvas3.pack()
                vue_courant.mainloop()

