import qutip as qt
import numpy as np
import matplotlib.pyplot as plt

class Excited_State():
	def __init__(self):
		self.sx1 = qt.jmat(1,'x')
		self.sy1 = qt.jmat(1,'y')
		self.sz1 = qt.jmat(1,'z')            
		self.Aes = 61e6 #hyperfine constant in Hz
		self.sx = qt.jmat(0.5,'x')
		self.sy = qt.jmat(0.5,'y')
		self.sz = qt.jmat(0.5,'z')
		self.D = 1.425e9 # zero field splitting in Hz
		self.g = 5.304265038e11 # gyromagnetic ratio
		 #excited state g factor. for ground state it is 2.0023
		self.Ees = 70e6 #doubtful value. there is a +-30MHz error.
		
	def onlyStrain(self):
		dot1 = qt.tensor(self.sx1,self.sx)
		dot2 = qt.tensor(self.sy1,self.sy)
		dot3 = qt.tensor(self.sz1,self.sz)
		dot = dot1 + dot2 + dot3
		H = self.D*qt.tensor(self.sz1*self.sz1,qt.qeye(2)) + self.Ees*(qt.tensor((self.sx1*self.sx1),qt.qeye(2))-qt.tensor((self.sy1*self.sy1),qt.qeye(2))) - self.Aes*dot 
		return H.eigenstates()[0]
		
	def strain_B(self,Bz):
		dot1 = qt.tensor(self.sx1,self.sx)
		dot2 = qt.tensor(self.sy1,self.sy)
		dot3 = qt.tensor(self.sz1,self.sz)
		dot = dot1 + dot2 + dot3
		H = self.D*qt.tensor(self.sz1*self.sz1,qt.qeye(2)) + self.Ees*qt.tensor(((self.sx1*self.sx1)-(self.sy1*self.sy1)),qt.qeye(2)) + self.g*Bz*qt.tensor(self.sz1,qt.qeye(2)) - self.Aes*dot 
		return H.eigenstates()[0]
		
	def freqs_BF(self,Bz):
		ham = np.vectorize(strain_B, otypes=[np.ndarray])
		egv = ham(Bz)
		f0 = (egv[0]+egv[1])/2
		freq = np.array([(egv[2]-f0),(egv[3]-f0),(egv[4]-f0),(egv[5]-f0)])
		return freq
		
	def plot_allFreqs(self,Bz):
		reso = np.full((8),1)
		egv = self.strain_B(Bz)
		freq = []
		for i in range (2):
			for j in range (2,6):
				freq.append(egv[j]-egv[i])
				
		freq = np.sort(freq)*0.000000001
		fig = plt.figure()
		ax1 = fig.add_subplot(211)
		#ax1.set_xlabel('Frequency in GHz',fontsize=12)
		ax1.set_ylabel('Resonant Amplitude',fontsize=12)
		ax1.set_title("Resonant Frequencies")
		ax1.bar(freq[0:4],reso[0:4],width=0.00003,bottom=None)
		
		ax2 = fig.add_subplot(212)
		ax2.set_xlabel('Frequency in GHz',fontsize=12)
		ax2.set_ylabel('Resonant Amplitude',fontsize=12)
		#ax2.set_title("Resonant Frequencies")
		ax2.bar(freq[4:8],reso[4:8],width=0.00003,bottom=None)
		plt.show()
		
	def plotter(self):
		B = np.linspace(0,1e-3,100)
		Bzoom = np.linspace(0,0.7e-3,100)
		f = np.vectorize(self.freqs_BF, otypes=[np.ndarray])
		freqs = np.array(f(B))
		freqs_zoom = np.array(f(Bzoom))
		freqs = np.array(freqs.tolist())
		freqs_zoom = np.array(freqs_zoom.tolist())
		
		#calculating slope array
		b1 = 1e-3
		f1 = f(b1)
		b2 = 0.8e-3
		f2 = f(b2)
		m = (f2-f1)/(b2-b1)
		
		#adding higher magnetic field values
		Bext = np.linspace(1e-3,1e-2,100)
		fext = np.outer(Bext-b1,m) + f1
		
		#appending B and f arrays
		B = np.append(B,Bext)
		freqs = np.append(freqs,fext,axis=0)
		
		fig = plt.figure()
		ax = plt.subplot2grid((5,5),(1,0),rowspan=3,colspan=3)  # for proper sizing and placement of graph
		ax.set_xlabel("Magnetic Field",fontsize=12)
		ax.set_ylabel("Transition Frequency", fontsize=12)
		ax.set_title("Transition frequencies vs Magnetic field")
		ax.plot(B,freqs[:,0],label="$m_{s}=-1$ \u2192 $m_{s}=0$, $m_{I}=-1/2$") 
		ax.plot(B,freqs[:,1],label="$m_{s}=-1$ \u2192 $m_{s}=0$, $m_{I}=+1/2$") 
		ax.plot(B,freqs[:,2],label="$m_{s}=+1$ \u2192 $m_{s}=0$, $m_{I}=+1/2$") 
		ax.plot(B,freqs[:,3],label="$m_{s}=+1$ \u2192 $m_{s}=0$, $m_{I}=-1/2$") 
		ax.legend()
		
		axz = plt.subplot2grid((5,5),(1,3),rowspan=3,colspan=2)  # for proper sizing and placement of graph
		axz.set_xlabel("Magnetic Field",fontsize=12)
		axz.set_title("Zoomed Graph")
		axz.plot(Bzoom,freqs_zoom[:,0],label="$m_{s}=-1$ \u2192 $m_{s}=0$, $m_{I}=-1/2$") 
		axz.plot(Bzoom,freqs_zoom[:,1],label="$m_{s}=-1$ \u2192 $m_{s}=0$, $m_{I}=+1/2$") 
		axz.plot(Bzoom,freqs_zoom[:,2],label="$m_{s}=+1$ \u2192 $m_{s}=0$, $m_{I}=+1/2$") 
		axz.plot(Bzoom,freqs_zoom[:,3],label="$m_{s}=+1$ \u2192 $m_{s}=0$, $m_{I}=-1/2$") 
		axz.locator_params(axis='x', nbins=4)  # to reduce crowding of ticks
		
		plt.show()
		
if __name__ == '__main__':
	run = Excited_State()
	run.plot_allFreqs(1.199e-4)
		
		
		
