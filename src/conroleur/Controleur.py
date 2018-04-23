from src.vue.VueConnection import VueConnection
from src.vue.AfficherPlanning import AfficherPlanning
from src.modele.Session import Session
from src.vue.VueExerciceOuLecon import VueExerciceOuLecon
from src.modele.Graphe import Graphe
from essai2.automatelib import *

import time
from threading import Thread, RLock


class Controleur(Thread):


    def __init__(self,verrou,message):
        Thread.__init__(self)
        self.verrou=verrou
        self.message=message
        self.message_intern={"Message":'',"Data":{}}

        self.session = None



    def getMessage(self):
        print("entre_message")
        return input()




    def automate(self):

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



    def run(self):
        def f1():
            print("action Etat1")

        def f2():
            print("action Etat2")

        def f3():
            print("action Etat3")
            Id_user=self.message.mes_get["Data"]["id"]
            self.session = Session(Id_user)
            self.message_intern={"Message":"ChargementFini","Data":{}}
            print("Data chargé")
            print("fin_action Etat3")



        def f4():
            print("action Etat4")

        def f5():
            print("action Etat5")

        def f6():
            self.message_intern={"Message":'',"Data":{}}
            self.message.messageRespond({"Message": "VuePlanning", "Data": self.session.planning_user.planning_user})

            print("action Etat6")

        def f7():
            mes_exo_to_get = self.session.graphe.getTypeRessourceFromId(self.session.planning_user.getProchain()["id"], "bite")
            if mes_exo_to_get["type"]=="Exercice":
                self.message_intern={"Message":"Exercice","Data":mes_exo_to_get}
            else:
                self.message_intern={"Message":"Cours","Data":mes_exo_to_get}
            print("action Etat7")

        def f8():
            data=self.message_intern["Data"]

            self.message.messageRespond({"Message": "VueCorrectionExo", "Data": data})
            self.message_intern={"Message":'',"Data":{}}
            print("action Etat8")

        def f9():

            print("action Etat9")
            self.session.planning_user.updatePlanning(self.message.mes_get["Data"]["nv_planning"])
            self.session.preference.nouvellePreference(self.message.mes_get["Data"]["matiere"], self.message.mes_get["Data"]["notion"],self.message.mes_get["Data"]["niveau"] ,self.message.mes_get["Data"]["statu"] ,self.message.mes_get["Data"]["opti"] )
            self.message_intern={"Message":'Validation',"Data":{}}
            print("fin_action Etat9")




        def f10():
            data=self.message_intern["Data"]
            self.message_intern = {"Message": '', "Data": {}}
            self.message.messageRespond({"Message": "VueExercice", "Data": data})
            print("action Etat10")

        def f11():
            data=self.message_intern["Data"]
            self.message_intern = {"Message": '', "Data": {}}
            self.message.messageRespond({"Message": "VueCours", "Data": data})

            print("action Etat11")

        def f12():
            print("action Etat12")
            self.session.lecon_vu.addLeconVu(self.message.mes_get["Data"]["id_lecon"])


            self.message_intern={"Message":"LeconVuPriseEnCompte","Data":{}}


        def f13():
            print("action Etat13")
            correction=self.session.resultat_exo.correctionExercice(self.message.mes_get["Data"]["id_exo"],self.message.mes_get["Data"]["Response_exo"],"bite")
            self.session.resultat_exo.updateResultatExo(self.message.mes_get["Data"]["id_exo"],correction["Score"],"TODO")
            data={"id_exo":self.message.mes_get["Data"]["id_exo"] ,"corection":correction}
            self.message_intern={"Message":"ResultatsExerciceAndPriseEnCompte","Data":data}


        def f14():
            print("action Etat14")
            if self.session.preference.pref!={}:
                self.session.demandeDePlanning("TODO")  # TODO
                L_L_exo = []

                for k in self.session.preference.getToDo():
                    niveau = k["Niveau"]
                    notion = k["Notion"]
                    matiere = k["Matière"]
                    opti = k["opti"]

                    self.session.graphe.cal_parcours(matiere, notion, niveau, self.session.graphe_de_connaissance)
                    self.session.graphe.defintion_exercice(niveau, opti, self.session.resultat_exo,self.session.lecon_vu)

                    L_L_exo += [self.session.graphe.parcour_avec_exo]

                self.session.planning_user.remplissagePlanning(L_L_exo)
            self.message_intern={"Message":"PlanningCalcule","Data":{}}



        s1 = State('Non connecter', f1)
        s2 = State('Verification Id,login', f2)
        s3 = State('Chargement des Datas Users', f3)
        s4 = State("Affichage Erreur D'indentification", f4)
        s5 = State("Inscription", f5)
        s14 = State("Calcul_planning",f14)
        s6 = State("Affichage Planning\n(session)", f6)
        s7 = State("Realisation Exo/Lecon", f7)
        s8 = State("Correction", f8)
        s9 = State("Formulaire de gestion des cours", f9)
        s10 = State("Realisation Exo",f10)
        s11 = State("Realisation Lecon",f11)
        s12 = State("Prise en compte de la lecon vu",f12)
        s13 = State("Prise en compte des resultat exercices",f13)

        a = Automaton('abc',
                      states=(s1, s2, s3, s4, s5, s6, s7, s8, s9,s10,s11,s12,s13),
                      initial_states=(s2,),
                      final_states=(s6,)
                      )

        ########
        a.add_transition(Transition(s1, s2, 'DemandeDeConnection',"TODO"))
        a.add_transition(Transition(s2, s4, 'IdentificationNonValide',"TODO"))
        a.add_transition(Transition(s4, s1, 'ok',"TODO"))
        a.add_transition(Transition(s1, s5, 'Demande_inscription',"TODO"))
        a.add_transition(Transition(s5, s1, 'InscriptionFaite',"TODO"))
        #######

        #######

        #######


        #######
        a.add_transition(Transition(s2, s3, 'IdentificationValide',"extern"))
        a.add_transition(Transition(s3, s14, 'ChargementFini',"intern"))
        a.add_transition(Transition(s14,s6, 'PlanningCalcule',"intern"))
        #######


        #######
        a.add_transition(Transition(s6, s7, "DemandeRealisationExo","extern"))

        a.add_transition(Transition(s7,s11,"Cours","intern"))
        a.add_transition(Transition(s11,s12,"ValidationLeconVu","extern"))
        a.add_transition(Transition(s12,s14,"LeconVuPriseEnCompte","intern"))
        a.add_transition(Transition(s14,s6, 'PlanningCalcule',"intern"))

        a.add_transition(Transition(s7,s10,"Exercice","intern"))
        a.add_transition(Transition(s10, s13, "ValidationReponseExo","extern"))
        a.add_transition(Transition(s13,s8,"ResultatsExerciceAndPriseEnCompte","intern"))
        a.add_transition(Transition(s8, s14, "SortirCorrection","extern"))
        a.add_transition(Transition(s14,s6, 'PlanningCalcule',"intern"))
        #######


        #######
        a.add_transition(Transition(s6, s9, "GestionCours","extern"))
        a.add_transition(Transition(s9, s14, "Validation","extern"))
        a.add_transition(Transition(s14,s6, 'PlanningCalcule',"intern"))
        #######



        ct_changement_etat=0
        i = 0
        while i < 100:
            time.sleep(0.1)
            with self.verrou:
                print()
                print()
                print("Controleur",i)
                time.sleep(0.2)
                message=self.message.getMesGet()
                print("controleur",message)

                if message!= None:
                    ct_changement_etat+=1
                    print("\nreceve message --->" + str(message["Message"]))
                    mes_auto=a.auto(message["Message"])
                    print(mes_auto)
                    if mes_auto!="N'est pas une transition valide":
                        a.render('graphe_de_seq'+str(ct_changement_etat)+'.png')

                secu=0
                while self.message_intern["Message"]!='' and secu<20:
                    ct_changement_etat+=1
                    secu+=1
                    if secu==19:
                        print('Pas de message intern')

                    print("\nreceve intern message --->" + str(self.message_intern["Message"]))
                    time.sleep(0.2)
                    mes_auto=a.auto(self.message_intern["Message"])
                    print(mes_auto)
                    if mes_auto!="N'est pas une transition valide":
                        a.render('graphe_de_seq'+str(ct_changement_etat)+'.png')


            i += 1





















