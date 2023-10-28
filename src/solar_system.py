from main import Planets, Space, Sun

solar_system = Space(height=900,width=1400)
sun = Sun(solar_system, mass=10_000, velocity=(0,0), position=(0,0))
earth = Planets(solar_system, mass=1, position=(-270, 0), velocity=(0,1))

while True:
    solar_system.calculate_path_with_g(sun, earth)
    solar_system.update_all_bodies()

sun.draw()

import turtle
turtle.done()