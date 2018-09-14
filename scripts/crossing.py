# Traficcrossing scene

'''
Szenario:
    Es gibt zwei Objekte, welche sich auf eine Kreuzung zubewegen. An dieser Kreuzung gibt es eine Ampelschaltung nach welcher die Objekte sich über die Kreuzung bewegen.
    Um eine Ausgabe zu simulieren wird hier das Pseudomodul 'street' importiert!
'''

import street # pseudomodule Street is the Adapter for the graphics output
from time import sleep # importing the sleep function from time module

def debug(x): # debug output module
    print("[DEBUG]: " + x)

canvas = street.init(width=1920, heigth=1080) # initializing a street canvas with 1920x1080 demensions
canvas.background(scene="pretty_street") # changing the canvas enviroment
canvas.title("Trafic light simulation") # changing the title of the window

class TraficLights:
    # init function: create objects, start loop
    def __init__(self, start_value):
        self.traf0 = canvas.create.traficlight(x=500, y=300) # Creating the car trafic light traf0
        self.traf1 = canvas.create.traficlight(x=300, y=500) # Creating the people trafic light traf1
        self.traf0_state, self.traf1_state = [2, 0] # assign start states

    # change function: change trafic lights visual output
    def change(self, state, trafic_light):
        state_colors = {0: "green", 1: "yellow", 2: "red"} # create set for a index to string conversion
        if state in [0,1] and trafic_light in [0,1]: # check if state and trafic_light have valide values
            if trafic_light == 0: # check if travic_light = 0 -> self.traf0
                self.traf0.state(state_colors[state]) # change visual state of traficlight 0 by getting color name by index
                self.traf0_state = state # change current state var
            else: # else change self.traf1
                self.traf1.state(state_colors[state]) # change visual state of traficlight 1 by getting color name by index
                self.traf1_state = state # change current state var
        else:
            return 1 # return that something went wrong

    # transition function: smooth change of values of traficlights
    def transition():
        pass

    # get function: get current value of traficlight
    def get(self, traf):
        pass

    # start function: traficlight cycle loop
    def start(self):
        self.change(state=self.traf0_state, trafic_light=0) # change visual to start value of car traficlight
        self.change(state=self.traf1_state, trafic_light=1) # change visual to start value of people traficlight
        while True: # starting a infinite loop
            self.transition()

class

traf = TraficLights() # initializing the traficlights
traf.start()
