import simpy
import random
import matplotlib.pyplot as plt


class Trafficlight():
    def __init__(self, env,chance_car = 7):
        self.env = env
        self.amountcars = 0
        self.chance_car = chance_car
        self.action = env.process(self.run())
        self.cars_list = []

    def run(self):
        print('System starts at %d' % self.env.now)
        while True:
            yield self.env.process(self.red(30))
            yield self.env.process(self.green(30))
            

    def green(self, duration):
        print('TrafficLight start green at %d' % self.env.now, "amount of cars: ", self.amountcars)

        for i in range(0,duration):
            if (random.randint(1,self.chance_car) == 1):
                self.env.process(self.addcar(i))
            self.env.process(self.removecar(i))
            # print("amount of cars: ", self.amountcars)
            self.cars_list.append(self.amountcars)
            yield self.env.timeout(1)        

        print('TrafficLight end green at %d' % self.env.now, "amount of cars: ", self.amountcars)
        yield self.env.timeout(0)  


    def red(self, duration):
        print('TrafficLight start red at %d' % self.env.now, "amount of cars: ", self.amountcars)
        for i in range(0,duration):
            if (random.randint(1,self.chance_car) == 1):
                self.env.process(self.addcar(i))
            self.cars_list.append(self.amountcars)
            # print("amount of cars: ", self.amountcars)
            yield self.env.timeout(1)  

        print('TrafficLight end red at %d' % self.env.now, "amount of cars: ", self.amountcars)
        yield self.env.timeout(0)  
        

    def addcar(self, duration):
        self.amountcars = self.amountcars + 1
        yield self.env.timeout(0)

    def removecar(self, duration):
        if (duration > 4) and (duration % 2 == 0):
            self.amountcars = self.amountcars - 1
        
        if (self.amountcars < 0):
            self.amountcars = 0

        yield self.env.timeout(0)

    

env = simpy.Environment()
trafficLight = Trafficlight(env,4)
env.run(361)

plt.plot(trafficLight.cars_list)
plt.show()

