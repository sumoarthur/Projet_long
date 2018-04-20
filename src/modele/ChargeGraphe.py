import pickle
from src.modele.arbre import  *




class ChargeGraphe:

    def __init__(self,preference):
        pass

    def get_arbre(self):

        # TODO connexion bdd ???neo4j???   barabé
        filename_data = open('/home/quince-art/PycharmProjects/Projet_long/data/graphe.txt', 'rb')
        fichier_data = pickle.load(filename_data)
        filename_data.close()
        return fichier_data


    def getExo(self):
        filename_data = open('/home/quince-art/PycharmProjects/Projet_long/data/Exo.txt', 'rb')
        fichier_data = pickle.load(filename_data)
        filename_data.close()
        return fichier_data

    def getCours(self):
        filename_data = open('/home/quince-art/PycharmProjects/Projet_long/data/Cours.txt', 'rb')
        fichier_data = pickle.load(filename_data)
        filename_data.close()
        return fichier_data








