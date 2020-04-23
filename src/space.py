import math
import numpy as np

class space_object(object):
    def __init__(self, mass, position = np.array([0.0, 0.0]), velocity = np.array([0.0, 0.0])):
        self.mass = mass
        self.pos = position
        self.vel = velocity

    def grav(self, pos):
        rtn = (self.pos-pos) 

        return (rtn * self.mass) / (math.sqrt(rtn[0]**2 + rtn[1]**2)**3)

    def move(self, act):
        self.pos = self.pos + self.vel * act

    def accelerate(self, force, act):
        self.vel = self.vel + (force * act / self.mass)


#def gravity(posistion, mass = 1):
#    grav = -posistion * mass
#    sum = 0
#    for i in grav:
#        sum = sum + (i * i)
#
#    sum = math.sqrt(sum)
#    return (grav / (sum * sum * sum))
#
#def array_reader(array_thing):
#    #numpy doing shenenigans, so just made a generator for that
#    for o in array_thing:
#        yield o
#
