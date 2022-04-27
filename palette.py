import application
import balle

class plaquette:
    def __init__(self,zone,w,h,touche1,touche2,nb):
        self.zone=zone
        self.plaquette=self.zone.create_rectangle(w,h,w+15,h+90,fill="red")
        self.touche1,self.touche2,self.nb=touche1,touche2,nb
        self.compteur_u = 0
        self.compteur_d = 0
        self.deplacer()


    y=0
    def deplacer(self):
        #self.y=0
        self.pos=self.zone.coords(self.plaquette)
        if self.nb==1:
            self.direction=application.game_window.liste_car_2
            balle.balle.pos_left = self.pos
        elif self.nb==2:
            self.direction = application.game_window.liste_car_1
            balle.balle.pos_right = self.pos

        self.limite_U=150
        self.limite_D=self.zone.winfo_reqheight()-30

        if self.direction[-1]==self.touche1:
            self.compteur_d=0
            if self.direction[-2]==self.touche1:
                self.compteur_u-=1
            if self.limite_U<int(self.pos[1]):
                self.y=-6+self.compteur_u
            else:
                self.compteur_u =0
                self.y = 0


        if self.direction[-1]==self.touche2:
            self.compteur_u = 0
            if self.direction[-2]==self.touche2:
                self.compteur_d += 1
            if self.limite_D>int(self.pos[3]):
                self.y=6+self.compteur_d
            else:
                self.compteur_d+=1
                self.y=0

        self.zone.move(self.plaquette,0,self.y)
        self.zone.after(40, self.deplacer)






class compteur:
    nb_point=-5

    def __init__(self,nb,zone,w,h):
        self.nb_point=nb
        self.zone=zone
        self.a=self.zone.create_text(w, h, text=self.get_point(), font=("Arial", 30))

    def remove_point(self):
        self.nb_point-=1
        self.zone.itemconfig(self.a,text=str(self.nb_point))

    def get_point(self):
        return str(self.nb_point)

    def replay_game(self):

        application.game_window.drapeau = True



