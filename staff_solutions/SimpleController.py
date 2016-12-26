import time, math
from Tkinter import *
from breezycreate2 import Robot

class SimpleController(object):

    def __init__(self):

        # this creates a robot
        # self.bot = Robot()

        # we want to keep track of these parameters

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
        self.position_var.set("Position\n x: NA\ny: NA")
        self.angle_var = StringVar()
        self.angle_label = Label(self.bottom_left, textvariable=self.angle_var, font=("Helvetica", 48))
        self.angle_label.pack()
        self.angle_var.set("Angle: NA")
        self.velocity = Scale(self.bottom_right, from_=-500, to=500, orient=HORIZONTAL, 
            length=500, command=self.set_velocity, label="Velocity of Robot")
        self.radius = Scale(self.bottom_right, from_=-2000, to=2000, orient=HORIZONTAL, 
            length=500, command=self.set_radius, label="Radius of Robot")
        self.velocity.pack()
        self.radius.pack()
        self.move_right_button = Button(self.bottom_right, text="Right", command=self.move_right, padx=10, pady=10)
        self.move_left_button = Button(self.bottom_right, text="Left", command=self.move_left, padx=10, pady=10)
        self.move_up_button = Button(self.bottom_right, text="Up", command=self.move_up, padx=10, pady=10)
        self.move_down_button = Button(self.bottom_right, text="Down", command=self.move_down, padx=10, pady=10)
        self.move_right_button.pack()
        self.move_left_button.pack()
        self.move_up_button.pack()
        self.move_down_button.pack()
        mainloop()

    def move_right(self):
        (x, y) = self.canvas.coords(self.robot_id)
        self.canvas.create_line(x, y, x+50, y, fill="red" )
        self.canvas.move(self.robot_id, 50, 0)
        self.position_var.set(str(self.canvas.coords(self.robot_id)))
        print "move right!"

    def move_left(self):
        (x, y) = self.canvas.coords(self.robot_id)
        self.canvas.create_line(x, y, x-50, y, fill="red" )
        self.canvas.move(self.robot_id, -50, 0)
        self.position_var.set(str(self.canvas.coords(self.robot_id)))
        print "move left!"

    def move_up(self):
        (x, y) = self.canvas.coords(self.robot_id)
        self.canvas.create_line(x, y, x, y-50, fill="red" )
        self.canvas.move(self.robot_id, 0, -50)
        self.position_var.set(str(self.canvas.coords(self.robot_id)))
        print "move up!"

    def move_down(self):
        (x, y) = self.canvas.coords(self.robot_id)
        self.canvas.create_line(x, y, x, y+50, fill="red" )
        self.canvas.move(self.robot_id, 0, 50)
        self.position_var.set(str(self.canvas.coords(self.robot_id)))
        print "move down!"

    def set_velocity(self, velocity):
        print "UPDATED VELOCITY IS: "+str(velocity)
        # needed to prevent from sending too many updates in a row
        time.sleep(0.1)

    def set_radius(self, radius):
        print "UPDATED RADIUS IS: "+str(radius)
        # slow updates
        time.sleep(0.1)


# create a controller 
SimpleController()


