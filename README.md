# NV-Center
Codes for performing numerical calculations to study the diamond nv-center quantum system
### Structure of the NV-Center
The NV-Center also known as nitrogen vacancy center is an impurity found in diamond wherein one of the carbon atoms is replaced by a nitrogen atom and the adjacent carbon atom is missing from the lattice creating a vacany. The nitrogen atom consists of a lone pair of electrons which interact with the electrons localized in the vacancy (coming from the adjacent carbon atoms) one at a time. The nv center is a spin 1 system.
### NV-Center Hamiltonian
The Hamiltonian of the center is affacted by a variety of factors such as magnetic field, electric field, strain, temperature and pressure. This makes it an important system for nanoscale measurment of quantities. To perform these measurments one has to know how the external parameters affect the system. Thus one has to study the hamiltoninan and its dynamics.
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

### Solving the Hamiltonian
The eigenstates and eigenvalues of both the spin hamiltonian and the hamiltonian with hyperfine coupling have been found from ```nvham.py```. 
The values considered for magnetic field, hyperfine tensor components, gyromagnetic ratios have been taken from [**References**](###references) 2 and 3.

Key points to note in ```nvham.py```:
- ```tensor(qeye(3),Iz)``` and ```tensor(qeye(2),Sz)``` are considered to couple the operators S<sub>n</sub> and I<sub>n</sub> which matches their dimensions.
- ```H.eigenstates()``` outputs the eigenenergies and the eigenkets of the Hamiltonian.

**Output:**
```
Spin Hamiltonian Eigenenergies: [-63.29995827   0.          63.29995827]

Spin Hamiltonian Eigenstates: (array([Quantum object: dims = [[3], [1]], shape = (3, 1), type = ket
Qobj data =
[[0.]
 [0.]
 [1.]],
       Quantum object: dims = [[3], [1]], shape = (3, 1), type = ket
Qobj data =
[[0.]
 [1.]
 [0.]],
       Quantum object: dims = [[3], [1]], shape = (3, 1), type = ket
Qobj data =
[[1.]
 [0.]
 [0.]]], dtype=object),)


Hyperfine Splitting Hamiltonian Eigenenergies: [-6.33120480e+01 -6.32878686e+01 -1.20896918e-02  1.20896918e-02
  6.32878686e+01  6.33120480e+01]

Hyperfine Splitting Hamiltonian Eigenenstates: (array([Quantum object: dims = [[3, 2], [1, 1]], shape = (6, 1), type = ket
Qobj data =
[[0.]
 [0.]
 [0.]
 [0.]
 [0.]
 [1.]],
       Quantum object: dims = [[3, 2], [1, 1]], shape = (6, 1), type = ket
Qobj data =
[[0.]
 [0.]
 [0.]
 [0.]
 [1.]
 [0.]],
       Quantum object: dims = [[3, 2], [1, 1]], shape = (6, 1), type = ket
Qobj data =
[[0.]
 [0.]
 [0.]
 [1.]
 [0.]
 [0.]],
       Quantum object: dims = [[3, 2], [1, 1]], shape = (6, 1), type = ket
Qobj data =
[[0.]
 [0.]
 [1.]
 [0.]
 [0.]
 [0.]],
       Quantum object: dims = [[3, 2], [1, 1]], shape = (6, 1), type = ket
Qobj data =
[[0.]
 [1.]
 [0.]
 [0.]
 [0.]
 [0.]],
       Quantum object: dims = [[3, 2], [1, 1]], shape = (6, 1), type = ket
Qobj data =
[[1.]
 [0.]
 [0.]
 [0.]
 [0.]
 [0.]]], dtype=object),)
```
### References 
- [Nitrogen-Vacancy Centers in Diamond: Nanoscale Sensors for Physics and Biology](https://www.annualreviews.org/doi/abs/10.1146/annurev-physchem-040513-103659)
- [Characterization of hyperfine interaction between an NV electron spin and a first-shell 13C nuclear spin in diamond](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.94.060101)
- [Gyromagnetic Ratios of different nuclei](https://home.uni-leipzig.de/energy/pdf/freuse4.pdf)

