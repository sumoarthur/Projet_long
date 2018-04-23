import tkinter as Tk
from src.modele.StructureData import *
from PIL import Image,ImageTk
from functools import partial
from src.modele.ChargeGraphe import ChargeGraphe

class VueExerciceOuLecon:

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


    def __init__(self,cours_or_exo):
        self.retour=""

        cours_or_exo=self.getRessourceFromId(cours_or_exo["id"],"bite")
        if type(cours_or_exo)==Cours:
            azer=cours_or_exo.lecon[0].version[0]
            if len(azer)<38:
                vue_courant = Tk.Tk()
                canvas3 = Tk.Canvas(vue_courant, background="white", width=1000, height=700)

                image = Image.open("/home/quince-art/PycharmProjects/Projet_long/"+"data/"+azer)
                photo2 = ImageTk.PhotoImage(image)

                canvas3.create_image(500, 500, image=photo2)
                canvas3.pack()
                button1 = Tk.Button(vue_courant, text="Quitter",
                                    command=partial(self.quitte_lecon, vue_courant))
                button1.pack()
                vue_courant.mainloop()
            else:

                vue_courant = Tk.Tk()
                canvas3 = Tk.Canvas(vue_courant, background="white", width=1000, height=700)

                image = Image.open("/home/quince-art/PycharmProjects/Projet_long/"+"data/"+"No_image.png")
                photo2 = ImageTk.PhotoImage(image)

                canvas3.create_image(500, 500, image=photo2)
                canvas3.pack()
                button1 = Tk.Button(vue_courant, text="Quitter",
                                    command=partial(self.quitte_lecon, vue_courant))
                button1.pack()
                vue_courant.mainloop()

            self.retour = {"Message":"LeconVu","Data":{"id_lecon":cours_or_exo.nom}}


        elif type(cours_or_exo)==Exercice:
            azer =cours_or_exo.version[0].data
            if len(azer)<38:
                vue_courant = Tk.Tk()
                canvas3 = Tk.Canvas(vue_courant, background="white", width=1000, height=500)

                image = Image.open("/home/quince-art/PycharmProjects/Projet_long/data/" + azer)
                photo2 = ImageTk.PhotoImage(image)

                canvas3.create_image(500, 200, image=photo2)
                canvas3.pack()

                label = Tk.Label(vue_courant, text="Question :")
                L=[]
                for k in cours_or_exo.reponse:
                    spamVar = Tk.BooleanVar()
                    spamCB = Tk.Checkbutton(label, text=str(k),
                                        variable=spamVar, onvalue=True, offvalue=False)
                    L+=[spamVar]
                    spamCB.pack()

                button1 = Tk.Button(label, text="Validation",
                                    command=partial(self.reponse, cours_or_exo,L,vue_courant))
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
                L=[]
                for k in cours_or_exo.reponse:
                    spamVar = Tk.BooleanVar()
                    spamCB = Tk.Checkbutton(label, text=str(k),
                                        variable=spamVar, onvalue=True, offvalue=False)
                    L+=[spamVar]
                    spamCB.pack()

                button1 = Tk.Button(label, text="Validation",
                                    command=partial(self.reponse, cours_or_exo,L,vue_courant))
                button1.pack()
                label.pack()
                vue_courant.mainloop()




