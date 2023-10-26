from main import Space, Sun

solar_system = Space(height=900,width=1400)
sun = Sun(solar_system, mass=10_000, velocity=(90,1))

while True:
    solar_system.update_all_bodies()

sun.draw()

import turtle
turtle.done()