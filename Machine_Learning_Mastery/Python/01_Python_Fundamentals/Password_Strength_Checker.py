import math
import re


def password_strength(password):
    R = 0
    length = len(password)

    if length < 8:
        return "Weak: Password must be at least 8 characters long."

    if not re.search(r"[A-Z]", password):
        return "Weak: Password must contain at least one uppercase letter."
        R += 26

    if not re.search(r"[a-z]", password):
        return "Weak: Password must contain at least one lowercase letter."
        R += 26

    if not re.search(r"[0-9]", password):
        return "Weak: Password must contain at least one digit."
        R += 10

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password must contain at least one special character."
        R += 33

    pool_size = max(R, 10)
    entropy = length * math.log2(pool_size)

    if entropy < 28:
        return "Weak: Password entropy is too low."

    elif entropy < 36:
        return "Moderate: Password entropy is acceptable."
    else:
        return "Strong: Password entropy is high."


password = input("Enter a password to check its strength: ")
strength = password_strength(password)
print(strength)