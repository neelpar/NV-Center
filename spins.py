import qutip as qt
import matplotlib.pyplot as plt
import numpy as np
from hamiltonians import SpinHamiltonian

ham = SpinHamiltonian()

def plotter():
	
	B = np.linspace(0,1,500)
	sham = np.vectorize(ham.spinProjection, otypes=[np.ndarray])
	spins = np.array(sham(B,0,0)) 			# contains all 9 spin components for all magnetic fields
	spins = np.array(spins.tolist())

	fig = plt.figure()
	ax = plt.subplot(311)  
	ax.set_ylabel("Spin Projection Magnitude", fontsize=12)
	ax.set_title("Rotation of Spins with Magnetic Field")
	ax.plot(B,spins[:,0],label="projection on X axis") 
	ax.plot(B,spins[:,1],label="projection on Y axis") 
	ax.plot(B,spins[:,2],label="projection on Z axis") 
	ax.legend()
	plt.grid(b=True, which='major', color='#666666', linestyle='-')
	plt.minorticks_on()
	plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
	
	ax1 = plt.subplot(312)
	ax1.set_ylabel("Spin Projection Magnitude", fontsize=12)
	ax1.plot(B,spins[:,3],label="projection on X axis") 
	ax1.plot(B,spins[:,4],label="projection on Y axis") 
	ax1.plot(B,spins[:,5],label="projection on Z axis")
	ax1.legend() 
	plt.grid(b=True, which='major', color='#666666', linestyle='-')
	plt.minorticks_on()
	plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
	
	ax2 = plt.subplot(313)
	ax2.set_xlabel("Magnetic Field along X axis (T)",fontsize=12)
	ax2.set_ylabel("Spin Projection Magnitude", fontsize=12)
	ax2.plot(B,spins[:,6],label="projection on X axis") 
	ax2.plot(B,spins[:,7],label="projection on Y axis") 
	ax2.plot(B,spins[:,8],label="projection on Z axis") 
	ax2.legend()
	plt.grid(b=True, which='major', color='#666666', linestyle='-')
	plt.minorticks_on()
	plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
	
	plt.show()
		
if __name__=="__main__":
	plotter()
		
		
		
		
		
