import pytest
from prime import generate_prime_factors

def test_invalid_input():
    """Test that non-integer inputs raise a ValueError"""
    with pytest.raises(ValueError):
        generate_prime_factors("hello")
    with pytest.raises(ValueError):
        generate_prime_factors(4.5)
