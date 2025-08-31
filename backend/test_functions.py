# test_functions.py

import pytest
from functions import validate_and_format_string

def test_valid_strings():
    assert validate_and_format_string("Hello_World123") == "Hello_World123"
    assert validate_and_format_string("abc_123") == "abc_123"

def test_invalid_characters():
    assert validate_and_format_string("Hello!@#World") == "Error: Input string must contain only alphanumeric characters and underscores."
    assert validate_and_format_string("abc-123") == "Error: Input string must contain only alphanumeric characters and underscores."

def test_length_constraints():
    assert validate_and_format_string("ab") == "Error: Input string length must be between 3 and 50 characters."
    assert validate_and_format_string("a"*51) == "Error: Input string length must be between 3 and 50 characters."

def test_edge_cases():
    # Underscores only are allowed if combined with alphanumeric
    assert validate_and_format_string("a_b_c") == "a_b_c"
    # Empty string
    assert validate_and_format_string("") == "Error: Input string length must be between 3 and 50 characters."
