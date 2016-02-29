import numpy as np
import matplotlib.pyplot as plt 
from modelicares import SimRes,LinRes 
sim = SimRes("C:\Users\lena\sciebo\Bachelorarbeit\Projekt\M2031_false.mat")

x1 = sim['multizoneEquipped.HeatingPowerHeater[1]'].values()
x2 = sim['multizoneEquipped.HeatingPowerHeater[2]'].values()
x3 = sim['multizoneEquipped.HeatingPowerHeater[3]'].values()
x4 = sim['multizoneEquipped.HeatingPowerHeater[4]'].values()
x5 = sim['multizoneEquipped.HeatingPowerHeater[5]'].values()
x6 = sim['multizoneEquipped.HeatingPowerHeater[6]'].values()
x7 = sim['multizoneEquipped.HeatingPowerHeater[7]'].values()
x8 = sim['multizoneEquipped.HeatingPowerAHU'].values()

x_sum = x1+x2+x3+x4+x5+x6+x7+x8
x_sumsum = sum(x_sum)
print x_sumsum