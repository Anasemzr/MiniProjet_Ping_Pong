from tkinter import Tk, Canvas, PhotoImage, Button
from balle import balle
from palette import compteur, plaquette


class game_window(Tk):
    drapeau=False
    def __init__(self):
        Tk.__init__(self)
        self.geometry("800x600")
        self.zoneJ=canvas(800, 600, "white")
        self.bind("<Key>", self.touche)
        self.replay()

    liste_car_1 = ["Start"]
    liste_car_2 = ["Start"]

    def touche(self, event):
        if event.keysym == "Up" or event.keysym == "Down":
            self.liste_car_1.append(event.keysym)
        if event.keysym == "z" or event.keysym == "s":
            self.liste_car_2.append(event.keysym)

    def replay(self):
        if game_window.drapeau:
            self.zoneJ.destroy()
            self.zoneJ=canvas(800, 600, "white")
            game_window.drapeau=None
            game_window.liste_car_2=["Start"]
            game_window.liste_car_1=["Start"]

        self.after(100,self.replay)


class canvas(Canvas):

    def __init__(self, width, height, bg):
        Canvas.__init__(self, width=width, height=height, bg=bg)
        self.w = width
        self.playgame=PhotoImage(file="img_play.png").subsample(5, 5)
        self.button1 = Button(self, image=self.playgame, command=self.start_game,bg="white",bord=0)
        self.play = self.create_window(self.w / 2, height/2+160, window=self.button1)


        self.pict = PhotoImage(file="pong.png").subsample(3,3)
        self.pics=self.create_image(self.w / 2, height/2-80, image=self.pict)

        self.txt=self.create_text(self.w/2,40,text="PONG GAME",font=('Arial',30))

        self.grid(row=0, column=0)

    def start_game(self):
        self.delete(self.txt)
        self.delete(self.pics)
        self.pict = PhotoImage(file="pong.png").subsample(5, 6)
        self.create_image(self.w / 2, 40, image=self.pict),

        self.line = PhotoImage(file="minus.png").subsample(1, 30)
        self.create_image(400, 150, image=self.line)

        self.dashed = PhotoImage(file="dashed.png")
        self.create_image(self.winfo_reqwidth() / 2, 360, image=self.dashed)

        self.balle=balle(self)
        plaquette(self, 50, self.winfo_reqheight() / 2, "z", "s", 1)
        plaquette(self, self.winfo_reqwidth() - 50, self.winfo_reqheight() / 2, "Up", "Down", 2)
        canvas.delete(self, self.play)


