import numpy as np
import qutip as qt
import matplotlib.pyplot as plt
import math

class SpinHamiltonian():
	def __init__(self):
		self.sx = qt.jmat(1,'x')
		self.sy = qt.jmat(1,'y')
		self.sz = qt.jmat(1,'z')            
		
		self.ge = 28e9                  
		self.D = 2.87e9                 
		self.ms0 = 0
		
	def eigenstates(self,B,theta,z):
		Bx = B*math.cos(theta)
		By = B*math.sin(theta)
		Bz=0
		if z :
			Bx =0
			By =0
			Bz = B
			
		Hs = self.D*((self.sz*self.sz)-(2/3)*qt.qeye(3)) + self.ge*(Bz*self.sz + Bx*self.sx + By*self.sy)      # Electric term ignored as it is negligible
		return Hs.eigenstates() 
		
	def transitionFreqs(self,B,theta,z):
		egvals = self.eigenstates(B,theta,z)[0]
		
		if(B == 0): self.ms0 = egvals[0] 
		f1 = egvals[2] - self.ms0 if(z) else egvals[2]-egvals[0]
		f0 = abs(egvals[1] + egvals[0] - (2*self.ms0)) if(z) else egvals[1]-egvals[0]
		
		return np.array([f1,f0])
		
	def spinProjection(self,B,theta,z):
		egst = self.eigenstates(B,theta,z)
		
		msx0 = qt.expect(self.sx,egst[1][0])   # spin projection of 0th spin eigenstate of Hs on x axis
		msy0 = qt.expect(self.sy,egst[1][0])   # spin projection of 0th spin eigenstate of Hs on y axis
		msz0 = qt.expect(self.sz,egst[1][0])   # spin projection of 0th spin eigenstate of Hs on z axis
		
		msx1 = qt.expect(self.sx,egst[1][1])   # spin projection of 1st spin eigenstate of Hs on x axis
		msy1 = qt.expect(self.sy,egst[1][1])   # spin projection of 1st spin eigenstate of Hs on y axis
		msz1 = qt.expect(self.sz,egst[1][1])   # spin projection of 1st spin eigenstate of Hs on z axis
		
		msx2 = qt.expect(self.sx,egst[1][2])   # spin projection of 2nd spin eigenstate of Hs on x axis
		msy2 = qt.expect(self.sy,egst[1][2])   # spin projection of 2nd spin eigenstate of Hs on y axis
		msz2 = qt.expect(self.sz,egst[1][2])   # spin projection of 2nd spin eigenstate of Hs on z axis
		
		return np.array([msx0,msy0,msz0,msx1,msy1,msz1,msx2,msy2,msz2])
	

	
class HyperfineSpinHalf():
	def __init__(self):
		self.sx = qt.jmat(1,'x')
		self.sy = qt.jmat(1,'y')
		self.sz = qt.jmat(1,'z')            # jmat is higher order spin operator. 1 in this case.
		self.ge = 28e9                      # gyromagnetic ration of electron in Hz/T
		self.gc = 10.705e6                  # gyromagnetic ratio of C-13 nucleus in Hz/T for hyperfine interaction
		self.D = 2870.2e6                   # zero field splitting frequency in Hz
		
		self.Axx = 189.3e6
		self.Ayy = 128.4e6
		self.Azz = 128.9e6
		self.Axz = 24.1e6                   # Hyperfine Tensor components in NV frame of reference. Taken from reference 2.
		self.Ix = qt.jmat(0.5,'x')
		self.Iy = qt.jmat(0.5,'y')
		self.Iz = qt.jmat(0.5,'z')          # Spin 1/2 operators for C-13 nucleus
		
		self.comp1 = self.Axx*qt.tensor(self.sx,self.Ix)
		self.comp2 = self.Ayy*qt.tensor(self.sy,self.Iy)
		self.comp3 = self.Azz*qt.tensor(self.sz,self.Iz)
		self.comp4 = self.Axz*(qt.tensor(self.sx,self.Iz)+qt.tensor(self.sz,self.Ix))
		self.Hhf = self.comp1 + self.comp2 + self.comp3 + self.comp4
		
	def transitionFreqs(self,Bz):
		H = self.D*(qt.tensor(self.sz*self.sz,qt.qeye(2))-(2/3)*qt.tensor(qt.qeye(3),qt.qeye(2))) + self.ge*Bz*qt.tensor(self.sz,qt.qeye(2)) + self.gc*Bz*qt.tensor(qt.qeye(3),self.Iz) + self.Hhf 
		egvals = H.eigenstates()[0]
		
		ms0 = (egvals[0] + egvals[1])/2
		return np.array([egvals[2]-ms0, egvals[3]-ms0, egvals[4]-ms0, egvals[5]-ms0])
	
	def eigenvalues(self,Bz):
		H = self.D*(qt.tensor(self.sz*self.sz,qt.qeye(2))-(2/3)*qt.tensor(qt.qeye(3),qt.qeye(2))) + self.ge*Bz*qt.tensor(self.sz,qt.qeye(2)) + self.gc*Bz*qt.tensor(qt.qeye(3),self.Iz) + self.Hhf 
		return H.eigenstates()[0]
	
	
		
class HyperfineSpin1():
	def __init__(self):
		self.sx = qt.jmat(1,'x')
		self.sy = qt.jmat(1,'y')
		self.sz = qt.jmat(1,'z')            # jmat is higher order spin operator. 1 in this case.
		self.ge = 28e9                      # gyromagnetic ration of electron in Hz/T
		self.gc = 10.705e6                  # gyromagnetic ratio of C-13 nucleus in Hz/T for hyperfine interaction
		self.D = 2870.2e6                   # zero field splitting frequency in Hz
		
		self.Axx = 189.3e6
		self.Ayy = 128.4e6
		self.Azz = 128.9e6
		self.Axz = 24.1e6                   # Hyperfine Tensor components in NV frame of reference. Taken from reference 2.
		self.Ix = qt.jmat(1,'x')
		self.Iy = qt.jmat(1,'y')
		self.Iz = qt.jmat(1,'z')          # Spin 1/2 operators for C-13 nucleus
		
		self.comp1 = self.Axx*qt.tensor(self.sx,self.Ix)
		self.comp2 = self.Ayy*qt.tensor(self.sy,self.Iy)
		self.comp3 = self.Azz*qt.tensor(self.sz,self.Iz)
		self.comp4 = self.Axz*(qt.tensor(self.sx,self.Iz)+qt.tensor(self.sz,self.Ix))
		self.Hhf = self.comp1 + self.comp2 + self.comp3 + self.comp4
	
	def eigenvalues(self,Bz):
		H = self.D*(qt.tensor(self.sz*self.sz,qt.qeye(3))-(2/3)*qt.tensor(qt.qeye(3),qt.qeye(3))) + self.ge*Bz*qt.tensor(self.sz,qt.qeye(3)) + self.gc*Bz*qt.tensor(qt.qeye(3),self.Iz) + self.Hhf  
		return H.eigenstates()[0]
		
	def transitionFreqs(self,Bz):
		#eigen = np.vectorize(self.eigenvalues)
		egvals = self.eigenvalues(Bz)
		ms0 = (egvals[0] + egvals[1] + egvals[2])/3
		return np.array([egvals[3]-ms0, egvals[4]-ms0, egvals[5]-ms0, egvals[6]-ms0, egvals[7]-ms0, egvals[8]-ms0])
		#return egvals[:,3:9] - ms0


class ExcitedState():
	def __init__(self):
		self.sx1 = qt.jmat(1,'x')
		self.sy1 = qt.jmat(1,'y')
		self.sz1 = qt.jmat(1,'z')            
		self.Aes = 61e6 #hyperfine constant in Hz
		self.sx = qt.jmat(0.5,'x')
		self.sy = qt.jmat(0.5,'y')
		self.sz = qt.jmat(0.5,'z')
		self.D = 1.425e9 # zero field splitting in Hz
		self.g = 28e9 # gyromagnetic ratio
		#excited state g factor. for ground state it is 2.0023
		self.Ees = 70e6 #doubtful value. there is a +-30MHz error
		
		dot1 = qt.tensor(self.sx1,self.sx)
		dot2 = qt.tensor(self.sy1,self.sy)
		dot3 = qt.tensor(self.sz1,self.sz)
		self.dot = dot1 + dot2 + dot3
		
	def eigenvalues(self,Bz):
		H = self.D*qt.tensor(self.sz1*self.sz1,qt.qeye(2)) + self.Ees*qt.tensor(((self.sx1*self.sx1)-(self.sy1*self.sy1)),qt.qeye(2)) + self.g*Bz*qt.tensor(self.sz1,qt.qeye(2)) - self.Aes*self.dot 
		return H.eigenstates()[0]
		
	def transitionFreqs(self,Bz):
		ham = np.vectorize(self.eigenvalues, otypes=[np.ndarray])
		egvals = ham(Bz)
		
		ms0 = (egvals[0]+egvals[1])/2
		return np.array([(egvals[2]-ms0),(egvals[3]-ms0),(egvals[4]-ms0),(egvals[5]-ms0)])
		

		



