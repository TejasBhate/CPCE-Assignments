# -*- coding: utf-8 -*-
"""CPCE Asg 6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dr2P66LbruN5dZl2Rolpht5BI26tkPBC
"""

#Q.1
#Stress When depth is constant
Q = float(input("Enter the value of Load in kN: "))
N = int(input("Number of data values of radial distance: "))
pi = 3.14159265359
Z = float(input("Depth: "))
r = []

for i in range(1, N + 1):
    print("Enter radial distance in m for data point {}".format(i))
    Value_r = float(input())
    r.append(Value_r)

for i in range(N):
    Stress = (3 * Q) / (2 * pi * Z * Z) * ((1 / (1 + ((r[i] / Z) ** 2))) ** 1.5)
    print("Stress at radial distance {} m: {} kN/m^2".format(r[i], Stress))

#Q.2
Q = float(input("Enter the value of Load in kN: "))
M = int(input("Number of data values of depth: "))
pi = 3.14159265359
r = float(input("Radial Distance: "))
Z = []

for j in range(1, M + 1):
    print("Enter depth in z for data point {}".format(j))
    Value_Z = float(input())
    Z.append(Value_Z)
    Stress = (3 * Q) / (2 * pi * r * r * Value_Z) * ((1 / (1 + ((r / Value_Z) ** 2))) ** 2.5)
    print("Stress at depth {} m: {} kN/m^2".format(Value_Z, Stress))

#Q.3
# Calculating the stress by Boussineq's Theory
Q= int(input("Enter the value of given load :"))
z= int(input("Enter the distance of vertical stress :"))
r= int(input("Enter the distance ofhorizntal stress:"))
stress = ((3*Q*(1/(1+(r/z)**2)) **2.5))/(2%3.14*(z**2))
print("The value of stress is", stress)