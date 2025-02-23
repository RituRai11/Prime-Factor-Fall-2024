import pytest
from prime import generate_prime_factors

def test_invalid_input():
    """Test that non-integer inputs raise a ValueError"""
    with pytest.raises(ValueError):
        generate_prime_factors("hello")
    with pytest.raises(ValueError):
        generate_prime_factors(4.5)
def test_prime_factors_of_1():
    """Test that when input is 1, an empty list is returned"""
    assert generate_prime_factors(1) == []

