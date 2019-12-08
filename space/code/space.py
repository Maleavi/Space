import math
import numpy as np

def gravity(posistion, mass = 1):
    grav = -posistion * mass
    sum = 0
    for i in grav:
        sum = sum + (i * i)

    sum = math.sqrt(sum)
    return (grav / (sum * sum * sum))
    
