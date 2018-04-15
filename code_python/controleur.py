from code_python.Graphe import  *

from code_python.ihm2 import  *


class Session:


    def __init__(self):


        self.date_planing={}
        self.creneau=[]
        self.cours_asck=None
        self.prochain_cours=None
        self.login=''
        self.mdp=''
        self.id=None

    def add_user(self,user):
        self.id=user

    def start_vue(self,a):
        self.vue_principale = Tk.Tk()
        Fenetre(self.vue_principale,a)

        self.vue_principale.mainloop()

        return self.login,self.mdp

    def quitte(self):
        self.vue_principale.destroy()

    def start_session(self,session):
        self.vue_principale = Tk.Tk()
        planning(self.vue_principale,session)




    def conversion_planning(self,planning):
        #TODO
        pass

    def add_demande(self,L_dipso,matiere, notion,niveau,root1):



        print("fff")

        #L_dipso=conversion_planning(planning)
        self.creneau=L_dipso
        self.cours_asck=(matiere,notion,niveau)

        #debloquage
        root1.destroy()
        self.vue_principale.destroy()

    def determination_parcours(self):
        graph = Graphe()
        niveau=self.cours_asck
        print(niveau)
        #graph.cal_parcours(niveau)
        #graph.defintion_exercice(niveau, "normal", "")

        self.prochain_cours=graph.parcour_avec_exo



    def chage_data(self):
        #TODO
        pass




class Controleur:

    def __init__(self):
        self.session = None


    def verification_connection(self, login, mdp):
        #####
        #      TODO
        #####
        print("magie")

        if login == "defaultlogin" and mdp=="defaultpass":
            return True
        else:
            return False

    def demande_possible(self,demande):
        # TODO
        #return True or False
        pass

    def connection(self):

        self.session = Session()
        i=0
        while i<10:

            if (self.session.login=='') and (self.session.mdp==''):
                self.session.start_vue(self.session)

            else:
                if self.verification_connection( self.session.login, self.session.mdp):
                    print("Connection")

                    self.session.add_user("User id")

                else:
                    print("pb de mots de passe")

                    self.session.start_vue(self.session)
            i+=1


    def load_session(self):

        #Look in data base


        # if user in data_base:
            # CHARGER parametre
            # chage_data()
        # else:


        self.session.start_session(self.session)
        print(self.session.prochain_cours)

        #if demande_possible :
        if True:
            #demande de planning
            self.session.determination_parcours()
            print(self.session.prochain_cours)

        else:
            self.session.start_session(self.session)













a=Controleur()

a.connection()

a.load_session()






