# test_water_flow.py
import pytest
from water_flow import (
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction
)

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(1.5, 3) == approx(-0.134739, rel=1e-3)
    assert pressure_loss_from_fittings(2.0, 5) == approx(-0.39936, rel=1e-3)

def test_reynolds_number():
    assert reynolds_number(0.05, 1.5) == approx(74705.15, rel=1e-3)
    assert reynolds_number(0.1, 2.0) == approx(199213.73, rel=1e-3)

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.1, 1.5, 80000, 0.05) == approx(-0.1404, rel=1e-3)
    assert pressure_loss_from_pipe_reduction(0.15, 2.0, 100000, 0.07) == approx(-0.1258, rel=1e-3)

if __name__ == "__main__":
    pytest.main()