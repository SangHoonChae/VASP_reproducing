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

At short distances, g(r) shows the average distance between the two closest atoms (or nearest neighbors).

It appears as the first peak, which corresponds to the bond length. If you integrate the area under the peak, you can get the coordination number.

In this example, there are no values between 0 and 1 Angstrom due to the Pauli exclusion principle.

At 90 fs in the MD simulation, the first peak appears at 2.4 Angstrom, which represents the average bond length.

You can distinguish the phase of the system by observing g(r) at large distances (e.g., > 4 Ang).

    Crystal structure (long-range order): Distinct peaks continue to appear.

    Liquid / gas (disordered): g(r) converges to ~1.

! Also note that it makes no sense to display g(r) for r longer than half the shortest dimension of the supercell. That is, here r should be kept below 5.4 Å.
