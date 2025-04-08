# water_flow.py
import pytest
from pytest import approx

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    density = 998.2  # kg/m^3
    return -0.04 * density * (fluid_velocity ** 2) * quantity_fittings / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    density = 998.2  # kg/m^3
    viscosity = 0.0010016  # Pascal seconds
    return (density * hydraulic_diameter * fluid_velocity) / viscosity

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    density = 998.2  # kg/m^3
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    return -k * density * (fluid_velocity ** 2) / 2000

# Constants
PVC_SCHED80_INNER_DIAMETER = 0.28687 # meters
PVC_SCHED80_FRICTION_FACTOR = 0.013
SUPPLY_VELOCITY = 1.65 # meters/second
HDPE_SDR11_INNER_DIAMETER = 0.048692 # meters
HDPE_SDR11_FRICTION_FACTOR = 0.018
HOUSEHOLD_VELOCITY = 1.75 # meters/second

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    
    diameter = PVC_SCHED80_INNER_DIAMETER
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    loss += pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    
    diameter = HDPE_SDR11_INNER_DIAMETER
    velocity = HOUSEHOLD_VELOCITY
    
    print(f"Pressure at house: {loss:.1f} kilopascals")

if __name__ == "__main__":
    main()
