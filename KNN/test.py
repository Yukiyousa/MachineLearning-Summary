import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,3*np.pi,0.1)
y = np.sin(x)
plt.title("Sinx's form")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y,color="red",label="sine")
plt.show()