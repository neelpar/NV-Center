import qutip as qt
import matplotlib.pyplot as plt
import numpy as np
from hamiltonians import HyperfineSpinHalf

ham = HyperfineSpinHalf()

# Plotting Hyperfine Resonant frequencies
def resonance_plotter(): 
	# generating all possible frequency transitions
	reso = np.full((8),1)
	freq = []
	egsts = ham.eigenvalues(1.199e-4)
	for i in range (2):
		for j in range (2,6):
			freq.append(egsts[j]-egsts[i])
	
	# plot first 4 frequencies
	freq = np.sort(freq)*0.000000001
	fig = plt.figure()
	ax1 = fig.add_subplot(211)
	ax1.set_ylabel('Resonant Amplitude',fontsize=12)
	ax1.set_title("Resonant Frequencies")
	ax1.bar(freq[0:4],reso[0:4],width=0.000007,bottom=None)
	
	# plot next 4 frequencies
	ax2 = fig.add_subplot(212)
	ax2.set_xlabel('Frequency in GHz',fontsize=12)
	ax2.set_ylabel('Resonant Amplitude',fontsize=12)
	ax2.bar(freq[4:8],reso[4:8],width=0.000007,bottom=None)
	plt.show()

# Plotting ms=0 to ms=+-1 transition frequency as a function of magnetic field for hyperfine Hamiltonian	
def BvsF_plotter():
	# B covers fields until the point where ms=-1 does not fall below ms=0
	# Bzoom is for the zoomed graph
	Bz = np.linspace(0,1e-2,100)
	Bzoom = np.linspace(0,0.7e-2,100)
	hpham = np.vectorize(ham.transitionFreqs, otypes=[np.ndarray])
	freqs = np.array(hpham(Bz))
	freqs_zoom = np.array(hpham(Bzoom))
	freqs = np.array(freqs.tolist())
	freqs_zoom = np.array(freqs_zoom.tolist())
	
	# Qutip by default arranges eigenvalues in sorted order. This never gives a negative frequency. So the graph has to be extended logically.
	# calculating slope array
	b1 = 1e-2
	f1 = hpham(b1)
	b2 = 0.8e-2
	f2 = hpham(b2)
	m = (f2-f1)/(b2-b1)
	
	# adding higher magnetic field values
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
	ax.plot(Bz,freqs[:,0],label="$m_{s}=-1$, $m_{I}=+1/2$ \u2192 $m_{s}=0$") 
	ax.plot(Bz,freqs[:,1],label="$m_{s}=-1$, $m_{I}=-1/2$ \u2192 $m_{s}=0$") 
	ax.plot(Bz,freqs[:,2],label="$m_{s}=+1$, $m_{I}=-1/2$ \u2192 $m_{s}=0$") 
	ax.plot(Bz,freqs[:,3],label="$m_{s}=+1$, $m_{I}=+1/2$ \u2192 $m_{s}=0$") 
	ax.legend()
	# insert gridlines
	plt.grid(b=True, which='major', color='#666666', linestyle='-')
	plt.minorticks_on()
	plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
	
	axz = plt.subplot2grid((5,5),(0,3),rowspan=5,colspan=2)  # for proper sizing and placement of graph
	axz.set_xlabel("Magnetic Field (T)",fontsize=12)
	axz.set_title("Zoomed Graph")
	axz.plot(Bzoom,freqs_zoom[:,0],label="$m_{s}=-1$, $m_{I}=+1/2$ \u2192 $m_{s}=0$") 
	axz.plot(Bzoom,freqs_zoom[:,1],label="$m_{s}=-1$, $m_{I}=-1/2$ \u2192 $m_{s}=0$") 
	axz.plot(Bzoom,freqs_zoom[:,2],label="$m_{s}=+1$, $m_{I}=-1/2$ \u2192 $m_{s}=0$") 
	axz.plot(Bzoom,freqs_zoom[:,3],label="$m_{s}=+1$, $m_{I}=+1/2$ \u2192 $m_{s}=0$") 
	axz.locator_params(axis='x', nbins=4)			 # to reduce crowding of ticks
	# insert gridlines
	plt.grid(b=True, which='major', color='#666666', linestyle='-')
	plt.minorticks_on()
	plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

	plt.show()
	
if __name__ == '__main__':
	BvsF_plotter()
	resonance_plotter()
	
		
		
