import matplotlib.pyplot as plt
import numpy as np

a = np.array([0.31,0.36,0.42,0.36,0.43,0.52,0.42,0.52,0.65]).reshape(3,3)

plt.title('image')
plt.imshow(a,interpolation='bilinear',cmap='bone',origin='lower')
plt.colorbar()
plt.show()