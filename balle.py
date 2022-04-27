from random import choice
import application
from palette import compteur,plaquette

class balle:
    liste_angle = [-2,2]
    liste_nb=[1,2]
    def __init__(self, zone):

        self.x_depart=0
        self.y_depart=0

        self.zone = zone
        self.height_zone = self.zone.winfo_reqheight()
        self.width_zone = self.zone.winfo_reqwidth()

        self.d=20

        self.ball = self.zone.create_oval(0,0,self.d,self.d, fill="black")

        self.compteur_left=compteur(3, self.zone, 30, 30)
        self.compteur_right=compteur(3, self.zone, self.zone.winfo_reqwidth() - 30, 30)

        self.x = choice(self.liste_angle)
        self.y = 2
        self.a = 0
        self.bolt=0
        self.zone.move(self.ball,600,350)
        self.mouvement()
    def mouvement(self):
        self.deplacer()
        self.zone.after(5,self.mouvement)

    pos_left = [0, 0, 0, 0]
    pos_right=[0,0,0,0]

    def deplacer(self):

        self.position = self.zone.coords(self.ball)

        if self.position[1] <= 150 or self.position[2] <= self.width_zone or self.position[3] <= self.height_zone or self.position[0] <= 0:
            self.rebondir()


    def rebondir(self):
        if (self.position[1] <= 150 or self.position[3] >= self.height_zone)  :
            self.y = -self.y

        elif (self.position[2] >= self.width_zone or self.position[0] <= 0) :
            self.x = -self.x

            if self.position[2] >= self.width_zone:
                self.compteur_right.remove_point()

            else:
                self.compteur_left.remove_point()

            if self.compteur_right.get_point()=="0" or self.compteur_left.get_point()=="0":
                self.compteur_right.replay_game()


        if self.position[2]==self.pos_right[0]:
            if self.position[1]>self.pos_right[1]-10 and self.position[3]<self.pos_right[3]+10:
                self.x = -self.x

                if self.bolt>=5:
                    if self.x < 0:
                        self.x =-2
                    if self.x > 0:
                        self.x =2

                if -2 <= self.x <= 2 and self.bolt < 3:
                    self.bolt += 1

                if self.bolt >= 3:
                    if self.x < 0:
                        self.x -=1
                    if self.x > 0:
                        self.x +=1

        if self.position[0] == self.pos_left[0]:
            if self.position[1] > self.pos_left[1]-10 and self.position[3] < self.pos_left[3]+10:
                self.x=-self.x

                if self.bolt>=5:
                    if self.x < 0:
                        self.x =-2
                    if self.x > 0:
                        self.x =2

                if -2 <= self.x <= 2 and self.bolt < 3:
                    self.bolt += 1

                if self.bolt >= 3:
                    if self.x < 0:
                        self.x -=1
                    if self.x > 0:
                        self.x +=1


        self.zone.move(self.ball, self.x, self.y)
