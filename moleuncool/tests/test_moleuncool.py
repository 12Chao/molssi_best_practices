"""
Unit and regression test for the moleuncool package.
"""

# Import package, test suite, and other packages as needed
import moleuncool
import pytest
import sys
import numpy as np

def test_moleuncool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "moleuncool" in sys.modules

@pytest.fixture
def methane_molecule():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])

    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4]
    ])

    return symbols, coordinates

def test_calculate_distance():
    """Test that the calculate distance function calculates what we expect."""
    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])
    expected_distance = 1
    observed_distance = moleuncool.calculate_distance(r1, r2)
    assert expected_distance == observed_distance

def test_build_bond_list(methane_molecule):

    symbols, coordinates = methane_molecule

    bonds = moleuncool.build_bond_list(coordinates)

    assert len(bonds) == 4
    
    for bond_length in bonds.values():
        assert bond_length == 1.4

@pytest.mark.skip
def test_build_bond_list_failure(methane_molecule):

    symbols, coordinates = methane_molecule
    
    with pytest.raises(ValueError):
        bonds = moleuncool.build_bond_list(coordinates, min_bond=-1)

def test_calculate_angle():

    r1 =  np.array([0, 0, 1])
    r2 =  np.array([0, 0, 0])
    r3 =  np.array([1, 0, 0])
    
    expected_value = 90
    calculated_value = moleuncool.calculate_angle(r1, r2, r3, degrees=True)

    assert expected_value == calculated_value