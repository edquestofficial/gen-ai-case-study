from sample_module.sample_code import add
import pytest
from sample_module import sample_code

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-2, -3) == -5

def test_add_mixed():
    assert add(-1, 1) == 0

def test_add_zeros():
    assert add(0, 0) == 0

def test_add_large():
    assert add(1_000_000, 2_000_000) == 3_000_000

def test_add():
    assert sample_code.add(2, 3) == 5

def test_subtract():
    assert sample_code.subtract(5, 3) == 2

def test_multiply():
    assert sample_code.multiply(4, 3) == 12

def test_divide():
    assert sample_code.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        sample_code.divide(5, 0)

def test_is_even_true():
    assert sample_code.is_even(4) is True

def test_is_even_false():
    assert sample_code.is_even(5) is False

def test_max_of_list():
    assert sample_code.max_of_list([1, 2, 3, 10]) == 10

def test_max_of_list_empty():
    with pytest.raises(ValueError, match="Empty list provided"):
        sample_code.max_of_list([])



# # failure test cases-------------------

# def test_add_failure():
#     assert sample_code.add(2, 2) == 5  # Intentional fail

# def test_subtract_failure():
#     assert sample_code.subtract(10, 3) == 5  # Intentional fail

# def test_multiply_failure():
#     assert sample_code.multiply(2, 5) == 11  # Intentional fail

# def test_divide_failure():
#     assert sample_code.divide(10, 2) == 6  # Intentional fail

# def test_is_even_failure():
#     assert sample_code.is_even(3) is True  # Intentional fail

# def test_max_of_list_failure():
#     assert sample_code.max_of_list([1, 2, 3]) == 5  # Intentional fail
