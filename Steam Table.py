
#SWADHA KUMARI
#2019UCH1501

import math

def sat_pressure(i):
    A=18.3036
    B=3816.44
    C=-46.13
    p=A-(B/(C+(273.15+i)))
    P1=math.exp(p)
    P=P1/7.501
    return P

def enthalpy_evap(i):
    Hfg=2501.7*((1-((273.15+i)/647.096))/(1-(273.15/647.096)))**(0.38)
    return Hfg

def enthalpy_liq(i):
    Hf=4.19*(i)
    return Hf

def enthalpy_vap(i):
    Hg=enthalpy_evap(i)+enthalpy_liq(i)
    return Hg

def internal_liq(i):
    Uf=4.182*(i)
    return Uf


def internal_evap(i):
    Ufg=enthalpy_evap(i)-(sat_pressure(i)*volume_evap(i)*0.001)
    return Ufg

def internal_vap(i):
    Ug=internal_evap(i)+internal_liq(i)
    return Ug

def volume_evap(i):
    v=(8.314*(273.15+i))/(sat_pressure(i)*18)
    Vfg=v*1000
    return Vfg


print("\n                                   SWADHA KUMARI   2019UCH1501")
print("\n                               SATURATED STEAM TABLE(SATURATED VAPOUR) \n")
print(" T : Temperature( celcius)\n")
print(" P : Pressure( KPa)\n")
print(" Vfg : Specific volume( cm3/g )\n")
print(" Hfg : Specific enthalpy( KJ/Kg )\n")
print(" Hf : Specific enthalpy of saturated liquid( KJ/Kg )\n")
print(" Hg : Specific enthalpy of saturated vapour( KJ/Kg )\n")
print(" Ufg : Specific internal energy( KJ/Kg )\n")
print(" Ug : Specific internal energy of saturated vapour( KJ/Kg ) \n")
print(" Uf : Specific internal energy of saturated liquid( KJ/Kg )\n")


i=1
print("{:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |\n".format("T(C)","P(kPa)","Vfg(cm3/g)","Ug(KJ/Kg)","Ufg(KJ/Kg)","Uf(KJ/Kg)","Hg(KJ/Kg)","Hfg(KJ/Kg)","Hf(KJ/Kg)"))
while i<=200:
    print("{:^10.2f} | {:^10.2f} | {:^10.2f} | {:^10.2f} | {:^10.2f} | {:^10.2f} | {:^10.2f} | {:^10.2f} | {:^10.2f} |".format(i, sat_pressure(i),volume_evap(i),internal_vap(i),internal_evap(i),internal_liq(i),enthalpy_vap(i),enthalpy_evap(i),enthalpy_liq(i)))
    i=i+1
