# cat ML_LOGFILE | grep ERR > ERR.dat

import numpy as np
import matplotlib.pyplot as plt

# Load the Error data
t2, inerr = np.loadtxt("ERR.dat", usecols=[1, 2], unpack=True)

plt.figure(figsize=(8, 5))
plt.plot(t2, inerr, color='red', label='Force RMSE')

plt.xlabel("Time step")
plt.ylabel("RMSE (eV/Å)")
plt.title("Root Mean Squared Error of Forces")
plt.grid(True, alpha=0.3)
plt.legend()
plt.savefig("ERR_plot.png")
plt.show()
