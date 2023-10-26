import math
import turtle

class CosmicBodies(turtle.Turtle):
    min_display_size = 20
    # used to convert mass to display size
    log_base = 1.1


    def __init__(self, space, mass, position=(0,0), velocity=(0,0),):
        super().__init__()
        self.mass = mass
        # self.forward(100)
        self.setposition(position)
        
        self.velocity = velocity

        self.display_size = max(math.log(self.mass, self.log_base), self.min_display_size)


        # so that the bodies do not make lines while moving
        self.penup()
        # hides the line drawer
        self.hideturtle()
        space.add_body(self)

    def draw(self):
        self.clear()
        self.dot(self.display_size)
        # space.update()
        # space.mainloop()
        # self.forward(100)
    
    def move(self):
        self.setx(self.xcor() + self.velocity[0])
        self.sety(self.ycor() + self.velocity[1])

class Sun(CosmicBodies):
    def __init__(self, space, mass, position=(0,0), velocity=(0,0)):
        super().__init__(space, mass, position, velocity)
        self.color('orange')


# class Planets(CosmicBodies):

# Used to create the screen
class Space:
    def __init__(self, height, width):
        self.space = turtle.Screen()
        # tracer(0) turns the screen updates off
        # stops the screen from blinking
        self.space.tracer(0)
        self.space.setup(width, height)
        self.space.bgcolor('black')
        # self.space.title('Space')
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        self.bodies.remove(body)

    def update_all_bodies(self):
        for body in self.bodies:
            body.move()
            body.draw()
        self.space.update()

