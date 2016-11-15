import numpy as np
import matplotlib.pyplot as plt

# arange - returns evenly spaces values within the given interval (start,stop,step,dtype)
t = np.arange(0.,5.,0.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()