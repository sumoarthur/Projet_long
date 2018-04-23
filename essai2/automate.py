#!/usr/bin/env python
# coding=utf8

from essai2.automatelib import State, Transition, Automaton, EpsilonTransition

import time

if True:


    def f1():
        print("action Etat1")

    def f2():
        print("action Etat2")

    def f3():
        print("action Etat3")

    def f4():
        print("action Etat4")



    s1 = State('Non connecter',f1)
    s2 = State('Verification Id,login',f2)
    s3 = State('Chargement des Datas Users',f3)
    s4 = State("Affichage Erreur D'indentification",f4)
    s5 = State("Inscription",f4)
    s6 = State("Affichage Planning\n(session)",f4)
    s7 = State("Realisation Exo/Lecon",f4)
    s8 = State("Correction",f4)
    s9 = State("Formulaire de gestion des cours",f4)
    s10 = State("Realisation Exo",f4)



    a = Automaton('abc',
    states=(s1, s2, s3, s4,s5,s6,s7,s8,s9 ),
    initial_states=(s2,),
    final_states=(s6, )
    )

    a.add_transition(Transition(s1, s2, 'Demande_de_connection',"extern"))
    a.add_transition(Transition(s2, s4, 'Identification_incorect',"intern"))
    # a.add_transition(Transition(s4, s1, 'ok'))
    # a.add_transition(Transition(s1,s5,'Demande_inscription'))
    # a.add_transition(Transition(s5,s1,'Inscription_faite'))
    #
    # a.add_transition(Transition(s2, s3, 'IdentificationValide'))
    # a.add_transition(Transition(s3, s6, 'chargement_fini'))
    # a.add_transition(Transition(s6,s7,"Demande_realisation_exo"))
    # a.add_transition(Transition(s7,s8,"validation_reponse_exo"))
    # a.add_transition(Transition(s8,s6,"Sortir_correction"))
    # a.add_transition(Transition(s6,s9,"Gestion_cours"))

    ct=0
    while ct<10:
        ct+=1
        print("entre_message")
        message=input()
        print(a.auto(message))

        a.render('zsd.png')
        time.sleep(1)



