import qutip as qt
import scipy.constants as const
import matplotlib.pyplot as plt
import numpy as np
from hamiltonians import HyperfineSpin1

ham = HyperfineSpin1()

def plotter_resonance(): #This function will need changes to plot. self.Eigenstates_hf has been removed.
	# Plotting Hyperfine Resonant frequencies
	reso = np.full((18),1)
	freq = []
	egsts = ham.eigenvalues(1.199e-4)
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
	ax1.bar(freq[0:6],reso[0:6],width=0.00003,bottom=None)
	
	ax2 = fig.add_subplot(312)
	#ax2.set_xlabel('Frequency in GHz',fontsize=12)
	ax2.set_ylabel('Resonant Amplitude',fontsize=12)
	#ax2.set_title("Resonant Frequencies")
	ax2.bar(freq[6:12],reso[0:6],width=0.00003,bottom=None)
	
	ax3 = fig.add_subplot(313)
	ax3.set_xlabel('Frequency in GHz',fontsize=12)
	ax3.set_ylabel('Resonant Amplitude',fontsize=12)
	#ax3.set_title("Resonant Frequencies")
	ax3.bar(freq[12:18],reso[0:6],width=0.00003,bottom=None)
	plt.show()

def BvsF_plotter():				
	hpham = np.vectorize(ham.transitionFreqs, otypes=[np.ndarray])
	#hpham = np.vectorize(ham.transitionFreqs)	
	#Plotting ms=0 to ms=1 transition frequency as a function of magnetic field for hyperfine Hamiltonian
	Bz = np.linspace(0,1e-2,100)
	Bzoom = np.linspace(0,5e-3,100)
	#hpham = np.vectorize(self.hyperfineHamiltonian, otypes=[np.ndarray])

	freqs = np.array(hpham(Bz))
	freqs = np.array(freqs.tolist())
	#print(freqs)
	freqs_zoom = np.array(hpham(Bzoom))

	freqs_zoom = np.array(freqs_zoom.tolist())

	#Qutip by default arranges eigenvalues in sorted order. This never gives a negative frequency. So the graph has to be extended logically.
	#calculating slope array
	b1 = 1e-2
	f1 = hpham(b1)
	b2 = 0.8e-2
	f2 = hpham(b2)
	m = (f2-f1)/(b2-b1)

	#adding higher magnetic field values
	Bzext = np.linspace(1e-2,0.2,200)
	fext = np.absolute(np.outer(Bzext-b1,m) + f1)

	#appending B and f arrays
	Bz = np.append(Bz,Bzext)
	freqs = np.append(freqs,fext,axis=0)

	fig = plt.figure()
	ax = plt.subplot2grid((5,5),(0,0),rowspan=5,colspan=3)  # for proper sizing and placement of graph
	ax.set_xlabel("Magnetic Field (T)",fontsize=12)
	ax.set_ylabel("Transition Frequency (GHz)", fontsize=12)
	ax.set_title("Transition frequencies vs Magnetic field")
	ax.plot(Bz,freqs[:,0],label="$m_{s}=-1$, $m_{I}=+1$ \u2192 $m_{s}=0$") 
	ax.plot(Bz,freqs[:,1],label="$m_{s}=-1$, $m_{I}=0$ \u2192 $m_{s}=0$") 
	ax.plot(Bz,freqs[:,2],label="$m_{s}=-1$, $m_{I}=-1$ \u2192 $m_{s}=0$") 
	ax.plot(Bz,freqs[:,3],label="$m_{s}=+1$, $m_{I}=-1$ \u2192 $m_{s}=0$") 
	ax.plot(Bz,freqs[:,4],label="$m_{s}=+1$, $m_{I}=0$ \u2192 $m_{s}=0$") 
	ax.plot(Bz,freqs[:,5],label="$m_{s}=+1$, $m_{I}=+1$ \u2192 $m_{s}=0$") 
	ax.legend(loc='upper left',fontsize=8,labelspacing=0)
	plt.grid(b=True, which='major', color='#666666', linestyle='-')
	plt.minorticks_on()
	plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

	axz = plt.subplot2grid((5,5),(0,3),rowspan=5,colspan=2)  # for proper sizing and placement of graph
	axz.set_xlabel("Magnetic Field (T)",fontsize=12)
	axz.set_title("Zoomed Graph")
	axz.plot(Bzoom,freqs_zoom[:,0],label="$m_{s}=-1$, $m_{I}=+1$ \u2192 $m_{s}=0$") 
	axz.plot(Bzoom,freqs_zoom[:,1],label="$m_{s}=-1$, $m_{I}=0$ \u2192 $m_{s}=0$") 
	axz.plot(Bzoom,freqs_zoom[:,2],label="$m_{s}=-1$, $m_{I}=-1$ \u2192 $m_{s}=0$") 
	axz.plot(Bzoom,freqs_zoom[:,3],label="$m_{s}=+1$, $m_{I}=-1$ \u2192 $m_{s}=0$") 
	axz.plot(Bzoom,freqs_zoom[:,4],label="$m_{s}=+1$, $m_{I}=0$ \u2192 $m_{s}=0$") 
	axz.plot(Bzoom,freqs_zoom[:,5],label="$m_{s}=+1$, $m_{I}=+1$ \u2192 $m_{s}=0$")
	axz.locator_params(axis='x', nbins=4)  # to reduce crowding of ticks
	plt.grid(b=True, which='major', color='#666666', linestyle='-')
	plt.minorticks_on()
	plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

	plt.show()
		
if __name__ == '__main__':
	plotter_resonance()
	BvsF_plotter()
	
	
		
		
