# bash volume_energy_MLFF.sh > volume_energy_MLFF.dat
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the datasets
vol_dft, eng_dft = np.loadtxt("volume_energy_DFT.dat", unpack=True)
vol_mlff, eng_mlff = np.loadtxt("volume_energy_MLFF.dat", unpack=True)

# 2. Initialize the plot
plt.figure(figsize=(8, 6))

# 3. Plot the data
# Using a line for MLFF and markers for DFT is a common convention
plt.plot(vol_dft, eng_dft, '-o', label='DFT (Reference)', color='purple', markersize=6)
plt.plot(vol_mlff, eng_mlff, '-o', label='MLFF', color='cyan', linewidth=2)

# 4. Add labels and formatting
plt.xlabel("Volume (Å³)")
plt.ylabel("Total energy (eV)")
plt.title("Comparison: DFT vs. Machine Learning Force Field")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# 5. Show or save
plt.savefig("volume_energy_comparison.png", dpi=300)  # Save the figure with high resolution
plt.show()
