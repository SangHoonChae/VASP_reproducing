Molecular dynamics in VASP tutorials

Part 1 : Melting silicon

notes)

MDALGO = 2    # Nose-hoover Thermostat. Canonical Ensemble (NVT)

SMASS = small(0.1), moderate(1.0), Large(10.0)    # controlling frequency from initial structure temperature to starting temperature(TEBEG). small : overshooting, moderate : increasing steadly, Large : increasing very slowly

# Due to the cannonical ensemble, TEBEG and TEEND must be the same(fixed T). Likewise volume must be fixed.(ISIF = 2)


2x2x2 supercell # Due to the large system, single K point is enough.

-----------------------------------------------------------------------
with each iterations,

T : temperature. ( derived from the kinetic energy of atoms via the equipartition theorem )

E : total energy. ( F + SP + SK + EK )

F : Helmholtz free energy (F = U -TS). ( The force acting on atoms is the negatice gradient of F )

ETOTAL : potential between ion and electron

