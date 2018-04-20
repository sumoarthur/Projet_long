import tkinter as Tk
from functools import partial
from PIL import Image,ImageTk


class AfficherPlanning :

    def __init__(self,panning_data):
        self.demande=None
        self.vue_principale=Tk.Tk()
        self.dic_item_to_date={}
        self.planning_data=panning_data

    def planning(self):
        global a
        global courant
        global niveau
        global canvas

        global L_dipso
        global graphe

        courant = []
        L_dipso = []
        niveau = ''
        root =self.vue_principale
        fc1 = Tk.Frame(root)

        canvas = Tk.Canvas(fc1, background="white", scrollregion=(0, 0, 2000, 1000), width=1700, height=900)
        hbar = Tk.Scrollbar(fc1, orient=Tk.HORIZONTAL)
        hbar.pack(side=Tk.BOTTOM, fill=Tk.X)
        hbar.config(command=canvas.xview)
        vbar = Tk.Scrollbar(fc1, orient=Tk.VERTICAL)
        vbar.pack(side=Tk.RIGHT, fill=Tk.Y)
        vbar.config(command=canvas.yview)

        n, nn = 15, 8
        ct=[]
        list_id = [[0 for k in range(nn)] for kk in range(n)]
        for k in range(n):
            for kk in range(nn):
                factor = 1.8
                if k == 0:
                    Label_jour = ['Heure', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
                    x11 = int((5 * (kk + 1) + 120 * kk) * factor)
                    x12 = int(5 * factor)
                    x21 = int((5 * (kk + 1) + 120 * (kk + 1)) * factor)
                    x22 = int(25 * factor)
                    rectangle_id = canvas.create_rectangle((x11, x12), (x21, x22), fill='burlywood')
                    text_id = canvas.create_text(x11 + (x21 - x11) / 2, x22 / 2, text=Label_jour[kk])
                    list_id[k][kk] = (rectangle_id, text_id)


                elif kk == 0 and (k != 0):
                    x11 = int((5 * (kk + 1) + 120 * kk) * factor)
                    x12 = int((5 * (k + 1) + 25 * k) * factor)
                    x21 = int((5 * (kk + 1) + 120 * (kk + 1)) * factor)
                    x22 = int((5 * (k + 1) + 25 * (k + 1)) * factor)

                    rectangle_id = canvas.create_rectangle((x11, x12), (x21, x22), fill='burlywood')
                    text_id = canvas.create_text(x11 + (x21 - x11) / 2, x12 + (x22 - x12) / 2,
                                                 text=str(8 + k) + 'H - ' + str(9 + k) + 'H')
                    list_id[k][kk] = (rectangle_id, text_id)

                else:
                    x11 = int((5 * (kk + 1) + 120 * kk) * factor)
                    x12 = int((5 * (k + 1) + 25 * k) * factor)
                    x21 = int((5 * (kk + 1) + 120 * (kk + 1)) * factor)
                    x22 = int((5 * (k + 1) + 25 * (k + 1)) * factor)
                    rectangle_id = canvas.create_rectangle((x11, x12), (x21, x22), fill='blanchedalmond')
                    text_id = canvas.create_text(x11 + (x21 - x11) / 2, x12 + (x22 - x12) / 2, text='neutre')
                    list_id[k][kk] = (rectangle_id, text_id)

                    self.dic_item_to_date.update({(Label_jour[kk], str(8 + k) + 'H - ' + str(9 + k) + 'H',str(k+7*kk)): {"id": list_id[k][kk]}})



        for k in list_id:
            for kk in k:
                canvas.tag_bind(kk[0], '<ButtonPress-1>', self.onObjectClick)

        f1 = Tk.Frame(root, bd=1, relief='solid')

        button = Tk.Button(f1, text="click", command=partial(self.update_item,
                                                             canvas, rectangle_id))
        image = Image.open("/home/quince-art/PycharmProjects/Projet_long/data/" + "visage.png")
        photo = ImageTk.PhotoImage(image)

        canvas2 = Tk.Canvas(f1, background="white", scrollregion=(0, 0, 1070, 400), width=200, height=400)
        canvas2.create_image(100, 70, image=photo)
        canvas2.create_text(40, 200, text='Nom: XXXX')

        canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        canvas.pack(side=Tk.LEFT, expand=True, fill=Tk.BOTH)
        fc1.grid(row=1, column=1)

        canvas2.grid(row=1, column=0)
        button.grid(row=2, column=0)
        f1.grid(row=1, column=0)

        if len(self.planning_data)>0:
            for k in self.planning_data.keys():
                canvas.itemconfig(int(self.dic_item_to_date[k]['id'][1]), text=self.planning_data[k]['data'])
                canvas.itemconfig(int(self.dic_item_to_date[k]['id'][0]), fill='yellowgreen')

        root.mainloop()

    def onObjectClick(self, event):
        global a
        a = event.widget.find_closest(event.x, event.y)[0]

        global canvas
        global L_dipso

        fill = canvas.itemcget(a, 'fill')

        if (fill == 'red') or (fill == 'blanchedalmond'):
            canvas.itemconfig(a, fill='yellowgreen')
            canvas.itemconfig(a + 1, text='Disponible')
            L_dipso += [a]
        else:
            canvas.itemconfig(a, fill='red')
            canvas.itemconfig(a + 1, text='Occupé')
            try:
                v = L_dipso.index(a)
                L_dipso.__delitem__(v)
            except:
                print('pb')
        print("L_dipso", L_dipso)

    def update_item(self, canvas, item_id):
        global matiere, notion, niveau
        matiere, notion = '', ''
        root1 = Tk.Tk()

        l = Tk.LabelFrame(root1, text="Ajout d'un nouvau cours", padx=20, pady=20)

        f1 = Tk.LabelFrame(l, text="Matiere")

        s1 = Tk.Scrollbar(f1)
        l1 = Tk.Listbox(f1, highlightcolor='red')
        liste = ['Mathématique', 'Sciences', 'Sciences économique et sociales', 'Français', 'Histoire-Géographie ']
        for k in range(len(liste)):
            l1.insert(k, liste[k])

        s1.config(command=l1.yview)
        l1.config(yscrollcommand=s1.set)
        l1.pack(side=Tk.LEFT, fill=Tk.Y)
        s1.pack(side=Tk.RIGHT, fill=Tk.Y)

        f1.grid(row=1, column=1)

        f2 = Tk.LabelFrame(l, text="Notion")

        s2 = Tk.Scrollbar(f2)
        l2 = Tk.Listbox(f2)
        liste = ['Fonction numérique', 'Polynômes du second degré', 'Derivation']
        for k in range(len(liste)):
            l2.insert(k, liste[k])

        s2.config(command=l2.yview)
        l2.config(yscrollcommand=s2.set)
        l2.pack(side=Tk.LEFT, fill=Tk.Y)
        s2.pack(side=Tk.RIGHT, fill=Tk.Y)

        f2.grid(row=1, column=2, padx=20, pady=20)

        f3 = Tk.LabelFrame(l, text="Niveau")

        s3 = Tk.Scrollbar(f3)
        l3 = Tk.Listbox(f3)
        liste = ['Debutant', 'Intermediaire', 'Avance']
        for k in range(len(liste)):
            l3.insert(k, liste[k])

        s3.config(command=l3.yview)
        l3.config(yscrollcommand=s3.set)
        l3.pack(side=Tk.LEFT, fill=Tk.Y)
        s3.pack(side=Tk.RIGHT, fill=Tk.Y)

        f3.grid(row=1, column=3)

        def clic1(event):
            global matiere
            index = l1.curselection()
            print("l1.get(index)", l1.get(index))
            matiere = l1.get(index)

        def clic2(event):
            global notion
            index = l2.curselection()
            print(l2.get(index))
            notion = l2.get(index)

        def clic3(event):
            global niveau
            index = l3.curselection()
            print(l3.get(index))
            niveau = l3.get(index)

        l1.bind('<ButtonRelease-1>', clic1)
        l2.bind('<ButtonRelease-1>', clic2)
        l3.bind('<ButtonRelease-1>', clic3)


        button1 = Tk.Button(l, text="Validation",
                            command=partial(self.add_demande, L_dipso, root1))
        button1.grid(row=2, column=2)
        l.pack(fill="both", expand="yes")
        root1.mainloop()

    def add_demande(self, L_dipso, root1):
        global matiere
        global notion
        global niveau

        # L_dipso=conversion_planning(planning)
        for i in self.dic_item_to_date.keys():
            for k in L_dipso:
                if k in self.dic_item_to_date[i]["id"]:
                    self.planning_data.update({i: {"data": "Dispo"}})


        if niveau=='':
            niveau='Debutant'
        if notion=='':
            notion='Derivation'
        if matiere=='':
            matiere='Mathematique'

        opti='normal'  #TODO selecteur d'optimisation
        statu="EnCours"

        self.demande = (self.planning_data,(matiere, notion, niveau,statu,opti))



        # debloquage
        root1.destroy()
        self.vue_principale.destroy()








#er={('Lundi', '18H - 19H'): {'data': 'cour1'}, ('Lundi', '17H - 18H'): {'data': 'Cours2'}, ('Lundi', '19H - 20H'): {'data': 'Cours3'}, ('Lundi', '16H - 17H'): {'data': 'Cours4'}}

