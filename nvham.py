
import qutip as qt
import scipy.constants as const
import matplotlib.pyplot as plt
import numpy as np

class NVHamiltonian():
	def __init__(self):
		self.hbar = const.hbar
		self.sx = qt.jmat(1,'x')
		self.sy = qt.jmat(1,'y')
		self.sz = qt.jmat(1,'z')            # jmat is higher order spin operator. 1 in this case.
		self.Bz = 1.199e-4                  # Magnetic field along z axis. Value taken from reference 2.
		self.ge = 5.27787566e11             # gyromagnetic ration of electron in Hz/T
		self.gc = 10.705e6                  # gyromagnetic ratio of C-13 nucleus in Hz/T for hyperfine interaction
		self.D = 2870.2e6                   # zero field splitting frequency in Hz
		
		self.Axx = 189.3e6
		self.Ayy = 128.4e6
		self.Azz = 128.9e6
		self.Axz = 24.1e6                   # Hyperfine Tensor components in NV frame of reference. Taken from reference 2.
		self.Ix = qt.jmat(0.5,'x')
		self.Iy = qt.jmat(0.5,'y')
		self.Iz = qt.jmat(0.5,'z')          # Spin 1/2 operators for C-13 nucleus
		
	def spinHamiltonian(self,Bz):
		Hs = self.D*(self.sz*self.sz) + self.ge*Bz*self.sz      # Electric term ignored as it is negligible
		self.Eigenstates_sp = Hs.eigenstates()
		#$print ("Spin Hamiltonian Eigenenergies: "+ str(abs(self.Eigenstates_sp[0])) + "\n")
	
	def hyperfineHamiltonian(self):
		comp1 = self.Axx*qt.tensor(self.sx,self.Ix)
		comp2 = self.Ayy*qt.tensor(self.sy,self.Iy)
		comp3 = self.Azz*qt.tensor(self.sz,self.Iz)
		comp4 = self.Axz*(qt.tensor(self.sx,self.Iz)+qt.tensor(self.sz,self.Ix))
		
		Hhf = comp1 + comp2 +comp3 +comp4
		H = self.D*(qt.tensor(self.sz*self.sz,qt.qeye(2))) + self.ge*self.Bz*qt.tensor(self.sz,qt.qeye(2)) + self.gc*self.Bz*qt.tensor(qt.qeye(3),self.Iz) + Hhf
		self.Eigenstates_hf = H.eigenstates()
		print("Hyperfine Splitting Hamiltonian Eigenenergies: " + str(abs(self.Eigenstates_hf[0])) + "\n")
		self.plotter()

	def plotter(self):
		# Plotting Resonant frequencies
		reso = np.full((8),1)
		freq = []
		for i in range (2):
			for j in range (2,6):
				freq.append(abs(self.Eigenstates_hf[0][i]-self.Eigenstates_hf[0][j]))
		freq = np.sort(freq)*0.000000001
		print(freq)
		fig1 = plt.figure()
		ax1 = fig1.add_subplot(111)
		ax1.set_xlabel('Frequency in GHz',fontsize=12)
		ax1.set_ylabel('Resonant Amplitude',fontsize=12)
		ax1.set_title("Resonant Frequencies")
		ax1.bar(freq[0:4],reso[0:4],width=0.0001,bottom=None)
		
		fig2 = plt.figure()
		ax2 = fig2.add_subplot(111)
		ax2.set_xlabel('Frequency in GHz',fontsize=12)
		ax2.set_ylabel('Resonant Amplitude',fontsize=12)
		ax2.set_title("Resonant Frequencies")
		ax2.bar(freq[4:8],reso[4:8],width=0.0001,bottom=None)
		
		#Plotting ms=0 to ms=1 transition frequency as a function of magnetic field for Spin Hamiltonian
		Bz = np.linspace(1e-6,1e-3,100)
		zTo = []
		zTmo = []
		for B in Bz:
			self.spinHamiltonian(B)
			zTo.append(self.Eigenstates_sp[0][2]-self.Eigenstates_sp[0][0])
			zTmo.append(self.Eigenstates_sp[0][1]-self.Eigenstates_sp[0][0])
		zTo = np.array(zTo)
		zTmo = np.array(zTmo)
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.set_xlabel("Magnetic Field",fontsize=12)
		ax.set_ylabel("Transition Frequency", fontsize=12)
		ax.set_title("Transition frequencies vs Magnetic field")
		ax.plot(Bz,zTo,label="$m_{s}=0$ to $m_{s}=1$") 
		ax.plot(Bz,zTmo,label="$m_{s}=0$ to $m_{s}=-1$")
		ax.legend()
		plt.show()
			
                    
                
		
if __name__ == '__main__':
	run = NVHamiltonian()
	run.hyperfineHamiltonian()
	run.plotter()
	
		
		
