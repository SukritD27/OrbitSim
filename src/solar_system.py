from src.main import Space, Sun

solar_system = Space(height=9000,width=14000)
sun = Sun(solar_system, mass=10_0000)
sun.draw()

import turtle
turtle.done()