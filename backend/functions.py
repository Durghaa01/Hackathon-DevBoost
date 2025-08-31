# functions.py

def validate_and_format_string(input_string: str) -> str:
    """
    Validates and formats a given string based on specific rules.

    Args:
        input_string (str): The string to be validated and formatted.

    Returns:
        str: A cleaned-up version of the input string if it passes validation; otherwise, an error message.
    """
    # Check if input_string contains only alphanumeric characters and underscores
    if not input_string.replace("_", "").isalnum():
        return "Error: Input string must contain only alphanumeric characters and underscores."

    # Check if the length of the string is between 3 and 50 characters
    if len(input_string) < 3 or len(input_string) > 50:
        return "Error: Input string length must be between 3 and 50 characters."

    return input_string
