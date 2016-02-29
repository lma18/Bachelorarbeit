 'multizoneEquipped.zone[4].buildingPhysics.reducedOrderModel.airload.der(T)',
 'multizoneEquipped.zone[2].buildingPhysics.sunblind.Rad_Out[5].I_diff',
 'multizoneEquipped.heaterCooler[6].pITempHeat.PI.gainPID.u',
 'multizoneEquipped.airFlowRate.zoneParam[6].Aw[5]',
 'multizoneEquipped.zone[3].zoneParam.l_cooler',
 'multizoneEquipped.zone[1].buildingPhysics.reducedOrderModel.heatConvWinRes.alpha',
 'multizoneEquipped.zone[6].ventilationController.redFac',
 'multizoneEquipped.zone[5].buildingPhysics.eqAirTemp.equalAirTempWindow.Q_flow',
 'multizoneEquipped.zone[6].buildingPhysics.weightfactorswall[5]',
 'multizoneEquipped.heaterCooler[3].pITempCool.TN',
 'multizoneEquipped.zone[4].buildingPhysics.reducedOrderModel.heatConvInnerwall.port_a.T',
 'multizoneEquipped.zone[6].ventilationController.userACH',
 'multizoneEquipped.buildingParam.zoneSetup[1].n',
 'multizoneEquipped.zone[5].buildingPhysics.solarRad_in[3].I_dir',
 'multizoneEquipped.heaterCooler[3].pITempCool.PI.y',
 'multizoneEquipped.airFlowRate.zoneParam[3].awin',
 'multizoneEquipped.zone[7].buildingPhysics.withInnerwalls',
 'multizoneEquipped.heaterCooler[5].pITempCool.KR',
 'multizoneEquipped.zone[3].buildingPhysics.corG.SR_input[4].I_diff',
 'multizoneEquipped.zone[1].ventilationController.Tzone',
 'multizoneEquipped.airFlowRate.zoneParam[4].RWin',
 'multizoneEquipped.conversion.k',
 'multizoneEquipped.buildingParam.zoneSetup[1].maxSummerACH[3]',
 'multizoneEquipped.heaterCooler[6].zoneParam.winterReduction[1]',
 'multizoneEquipped.heaterCooler[3].pITempCool.PI.k',
 'multizoneEquipped.zone[4].solarRad_in[5].I_diff',
 'multizoneEquipped.zone[2].ventilationController.dEMA.y[1]',
 'multizoneEquipped.zone[6].buildingPhysics.reducedOrderModel.outerwall.load1.der(T)',
 'multizoneEquipped.zone[6].zoneParam.alphaConvWinOuter',
 'multizoneEquipped.zone[4].buildingPhysics.reducedOrderModel.alphaWin',
 'weather.RadOnTiltedSurf[1].InHourAngleSun',
 'multizoneEquipped.heaterCooler[7].zoneParam.ActivityTypeMachines',
 'multizoneEquipped.zone[2].lights.Schedule',
 'multizoneEquipped.zone[7].zoneParam.l_cooler',
 'multizoneEquipped.heaterCooler[4].pITempHeat.PI.Ni',
 'multizoneEquipped.zone[4].buildingPhysics.reducedOrderModel.thermSplitterLoads.dimension',
 'multizoneEquipped.heaterCooler[7].zoneParam.gsunblind[3]',
 'multizoneEquipped.airFlowRate.zoneParam[6].ActivityTypeMachines',
 'multizoneEquipped.zone[6].buildingPhysics.sunblind.Rad_In[1].I',
 'multizoneEquipped.zone[5].buildingPhysics.corG.SR_input[4].I',
 'multizoneEquipped.zone[2].buildingPhysics.gsunblind[4]',
 'multizoneEquipped.zone[2].buildingPhysics.reducedOrderModel.thermSplitterLoads.splitFactor[2]',
 'multizoneEquipped.zone[2].solarRad_in[2].I_dir',
 'multizoneEquipped.heaterCooler[4].zoneParam.Q_flow_cooler',
 'multizoneEquipped.zone[7].buildingPhysics.reducedOrderModel.heatConvOuterwall.dT',
 'multizoneEquipped.heaterCooler[4].zoneParam.Bchar',
 'const[6].y',
 'multizoneEquipped.zone[6].buildingPhysics.eqAirTemp.T_sky',
 'tableAHU.extrapolation',
 'multizoneEquipped.zone[5].human_SensibleHeat_VDI2078.limiter.uMin',
 ...]

In [29]: sim(['multizoneEquipped.zone[4].zoneParam.Aw[5]']).unit
Out[29]: ['m2']

In [30]: sim.__contains__('multizoneEquipped.zone[4].zoneParam.Aw[5]')
Out[30]: True

In [31]: 'multizoneEquipped.zone[2].solarRad_in[2].I_dir' in sim
Out[31]: True

In [32]: sim.__getitem__('multizoneEquipped.zone[2].solarRad_in[2].I_dir').array()
Out[32]: 
array([[  0.0000e+00,   0.0000e+00],
       [  3.6000e+03,   0.0000e+00],
       [  7.2000e+03,   0.0000e+00],
       ..., 
       [  3.1529e+07,   0.0000e+00],
       [  3.1532e+07,   0.0000e+00],
       [  3.1536e+07,   0.0000e+00]], dtype=float32)

In [33]: sim.__getitem__('multizoneEquipped.zone[2].solarRad_in[2].I_dir').values()
Out[33]: array([ 0.,  0.,  0., ...,  0.,  0.,  0.], dtype=float32)

In [34]: sim.__getitem__('multizoneEquipped.zone[2].solarRad_in[2].I_dir').max()
Out[34]: 841.23035

In [35]: sim.__getitem__('multizoneEquipped.zone[2].solarRad_in[2].I_dir').unit
Out[35]: 'W/m2'

In [36]: sim('multizoneEquipped.zone[2].solarRad_in[2].I_dir').unit
Out[36]: 'W/m2'

In [37]: sim('multizoneEquipped.zone[2].solarRad_in[2].I_dir').max()
Out[37]: 841.23035

In [38]: sim('multizoneEquipped.zone[2].solarRad_in[2].I_dir').RMS()
Out[38]: 123.6889

In [39]: sim('multizoneEquipped.zone[2].solarRad_in[2].I_dir').is_constant()
Traceback (most recent call last):

  File "<ipython-input-39-734fb8a858fb>", line 1, in <module>
    sim('multizoneEquipped.zone[2].solarRad_in[2].I_dir').is_constant()

TypeError: 'bool' object is not callable


In [40]: sim('multizoneEquipped.zone[2].solarRad_in[2].I_dir').is_constant
Out[40]: False

In [41]: sim.len()
Traceback (most recent call last):

  File "<ipython-input-41-06c3afb3339a>", line 1, in <module>
    sim.len()

AttributeError: 'SimRes' object has no attribute 'len'


In [42]: sim.__len__
Out[42]: <bound method SimRes.__len__ of SimRes('C:\Users\lena\sciebo\Bachelorarbeit\M2030.mat')>

In [43]: sim__len__()
Traceback (most recent call last):

  File "<ipython-input-43-46e810d9cc4d>", line 1, in <module>
    sim__len__()

NameError: name 'sim__len__' is not defined


In [44]: sim.__len__()
Out[44]: 9876

In [45]: sim.browse()

In [46]: sim.find(pattern = "*CoolingPowerAHU*", re = False)
Traceback (most recent call last):

  File "<ipython-input-46-43b694ffdb34>", line 1, in <module>
    sim.find(pattern = "*CoolingPowerAHU*", re = False)

AttributeError: 'SimRes' object has no attribute 'find'


In [47]: sim.find('CoolingPowerAHU', re = False)
Traceback (most recent call last):

  File "<ipython-input-47-29ac830bc844>", line 1, in <module>
    sim.find('CoolingPowerAHU', re = False)

AttributeError: 'SimRes' object has no attribute 'find'


In [48]: sim.nametree
Out[48]: <bound method SimRes.nametree of SimRes('C:\Users\lena\sciebo\Bachelorarbeit\M2030.mat')>

In [49]: ['CoolingPowerAHU']
Out[49]: ['CoolingPowerAHU']

In [50]: ['CoolingPowerAHU'].values()
Traceback (most recent call last):

  File "<ipython-input-50-f8387768e888>", line 1, in <module>
    ['CoolingPowerAHU'].values()

AttributeError: 'list' object has no attribute 'values'


In [51]: sim.__getitem__['CoolingPowerAHU'].values()
Traceback (most recent call last):

  File "<ipython-input-51-557a1b7d3bee>", line 1, in <module>
    sim.__getitem__['CoolingPowerAHU'].values()

TypeError: 'instancemethod' object has no attribute '__getitem__'


In [52]: sim.__getitem__("CoolingPowerAHU").values()
Traceback (most recent call last):

  File "<ipython-input-52-fad27175500b>", line 1, in <module>
    sim.__getitem__("CoolingPowerAHU").values()

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1614, in __getitem__
    return self._variables[name]

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 606, in __getitem__
    raise LookupError(msg)

LookupError: CoolingPowerAHU is not a valid variable name.

Did you mean one of these?
       multizoneEquipped.CoolingPowerAHU


In [53]: sim.__getitem__("multizoneEquipped.CoolingPowerAHU").values()
Out[53]: array([ 0.001,  0.   ,  0.   , ...,  0.   ,  0.   ,  0.   ], dtype=float32)

In [54]: sim.plot(ynames1 = [(sim.__getitem__("multizoneEquipped.CoolingPowerAHU").values())], ylabel= "Kühlung der RLT", xlabel = 'Time', title = 'mein erster Graph', )

￼
Traceback (most recent call last):

  File "<ipython-input-54-5d5f813f6661>", line 1, in <module>
    sim.plot(ynames1 = [(sim.__getitem__("multizoneEquipped.CoolingPowerAHU").values())], ylabel= "Kühlung der RLT", xlabel = 'Time', title = 'mein erster Graph', )

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1238, in plot
    ylabel1, legends1 = ystrings(ynames1, ylabel1, legends1, f1)

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1182, in ystrings
    descriptions = self(ynames).description

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1531, in __call__
    return VarList(entries(names))

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

TypeError: 'numpy.float32' object is not iterable


In [55]: sim.plot(ynames1 = [(sim.("multizoneEquipped.CoolingPowerAHU").values())], ylabel= "Kühlung der RLT", xlabel = 'Time', title = 'mein erster Graph', )
  File "<ipython-input-55-5a1aeaf534be>", line 1
    sim.plot(ynames1 = [(sim.("multizoneEquipped.CoolingPowerAHU").values())], ylabel= "Kühlung der RLT", xlabel = 'Time', title = 'mein erster Graph', )
                             ^
SyntaxError: invalid syntax


In [56]: sim.plot(ynames1 = [(sim.("multizoneEquipped.CoolingPowerAHU").values())], ylabel= "Kühlung der RLT", xlabel = 'Time', title= 'mein erster Graph')
  File "<ipython-input-56-19690fbd7995>", line 1
    sim.plot(ynames1 = [(sim.("multizoneEquipped.CoolingPowerAHU").values())], ylabel= "Kühlung der RLT", xlabel = 'Time', title= 'mein erster Graph')
                             ^
SyntaxError: invalid syntax


In [57]: sim.plot(ynames1 = [(sim.("multizoneEquipped.CoolingPowerAHU").values())], ylabel= "Kühlung der RLT", xlabel = 'Time', title= mein erster Graph)
  File "<ipython-input-57-71793e8bdd39>", line 1
    sim.plot(ynames1 = [(sim.("multizoneEquipped.CoolingPowerAHU").values())], ylabel= "Kühlung der RLT", xlabel = 'Time', title= mein erster Graph)
                             ^
SyntaxError: invalid syntax


In [58]: sim.plot(ynames1 = [(sim.("multizoneEquipped.CoolingPowerAHU").values())], ylabel= "Kühlung der RLT", xlabel = 'Time', title="mein erster Graph")
  File "<ipython-input-58-66cbed2d85ee>", line 1
    sim.plot(ynames1 = [(sim.("multizoneEquipped.CoolingPowerAHU").values())], ylabel= "Kühlung der RLT", xlabel = 'Time', title="mein erster Graph")
                             ^
SyntaxError: invalid syntax


In [58]: 

In [59]: sim.plot(ynames1 = [(sim.("multizoneEquipped.CoolingPowerAHU").values())], ylabel= "Kühlung der RLT", xlabel = 'Time', title = 'mein erster Graph')
  File "<ipython-input-59-a35b190e469a>", line 1
    sim.plot(ynames1 = [(sim.("multizoneEquipped.CoolingPowerAHU").values())], ylabel= "Kühlung der RLT", xlabel = 'Time', title = 'mein erster Graph')
                             ^
SyntaxError: invalid syntax


In [60]: sim.plot(ynames1 = [(sim.__getitem__("multizoneEquipped.CoolingPowerAHU").values())], ylabel= "Kühlung der RLT", xlabel = 'Time', title = 'mein erster Graph', )

￼
Traceback (most recent call last):

  File "<ipython-input-60-5d5f813f6661>", line 1, in <module>
    sim.plot(ynames1 = [(sim.__getitem__("multizoneEquipped.CoolingPowerAHU").values())], ylabel= "Kühlung der RLT", xlabel = 'Time', title = 'mein erster Graph', )

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1238, in plot
    ylabel1, legends1 = ystrings(ynames1, ylabel1, legends1, f1)

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1182, in ystrings
    descriptions = self(ynames).description

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1531, in __call__
    return VarList(entries(names))

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

TypeError: 'numpy.float32' object is not iterable


In [61]: sim.__getitem__("multizoneEquipped.CoolingPowerAHU").values()
Out[61]: array([ 0.001,  0.   ,  0.   , ...,  0.   ,  0.   ,  0.   ], dtype=float32)

In [62]: x = sim.__getitem__("multizoneEquipped.CoolingPowerAHU").values()

In [63]: print c
Traceback (most recent call last):

  File "<ipython-input-63-8e698a6f794d>", line 1, in <module>
    print c

NameError: name 'c' is not defined


In [64]: print x
[ 0.001  0.     0.    ...,  0.     0.     0.   ]

In [65]: sim.plot(ynames = x, ylabel = "CoolingPowerAHU", xname = 'Time', xlabel = 'Time',title "Mal gucken was jezt geht")
  File "<ipython-input-65-6530040459ea>", line 1
    sim.plot(ynames = x, ylabel = "CoolingPowerAHU", xname = 'Time', xlabel = 'Time',title "Mal gucken was jezt geht")
                                                                                                                    ^
SyntaxError: invalid syntax


In [66]: sim.plot(ynames = x, ylabel = "CoolingPowerAHU", xname = 'Time', xlabel = 'Time',title "Mal")
  File "<ipython-input-66-486215d703eb>", line 1
    sim.plot(ynames = x, ylabel = "CoolingPowerAHU", xname = 'Time', xlabel = 'Time',title "Mal")
                                                                                               ^
SyntaxError: invalid syntax


In [67]: sim.plot(ynames = x, ylabel = "CoolingPowerAHU", xname = 'Time', xlabel = 'Time', title 'Mal')
  File "<ipython-input-67-b783640169b1>", line 1
    sim.plot(ynames = x, ylabel = "CoolingPowerAHU", xname = 'Time', xlabel = 'Time', title 'Mal')
                                                                                                ^
SyntaxError: invalid syntax


In [68]: sim.plot(ynames = x, ylabel = "CoolingPowerAHU", xname = 'Time', xlabel = 'Time')
Traceback (most recent call last):

  File "<ipython-input-68-63b77216fb86>", line 1, in <module>
    sim.plot(ynames = x, ylabel = "CoolingPowerAHU", xname = 'Time', xlabel = 'Time')

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1218, in plot
    assert ynames1 or ynames2, "No signals were provided."

AssertionError: No signals were provided.


In [69]: sim.plot(ynames1 = x, ylabel = "CoolingPowerAHU", xname = 'Time', xlabel = 'Time')

￼
Traceback (most recent call last):

  File "<ipython-input-69-949702f941d2>", line 1, in <module>
    sim.plot(ynames1 = x, ylabel = "CoolingPowerAHU", xname = 'Time', xlabel = 'Time')

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1238, in plot
    ylabel1, legends1 = ystrings(ynames1, ylabel1, legends1, f1)

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1182, in ystrings
    descriptions = self(ynames).description

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1531, in __call__
    return VarList(entries(names))

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

TypeError: 'numpy.float32' object is not iterable


In [70]: sim.plot(ynames1 = x, ylabel = "CoolingPowerAHU", xname = 'Time', xlabel = 'Time')

￼
Traceback (most recent call last):

  File "<ipython-input-70-949702f941d2>", line 1, in <module>
    sim.plot(ynames1 = x, ylabel = "CoolingPowerAHU", xname = 'Time', xlabel = 'Time')

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1238, in plot
    ylabel1, legends1 = ystrings(ynames1, ylabel1, legends1, f1)

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1182, in ystrings
    descriptions = self(ynames).description

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1531, in __call__
    return VarList(entries(names))

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

TypeError: 'numpy.float32' object is not iterable


In [71]: x=
  File "<ipython-input-71-59d2dffd692f>", line 1
    x=
      ^
SyntaxError: invalid syntax


In [72]: x
Out[72]: array([ 0.001,  0.   ,  0.   , ...,  0.   ,  0.   ,  0.   ], dtype=float32)

In [73]: print x
[ 0.001  0.     0.    ...,  0.     0.     0.   ]

In [74]: sim.plot(ynames1 = print x, ylabel = "CoolingPowerAHU", xname = 'Time', xlabel = 'Time')
  File "<ipython-input-74-51e74289c9b8>", line 1
    sim.plot(ynames1 = print x, ylabel = "CoolingPowerAHU", xname = 'Time', xlabel = 'Time')
                           ^
SyntaxError: invalid syntax


In [75]: sim.plot(ynames1 = print (x), ylabel = "CoolingPowerAHU", xname = 'Time', xlabel = 'Time')
  File "<ipython-input-75-d0809eb46c14>", line 1
    sim.plot(ynames1 = print (x), ylabel = "CoolingPowerAHU", xname = 'Time', xlabel = 'Time')
                           ^
SyntaxError: invalid syntax


In [75]: 

In [76]: sim.plot(ynames1 = print (x), ylabel = "CoolingPowerAHU", xlabel = 'Time')
  File "<ipython-input-76-1292f79996e3>", line 1
    sim.plot(ynames1 = print (x), ylabel = "CoolingPowerAHU", xlabel = 'Time')
                           ^
SyntaxError: invalid syntax


In [77]: sim.plot(ynames1 = x, ylabel = "CoolingPowerAHU", xlabel = 'Time')

￼
Traceback (most recent call last):

  File "<ipython-input-77-5d3ec26db4ba>", line 1, in <module>
    sim.plot(ynames1 = x, ylabel = "CoolingPowerAHU", xlabel = 'Time')

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1238, in plot
    ylabel1, legends1 = ystrings(ynames1, ylabel1, legends1, f1)

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1182, in ystrings
    descriptions = self(ynames).description

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1531, in __call__
    return VarList(entries(names))

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

TypeError: 'numpy.float32' object is not iterable


In [78]: sim.plot(ynames1 = x, ylabel = "CoolingPowerAHU", xlabel = 'Time')

￼
Traceback (most recent call last):

  File "<ipython-input-78-5d3ec26db4ba>", line 1, in <module>
    sim.plot(ynames1 = x, ylabel = "CoolingPowerAHU", xlabel = 'Time')

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1238, in plot
    ylabel1, legends1 = ystrings(ynames1, ylabel1, legends1, f1)

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1182, in ystrings
    descriptions = self(ynames).description

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1531, in __call__
    return VarList(entries(names))

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

  File "C:\Python27\lib\site-packages\modelicares\simres.py", line 1526, in entries
    return [entries(name) for name in names] # Recursion

TypeError: 'numpy.float32' object is not iterable


In [79]: len(x)
Out[79]: 8761
