# NV-Center
Codes for performing numerical calculations to study the diamond nv-center quantum system
### Structure of the NV-Center
The NV-Center also known as nitrogen vacancy center is an impurity found in diamond wherein one of the carbon atoms is replaced by a nitrogen atom and the adjacent carbon atom is missing from the lattice creating a vacany. The nitrogen atom consists of a lone pair of electrons which interact with the electrons localized in the vacancy (coming from the adjacent carbon atoms) one at a time. The nv center is a spin 1 system.
### NV-Center Hamiltonian
The Hamiltonian of the center is affacted by a variety of factors such as magnetic field, electric field, strain, temperature and pressure. This makes it an important system for nanoscale measurment of quantities. To perform these measurments one has to know how the external parameters affect the system. Thus one has to study the hamiltoninan and its dynamics.
Following formulae for the hamiltonians have been taken from [**References**](###references) 1 and 2
The spin hamiltonian of the center is given by:
> H<sub>s</sub> = D(S<sub>z</sub><sup>2</sup> - 2/3) + &#947;B.S + &#949;<sub>z</sub>E<sub>z</sub>(S<sub>z</sub><sup>2</sup> - 2/3) + &#949;<sub>xy</sub>{E<sub>x</sub>(S<sub>x</sub>S<sub>y</sub> + S<sub>y</sub>S<sub>x</sub>) + E<sub>y</sub>(S<sub>x</sub><sup>2</sup> + S<sub>y</sub><sup>2</sup>)}

where:
- S<sub>n</sub> is the n<sup>th</sup> component of the nv-center spin operator
- D is the zero field splitting energy
- &#947; is the gyromagnetic ratio of an electron
- B, E are magnetic and electric fields respectively

If the carbon atom adjacent to the vacancy is the isotope <sup>13</sup>C, the hamitonian is also influenced by the hyperfine interactions between the nv-center electrons and the <sup>13</sup>C nucleus owing to its 1/2 spin. In this case the hamiltonian takes the form:
> H = DS<sub>z</sub><sup>2</sup> + &#947;<sub>e</sub>B.S + &#947;<sub>n</sub>B.I + H<sub>hf</sub>

> H<sub>hf</sub> = A<sub>zz</sub>S<sub>z</sub>I<sub>z</sub> +  A<sub>xx</sub>S<sub>x</sub>I<sub>x</sub> +  A<sub>yy</sub>S<sub>y</sub>I<sub>y</sub> +  A<sub>xz</sub>(S<sub>z</sub>I<sub>x</sub> + S<sub>x</sub>I<sub>z</sub>)

where:
- I<sub>n</sub> is the n<sup>th</sup> component of the nuclear spin operator
- A<sub>ij</sub> is the ij<sup>th</sup> component of the Hyperfine tensor
- &#947;<sub>n</sub> is the gyromagnetic ratio of the <sup>13</sup>C nucleus

The above hamiltonians do not have the scaling factor of &#8463;. Hence the obtained eigenvalues are transition frequencies.

### Solving the Hamiltonian
The Spin Hamiltonian has been solved for a range of Magnetic field values. The transition frequencies from m<sub>s</sub>=1 to m<sub>s</sub>=0 and m<sub>s</sub>=-1 to m<sub>s</sub>=0 have been plotted as a function of the magnetic field in fig(1).

The hyperfine Hamiltonian has been solved for B<sub>z</sub> = 1.199x10<sup>-4</sup>T and a bar plot for the resonance frequencies has been plotted in fig(2) and fig(3). This value of magnetic field is same as in [**References**](###references) 2 and the corresponding resonant frequencies have been reproduced. The hyperfine splitting may not be visible directly. You may have to zoom into the image to see it.

### Results
Fig(1)
![alt text](https://github.com/neelpar/NV-Center/blob/master/Figure_1.png?raw=true)
Fig(2)
![alt text](https://github.com/neelpar/NV-Center/blob/master/Figure_2.png?raw=true)
Fig(3)
![alt text](https://github.com/neelpar/NV-Center/blob/master/Figure_3.png?raw=true)

### Conclusion
- In zero magnetic field and without hyperfine interactions the spin 1 states are at equal energy levels. With application of magnetic field the energies split with 2&#947;B as the difference in energies.
- Hyperfine Splitting is of the order of 10<sup>-3</sup> times smaller than the frequency scale. 

### References 
- [Nitrogen-Vacancy Centers in Diamond: Nanoscale Sensors for Physics and Biology](https://www.annualreviews.org/doi/abs/10.1146/annurev-physchem-040513-103659)
- [Characterization of hyperfine interaction between an NV electron spin and a first-shell 13C nuclear spin in diamond](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.94.060101)
- [Gyromagnetic Ratios of different nuclei](https://home.uni-leipzig.de/energy/pdf/freuse4.pdf)

