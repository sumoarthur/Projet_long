import datetime
from src.modele.StructureData import *



class GrapheDeConnaissance:
    def __init__(self):
        self.grapheDeConnaissance={}            # self.grapheDeConnaissance={"id_connaissance": {"Date":{"Score":"..."},"Date2"{"Score":"..."}.....}........}

    def updateGrapheDeConnaissance(self,id_connaissance,Score):

        if len(self.grapheDeConnaissance) > 0:
            if id_connaissance in self.grapheDeConnaissance.keys():

                self.grapheDeConnaissance[id_connaissance].update({str(datetime.datetime.now()).split('.')[0]:{"Score":Score}})
            else :
                self.grapheDeConnaissance.update({id_connaissance: {str(datetime.datetime.now()).split('.')[0]: {"Score": Score}}})
        else:
            self.grapheDeConnaissance.update({id_connaissance: {str(datetime.datetime.now()).split('.')[0]: {"Score": Score}}})


    def selectionDesNotionNonMaitrise(self,L_lecon):

        for k in range(len(L_lecon)):
            if k<len(L_lecon):
                if type(L_lecon[k])==Cours:
                    if L_lecon[k].nom in self.grapheDeConnaissance.keys():
                        L_lecon.__delitem__(k)


        # TODO  ici prendre en compte l oublie   + selection des condition des maitrise d'une notion

        return L_lecon


class PlanningUser:
    def __init__(self):
        self.planning_user={}

    def updatePlanning(self,planning):

        if len(self.planning_user) > 0:
            if len(planning)>0:
                for k in planning.keys():
                    if k not in self.planning_user.keys():
                        self.planning_user.update({k:planning[k]})
        else:
            self.planning_user.update(planning)

    def remplissagePlanning(self,L_L_exo):

        #TODO si plusieur lecon en paralleles commment faire

        # ici leçon donner en serie
        l=[]
        for k in L_L_exo:
            for kk in k:
                l+=[kk]

        if len(self.planning_user)>0:
            for key in sorted(self.planning_user.keys(), key=lambda t: int(t[2])):  # Ne pas oublié de trié les creneau horaire dans l'ordre
                self.planning_user[key]["data"]=l.pop(0).nom

    def getProchain(self):
        print(self.planning_user)
        if len(self.planning_user)>0:
            key=sorted(self.planning_user.keys(), key=lambda t: int(t[2]))  # Ne pas oublié de trié les creneau horaire dans l'ordre
            return self.planning_user[key[0]]["data"]












class Preference:
    def __init__(self):
        self.pref={}    #selt.pref={"ID":{"Date":"..","Statut":"EnCours or Fini","type":{"opti":"Normal or Date_limite","Matière":"...", "Notion":"..." , "Niveau":"..."}}}
                            #TODO date limite

    def nouvellePreference(self,matiere,notion,niveau,statut,opti):

        if len(self.pref)>0:
            l=[]
            for v in self.pref.keys(): l+=[int(v)]
            Id=max(l)+1
            self.pref.update({str(Id):{"Date":str(datetime.datetime.now()).split('.')[0],"Statut":statut,"type":{"opti":opti,"Matière":matiere, "Notion":notion , "Niveau":niveau}}})

        else:
            self.pref.update({str(0):{"Date":str(datetime.datetime.now()).split('.')[0],"Statut":statut,"type":{"opti":opti,"Matière":matiere, "Notion":notion , "Niveau":niveau}}})

    def getToDo(self):
        L=[]

        if len(self.pref)>0:
            for k in self.pref.keys():
                print(k)
                print(self.pref[k]["Statut"])
                if self.pref[k]["Statut"]=="EnCours":
                    L.append(self.pref[k]["type"])
            return L
        else:
            print('Pas de tache a faire')


class ResultatExo:
    def __init__(self):
        self.resExo={}         #  self.resExo ={"idExo":{"Resultat":"...","V_cognitif":"...","Date":"..."}}

    def updateResultatExo(self,id_exo,Resultat,V_cognitif):

        if len(self.resExo) > 0:
            if id_exo not in self.resExo.keys():
                self.resExo.update({id_exo:{"Resultat":Resultat,"V_cognitif":V_cognitif,"Date":str(datetime.datetime.now()).split('.')[0]}})

        else:
            self.resExo.update({id_exo:{"Resultat":Resultat,"V_cognitif":V_cognitif,"Date":str(datetime.datetime.now()).split('.')[0]}})

    def exerciceNonRealise(self,id_exo):

        if len(self.resExo)>0:
            if id_exo in self.resExo.keys():
                print(False)
                return False
            else:
                return True
                print("True1")
        else:
            return True
            print("True2")




class ProfilCognitif:
    def __init__(self):
        self.profilCognitif={}    #  self.profilCognitif={"Date":{"Critere_1":"...","Critere_2":"...",..............}}

    def upadateProfilCognitif(self,Critere1,Critere2,Critere3):
        Date=str(datetime.datetime.now()).split('.')[0]
        if len(self.profilCognitif) > 0:
            if Date not in self.profilCognitif.keys():
                self.profilCognitif.update({Date:{"Critere_1":Critere1,"Critere_2":Critere2,"Critere_3":Critere3}})

        else:
            self.profilCognitif.update({Date:{"Critere_1":Critere1,"Critere_2":Critere2,"Critere_3":Critere3}})

