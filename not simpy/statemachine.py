import time
import random
class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self, cargo,car):
        try:
            handler = self.handlers[self.startState]
        except:
            print("must call .set_start() before .run()")
        if not self.endStates:
            print("at least one state must be an end_state")
    
        globaltimer = 0
        while True:
            (newState, cargo,car) = handler(cargo,car)
            

            
            globaltimer = globaltimer + 1
            if globaltimer % 5 == 0:
                car = car +  1

            print(newState , cargo, car)
            handler = self.handlers[newState.upper()] 

        # while True:
        #     (newState, cargo) = handler(cargo)
        #     print("reached ", newState,cargo)

        #     if (cargo == "") and (newState.upper() in self.endStates) :
        #         print("True, ended in ", newState)
        #         break

        #     elif (cargo == ""):
        #         print("False, ended ", newState)
        #         break

        #     else:
        #         handler = self.handlers[newState.upper()] 