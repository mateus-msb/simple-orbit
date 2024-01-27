from scipy.integrate import solve_ivp as solver
import matplotlib.pyplot as plt
    
class MassSpringDamp():
    def __init__(self,m=1,k=1,c=1):
        self.m = m
        self.k = k
        self.c = c

    def equation_of_motion(self,t,y,r=1):
        """
        Variables:
        t:  time
        y:  state (x,v)
        dy: state (v,a)
        k:  stiffness constant
        c:  damping coefficient
        u:  control signal
        """

        x,v = y
        u = r - x

        dy  = [v,(u-self.c*v-self.k*x)/self.m]

        return dy

    def simulate(self,times=(0,10),step=0.1,initial_conditions=[0,0],input=1):
        solution        = solver(self.equation_of_motion,times,initial_conditions,max_step=step,args=(input,))
        self.time       = solution.t
        self.position, self.speed = solution.y

    def plot_results(self):
        plt.figure(1)
        plt.plot(self.time,self.position)
        plt.xlabel("Time (s)")
        plt.ylabel("Position (m)")
        plt.grid(True)
        plt.show()


def main():
    System = MassSpringDamp()
    System.simulate()
    System.plot_results()


if __name__ == "__main__":
    main()