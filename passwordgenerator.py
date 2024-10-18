import random
import string
import secrets

def generate_password(length, complexity):
    """
    Generates a strong password based on the specified length and complexity level.

    Args:
        length: The desired length of the password.
        complexity: The complexity level (1-4):
            1: Lowercase letters only
            2: Lowercase and uppercase letters
            3: Lowercase, uppercase letters, and digits
            4: Lowercase, uppercase letters, digits, and special characters

    Returns:
        The generated password.
    """

    # Define character sets based on complexity level
    if complexity == 1:
        chars = string.ascii_lowercase
    elif complexity == 2:
        chars = string.ascii_lowercase + string.ascii_uppercase
    elif complexity == 3:
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    elif complexity == 4:
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level. Choose 1-4.")

    # Generate password using a combination of algorithms
    password = ''.join(random.choice(chars) for _ in range(length))

    # Add entropy using secrets.choice() for stronger randomness
    password = ''.join(secrets.choice(password) for _ in range(length))

    return password

# Example usage:
password = generate_password(12, 4)
print(password)