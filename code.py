import numpy as np
import matplotlib.pyplot as plt
from sympy import *
Vrms = 12  #output volatge of the transformer

Vm = np.sqrt(2)*Vrms #calculating peak voltage

Vth = 0.7 #threshold voltage

Vr = Vm - 2*Vth #peak voltage of bridge rectifier output

#t, f,n = symbols('t f n')
#V= Function('V')
#an= Function('an')
#bn= Function('bn')
f = 100 # in hertz
t = np.arange(-0.020,0.025,0.00001)
y = Vr*abs(np.sin(2*np.pi*f*t)) #Bridge rectifier output
plt.plot(t, y, 'r')
plt.title('Bridge_output')
plt.show()

i=2
s = 0
for i in range(2,1000,2):
    s+=np.cos(i*2*np.pi*f*t)/(i**2-1)
   
bridge_fs = 2/np.pi - 4/np.pi*(s)
plt.title('Bridge_fs')
plt.plot(t,bridge_fs,'g')
plt.show()
