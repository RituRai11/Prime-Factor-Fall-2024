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

def test_prime_factors_of_2():
    """Test that when input is 2, it returns [2]"""
    assert generate_prime_factors(2) == [2]

def test_prime_factors_of_3():
    """Test that when input is 3, it returns [3]"""
    assert generate_prime_factors(3) == [3]

def test_prime_factors_of_4():
    """Test that when input is 4, it returns [2, 2]"""
    assert generate_prime_factors(4) == [2, 2]

def test_prime_factors_of_6():
    """Test that when input is 6, it returns [2, 3]"""
    assert generate_prime_factors(6) == [2, 3]

def test_prime_factors_of_8():
    """Test that when input is 8, it returns [2, 2, 2]"""
    assert generate_prime_factors(8) == [2, 2, 2]

def test_prime_factors_of_9():
    """Test that when input is 9, it returns [3, 3]"""
    assert generate_prime_factors(9) == [3, 3]
