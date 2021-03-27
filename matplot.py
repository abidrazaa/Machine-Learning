Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import matplotlib.pyplot
ModuleNotFoundError: No module named 'matplotlib'
>>> import matplotlib.pyplot
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> import pandas as pd
>>> x= np.linspace(0,10,10)
>>> x
array([ 0.        ,  1.11111111,  2.22222222,  3.33333333,  4.44444444,
        5.55555556,  6.66666667,  7.77777778,  8.88888889, 10.        ])
>>> x
array([ 0.        ,  1.11111111,  2.22222222,  3.33333333,  4.44444444,
        5.55555556,  6.66666667,  7.77777778,  8.88888889, 10.        ])
>>> y = np.sin(x)
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000193EF0451D0>]
>>> plt.show
<function show at 0x00000193EABA36A8>
>>> plt.show()

>>> z=np.cos(x)
>>> plt.plot(x,z)
[<matplotlib.lines.Line2D object at 0x00000193EEDC6828>]
>>> plt.show()
>>> x= np.linspace(0,10,1000)
>>> y= np.sin(x)
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000193EFCD0E80>]
>>> plt.show()
>>> 
>>> y= np.cos(x)
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000193EFE85668>]
>>> plt.show()
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000193F0029940>]
>>> plt.xlabel('abid')
Text(0.5, 0, 'abid')
>>> plt.ylabel('raza')
Text(0, 0.5, 'raza')
>>> plt.title('machine learning')
Text(0.5, 1.0, 'machine learning')
>>> plt.show()
>>> x= np.linspace(0,100)
>>> y= 2*x+1
>>> plt.scatter(x,y)
<matplotlib.collections.PathCollection object at 0x00000193EFB31DD8>
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000193EFEB4A90>]
>>> plt.show()
>>> x= np.linspace(0,100)
>>> x= np.linspace(0,100,100)
>>> y= x**2
>>> plt.plot(y)
[<matplotlib.lines.Line2D object at 0x00000193EFBAB588>]
>>> plt.show()
>>> plt.plot(y)
[<matplotlib.lines.Line2D object at 0x00000193EFC08A20>]
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000193EEDD8B00>]
>>> plt.show()
>>> plt.scatter(x,y)
<matplotlib.collections.PathCollection object at 0x00000193F16A32E8>
>>> plt.show()
>>> 
