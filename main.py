import matplotlib.pyplot as plt
import pandas as pd

import Primera as a
import Segunda as b
import Tercera as c

print("----------------------")
print(a.pais())
print("----------------------")
print(b.morts())
print("----------------------")
print(c.fallecidos())

def A():
    gM = a.pais()

    X = list(gM.iloc[:,0])
    Y = list(gM.iloc[:, 1])

    plt.plot(Y,X, color="red")
    plt.title("Pais")
    plt.xlabel("Id Pais")
    plt.ylabel("Pais")
    plt.show()

A()