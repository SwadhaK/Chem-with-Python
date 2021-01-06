
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets



def a(T):
    B = 'Benzene'
    To = 'Toluene'

    def PsatB(T):
        return 10**(6.90565-(1211.033/(220.79+T)))

    def PsatT(T):
        return 10**(6.95334-( 1343.943/(219.377+T)))

    xB = np.linspace(0,1)
    pB = xB*PsatB(T)
    pT = (1-xB)*PsatT(T)
    Pv = pB+pT
    yB=pB/Pv


    plt.figure(figsize=(10,6))
    plt.plot(xB,Pv,'b')
    plt.plot(xB,pB,'c--')
    plt.plot(xB,pT,'m--')
    plt.plot(yB,Pv,'r')
    plt.plot(0, PsatT(T), 'm.', ms=20)
    plt.plot(1, PsatB(T), 'c.', ms=20)


    plt.xlim(-0.01,1.01)
    plt.ylim(0, 1500)
    plt.xlabel('$x_B$ = Mole fraction ' + B, fontsize = 14)
    plt.ylabel('Vapor Pressure / mmHg', fontsize = 14)
    plt.title('Raoult\'s Law: ' + B + ' / ' + To + ' at {:.1f} deg C'.format(T), fontsize = 16)
    plt.legend(['Total Pressure: Raoult\'s Law','Vapor Pressure of Benzene',
            'Vapor Pressure of Toluene']);



w = interactive(a, T = (10, 150))
display(w)
