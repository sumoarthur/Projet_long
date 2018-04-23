import time
from threading import Thread, RLock

from src.vue.VueConnection import VueConnection
from src.vue.AfficherPlanning import AfficherPlanning
from src.vue.VueExerciceOuLecon import VueExerciceOuLecon
from src.vue.VueCorrection import VueCorrection

class MainVueConection(Thread):




    def __init__(self,verrou,message):
        Thread.__init__(self)
        self.verrou=verrou
        self.message=message





    def verificationConnection(self,login,mdp):
        #A ne pas faire
        return {'id': "46455"}







    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 100:
            time.sleep(0.1)
            with self.verrou:
                print()
                print()
                print("Vue")
                time.sleep(0.2)
                message=self.message.getMesResp()
                print("vue",message)

                if message!=None:

                    if message["Message"] == "Connection":
                        print("receve message --->"+str(message["Message"]))
                        vue_connection = VueConnection()
                        Id_user = self.verificationConnection(vue_connection.login, vue_connection.mdp)
                        self.message.messageToGet({"Message": "IdentificationValide", "Data": Id_user})



                    elif message["Message"] =="VuePlanning":
                        ave = AfficherPlanning(message["Data"])
                        ave.planning()
                        if ave.next:
                            self.message.messageToGet({'Message':"DemandeRealisationExo","Data":""})
                        else:
                            data = ave.demande
                            self.message.messageToGet({"Message": "GestionCours", "Data": data})

                    elif message["Message"]=="VueExercice":
                        a = VueExerciceOuLecon(message["Data"])
                        response=a.retour
                        self.message.messageToGet({"Message":"ValidationReponseExo","Data":response})

                    elif message["Message"]=="VueCours":
                        a= VueExerciceOuLecon(message["Data"])
                        response=a.retour["Data"]
                        self.message.messageToGet({"Message":"ValidationLeconVu","Data":response})

                    elif message["Message"]=="VueCorrectionExo":
                        a=VueCorrection(message["Data"]["id_exo"],message["Data"]["corection"])

                        self.message.messageToGet({"Message":"SortirCorrection","Data":{}})





            i += 1




