import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from modelicares import SimRes

sim = SimRes("D:\jte-lma\Project\M2031_26_5.mat")
x = sim["tEnergyMeterTot.q_kwh"].values()
xL = sim["tEnergyMeterAHU.q_kwh"].values()
x1 = sim["tEnergyMeterZones[1].q_kwh"].values()
x2 = sim["tEnergyMeterZones[2].q_kwh"].values()
x3 = sim["tEnergyMeterZones[3].q_kwh"].values()
x4 = sim["tEnergyMeterZones[4].q_kwh"].values()
x5 = sim["tEnergyMeterZones[5].q_kwh"].values()
x6 = sim["tEnergyMeterZones[6].q_kwh"].values()
x7 = sim["tEnergyMeterZones[7].q_kwh"].values()
xHeizungTot = x1[-1]+x2[-1]+x3[-1]+x4[-1]+x5[-1]+x6[-1]+x7[-1]

