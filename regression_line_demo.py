#York method: Modified after UPbplot.py (Noda, 2017)

import pandas as pd
import csv
from matplotlib import pyplot as plt
import numpy as np
from scipy import optimize as opt
from scipy import stats
from scipy import optimize


df = pd.read_csv("test.csv")
x = df["x"]
y = df["y"]
x_err = df["x_err"]
y_err = df["y_err"]
#regression line; non-correlated error; r = 0
wx = (x_err)**(-2)
wy = (y_err)**(-2)
ymean = np.sum(y)/len(y)
xmean = np.sum(x)/len(x)
b_init = np.sum((y-ymean)*(x-xmean))/np.sum((x-xmean)*(x-xmean))
def z(b):
    return (wx*wy)/((b**2)*wy+wx)
def x_ave(b):
    return np.sum(z(b)*x)/np.sum(z(b))
def y_ave(b):
    return np.sum(z(b)*y)/np.sum(z(b))
def u(b):
    return x - x_ave(b)
def v(b):
    return y - y_ave(b)
alpha = np.sqrt(wx*wy)
r = 0
def calc(b):
    return (b**2)*np.sum((z(b)**2)*(u(b)*v(b)/wx-r*(u(b)**2)/alpha))+b*np.sum((z(b)**2)*(u(b)**2/wy-v(b)**2/wx))-np.sum((z(b)**2)*(u(b)*v(b)/wy-r*(v(b)**2)/alpha))
b_reg = opt.fsolve(calc,b_init)
a = y_ave(b_reg)-b_reg*x_ave(b_reg)
print(a, b_reg)




'''
#regression line; correlated error
s =
wx = (x_err)**(-2)
wy = (y_err)**(-2)
ymean = np.sum(y)/len(y)
xmean = np.sum(x)/len(x)
b_init = np.sum((y-ymean)*(x-xmean))/np.sum((x-xmean)*(x-xmean))
def z(b):
    return (wx*wy)/((b**2)*wy+wx-2*b*r*np.sqrt(wx*wy))
def x_ave(b):
    return np.sum(z(b)*x)/np.sum(z(b))
def y_ave(b):
    return np.sum(z(b)*y)/np.sum(z(b))
def u(b):
    return x - x_ave(b)
def v(b):
    return y - y_ave(b)
alpha = np.sqrt(wx*wy)
r = df["error correlation"]
def calc(b):
    return (b**2)*np.sum((z(b)**2)*(u(b)*v(b)/wx-r*(u(b)**2)/alpha))+b*np.sum((z(b)**2)*(u(b)**2/wy-v(b)**2/wx))-np.sum((z(b)**2)*(u(b)*v(b)/wy-r*(v(b)**2)/alpha))
b_reg = opt.fsolve(calc,b_init)
a = y_ave(b_reg)-b_reg*x_ave(b_reg)
print(a, b_reg)
 '''
