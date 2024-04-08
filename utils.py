import math     #Import math bib

# Calculation of apparent power
def calculate_apparent_power(U, i):
    S = U * i
    return S

# Calculation of active power
def calculate_active_power(S, powerfactor):
    P = S * powerfactor
    return P

# Calculation of reactive power
def calculate_reactive_power(S, P):
    Q = math.sqrt(S**2 - P**2)
    return Q

# Calculating the phase shift
def calculate_phase_angle(powerfactor):
    phi = math.acos(powerfactor)
    return phi

# Checking if the reactive power is inductive or capacitive
# this works through checking of the sign of the reactive power
def check_reactive_power_type(Q):
    if Q > 0:
        return "Kapazitiv"
    elif Q < 0:
        return "Induktiv"
    else:
        return "Reaktiv, aber ausgeglichen"



# Example values ​​for voltage, current and power factor
U = 230             # Voltage in volts
a = 10              # Current in amperes
powerfactor = 0.8   # Power factor (cos phi)

# Calculation of apparent power
S = calculate_apparent_power(U, a)

# Calculation of active power
P = calculate_active_power(S, powerfactor)

# Calculation of reactive power
Q = calculate_reactive_power(S, P)

# Calculation of phi
phi = calculate_phase_angle(powerfactor)

# Checking the type of reactive power
reactive_power_type = check_reactive_power_type(Q)


# results
print("Wirkleistung (P):", P, "Watt")
print("Blindleistung (Q):", Q, "VAR")
print("Scheinleistung (S):", S, "VA")
print("Phasenverschiebung (phi):", math.degrees(phi), "Grad")
print(reactive_power_type)
