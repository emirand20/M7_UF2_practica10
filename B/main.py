import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import Primera as a
import Segunda as b
import Tercera as c

print("----------------------")
print(a.totalPoblacio())
print("----------------------")
print(b.mk2())
print("----------------------")
print(c.M2())


def Primera():
    ga = a.totalPoblacio().replace({",":""},regex=True)

    X = list(ga.iloc[:, 1])
    Y = list(ga.iloc[:, 0])

    plt.pie(X, labels=Y, autopct="%0.1f %%")
    plt.axis("equal")
    plt.show()


Primera()


def Segunda():
    gc = b.mk2().replace({",":""},regex=True)

    X = list(gc.iloc[:, 0])
    Y = list(gc.iloc[:, 1])

    plt.pie(X, labels=Y, autopct="%0.1f %%")
    plt.axis("equal")
    plt.show()


Segunda()


def Tercera():
    gb = c.M2().replace({",":""},regex=True)
    
    X = list(gb.iloc[:, 0])
    Y = list(gb.iloc[:, 1])

    plt.pie(X, labels=Y, autopct="%0.1f %%")
    plt.axis("equal")
    plt.show()


Tercera()
