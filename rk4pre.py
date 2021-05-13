import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog


n = 1
yn = 0
zn = 1.0
xn = 0.0
n = 1
e = pow(n,2) * 10 #( 10, 40, 90, 160,...)
h = 0.001
space = np.arange(0, 1, h)


def v(xo):
    if (xo < 1) and (xo >= 0):
        return 0
    else:
        return np.inf


def f(zo):
    return zo


def g(xo, yo):
    return  -(e - v(xo)) * yo


rkplot = []
for m in space:
    k1 = h * f(zn)
    l1 = h * g(xn, yn)
    k2 = h * f(zn + 1/2 * l1)
    l2 = h * g(xn+1/2*h, yn + 1/2 * k1)
    k3 = h * f(zn + 1/2 * l2)
    l3 = h * g(xn+1/2*h, yn + 1/2 * k2)
    k4 = h * f(zn + l3)
    l4 = h * g(xn+h, yn + k3)
    yn = yn + 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)
    zn = zn + 1/6 * (l1 + 2 * l2 + 2 * l3 + l4)
    rkplot.append(yn)

plt.plot(space, rkplot)
plt.xlabel('Length of well')
plt.ylabel('$\Psi(x_n)$, $n=$ %i' %n)
plt.show()