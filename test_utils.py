from utils import calculate_apparent_power, calculate_active_power, calculate_reactive_power, calculate_phase_angle, check_reactive_power_type
import math

def test_power_calculation():
    # Example values ​​for voltage, current and power factor
    U = 230             # Voltage in volts
    i = 10              # Current in amperes
    powerfactor = 0.8   # Power factor (cos phi)

    # Calculation of apparent power
    S = calculate_apparent_power(U, i)

    # Calculation of active power
    P = calculate_active_power(S, powerfactor)

    # Calculation of reactive power
    Q = calculate_reactive_power(S, P)

    # Calculating the phase shift
    phi = calculate_phase_angle(powerfactor)

    # Checking the values
    assert round(S, 2) == 2300.0
    assert round(P, 2) == 1840.0
    assert round(Q, 2) == 1580.0
    assert round(math.degrees(phi), 2) == 36.87

# test for the aktive power
def test_aktive_power():
    assert round(calculate_active_power(200*10, 0.7), 2) == 1200.0
    assert round(calculate_active_power(400*5, 0.5), 2) == 800.0
    assert round(calculate_active_power(2000*50, 0.2), 2) == 20000.0

# test for the reactive power
def test_reactive_power():
    assert round(calculate_reactive_power(200*10, 1400), 2) == 1428.29
    assert round(calculate_reactive_power(400*5, 1000), 2) == 1432.05
    assert round(calculate_reactive_power(2000*50, 20000), 2) == 97979.59

# test for the apparent power
def test_apparent_power():
    assert round(calculate_apparent_power(200, 10), 2) == 1000.0
    assert round(calculate_apparent_power(400, 5), 2) == 2000.0
    assert round(calculate_apparent_power(2000, 50), 2) == 100000.0

# test for power faktor type
def test_reactive_power_type():
    assert check_reactive_power_type(100) == "Induktiv"
    assert check_reactive_power_type(-100) == "Induktiv"
    assert check_reactive_power_type(0) == "Reaktiv, aber ausgeglichen"

# Run the tests
test_power_calculation()
test_aktive_power()
test_reactive_power()
test_apparent_power()
test_reactive_power_type()

print("Alle Tests erfolgreich durchgeführt.")
