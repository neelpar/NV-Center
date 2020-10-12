
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
		self.Ix = qt.jmat(1,'x')
		self.Iy = qt.jmat(1,'y')
		self.Iz = qt.jmat(1,'z')          # Spin 1 operators
		
	def spinHamiltonian(self,Bz):
		Hs = self.D*((self.sz*self.sz)-(2/3)*qt.qeye(3)) + self.ge*Bz*self.sz      # Electric term ignored as it is negligible
		self.Eigenstates_sp = Hs.eigenstates()
		#$print ("Spin Hamiltonian Eigenenergies: "+ str(abs(self.Eigenstates_sp[0])) + "\n")
	
	def hyperfineHamiltonian(self,Bz):
		comp1 = self.Axx*qt.tensor(self.sx,self.Ix)
		comp2 = self.Ayy*qt.tensor(self.sy,self.Iy)
		comp3 = self.Azz*qt.tensor(self.sz,self.Iz)
		comp4 = self.Axz*(qt.tensor(self.sx,self.Iz)+qt.tensor(self.sz,self.Ix))
		
		Hhf = comp1 + comp2 +comp3 +comp4
		H = self.D*(qt.tensor(self.sz*self.sz,qt.qeye(3))-(2/3)*qt.tensor(qt.qeye(3),qt.qeye(3))) + self.ge*Bz*qt.tensor(self.sz,qt.qeye(3)) + self.gc*Bz*qt.tensor(qt.qeye(3),self.Iz) + Hhf 
		eigenvals = H.eigenstates()[0]
		#print(eigenvals)
		f0 = (eigenvals[0]+eigenvals[1]+eigenvals[2])/3 #
		a = np.array([(eigenvals[3]-f0),(eigenvals[4]-f0),(eigenvals[5]-f0),(eigenvals[6]-f0),(eigenvals[7]-f0),(eigenvals[8]-f0)]) #
		return a #return eigenvals for plotter_resonance
		#print("Hyperfine Splitting Hamiltonian Eigenenergies: " + str(abs(self.Eigenstates_hf[0])) + "\n")
		#self.plotter()

	def plotter_resonance(self): #This function will need changes to plot. self.Eigenstates_hf has been removed.
		# Plotting Hyperfine Resonant frequencies
		reso = np.full((18),1)
		freq = []
		egsts = self.hyperfineHamiltonian(1.199e-4)
		for i in range (3):
			for j in range (3,9):
				freq.append(egsts[j]-egsts[i])
		freq = np.sort(freq)*0.000000001
		
		#print(freq)
		fig = plt.figure()
		ax1 = fig.add_subplot(311)
		#ax1.set_xlabel('Frequency in GHz',fontsize=12)
		ax1.set_ylabel('Resonant Amplitude',fontsize=12)
		ax1.set_title("Resonant Frequencies")
		ax1.bar(freq[0:6],reso[0:6],width=0.0001,bottom=None)
		
		ax2 = fig.add_subplot(312)
		#ax2.set_xlabel('Frequency in GHz',fontsize=12)
		ax2.set_ylabel('Resonant Amplitude',fontsize=12)
		#ax2.set_title("Resonant Frequencies")
		ax2.bar(freq[6:12],reso[0:6],width=0.0001,bottom=None)
		
		ax3 = fig.add_subplot(313)
		ax3.set_xlabel('Frequency in GHz',fontsize=12)
		ax3.set_ylabel('Resonant Amplitude',fontsize=12)
		#ax3.set_title("Resonant Frequencies")
		ax3.bar(freq[12:18],reso[0:6],width=0.0001,bottom=None)
		plt.show()
				
	def plotter_BvsF(self):
		#Plotting ms=0 to ms=1 transition frequency as a function of magnetic field for hyperfine Hamiltonian
		Bz = np.linspace(0,1e-3,100)
		Bzoom = np.linspace(0,2e-4,50)
		hpham = np.vectorize(self.hyperfineHamiltonian, otypes=[np.ndarray])
		freqs = np.array(hpham(Bz))
		freqs_zoom = np.array(hpham(Bzoom))
		freqs = np.array(freqs.tolist())
		freqs_zoom = np.array(freqs_zoom.tolist())
		
		#Qutip by default arranges eigenvalues in sorted order. This never gives a negative frequency. So the graph has to be extended logically.
		#calculating slope array
		b1 = 1e-3
		f1 = hpham(b1)
		b2 = 0.8e-3
		f2 = hpham(b2)
		m = (f2-f1)/(b2-b1)
		
		#adding higher magnetic field values
		Bzext = np.linspace(1e-3,1e-2,100)
		fext = np.outer(Bzext-b1,m) + f1
		
		#appending B and f arrays
		Bz = np.append(Bz,Bzext)
		freqs = np.append(freqs,fext,axis=0)
		
		fig = plt.figure()
		ax = plt.subplot2grid((5,5),(1,0),rowspan=3,colspan=3)  # for proper sizing and placement of graph
		ax.set_xlabel("Magnetic Field",fontsize=12)
		ax.set_ylabel("Transition Frequency", fontsize=12)
		ax.set_title("Transition frequencies vs Magnetic field")
		ax.plot(Bz,freqs[:,0],label="$m_{s}=-1$ \u2192 $m_{s}=0$, $m_{I}=-1$") 
		ax.plot(Bz,freqs[:,1],label="$m_{s}=-1$ \u2192 $m_{s}=0$, $m_{I}=0$") 
		ax.plot(Bz,freqs[:,2],label="$m_{s}=-1$ \u2192 $m_{s}=0$, $m_{I}=+1$") 
		ax.plot(Bz,freqs[:,3],label="$m_{s}=+1$ \u2192 $m_{s}=0$, $m_{I}=+1$") 
		ax.plot(Bz,freqs[:,4],label="$m_{s}=+1$ \u2192 $m_{s}=0$, $m_{I}=0$") 
		ax.plot(Bz,freqs[:,5],label="$m_{s}=+1$ \u2192 $m_{s}=0$, $m_{I}=-1$") 
		ax.legend(loc='upper left',fontsize=8,labelspacing=0)
		
		axz = plt.subplot2grid((5,5),(1,3),rowspan=3,colspan=2)  # for proper sizing and placement of graph
		axz.set_xlabel("Magnetic Field",fontsize=12)
		axz.set_title("Zoomed Graph")
		axz.plot(Bzoom,freqs_zoom[:,0],label="$m_{s}=-1$ \u2192 $m_{s}=0$, $m_{I}=-1$") 
		axz.plot(Bzoom,freqs_zoom[:,1],label="$m_{s}=-1$ \u2192 $m_{s}=0$, $m_{I}=0$") 
		axz.plot(Bzoom,freqs_zoom[:,2],label="$m_{s}=-1$ \u2192 $m_{s}=0$, $m_{I}=+1$") 
		axz.plot(Bzoom,freqs_zoom[:,3],label="$m_{s}=+1$ \u2192 $m_{s}=0$, $m_{I}=+1$") 
		axz.plot(Bzoom,freqs_zoom[:,4],label="$m_{s}=+1$ \u2192 $m_{s}=0$, $m_{I}=0$") 
		axz.plot(Bzoom,freqs_zoom[:,5],label="$m_{s}=+1$ \u2192 $m_{s}=0$, $m_{I}=-1$")
		axz.locator_params(axis='x', nbins=4)  # to reduce crowding of ticks
	
		plt.show()
		
if __name__ == '__main__':
	run = NVHamiltonian()
	run.plotter_resonance()
	
		
		
