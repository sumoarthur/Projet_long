import tkinter as Tk
from src.modele.StructureData import *
from PIL import Image,ImageTk
from functools import partial
from src.modele.ChargeGraphe import ChargeGraphe

class VueCorrection:

    def reponse(self,exo,L,vue):
        l=[]
        for k in L:
            l+=[k.get()]
        self.retour={"id_exo":exo.nom,"Response_exo":l}
        vue.destroy()

    def getRessourceFromId(self,id,preference):
        abe = ChargeGraphe(preference)
        exo=abe.getExo()
        cours=abe.getCours()

        print(exo+cours)

        for k in exo:
            if type(k)==list:
                for kk in k:
                    if kk.nom==id:
                        return kk

        for k in cours:
                if k.nom==id:
                    return k

    def quitte_lecon(self,vue_courant):
        vue_courant.destroy()


    def __init__(self,cours_or_exo,correction):
        self.retour=""

        cours_or_exo=self.getRessourceFromId(cours_or_exo,"bite")
        azer = cours_or_exo.version[0].data
        if len(azer) < 38:
            vue_courant = Tk.Tk()
            canvas3 = Tk.Canvas(vue_courant, background="white", width=1000, height=500)

            image = Image.open("/home/quince-art/PycharmProjects/Projet_long/data/" + azer)
            photo2 = ImageTk.PhotoImage(image)

            canvas3.create_image(500, 200, image=photo2)
            canvas3.pack()

            label = Tk.Label(vue_courant, text="Question :")
            L = []
            a=correction.pop("Score")
            canvas3.create_text(500, 400, text="Score :"+a)
            ct=0
            for k in correction.keys():
                ct+=1
                canvas3.create_text(500, 400+15*ct, text=k+" "+correction[k]["etat"],fill=correction[k]["color"])



            button1 = Tk.Button(label, text="Quitter",
                                command=partial(self.reponse, cours_or_exo, L, vue_courant))
            button1.pack()
            label.pack()
            vue_courant.mainloop()
        else:
            vue_courant = Tk.Tk()
            canvas3 = Tk.Canvas(vue_courant, background="white", width=1000, height=500)

            image = Image.open("/home/quince-art/PycharmProjects/Projet_long/data/" + "No_image.png")
            photo2 = ImageTk.PhotoImage(image)

            canvas3.create_image(500, 200, image=photo2)
            canvas3.pack()

            label = Tk.Label(vue_courant, text="Question :")
            L = []
            a=correction.pop("Score")
            canvas3.create_text(500, 400, text="Score :"+a)
            ct=0
            for k in correction.keys():
                ct+=1
                canvas3.create_text(500, 400+15*ct, text=k+" "+correction[k]["etat"],fill=correction[k]["color"])



            button1 = Tk.Button(label, text="Quitter",
                                command=partial(self.reponse, cours_or_exo, L, vue_courant))
            button1.pack()
            label.pack()
            vue_courant.mainloop()
