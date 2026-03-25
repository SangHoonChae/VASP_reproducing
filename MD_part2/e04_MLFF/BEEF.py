# cat ./e04_MLFF/ML_LOGFILE | grep BEEF > ./e04_MLFF/BEEF.dat

import numpy as np
import matplotlib.pyplot as plt

# 1. Load the data using NumPy (same as before)
# usecols=[1,3] picks the 2nd and 4th columns from the BEEF.dat file
t1, beef = np.loadtxt("BEEF.dat", usecols=[1, 3], unpack=True)

# 2. Create the plot using Matplotlib
plt.figure(figsize=(8, 5))  # Set the size of the window
plt.plot(t1, beef, label='Bayesian Error', color='purple', linewidth=1.5)

# 3. Add labels and title (manually replacing what py4vasp did)
plt.xlabel("Time step")
plt.ylabel("Bayesian error (eV Angst^-1)")
plt.title("Bayesian error estimate of forces (max)")

# 4. Optional: Add a grid and legend to make it easier to read
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.savefig("BEEF_plot.png")
# 5. Show the plot
plt.show()
