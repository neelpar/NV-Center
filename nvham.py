
import qutip as qt
import scipy.constants as const

class NVHamiltonian():
	def __init__(self):
		self.hbar = const.hbar
		self.sx = qt.jmat(1,'x')
		self.sy = qt.jmat(1,'y')
		self.sz = qt.jmat(1,'z')            # jmat is higher order spin operator. 1 in this case.
		self.Bz = 2.2587e-9                 # Magnetic field along z axis. Value taken from reference 2.
		self.ge = 28024.95164e6             # gyromagnetic ration of electron in Hz/T
		self.gc = 10.705e6                  # gyromagnetic ratio of C-13 nucleus in Hz/T for hyperfine interaction
		self.D = 2870.2e6                   # zero field splitting frequency in MHz
		
		self.Axx = 189.3
		self.Ayy = 128.4
		self.Azz = 128.9
		self.Axz = 24.1                     # Hyperfine Tensor components in NV frame of reference. Taken from reference 2.
		self.Ix = qt.jmat(0.5,'x')
		self.Iy = qt.jmat(0.5,'y')
		self.Iz = qt.jmat(0.5,'z')          # Spin 1/2 operators for C-13 nucleus
		
	def spinHamiltonian(self):
		Hs = self.D*self.hbar*(self.sz*self.sz - (qt.qeye(3)*2/3)) + self.ge*self.Bz*self.sz      # Electric term ignored as it is negligible
		Eigenstates = Hs.eigenstates()
		print ("Spin Hamiltonian Eigenenergies: "+ str(Eigenstates[0]) + "\n")
		print ("Spin Hamiltonian Eigenstates: "+ str(Eigenstates[1:]) + "\n\n")
	
	def hyperfineHamiltonian(self):
		comp1 = self.Axx*self.hbar*qt.tensor(self.sx,self.Ix)
		comp2 = self.Ayy*self.hbar*qt.tensor(self.sy,self.Iy)
		comp3 = self.Azz*self.hbar*qt.tensor(self.sz,self.Iz)
		comp4 = self.Axz*self.hbar*(qt.tensor(self.sx,self.Iz)+qt.tensor(self.sz,self.Ix))
		
		Hhf = comp1 + comp2 +comp3 +comp4
		H = self.D*self.hbar*qt.tensor(self.sz*self.sz,qt.qeye(2)) + self.ge*self.Bz*qt.tensor(self.sz,qt.qeye(2)) + self.gc*self.Bz*qt.tensor(qt.qeye(3),self.Iz) + Hhf
		Eigenstates = H.eigenstates()
		print("Hyperfine Splitting Hamiltonian Eigenenergies: " + str(Eigenstates[0]) + "\n")
		print("Hyperfine Splitting Hamiltonian Eigenenstates: " + str(Eigenstates[1:]))
		
if __name__ == '__main__':
	run = NVHamiltonian()
	run.spinHamiltonian()
	run.hyperfineHamiltonian()
	
		
		
