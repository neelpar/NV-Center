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

The excited state Hamiltonian is given by:
> H = D<sub>es</sub>S<sub>z</sub><sup>2</sup> + &#956;<sub>B</sub>g<sub>es</sub>B.S + E<sub>es</sub>(S<sub>x</sub><sup>2</sup> - S<sub>y</sub><sup>2</sup>) - A<sub>es</sub>S.I

where:
- D<sub>es</sub> = 1.425&#177;003 GHz is the excited state zero field splitting frequency
- A<sub>es</sub> = 61&#177;6 MHz is the hyperfine splitting constant
- g<sub>es<sub> = 2.01&#177;0.01 is the g factor
- E<sub>es</sub> = 70&#177;30 MHz is the strain constant

The above values and formula are taken from [**Reference**](###references) 4.

### Solving the Hamiltonian
The Spin Hamiltonian has been solved for a range of Magnetic field values. The transition frequencies from m<sub>s</sub>=1 to m<sub>s</sub>=0 and m<sub>s</sub>=-1 to m<sub>s</sub>=0 have been plotted as a function of the magnetic field in Fig(1).

The hyperfine Hamiltonian has been solved for both spin-1 and spin-1/2 coupling nuclei. 

For a spin-1/2 coupling nucleus, <sup>13</sup>C an be assumed. A bar plot for the resonance frequencies has been plotted in Fig(2) for B<sub>z</sub> = 1.199x10<sup>-4</sup>T. This value of magnetic field is same as in [**Reference**](###references) 2 and the corresponding resonant frequencies have been reproduced. Fig(3) shows the frequency response of the system for a range of magnetic fields from 0T - 0.1T.
In the unlikely case of hyperfine lines not being visible, you can zoom in to see them clearly.

Similar plots have been plotted for a spin-1 coupling nucleus in Fig(4) and Fig(5).

When it comes to the excited state of the NV-Center, local strain plays an important role. For the ground state, the effect of strain is negligible. The zero field splitting is lesser than the ground state case. Fig(6) shows the F vs B graph for the excited state under spin-1/2 hyperfine coupling and Fig(7) shows the resonant frequencies. When the energy of the m<sub>s</sub>=-1 state falls below m<sub>s</sub>=0 only 4 lines are observed practically. The plot in Fig(7) considers a relatively lower magnetic field and hence 8 lines are shown. 

### Results
Fig(1)
![alt text](https://github.com/neelpar/NV-Center/blob/master/spinham-BF.png?raw=true)
Fig(2)
![alt text](https://github.com/neelpar/NV-Center/blob/master/13C-BF.png?raw=true)
Fig(3)
![alt text](https://github.com/neelpar/NV-Center/blob/master/13C-reso.png?raw=true)
Fig(4)
![alt text](https://github.com/neelpar/NV-Center/blob/master/spin1-BF.png?raw=true)
Fig(5)
![alt text](https://github.com/neelpar/NV-Center/blob/master/spin1-reso.png?raw=true)
Fig(6)
![alt text](https://github.com/neelpar/NV-Center/blob/master/es_strain_bf.png?raw=true)
Fig(7)
![alt text](https://github.com/neelpar/NV-Center/blob/master/es-reso.png?raw=true)


### Conclusion
- For a spin-1/2 coupling nucleus, the system has 4 pairs of resonant lines, each pair having 2 hyperfine lines.
- For a spin-1 coupling nucleus, the system has 6 groups of resonant lines, each group having 3 hyperfine lines.
- In zero magnetic field, the B vs F graph for hyperfine coupled NV-Center shows unequal transition frequencies from m<sub>s</sub>=1 and m<sub>s</sub>=-1 to m<sub>s</sub>=0 unlike the case of the normal spin hamiltonian.
- For magnetic fields close to zero, the transition frequencies show an interesting zig-zag behaviour, but for higher fields follow a linear dependance.

### References 
- [Nitrogen-Vacancy Centers in Diamond: Nanoscale Sensors for Physics and Biology](https://www.annualreviews.org/doi/abs/10.1146/annurev-physchem-040513-103659)
- [Characterization of hyperfine interaction between an NV electron spin and a first-shell 13C nuclear spin in diamond](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.94.060101)
- [Gyromagnetic Ratios of different nuclei](https://home.uni-leipzig.de/energy/pdf/freuse4.pdf)
- [Excited State Spectroscopy](https://link.aps.org/doi/10.1103/PhysRevLett.101.117601)

