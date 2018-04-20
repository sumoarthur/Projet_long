from src.vue.VueConnection import VueConnection
from src.vue.AfficherPlanning import AfficherPlanning
from src.modele.Session import Session
from src.vue.VueExerciceOuLecon import VueExerciceOuLecon
from src.modele.Graphe import Graphe


class Controleur(object):


    def __init__(self):
        self.session=None

    def verificationConnection(self,login,mdp):
        #A ne pas faire
        return {'id': "46455"}




    def automate(self):

        vue_connection=VueConnection()
        Id_user=self.verificationConnection(vue_connection.login,vue_connection.mdp)
        self.session=Session(Id_user)


        ave = AfficherPlanning(self.session.planning_user.planning_user)
        ave.planning()
        (nv_planning,(matiere,notion,niveau,statu,opti))=ave.demande
        self.session.planning_user.updatePlanning(nv_planning)
        print(statu,opti)
        self.session.preference.nouvellePreference(matiere,notion,niveau,statu,opti)
        self.session.demandeDePlanning("TODO") #TODO

        L_L_exo=[]

        for k in self.session.preference.getToDo():
            niveau=k["Niveau"]
            notion=k["Notion"]
            matiere=k["Matière"]
            opti=k["opti"]
            print(niveau,notion,matiere,opti)


            self.session.graphe.cal_parcours(matiere,notion,niveau,self.session.graphe_de_connaissance)
            self.session.graphe.defintion_exercice(niveau, opti,self.session.resultat_exo)

            L_L_exo+=[self.session.graphe.parcour_avec_exo]

        self.session.planning_user.remplissagePlanning(L_L_exo)
        ave = AfficherPlanning(self.session.planning_user.planning_user)
        ave.planning()

        ct=0
        while ct<10 :
            ct+=1
            if ave.next:
                #Prendre l id du dernier
                # getExoOrCoursFromId
                cours_or_exo=self.session.graphe.getRessourceFromId(self.session.planning_user.getProchain(),"bite")

                a=VueExerciceOuLecon(cours_or_exo)
                ave = AfficherPlanning(self.session.planning_user.planning_user)
                ave.planning()

























contoleur=Controleur()
contoleur.automate()