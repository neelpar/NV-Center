import qutip as qt
import matplotlib.pyplot as plt
import numpy as np
from hamiltonians import SpinHamiltonian

ham = SpinHamiltonian()

#Plotting ms=0 to ms=1 transition frequency as a function of magnetic field for hyperfine Hamiltonian
def BvsF_plotter():
	B = np.linspace(0,3,100)
	Bzoom = np.linspace(0,0.175,100)
	
	# freqs: perpendicular field frequency array
	# freqsz: parallel field frequency array
	sham = np.vectorize(ham.transitionFreqs, otypes=[np.ndarray])
	freqs = np.array(sham(B,0,0))		
	freqs = np.array(freqs.tolist())
	freqsz = np.array(sham(B,0,1))
	freqsz = np.array(freqsz.tolist())
	
	# freqs_z: zoomed perpendicular field frequency array
	# freqsz_z: zoomed parallel field frequency array
	freqs_z = np.array(sham(Bzoom,0,0))		
	freqs_z = np.array(freqs_z.tolist())
	freqsz_z = np.array(sham(Bzoom,0,1))
	freqsz_z = np.array(freqsz_z.tolist())
	
	fig = plt.figure()
	ax = plt.subplot2grid((5,5),(0,0),rowspan=5,colspan=3)  # for proper sizing and placement of graph
	ax.set_xlabel("Magnetic Field (T)",fontsize=12)
	ax.set_ylabel("Transition Frequency (GHz)", fontsize=12)
	ax.set_title("Transition frequencies vs Magnetic field")
	ax.plot(B,freqs[:,0],label="$m_{s}=1$ \u2192 $m_{s}=0$, B along x") 
	ax.plot(B,freqs[:,1],label="$m_{s}=-1$ \u2192 $m_{s}=0$, B along x") 
	ax.plot(B,freqsz[:,0],label="$m_{s}=1$ \u2192 $m_{s}=0$, B along z") 
	ax.plot(B,freqsz[:,1],label="$m_{s}=-1$ \u2192 $m_{s}=0$, B along z") 
	ax.legend()
	plt.grid(b=True, which='major', color='#666666', linestyle='-')
	plt.minorticks_on()
	plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
	
	axz = plt.subplot2grid((5,5),(0,3),rowspan=5,colspan=2)  # for proper sizing and placement of graph
	axz.set_xlabel("Magnetic Field (T)",fontsize=12)
	axz.set_title("Zoomed Graph")
	axz.plot(Bzoom,freqs_z[:,0],label="$m_{s}=1$ \u2192 $m_{s}=0$, B along x") 
	axz.plot(Bzoom,freqs_z[:,1],label="$m_{s}=-1$ \u2192 $m_{s}=0$, B along x") 
	axz.plot(Bzoom,freqsz_z[:,0],label="$m_{s}=1$ \u2192 $m_{s}=0$, B along z") 
	axz.plot(Bzoom,freqsz_z[:,1],label="$m_{s}=-1$ \u2192 $m_{s}=0$, B along z") 
	axz.locator_params(axis='x', nbins=4)  			# to reduce crowding of ticks
	plt.grid(b=True, which='major', color='#666666', linestyle='-')
	plt.minorticks_on()
	plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

	plt.show()
	
if __name__ == '__main__':
	BvsF_plotter()
	
	
		
		
