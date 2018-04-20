import tkinter as Tk
from functools import partial


class VueConnection:

    def __init__(self):
        class LoginDialog(Tk.Toplevel):
            def __init__(self, parent,a):
                super().__init__(parent)
                self.title("Fenêtre Modale")
                self.parent=parent
                self.controleur=a
                # ---------------------------------------
                Tk.Label(self, text="Login : ").pack()
                self.entry_login = Tk.Entry(self)
                self.entry_login.insert(0, "defaultlogin")
                self.entry_login.pack()
                # ---------------------------------------
                Tk.Label(self, text="Clé : ").pack()
                self.entry_pass = Tk.Entry(self, show='*')
                self.entry_pass.insert(0, "defaultpass")
                self.entry_pass.pack()
                # ---------------------------------------
                Tk.Button(self, text="Connexion", command=self.connect).pack()

            def connect(self):
                login = self.entry_login.get().strip()
                key = self.entry_pass.get().strip()

                self.controleur.set_login(login)
                self.controleur.set_mdp(key)

                self.destroy()
                self.parent.destroy()

        def connect(parent,a):
            """ Ouvre une fenêtre modale """
            result = LoginDialog(parent,a)
            result.transient(parent)
            result.grab_set()
            parent.wait_window(result)

        class Fenetre(Tk.Frame):
            def __init__(self, parent,a):
                super().__init__(parent)
                Frame1 = Tk.Frame(self, borderwidth=2, relief=Tk.GROOVE)

                self.master.title("Fenêtre principale")
                self.pack(fill='both', expand=1)
                bouton_new = Tk.Button(Frame1, width=10, height=1, text="Connexion", command=partial(connect,parent,a))
                bouton_new.pack()

                Frame1.pack(side=Tk.LEFT, padx=300, pady=300)

        class Connect:
            def __init__(self):
                self.login=None
                self.mdp=None
            def set_login(self,value):
                self.login=value
            def set_mdp(self,value):
                self.mdp=value

        info_conct=Connect()
        a = Tk.Tk()
        Fenetre(a,info_conct)
        a.mainloop()


        self.login=info_conct.login
        self.mdp=info_conct.mdp

