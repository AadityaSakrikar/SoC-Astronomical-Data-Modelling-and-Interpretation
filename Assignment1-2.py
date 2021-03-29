import numpy as np
import matplotlib.pyplot as plt
def roll_dice(n):
    return [(np.random.randint(1, 7)**2 + np.random.randint(1, 7)**2) for i in range(n)] 

dices = roll_dice(100000)
plt.hist(dices, bins = 200,density=True)
plt.xlabel('Sum of squares of numbers on the die')
plt.ylabel('Probability')
