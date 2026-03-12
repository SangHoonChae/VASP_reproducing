# Compute and interpret the pair-correlation function.

# First, we should refine the PCDAT files.
cp PCDAT PCDAT.180fs
cp ../e01_*/PCDAT PCDAT.90fs

# Run pair_correlation.sh on the PCDAT.* files.
bash pair_correlation.sh .90fs
bash pair_correlation.sh .180fs

# Plot the pair-correlation function and save it as a .png file.
gnuplot pair_correlation.gp
