import numpy as np
from scipy.integrate import solve_ivp as solver
import matplotlib.pyplot as plt
    
class SimpleOrbit():
    def __init__(self,mu=398_600,R=6_378,g=9.807,initial_condition=[42_164,0,0,0,3.075,0]):
        self.mu = mu
        self.R  = R
        self.g  = g
        
        self.initial_condition = initial_condition

    def equation_of_motion(self,t,y):
        """
        Variables:
        t:  time
        y:  state (X,Y,Z,vx,vy,vz)
        dy: state (vx,vy,vz,ax,ay,az)
        """

        X,Y,Z,vx,vy,vz = y

        r = np.sqrt(X**2 + Y**2 + Z**2)

        v = np.array([vx,vy,vz])
        a = -(self.mu/r**3)*np.array([X,Y,Z])
        
        dy = np.concatenate((v,a))

        return dy

    def simulate(self,times=(0,48*3600),step=10):
        solution        = solver(self.equation_of_motion,times,self.initial_condition,method='DOP853',max_step=step)
        self.time       = solution.t
        self.X, self.Y, self.Z, self.Vx, self.Vy, self.Vz = solution.y

    def plot_results(self):
        plt.figure(1)
        plt.subplot(311)
        plt.plot(self.time/3600,self.X,label='X')
        plt.ylim([-50_000,50_000])
        plt.legend()

        plt.subplot(312)
        plt.plot(self.time/3600,self.Y,label='Y')
        plt.ylim([-50_000,50_000])
        plt.ylabel("Position (km)")
        plt.legend()

        plt.subplot(313)
        plt.plot(self.time/3600,self.Z,label='Z')
        plt.xlabel("Time (h)")
        plt.legend()

        tri = plt.figure(3)
        ax = tri.add_subplot(111,projection='3d')
        ax.plot(self.X,self.Y,self.Z, label='3D')
        ax.legend()

        plt.show()


def main():
    System = SimpleOrbit()
    System.simulate()
    System.plot_results()


if __name__ == "__main__":
    main()