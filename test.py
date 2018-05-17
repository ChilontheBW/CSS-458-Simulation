from tkinter import *
import time
import numpy as np

WIDTH = 800
HEIGHT = 300
SIZE = 60
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="green")
canvas.pack()
canvas.create_line(0,(HEIGHT/2), WIDTH,(HEIGHT/2), width="120", fill="grey")
canvas.create_line(0,(HEIGHT/2)+60, WIDTH,(HEIGHT/2)+60, width="3", fill="white")
canvas.create_line(0,(HEIGHT/2)-60, WIDTH,(HEIGHT/2)-60, width="3", fill="white")
canvas.create_line(0,(HEIGHT/2)+30, WIDTH,(HEIGHT/2)+30, width="1", fill="white")
canvas.create_line(0,(HEIGHT/2)-30, WIDTH,(HEIGHT/2)-30, width="1", fill="white")
canvas.create_line(0,(HEIGHT/2), WIDTH,(HEIGHT/2), width="1", fill="white")
canvas.create_line
color = 'black'

"""
class Ball:
    def __init__(self):
        self.shape = canvas.create_oval(0, 0, SIZE, SIZE, fill=color)
        self.speedx = 9 # changed from 3 to 9
        self.speedy = 9 # changed from 3 to 9
        self.active = True
        self.move_active()
"""
class Car:
    def __init__(self, lane, speed):
        self.shape = canvas.create_rectangle(0, 7+(HEIGHT/2) + ( (lane - 3) *30), SIZE/2, 7+SIZE/4+(HEIGHT/2) + ( (lane - 3) *30), fill=color)
        self.speedx = speed
        self.speedy = 0
        self.active = True
        self.move_active()


    def ball_update(self):
        canvas.move(self.shape, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        """
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1

        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1
            """

    def move_active(self):
        if self.active:
            self.ball_update()
            tk.after(40, self.move_active) # changed from 10ms to 30ms
def make_car():
        lane = np.random.randint(1,5)
        speed = np.random.uniform(1,5)
        car = Car(lane, speed)
        tk.after(1000, make_car)    
    

car1 = Car(1, 5)
car2 = Car(2, 2)
car3 = Car(3, 3)
car4 = Car(4, 4)
make_car()




tk.mainloop()