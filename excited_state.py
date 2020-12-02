import qutip as qt
import numpy as np
import matplotlib.pyplot as plt
from hamiltonians import ExcitedState

es = ExcitedState()

def resonance_plotter(self,Bz):
	reso = np.full((8),1)
	egv = es.eigenvalues(1.199e-4)
	freq = []
	for i in range (2):
		for j in range (2,6):
			freq.append(egv[j]-egv[i])
			
	freq = np.sort(freq)*0.000000001
	fig = plt.figure()
	ax1 = fig.add_subplot(211)
	ax1.set_ylabel('Resonant Amplitude',fontsize=12)
	ax1.set_title("Resonant Frequencies")
	ax1.bar(freq[0:4],reso[0:4],width=0.000003,bottom=None)
	
	ax2 = fig.add_subplot(212)
	ax2.set_xlabel('Frequency in GHz',fontsize=12)
	ax2.set_ylabel('Resonant Amplitude',fontsize=12)
	ax2.bar(freq[4:8],reso[4:8],width=0.000003,bottom=None)
	plt.show()
		
def BvsF_plotter():
	hpham = np.vectorize(es.transitionFreqs, otypes = [np.ndarray])
	B = np.linspace(0,1e-2,100)
	Bzoom = np.linspace(0,1e-2,100)
	
	freqs = np.array(hpham(B))
	freqs_zoom = np.array(hpham(Bzoom))
	freqs = np.array(freqs.tolist())
	freqs_zoom = np.array(freqs_zoom.tolist())
	
	#calculating slope array
	b1 = 1e-2
	f1 = hpham(b1)
	b2 = 0.8e-2
	f2 = hpham(b2)
	m = (f2-f1)/(b2-b1)
	
	#adding higher magnetic field values
	Bext = np.linspace(1e-2,0.2,100)
	fext = np.absolute(np.outer(Bext-b1,m) + f1)
	
	#appending B and f arrays
	B = np.append(B,Bext)
	freqs = np.append(freqs,fext,axis=0)
	
	fig = plt.figure()
	ax = plt.subplot2grid((5,5),(0,0),rowspan=5,colspan=3)  # for proper sizing and placement of graph
	ax.set_xlabel("Magnetic Field",fontsize=12)
	ax.set_ylabel("Transition Frequency", fontsize=12)
	ax.set_title("Transition frequencies vs Magnetic field")
	ax.plot(B,freqs[:,0],label="$m_{s}=-1$, $m_{I}=+1/2$ \u2192 $m_{s}=0$") 
	ax.plot(B,freqs[:,1],label="$m_{s}=-1$, $m_{I}=-1/2$ \u2192 $m_{s}=0$") 
	ax.plot(B,freqs[:,2],label="$m_{s}=+1$, $m_{I}=-1/2$ \u2192 $m_{s}=0$") 
	ax.plot(B,freqs[:,3],label="$m_{s}=+1$, $m_{I}=+1/2$ \u2192 $m_{s}=0$") 
	ax.legend()
	plt.grid(b=True, which='major', color='#666666', linestyle='-')
	plt.minorticks_on()
	plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
	
	axz = plt.subplot2grid((5,5),(0,3),rowspan=5,colspan=2)  # for proper sizing and placement of graph
	axz.set_xlabel("Magnetic Field",fontsize=12)
	axz.set_title("Zoomed Graph")
	axz.plot(Bzoom,freqs_zoom[:,0],label="$m_{s}=-1$, $m_{I}=+1/2$ \u2192 $m_{s}=0$") 
	axz.plot(Bzoom,freqs_zoom[:,1],label="$m_{s}=-1$, $m_{I}=-1/2$ \u2192 $m_{s}=0$") 
	axz.plot(Bzoom,freqs_zoom[:,2],label="$m_{s}=+1$, $m_{I}=-1/2$ \u2192 $m_{s}=0$") 
	axz.plot(Bzoom,freqs_zoom[:,3],label="$m_{s}=+1$, $m_{I}=+1/2$ \u2192 $m_{s}=0$") 
	axz.locator_params(axis='x', nbins=4)  # to reduce crowding of ticks
	plt.grid(b=True, which='major', color='#666666', linestyle='-')
	plt.minorticks_on()
	plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
	
	plt.show()
		
if __name__ == '__main__':
	BvsF_plotter()
		
		
		
