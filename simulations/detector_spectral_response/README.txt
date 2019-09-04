The data file in this folder contains two matrices containing simulated energy deposition on the 12 HED BGO crystals.
This is only valid for the ASIM 180916 event.

It contains 9 or 7 fields:
             rng_seed: random number seed
                 type: particle type (0 for TGF, and -1 1 for TEB)
               energy: list of deposited energies
          energy_unit: unit energy used
    nb_total_recorded: total number of counts recorded in the crystals
     nb_total_sampled: total number of particles sampled
    incident_geometry: sampling geometry of the incident particles
            polar_ang: incident polar angle (only relevant for TGF)
          azimuth_ang: incident azimuthal angle (only relevant for TGF)

The source TGF is at 15 km altitude, Gaussian angular distribution (sigma 30 deg) and has a spectrum  F(E) = 1/E * exp(-E/7.3MeV)

IMPORTANT: This data is specific for the ASIM 160918 event (650 km radial distance between source and TGF).
IMPORTANT: To compare the energies with the real measurement, a degradation of the resolution should be applied (have 15 % resolution at 511 keV.)