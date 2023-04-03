Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

================================ RESTART: Shell ================================
import math
math.squrt(4)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    math.squrt(4)
AttributeError: module 'math' has no attribute 'squrt'. Did you mean: 'sqrt'?
>>> from math import
SyntaxError: incomplete input
>>> from math import *
>>> x = 2
>>> y = 3
>>> sqrt(x**2 + y**2)
3.605551275463989
>>> from math import *
>>> 
================================ RESTART: Shell ================================
>>> from math import sqrt
>>> sqrt(4)
2.0
>>> sin(30)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sin(30)
NameError: name 'sin' is not defined. Did you mean: 'bin'?
>>> 
================================ RESTART: Shell ================================
>>> from math import *
>>> sin(30)
-0.9880316240928618
>>> sin(0)
0.0
>>> sin(3.14)
0.0015926529164868282
>>> sin(1.57)
0.9999996829318346
>>> 
================================ RESTART: Shell ================================
>>> from math import sqrt, sin
>>> sin(43)
-0.8317747426285983
>>> sqrt(234)
15.297058540778355
