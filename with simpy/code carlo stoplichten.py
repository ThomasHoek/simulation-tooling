import simpy
import random


class TrafficLight():
    def __init__(self, state="red", trafficflow=7,time = 0):
        self.queue = 0
        self.state = state
        self.trafficFlow = trafficflow
        self.seconds_passed = time

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_seconds_passed(self,time):
        self.seconds_passed = time	
        

    def add_car_to_queue(self,trafficflow):
        ''''chance is de kans dat er een nieuwe auto komt aanrijden.
         Amount of cars is de huide aantal autos, daarbij komt als de kans 1 is een auto bij.'''
        if (random.randint(1,trafficflow) == 1):
            self.queue = self.queue + 1
        

    def removecar(self,amount):
        '''De secondsPassed is de aantal seconden dat het stoplicht op groen staat.
            Als het stoplicht minimaal 4 seconden op groen staat dan gaat er elke 2 seconden een auto weg.
            Als het aantal negatief wordt dan wordt het 0 gemaakt.'''

        if (self.seconds_passed > 4) and (self.seconds_passed % 2 == 0):
            amount = amount - 1
        if (amount < 0):
            amount = 0
        return amount


class TrafficlightSystem():
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())  # om run aan te roepen.

    def run(self):
        trafficlight_0 = TrafficLight("red")
        trafficlight_1 = TrafficLight("green")
        print('System starts at {}'.format(env.now))
        print("trafficlight 0 turns {} at {}".format(trafficlight_0.get_state(), env.now))
        print("trafficlight 1 turns {} at {}".format(trafficlight_1.get_state(), env.now))
        while True:
            yield env.timeout(30)
            trafficlight_1.set_state("red")
            print("trafficlight 1 turns {} at {}".format(trafficlight_1.get_state(), env.now))
            yield env.timeout(3)
            trafficlight_0.set_state("green")
            print("trafficlight 0 turns {} at {}".format(trafficlight_0.get_state(), env.now))
            yield env.timeout(30)
            trafficlight_0.set_state("red")
            print("trafficlight 0 turns {} at {}".format(trafficlight_0.get_state(), env.now))
            yield env.timeout(3)
            trafficlight_1.set_state("green")
            print("trafficlight 1 turns {} at {}".format(trafficlight_1.get_state(), env.now))


env = simpy.Environment()
TLS = TrafficlightSystem(env)
env.run(361)