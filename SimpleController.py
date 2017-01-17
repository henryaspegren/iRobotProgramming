from __future__ import print_function
import time
from Tkinter import *
from breezycreate2 import Robot

class SimpleController(object):

    def __init__(self):

        # YOUR CODE HERE 
        #
        # - create a robot and store it as an instance variable
        # - create instance variables for the different parameters we want to keep track of
        # 

        # this sets up the GUI
        self.master = Tk()
        self.main_frame = Frame(self.master, background="bisque")
        self.main_frame.pack(side="top", fill="both", expand=True)
        self.top_frame = Frame(self.main_frame, background="bisque")
        self.bottom_frame = Frame(self.main_frame, background="bisque")
        self.top_frame.pack(side="top", fill="both", expand=True)
        self.bottom_frame.pack(side="bottom", fill="both", expand=True)
        self.bottom_left = Frame(self.bottom_frame, background="bisque")
        self.bottom_right = Frame(self.bottom_frame, background="bisque")
        self.bottom_left.pack(side="left", fill="both", expand=True)
        self.bottom_right.pack(side="right", fill="both", expand=True)
        self.photo = PhotoImage(file="roomba.gif").subsample(20, 20)
        self.canvas = Canvas(self.top_frame, width=500, height=500)
        self.canvas.pack()
        self.robot_id = self.canvas.create_image(250,250, image=self.photo)
        self.position_var = StringVar()
        self.position_label = Label(self.bottom_left, textvariable=self.position_var, font=("Helvetica", 36))
        self.position_label.pack()
        self.position_var.set("Position\n x: 250\ny: 250")
        self.angle_var = StringVar()
        self.angle_label = Label(self.bottom_left, textvariable=self.angle_var, font=("Helvetica", 48))
        self.angle_label.pack()
        self.angle_var.set("Angle: 0")
        self.speed = Scale(self.bottom_right, from_=0, to=500, orient=HORIZONTAL, 
            length=500, command=self.set_speed, label="Speed")
        self.speed.pack()
        self.move_forward = Button(self.bottom_right, text="Forward", command=self.move_forward, padx=10, pady=10)
        self.move_backward = Button(self.bottom_right, text="Backward", command=self.move_backward, padx=10, pady=10)
        self.move_turn_right= Button(self.bottom_right, text="Turn Right", command=self.turn_right, padx=10, pady=10)
        self.move_turn_left= Button(self.bottom_right, text="Turn Left", command=self.turn_left, padx=10, pady=10)
        self.move_forward.pack(fill="x")
        self.move_backward.pack(fill="x")
        self.move_turn_right.pack(fill="x")
        self.move_turn_left.pack(fill="x")

        self.master.bind("<KeyPress-Left>", lambda event: self.move_forward_cmd() )
        self.master.bind("<KeyRelease-Left>", lambda event: print('released') )
        mainloop()


    def move_forward(self):
        return None

    def move_forward_cmd(self):
        print('here')

    def move_backward(self):
        # your code here
        #
        #
        return None

    def turn_left(self):
        # your code here
        # 
        #
        return None

    def turn_right(self):
        # your code here
        #
        #
        return None


    def set_speed(self, velocity):
        # your code here
        #
        #


        # needed to prevent from sending too many updates in a row
        time.sleep(0.1)


# create a controller 
SimpleController()


