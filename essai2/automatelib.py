#!/usr/bin/env python
# coding=utf8
import pygraphviz as gv

class State(object):
    '''
        Classe définissant un état
    '''

    def __init__(self, name,f):
        self.name = name
        self.fonction=f

    def __repr__(self):
        return u'<State %s>' % self.name


class Transition(object):
    '''
        Classe définissant une transition
    '''

    def __init__(self, state_from, state_to, labels,type):
        self.state_from = state_from
        self.state_to = state_to
        self.labels = labels
        self.type=type

    def getStateTo(self):
        return self.state_to


    def equals(self,a):
        print(self.labels,a)
        if a==self.labels:
            return True
        else :
            return False

    def __repr__(self):
        return u'<Transition %s -> %s labeled %s>' % (self.state_from,
                                                      self.state_to, ', '.join(self.labels))


class EpsilonTransition(Transition):
    '''
        Classe définissant une Epsilon transition
    '''

    def __init__(self, state_from, state_to):
        self.state_from = state_from
        self.state_to = state_to

    def __repr__(self):
        return u'<EpsilonTransition %s -> %s >' % (self.state_from,
                                                   self.state_to)


class Automaton(object):
    '''
        Classe définissant un Automate Fini A
    '''

    def __init__(self, alphabet, states=(), initial_states=(),
                 final_states=(), transitions=()):

        # L'alphabet Σ de l'automate
        self.alphabet = set(alphabet)

        # Ses états Q (objets State)
        self.states = set(states)

        # Ses états finaux Q_f (objets State)
        self.final_states = set(final_states)

        # Et ses états initiaux Q_0 (objets State)
        self.initial_states = set(initial_states)

        # Et ses transition δ (objets Transision)
        self.transitions = set(transitions)

        if len(self.initial_states) >0:
            self.courant_state=self.initial_states.pop()
            self.initial_states.add(self.courant_state)
        else:
            self.courant_state=None

    def add_state(self, state):
        '''
            Ajouter un état à l'automate.
        '''

        self.states.add(state)

    def add_initial_state(self, state):
        '''
            Ajouter un état initial à l'automate
        '''
        self.courant_state = state
        self.initial_states.add(state)

    def add_final_state(self, state):
        '''
            Ajouter un état final à l'automate
        '''

        self.final_state.add(state)

    def add_transition(self, transition):
        '''
            Ajouter une transition à l'automate
        '''

        self.transitions.add(transition)

    def leave(self, state):
        '''
            Méthode qui retourne toutes les transisions qui
            quittent state
        '''

        return set([tr for tr in self.transitions if tr.state_from is state])

    def auto(self,event):

        if len(self.initial_states)>0:

            if self.courant_state==None:
                self.courant_state=self.initial_states[0]
            Validation=False
            for k in list(self.leave(self.courant_state)):
                if k.labels ==event:
                    Validation=True
                    self.courant_state=k.getStateTo()
            if Validation==True:
                self.__call__()
                return "Transition valide ---> changement d'etat"
            else:
                return "N'est pas une transition valide"

        else:
            return '''Impossible pas d'etat initial'''

    def __call__(self, *args, **kwargs):
        self.courant_state.fonction()

    def solve_epsilons(self, tr):
        '''
            Retourne tous les états joints à une série d'epsilon transitions
        '''

        states_to_travel = set((tr.state_to,))
        states_travelled = set()
        tr_travelled = set((tr,))

        while states_to_travel:
            # On récupère un état que l'on a pas encore traité
            state = states_to_travel.pop()

            # Par rapport à cet état, on récupère toutes les
            # epsilons transition qui partent de cet état
            tr_to_travel = set(
                [tr for tr in self.leave(states_travelled) if type(tr) is EpsilonTransition and tr not in tr_travelled])
            states_to_travel |= set([tr.state_to for tr in tr_to_travel]) - states_travelled
            tr_travelled |= tr_to_travel
            states_travelled.add(state)
        return states_travelled

    def acceptance(self, word):
        states = self.initial_states

        for f in word:
            next_states = set()
            for s in states:
                for tr in self.leave(s):
                    if type(tr) == Transition and f == tr.labels:
                        next_states.add(tr.state_to)
                    elif type(tr) == EpsilonTransition:
                        next_states |= self.solve_epsilons(tr)

            states = next_states
            print(f, ' --> ', states)
        # En Python, & est l'opérateur d'intersection des ensembles

        return bool(states & self.final_states)

    def render(self, filename):
        '''
            Générer une image de l'automate
        '''

        try:
            import pygraphviz as gv
        except ImportError:
            print
            'Il faut installer pygraphviz pour utiliser les méthodes de'
            print
            'visualisation de l\'automate : easy_install pygraphviz'
        else:
            graph = gv.AGraph(directed=True)  # Un automate est un graphe dirigé

            l=[n.name for n in self.states]
            l.sort()
            graph.add_nodes_from(l)

            #graph.graph_attr['rankdir'] = 'LR';
            for st in self.final_states:
                n = graph.get_node(st.name)
                n.attr['shape'] = 'doublecircle'

            for st in self.initial_states:
                n = graph.get_node(st.name)
                n.attr['style'] = 'filled'
                n.attr['fillcolor'] = '#DDDDDD'

            for tr in self.transitions:
                if type(tr) is Transition:
                    if tr.type=="intern":
                        graph.add_edge(tr.state_from.name, tr.state_to.name, label=tr.labels,color='forestgreen',fontcolor='forestgreen')
                    elif tr.type=="extern":
                        graph.add_edge(tr.state_from.name, tr.state_to.name, label=tr.labels,color='red',fontcolor='red')
                    else:
                        graph.add_edge(tr.state_from.name, tr.state_to.name, label=tr.labels)
                elif type(tr) is EpsilonTransition:
                    graph.add_edge(tr.state_from.name, tr.state_to.name)

            n = graph.get_node(self.courant_state.name)
            print(self.courant_state)
            n.attr['style'] = 'filled'
            n.attr['fillcolor'] = 'tomato'
            print(n)

            graph.draw(filename, prog='dot')

    def __repr__(self):
        return u'<Automaton with %s states and %s transition>' % (
            len(self.states),
            len(self.transitions)
        )