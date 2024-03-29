# -*- coding: utf-8 -*-
"""CPCE Asg 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iyyciufX2LVdYRJI-e7lH4sNSgMuN3lY
"""

#Q.1
# Calculation of total Infiltration by Horton's Equation
fo = float(input("Enter the value of initial Infiltration Rate:"))
fc = float(input("Enter the value of Final infiltration Rate:"))
t = int(input("Enter the value of Time:"))
kh = float(input("Enter the value of Decay Coefficient:"))

# The total Infiltration is given by:
Fp = fc * t + (fo - fc) / kh
print("The value of Infiltration is:", Fp)

#Q.2
# Calculation of Mean Precipitation by the Thiessen Polygon Method
# The value of precipitation at Each station is
p1 = float(input("Enter the value of rainfall at station 1:"))
p2 = float(input("Enter the value of rainfall at station 2:"))
p3 = float(input("Enter the value of rainfall at station 3:"))
p4 = float(input("Enter the value of rainfall at station 4:"))
p5 = float(input("Enter the value of rainfall at station 5:"))

# Area of each station
A1 = float(input("Enter the value of Catchment Area for raingauge station 1:"))
A2 = float(input("Enter the value of Catchment Area for raingauge station 2:"))
A3 = float(input("Enter the value of Catchment Area for raingauge station 3:"))
A4 = float(input("Enter the value of Catchment Area for raingauge station 4:"))
A5 = float(input("Enter the value of Catchment Area for raingauge station 5:"))

# The total catchment area is the sum of individual areas
A = A1 + A2 + A3 + A4 + A5
print("The value of Catchment area is:", A)

# Runoff volume
# The volume shall be multiplied by the coefficient 2500 to cater to scale effects
V = (p1 * A1 + p2 * A2 + p3 * A3 + p4 * A4 + p5 * A5) / A * 2500
print("The value of mean Precipitation is:", V)

#Q.3
# Calculation of Mean Precipitation by the Isohytel Method
# The value of precipitation at Each station is
p1 = float(input("Enter the value of rainfall at Station 1:"))
p2 = float(input("Enter the value of rainfall at Station 2:"))
p3 = float(input("Enter the value of rainfall at Station 3:"))
p4 = float(input("Enter the value of rainfall at Station 4:"))
p5 = float(input("Enter the value of rainfall at Station 5:"))
p6 = float(input("Enter the value of rainfall at Station 6:"))
p7 = float(input("Enter the value of rainfall at Station 7:"))
p8 = float(input("Enter the value of rainfall at Station 8:"))

# Area of each station
A1 = float(input("Enter the value of Catchment Area for raingauge station 1:"))
A2 = float(input("Enter the value of Catchment Area for raingauge station 2:"))
A3 = float(input("Enter the value of Catchment Area for raingauge station 3:"))
A4 = float(input("Enter the value of Catchment Area for raingauge station 4:"))
A5 = float(input("Enter the value of Catchment Area for raingauge station 5:"))
A6 = float(input("Enter the value of Catchment Area for raingauge station 6:"))
A7 = float(input("Enter the value of Catchment Area for raingauge station 7:"))

# The total catchment area is the sum of individual areas
A = A1 + A2 + A3 + A4 + A5 + A6 + A7
print("The value of Total Catchment area is:", A)

# Mean Precipitation
p = (
    (p1 + p2) * A1 / 2 +
    (p2 + p3) * A2 / 2 +
    (p3 + p4) * A3 / 2 +
    (p4 + p5) * A4 / 2 +
    (p5 + p6) * A5 / 2 +
    (p6 + p7) * A6 / 2 +
    (p7 + p8) * A7 / 2
) / A

print("The value of Mean Precipitation is:", p)