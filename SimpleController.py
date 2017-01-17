import time
from Tkinter import *
from breezycreate2 import Robot
import os, time
from Tkinter import *

class SimpleController(object):

    def __init__(self):

        # YOUR CODE HERE 
        #
        # - create a robot and store it as an instance variable
        # - create instance variables for the different parameters we want to keep track of
        # 
        self.x = 250
        self.y = 250
        self.angle = 0
        self.bot = Robot()
        self.bot.robot.full()

        # this sets up the GUI
        self.master = Tk()
        self.main_frame = Frame(self.master, background="mistyrose")
        self.main_frame.pack(side="top", fill="both", expand=True)
        self.top_frame = Frame(self.main_frame, background="mistyrose")
        self.bottom_frame = Frame(self.main_frame, background="mistyrose")
        self.top_frame.pack(side="top", fill="both", expand=True)
        self.bottom_frame.pack(side="bottom", fill="both", expand=True)
        self.bottom_left = Frame(self.bottom_frame, background="mistyrose")
        self.bottom_right = Frame(self.bottom_frame, background="mistyrose")
        self.bottom_left.pack(side="left", fill="both", expand=True)
        self.bottom_right.pack(side="right", fill="both", expand=True)
        self.photo = PhotoImage(file="roomba.gif").subsample(20, 20)
        self.canvas = Canvas(self.top_frame, width=500, height=500)
        self.canvas.pack()
        self.robot_id = self.canvas.create_image(250,250, image=self.photo)
        self.position_var = StringVar()
        self.position_label = Label(self.bottom_left, textvariable=self.position_var, font=("Helvetica", 36))
        self.position_label.pack()
        self.position_var.set('Position\n x:'+ str(self.x)+'\ny:' + str(self.y))
        self.angle_var = StringVar()
        self.angle_label = Label(self.bottom_left, textvariable=self.angle_var, font=("Helvetica", 48))
        self.angle_label.pack()
        self.angle_var.set("Angle: 000")
        self.speed = Scale(self.bottom_right, from_=0, to=500, orient=HORIZONTAL, 
            length=500, command=self.set_speed, label="Speed")
        self.speed.pack()
        self.move_forward = Button(self.bottom_right, text="Forward", command=self.move_forward_cmd, padx=10, pady=10)
        self.move_backward = Button(self.bottom_right, text="Backward", command=self.move_backward_cmd, padx=10, pady=10)
        self.move_turn_right= Button(self.bottom_right, text="Turn Right", command=self.turn_right, padx=10, pady=10)
        self.move_turn_left= Button(self.bottom_right, text="Turn Left", command=self.turn_left, padx=10, pady=10)
        self.move_forward.pack(fill="x")
        self.move_backward.pack(fill="x")
        self.move_turn_right.pack(fill="x")
        self.move_turn_left.pack(fill="x")

          

        # self.master.bind('<Left>', lambda event: self.turn_left())
        # self.master.bind('<Right>', lambda event: self.turn_right())
        # self.master.bind('<Up>', lambda event: self.move_forward_cmd())
        # self.master.bind('<Down>', lambda event: self.move_backward_cmd())

        self.main_frame.bind("<KeyPress-Up>", self.move_forward_cmd)
        self.main_frame.bind("<KeyRelease-Up>", self.move_stop)
        self.main_frame.bind("<KeyPress-Down>", self.move_backward_cmd)
        self.main_frame.bind("<KeyRelease-Down>", self.move_stop)
        self.main_frame.bind("<KeyPress-Right>", self.turn_right)
        self.main_frame.bind("<KeyRelease-Right>", self.turn_stop)
        self.main_frame.bind("<KeyPress-Left>", self.turn_left)
        self.main_frame.bind("<KeyRelease-Left>", self.turn_stop)

        self.main_frame.pack()
        self.main_frame.focus_set()

        mainloop()

    def move_forward_cmd(self, event = None):
        print "move forward button pushed"
        self.bot.setForwardSpeed(self.speed)
        if self.angle == 90:
            self.x = self.x + self.speed
            self.canvas.move(self.robot_id, self.speed, 0)
            self.canvas.create_line(self.x - self.speed, self.y, self.x, self.y, fill="red")
        elif self.angle == 180:
            self.y = self.y + self.speed
            self.canvas.move(self.robot_id, 0, self.speed)
            self.canvas.create_line(self.x, self.y - self.speed, self.x, self.y, fill="red")
        elif self.angle == 270:
            self.x = self.x - self.speed
            self.canvas.move(self.robot_id, - self.speed, 0)
            self.canvas.create_line(self.x + self.speed, self.y, self.x, self.y, fill="red")
        else : 
            self.y = self.y - self.speed
            self.canvas.move(self.robot_id, 0, - self.speed)
            self.canvas.create_line(self.x , self.y + self.speed, self.x, self.y, fill="red")
        
        self.position_var.set('Position\n x:'+ str(self.x)+'\ny:' + str(self.y))
        return None

    def move_backward_cmd(self, event = None):
        print "move backward button pushed"
        self.bot.setForwardSpeed(-self.speed)
        if self.angle == 90:
            self.x = self.x - self.speed
            self.canvas.move(self.robot_id, - self.speed, 0)
            self.canvas.create_line(self.x + self.speed, self.y, self.x, self.y, fill="blue")
        elif self.angle == 180:
            self.y = self.y - self.speed
            self.canvas.move(self.robot_id, 0, - self.speed)
            self.canvas.create_line(self.x, self.y + self.speed, self.x, self.y, fill="blue")
        elif self.angle == 270:
            self.x = self.x + self.speed
            self.canvas.move(self.robot_id, self.speed, 0)
            self.canvas.create_line(self.x - self.speed, self.y, self.x, self.y, fill="blue")
        else:
            self.y = self.y + self.speed
            self.canvas.move(self.robot_id, 0, self.speed)
            self.canvas.create_line(self.x, self.y - self.speed, self.x, self.y, fill="blue")

        self.position_var.set('Position\n x:'+ str(self.x)+'\ny:' + str(self.y))
        return None

    def move_stop(self, event = None):
        self.bot.setForwardSpeed(0)
        return None

    def turn_left(self, event = None):
        self.bot.setTurnSpeed(200)
        self.angle = (self.angle - 90) % 360
        angle_string = str(self.angle)
        while len(angle_string) < 3:
            angle_string = '0' + angle_string
        string_to_update = "Angle: " + angle_string
        self.angle_var.set(string_to_update)
        print "turn right button pushed"
        return None

    def turn_right(self,event=None):
        self.bot.setTurnSpeed(-200)
        self.angle =  (self.angle + 90) % 360
        angle_string = str(self.angle)
        while len(angle_string) < 3:
            angle_string = '0' + angle_string
        self.angle_var.set("Angle: " + angle_string)
        print "turn right button pushed"
        return None

    def turn_stop(self, event = None):
        self.bot.setTurnSpeed(0)
        return None

    def set_speed(self, velocity):
        self.speed = int(velocity)
        print self.speed


# create a controller 
SimpleController()
