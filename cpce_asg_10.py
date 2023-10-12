# -*- coding: utf-8 -*-
"""CPCE Asg 10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kv7Hc5Oo_Zn6C0iM-8Xl_nyZVYG4D1Lg
"""

# Design of tension member

# Input values
Tu = float(input("Enter the value of ultimate tensile strength:"))
fy = float(input("Enter the value of yield strength of steel:"))
fu = float(input("Enter the value of ultimate strength of steel:"))
fub = float(input("Enter the value of ultimate strength of bolt:"))
Gamma_mo = float(input("Enter the value of partial factor of safety Gamma_mo:"))
Gamma_m1 = float(input("Enter the value of partial factor of safety Gamma_m1:"))
Gamma_mb = float(input("Enter the value of partial factor of safety Gamma_mb:"))

# Gross Area Required
Agreq = Tu * 1000 / (1.1 * fy)
print("The value of gross area required is:", Agreq)

# Selection of section
# Assuming Ag value
Ag = float(input("Enter the value of gross area of steel:"))
Lcl = float(input("Enter the length of connected leg:"))
Lol = float(input("Enter the length of outstand leg:"))
t = float(input("Enter the value of least thickness:"))
Ag = 1257  # Example value, you can replace with your calculated value

# Design of connections
d = float(input("Enter the value of diameter of bolt:"))
do = d + 2
print("The diameter of bolt hole is:", do)

# Minimum pitch distance
pmin = 2.5 * d
print("The minimum pitch is:", pmin)

# Edge distance
e = 1.5 * do
print("Enter the value of edge distance:", e)

nn = float(input("Number of shear planes with threaded intercepting the shear plane:"))
ns = float(input("Number of shear planes without threads:"))

Anb = 0.7854 * d * d
print("Threaded area of bolt is:", Anb)

Asb = 0.7854 * d * d
print("Plane shank area of bolt is:", Asb)

Vdsb = (fub / (1.732 * Gamma_mb)) * (nn * Anb + ns * Asb) * 10**-3
print("The value of Vdsb:", Vdsb)

kbl = e / (3 * do)
print("Kbl:", kbl)

kb2 = (pmin / (3 * do)) - 0.25
print("Kb2:", kb2)

kb3 = fub / fu
print("Kb3:", kb3)

kb4 = 1
print("Kb4:", kb4)

kb = min(kbl, kb2, kb3, kb4)
print("Kb:", kb)

Vdpb = (2.5 * kb * d * t * fu * 10**-3) / Gamma_mb
print("Vdpb:", Vdpb)

Vd = min(Vdsb, Vdpb)
print("Vd:", Vd)

N = Tu / Vd
print("Number of bolts required:", N)

N = float(input("Enter the value of number of bolts:"))

# Check for strength
# Criteria 1: Yielding of Gross Section
Tdg = (Ag * fy) / (1.1 * Gamma_mo)
print("The value of tensile strength due to yielding of gross section is:", Tdg)

# Criteria 2: Rupture
Anc = (Lcl - (t / 2) - do) * t
print("Net Area of Connecting leg is: (Anc):", Anc)

Ago = (Lol - (t / 2)) * t
print("Gross Area of outstand leg is: (Ago):", Ago)

Lc = (N - 1) * pmin
print("Le:", Lc)

bs = 0.6 * (Lcl + Lol) * t
print("bs:", bs)

Beta = ((fy / fu) * (bs / Lc)) * (Lol / t)
print("Beta:", Beta)

print("Check 1")
if Beta > 1.4:
    print("Not Safe")
else:
    print("Safe")

print("Check 2")
if Beta < 0.7:
    print("Not Safe")
else:
    print("Safe")

Tdn = ((0.9 * fu * Anc) / Gamma_m1) + (Beta * Ago * fy / Gamma_mo)
print("Tdn:", Tdn)

# Criteria 3: Block Shear
Avg = (pmin * (N - 1) + e) * t
print("Avg:", Avg)

Avn = ((pmin * (N - 1) + e) - (N - 1) * do + (8.5 * do)) * t
print("Avn:", Avn)

Atg = 0.6 * Lcl * t
print("Atg:", Atg)

Atn = Atg - 0.5 * do
print("Atn:", Atn)

Tb1 = (((Avg * fy) / (1.732 * Gamma_mo)) + (0.9 * fu * Atn) / Gamma_m1) * 10**-3
print("Tb1:", Tb1)

Tb2 = ((0.9 * Avn * fu) / (1.732 * Gamma_m1)) + ((Atg * fy) / Gamma_mo) * 10**-3
print("Tb2:", Tb2)

Tb = min(Tb1, Tb2)
print("Tb", Tb)

Td = min(Tdg, Tdn, Tb)
print("Td", Td)

if Td > Tu:
    print("SAFE")
else:
    print("Revise the Section")