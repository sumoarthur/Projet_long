from src.modele.ChargeDataUser import ChargeDataUser
from src.modele.DataUser import *
from src.modele.Graphe import Graphe

class Session:

    def __init__(self,id_user):


        a=ChargeDataUser(id_user)



        self.graphe_de_connaissance=GrapheDeConnaissance()
        self.planning_user=PlanningUser()
        self.preference=Preference()
        self.resultat_exo=ResultatExo()
        self.profil_cognitif=ProfilCognitif()
        self.lecon_vu=LeconVu()
        self.graphe=None


    def demandeDePlanning(self,preference):
        print("merde")
        self.graphe=Graphe(self.preference)


    def resultatExercice(self):
        pass

    def suppressionDeLaTacheEffectuer(self):
        pass