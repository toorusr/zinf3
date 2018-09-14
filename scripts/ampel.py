# Traficcrossing scene

'''
Szenario:
    Es gibt zwei Objekte, welche sich auf eine Kreuzung zubewegen. An dieser Kreuzung gibt es eine Ampelschaltung nach welcher die Objekte sich über die Kreuzung bewegen.
    Um eine Ausgabe zu simulieren wird hier das Pseudomodul 'street' importiert!
'''

import street
import time

canvas = street.init(width=1920, heigth=1080)
canvas.background(scene="pretty_street")
canvas.title("Trafic light simulation")

class Crossing:
    def __init__(self, start_value):
        self.traf0 = canvas.create.traficlight(x=500, y=300)
        # Creating the second trafic light traf1
        self.traf1 = canvas.create.traficlight(x=300, y=500)
        # Starting the loop
        self.loop(start_value)

    def change(self, value, trafic_light):
        values = {"green": 0, "yellow": 1, "red": 2}
        trafic_lights = {"traf0": 0, "traf1": 1}

        if value in values and trafic_light in trafic_lights:
            pass


    def get(self):
        pass

    def loop(self):
        pass

    def graphics(self):
