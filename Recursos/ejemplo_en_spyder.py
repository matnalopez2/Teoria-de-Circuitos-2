# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:24:36 2024

@author: Mati
"""


import math
import numpy as np
from pytc2.sistemas_lineales import tf2sos_analog, analyze_sys, pretty_print_SOS
import scipy.signal as sig

epsilon = math.sqrt(10**0.1 - 1)
print("Epsilon: " + str(epsilon))


# Definición de una implementación de analyze_sys para evitar logueos innecesarios, mejorando la prolijidad.
def analyze_sys_silent(all_sys, sys_name=None, img_ext='none', same_figs=True, annotations=True, xaxis='omega', fs=2*np.pi):
    analyze_sys(all_sys, sys_name=None, img_ext='none', same_figs=True, annotations=True, xaxis='omega', fs=2*np.pi)
    return

w_0 = math.sqrt(epsilon)

k = (1 / (2 * epsilon**2)) / epsilon
print("k = " + str(k))

w1 = 0.95
w2 = 1.05

Q = (math.sqrt(w1*w2)/(w2-w1))
print("Q = " + str(Q))


# Calculamos los coeficientes del denominador para mayor claridad.
A = Q**2
B = Q
C = ((2 * w_0**2 * Q**2) + (w_0**2))
D = w_0**2 * Q
E = Q**2 * w_0**4

# Con los datos definidos anteriormente, se arman los array de la transferencia.
kn = k
kp = 1
num = kn * np.array([w_0**2, 0, 0])
den = kp * np.array([A, B, C, D, E])
tf_bicuad_sos = tf2sos_analog( num, den )

# Imprimir en formato latex la transferencia
pretty_print_SOS(tf_bicuad_sos)


# Plotear de forma silenciosa las características de mi función 
analyze_sys([sig.TransferFunction(num,den)], 'mi_bicuad', same_figs=False)
