# Compute and interpret the pair-correlation function.

# First, we should refine the PCDAT files.
cp PCDAT PCDAT.180fs
cp ../e01_*/PCDAT PCDAT.90fs

# Run pair_correlation.sh on the PCDAT.* files.
bash pair_correlation.sh .90fs
bash pair_correlation.sh .180fs

# Plot the pair-correlation function and save it as a .png file.
gnuplot pair_correlation.gp

-------------------------------------------------------------------

notes)

g(r) at short distance shows the average distance between the closest two atom.
It appears as first peak which is alike bonding length. If you intgrate under the graph, you can get the coordination number.

In this example, there ar no value at 0,1 Angstrom due to the Pauli exclusion principle.

In 90fs MD, first peak appears at 2.4 Angstrom and this means the average bonding length.

You can distinguish the phase of the system by the large distance (ex. 4 Ang) g(r).

Crystall structure (long-range order) : the Peak appears.
liquid / gas (Disorderd) : g(r) converges to ~1
