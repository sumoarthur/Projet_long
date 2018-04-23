from src.vue.main import MainVueConection
from src.conroleur.Controleur import Controleur

import sys
from threading import Thread, RLock
import time


class Message:

    def __init__(self):
        self.mes_get={"Message":"Connection","Data":{}}
        self.new_mes_get=False
        self.mes_resp={"Message":"","Data":{}}
        self.new_mes_resp=False

    def messageRespond(self,message):
        self.mes_resp=message
        self.new_mes_resp=True

    def messageToGet(self,message):
        self.mes_get=message
        self.new_mes_get=True

    def getMesGet(self):

        if self.new_mes_get:
            self.new_mes_get=False
            return self.mes_get
        else:
            return None

    def getMesResp(self):

        if self.new_mes_resp:
            self.new_mes_resp=False
            return self.mes_resp
        else:
            return None

verrou = RLock()

mes=Message()
mes.messageRespond({"Message":"Connection"})

# Création des threads
thread_1 = Controleur(verrou,mes)
thread_2 = MainVueConection(verrou,mes)

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()