from functools import partial

from Graphe import *
from PIL import Image,ImageTk
from structure_data import *

from code_python.controleur import *


def onObjectClick(event):
    global a
    a = event.widget.find_closest(event.x, event.y)[0]

    #def onObjectClickoccu(event):
    global canvas
    global L_dipso

    fill = canvas.itemcget(a, 'fill')

    if (fill == 'red') or (fill == 'blanchedalmond'):
        canvas.itemconfig(a, fill='yellowgreen')
        canvas.itemconfig(a+1,text='Disponible')
        L_dipso+= [a]
    else:
        canvas.itemconfig(a, fill='red')
        canvas.itemconfig(a+1,text='Occupé')
        try :
            v=L_dipso.index(a)
            L_dipso.__delitem__(v)
        except:
            print('pb')
    print("L_dipso",L_dipso)


def onObjectClick2(event):
    global graphe
    print("L_parcour_avec_exo",graphe.parcour_avec_exo)

    bnb= event.widget.find_closest(event.x, event.y)[0]
    index=L_dipso.index(bnb)
    courant2=graphe.parcour_avec_exo[index]

    if type(courant2)==Cours:
        azer=courant2.lecon[0].version[0]
        if len(azer)<38:
            vue_courant = Tk.Toplevel()
            canvas3 = Tk.Canvas(vue_courant, background="white", width=1000, height=1000)

            image = Image.open("data/"+azer)
            photo2 = ImageTk.PhotoImage(image)

            canvas3.create_image(500, 500, image=photo2)
            canvas3.pack()
            vue_courant.mainloop()
        else:

            vue_courant = Tk.Toplevel()
            canvas3 = Tk.Canvas(vue_courant, background="white", width=1000, height=1000)

            image = Image.open("data/"+"No_image.png")
            photo2 = ImageTk.PhotoImage(image)

            canvas3.create_image(500, 500, image=photo2)
            canvas3.pack()
            vue_courant.mainloop()


    elif type(courant2)==Exercice:
        azer =courant2.version[0].data
        if len(azer)<38:
            vue_courant = Tk.Toplevel()
            canvas3 = Tk.Canvas(vue_courant, background="white", width=1000, height=1000)

            image = Image.open("data/"+azer)
            photo2 = ImageTk.PhotoImage(image)

            canvas3.create_image(500, 500, image=photo2)
            canvas3.pack()
            vue_courant.mainloop()
        else:
            vue_courant = Tk.Toplevel()
            canvas3 = Tk.Canvas(vue_courant, background="white", width=1000, height=1000)

            image = Image.open("data/"+"No_image.png")
            photo2 = ImageTk.PhotoImage(image)

            canvas3.create_image(500, 500, image=photo2)
            canvas3.pack()
            vue_courant.mainloop()


def planning_cours(canvas,matiere, notion):
    global graphe
    global niveau

    print("niveau 24453",niveau)

    graphe=Graphe()
    graphe.cal_parcours(niveau)
    graphe.defintion_exercice(niveau,"normal","")



    for k in range(len(L_dipso)):
        canvas.itemconfig(L_dipso[k]+1, text=graphe.parcour_avec_exo[k].nom)
        canvas.tag_bind(L_dipso[k], '<ButtonPress-1>', onObjectClick2)


def update_item(canvas, item_id):
    global matiere,notion,niveau
    matiere, notion='',''
    root1 = Tk.Tk()

    l = Tk.LabelFrame(root1, text="Ajout d'un nouvau cours", padx=20, pady=20)

    f1= Tk.LabelFrame(l, text="Matiere")

    s1 = Tk.Scrollbar(f1)
    l1 = Tk.Listbox(f1,highlightcolor='red')
    liste=['Mathématique','Sciences','Sciences économique et sociales','Français','Histoire-Géographie ']
    for k in range(len(liste)):
        l1.insert(k,liste[k])

    s1.config(command=l1.yview)
    l1.config(yscrollcommand=s1.set)
    l1.pack(side=Tk.LEFT, fill=Tk.Y)
    s1.pack(side=Tk.RIGHT, fill=Tk.Y)

    f1.grid(row=1, column=1)

    f2= Tk.LabelFrame(l, text="Notion")

    s2 = Tk.Scrollbar(f2)
    l2 = Tk.Listbox(f2)
    liste=['Fonction numérique','Polynômes du second degré','Derivation']
    for k in range(len(liste)):
        l2.insert(k,liste[k])

    s2.config(command=l2.yview)
    l2.config(yscrollcommand=s2.set)
    l2.pack(side=Tk.LEFT, fill=Tk.Y)
    s2.pack(side=Tk.RIGHT, fill=Tk.Y)

    f2.grid(row=1, column=2, padx=20, pady=20)

    f3= Tk.LabelFrame(l, text="Niveau")

    s3 = Tk.Scrollbar(f3)
    l3 = Tk.Listbox(f3)
    liste=['Debutant','Intermediaire','Avance']
    for k in range(len(liste)):
        l3.insert(k,liste[k])

    s3.config(command=l3.yview)
    l3.config(yscrollcommand=s3.set)
    l3.pack(side=Tk.LEFT, fill=Tk.Y)
    s3.pack(side=Tk.RIGHT, fill=Tk.Y)

    f3.grid(row=1, column=3)



    def clic1(event):
        index = l1.curselection()
        print("l1.get(index)",l1.get(index))
        matiere=l1.get(index)
    def clic2(event):
        index = l2.curselection()
        print(l2.get(index))
        notion=l2.get(index)
    def clic3(event):
        global niveau
        index = l3.curselection()
        print(l3.get(index))
        niveau=l3.get(index)

    l1.bind('<ButtonRelease-1>',clic1)
    l2.bind('<ButtonRelease-1>', clic2)
    l3.bind('<ButtonRelease-1>', clic3)


    button1 = Tk.Button(l, text="Validation",command=partial(planning_cours,canvas,matiere, notion))
    button1.grid(row=2,column=2)
    l.pack(fill="both", expand="yes")
    root1.mainloop()



def planning(root):
    global a
    global courant
    global niveau

    global L_dipso
    global graphe

    courant = []
    L_dipso = []
    niveau = ''

    fc1= Tk.Frame(root)

    canvas = Tk.Canvas(fc1, background="white",scrollregion=(0, 0, 2000, 1000),width=1700, height=900)
    hbar=Tk.Scrollbar(fc1,orient=Tk.HORIZONTAL)
    hbar.pack(side=Tk.BOTTOM,fill=Tk.X)
    hbar.config(command=canvas.xview)
    vbar=Tk.Scrollbar(fc1,orient=Tk.VERTICAL)
    vbar.pack(side=Tk.RIGHT,fill=Tk.Y)
    vbar.config(command=canvas.yview)

    n,nn=15,8
    list_id=[[0 for k in range(nn)] for kk in range(n)]
    for k in range(n):
        for kk in range(nn):
            factor=1.8
            if k==0:
                Label_jour=['Heure','Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']
                x11=int((5*(kk+1)+120*kk)*factor)
                x12=int(5*factor)
                x21=int((5*(kk+1)+120*(kk+1))*factor)
                x22=int(25*factor)
                rectangle_id = canvas.create_rectangle((x11, x12), (x21, x22), fill='burlywood')
                text_id=canvas.create_text(x11+(x21-x11)/2,x22/2, text=Label_jour[kk])
                list_id[k][kk]=(rectangle_id,text_id)

            elif kk==0 and (k!=0):
                x11=int((5*(kk+1)+120*kk)*factor)
                x12=int((5*(k+1)+25*k)*factor)
                x21=int((5*(kk+1)+120*(kk+1))*factor)
                x22=int((5*(k+1)+25*(k+1))*factor)

                rectangle_id = canvas.create_rectangle((x11, x12), (x21, x22), fill='burlywood')
                text_id=canvas.create_text(x11+(x21-x11)/2,x12+(x22-x12)/2, text=str(8+k)+'H - '+str(9+k)+'H')
                list_id[k][kk]=(rectangle_id,text_id)

            else:
                x11=int((5*(kk+1)+120*kk)*factor)
                x12=int((5*(k+1)+25*k)*factor)
                x21=int((5*(kk+1)+120*(kk+1))*factor)
                x22=int((5*(k+1)+25*(k+1))*factor)
                rectangle_id = canvas.create_rectangle((x11, x12), (x21, x22), fill='blanchedalmond')
                text_id = canvas.create_text(x11 + (x21 - x11) / 2, x12 + (x22 - x12) / 2,text='neutre')
                list_id[k][kk]=(rectangle_id,text_id)


    for k in list_id:
        for kk in k:
            canvas.tag_bind(kk[0], '<ButtonPress-1>', onObjectClick)


    f1 = Tk.Frame(root, bd=1, relief='solid')

    button = Tk.Button(f1, text="click", command=partial(update_item,
                               canvas, rectangle_id))
    image = Image.open("data/"+"visage.png")
    photo = ImageTk.PhotoImage(image)



    canvas2 = Tk.Canvas(f1, background="white",scrollregion=(0, 0, 1070, 400),width=200, height=400)
    canvas2.create_image(100,70, image=photo)
    canvas2.create_text(40,200 ,text='Nom: XXXX')


    canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    canvas.pack(side=Tk.LEFT,expand=True,fill=Tk.BOTH)
    fc1.grid(row=1, column=1)


    canvas2.grid(row=1, column=0)
    button.grid(row=2, column=0)
    f1.grid(row=1, column=0)


    root.mainloop()
