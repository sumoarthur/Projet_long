
from random import *




class Lecon:


    def __init__(self,nom,version):
        self.nom=nom
        self.version=version

    def __str__(self):
        return self.nom



class Ex_verion:

    def __init__(self,data,cri1,cri2):
        self.data=data
        self.cri1=cri1
        self.cri2=cri2



class Exercice:


    def __init__(self,nom,niveau,version):
        self.nom=nom
        self.niveau=niveau
        self.version=version
        self.duree=randrange(5,30,5)
        self.score=random()

    def __str__(self):
        return self.nom




class Cours:


    def __init__(self,nom_cours,niveau,Llecon,Lexo):
        self.nom=nom_cours
        self.niveau=niveau
        self.lecon=Llecon
        self.exo=Lexo
        self.duree =20


    def __str__(self):
        return self.nom



