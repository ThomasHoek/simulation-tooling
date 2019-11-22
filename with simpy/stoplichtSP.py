import simpy
import random
import matplotlib.pyplot as plt


# class trafficsystem():
    # def __init__(self, startingclass):
        # self.startingclass = startingclass



class Trafficlight():
    def __init__(self, env,chance_car1 = 5,chance_car2 = 4):
        '''Standaard kans dat een auto op weg 1 aankomt is elke 6 seconden, en op weg twee elke 4 seconden'''
        self.env = env
        self.amountcars1 = 0        # start aantal autos op weg 1
        self.amountcars2 = 0        # start aantal autos op weg 2

        self.chance_car1 = chance_car1        # de kans dat er een auto komt aanrijden elke seconde op weg 1. 
        self.chance_car2 = chance_car2        # de kans dat er een auto komt aanrijden elke seconde op weg 2
        # Als de kans 4 is dan: 1/4 -> 25% kans elke seconde. Of ongeveer elke 4 seconden een auto.
        

        self.cars_list1 = []        # een lijst die bij houdt hoeveel autos op weg 1 waren
        self.cars_list2 = []        # een lijst die bij houdt hoeveel autos op weg 1 waren

        self.action = env.process(self.run())           # om run aan te roepen.
        

    def run(self):
        ''' Om de 30 seconden wordt er geswitcht tussen de wegen. Eerst staat weg 1 op groen, daarna weg 2.'''
        print('System starts at %d' % self.env.now)
        while True:
            
            yield self.env.process(self.road1(30))      
            yield self.env.process(self.road2(30))      


    def addcarstolist(self):
        '''Voeg in de lijst de huidige waarde toe aan het einde.'''
        self.cars_list1.append(self.amountcars1)        
        self.cars_list2.append(self.amountcars2)         



    def road1(self, duration):
        '''Als weg 1 op groen gaat, dan staat weg 2 op rood. 
            Elke seconde wordt er in de functie bekeken of er een auto op weg 1 of 2 bijkomt of dat er één wegrijdt.
        '''
        # print('TrafficLight 1 start green at %d' % self.env.now + ", amount of cars:", self.amountcars1)
        # print('TrafficLight 2 start red at %d' % self.env.now + ", amount of cars:", self.amountcars2)
        # print('\n')
        counter = 0
        for second in range(0,duration):
            self.addcarstolist()
            counter = counter + 1            
            self.amountcars2 = self.red(self.chance_car2, self.amountcars2)

            if (second < 3): # na 3 seconden op groen.
                self.amountcars1 = self.red(self.chance_car1, self.amountcars1)
            else:
                self.amountcars1 = self.green(counter,self.chance_car1, self.amountcars1)

            

            yield self.env.timeout(1)
                 
        yield self.env.timeout(0)  


    def road2(self, duration):
        '''Als weg 2 op groen gaat, dan gaat weg 1 op rood. '''
        
        # print('TrafficLight 1 start red at %d' % self.env.now + ", amount of cars:", self.amountcars1)
        # print('TrafficLight 2 start green at %d' % self.env.now + ", amount of cars:", self.amountcars2)
        # print('\n')
        counter = 0
        for second in range(0,duration):
            self.addcarstolist()
            counter = counter + 1
            self.amountcars1 = self.red(self.chance_car1, self.amountcars1)

            if (second > 3):
                self.amountcars2 = self.green(counter,self.chance_car2, self.amountcars2)
            else:
                self.amountcars2 = self.red(self.chance_car2, self.amountcars2)
            

            

            yield self.env.timeout(1)        
        yield self.env.timeout(0)  
    

#  --------------- RED ----------
    def red(self,chance,amountCars):
        ''''chance is de kans dat er een nieuwe auto komt aanrijden.
         Amount of cars is de huide aantal autos, daarbij komt als de kans 1 is een auto bij.'''
        amountCars = self.addcar(chance,amountCars)
        return amountCars
#  --------------- RED ----------


#  --------------- Green ----------
    def green(self,secondsPassed,chance,amountCars):
        '''Als het groen is kan er een auto bijkomen, maar de autos rijden ook weg.'''
        amountCars = self.addcar(chance, amountCars)
        amountCars = self.removecar(secondsPassed,amountCars)
        return amountCars
#  --------------- Green ----------


#  --------------- Add cars ----------
    def addcar(self, chance, amount):        
        ''''chance is de kans dat er een nieuwe auto komt aanrijden.
            Er wordt tegelijk een auto bij gedaan en ervan af gehaald.'''
        if (random.randint(1,chance) == 1):
            return amount + 1
        else:
            return amount

#  --------------- Add cars ----------


#  --------------- Remove cars ----------
    def removecar(self, secondsPassed,amount):
        '''De secondsPassed is de aantal seconden dat het stoplicht op groen staat.
            Als het stoplicht minimaal 4 seconden op groen staat dan gaat er elke 2 seconden een auto weg.
            Als het aantal negatief wordt dan wordt het 0 gemaakt.'''

        if (secondsPassed > 3) and (secondsPassed % 2 == 0):
            amount = amount - 1
        if (amount < 0):
            amount = 0
        return amount
#  --------------- Remove cars ----------
    

env = simpy.Environment()
trafficLight = Trafficlight(env)
env.run(601)


plt.plot(trafficLight.cars_list1)
plt.plot(trafficLight.cars_list2)

plt.show()
