""" tests/test_operations.py """
import pytest
from app.operations.operations import Operations

def test_addition():
    """Test addition outputs"""
    assert Operations.add(1, 2) == 3
    assert Operations.add(-1, 2) == 1
    assert Operations.add(-1, -2) == -3

def test_subtraction():
    """Test subtraction outputs"""
    assert Operations.subtract(3, 2) == 1
    assert Operations.subtract(1, 2) == -1
    assert Operations.subtract(-1, 2) == -3
    assert Operations.subtract(-1, -2) == 1

def test_multiplication():
    """Test multiplication outputs"""
    assert Operations.multiply(2, 4) == 8
    assert Operations.multiply(-2, 4) == -8
    assert Operations.multiply(-2, -4) == 8

def test_division():
    """Test division outputs"""
    assert Operations.divide(12, 6) == 2
    assert Operations.divide(-12, 4) == -3
    assert Operations.divide(12, -3) == -4
    assert Operations.divide(-12, -2) == 6

