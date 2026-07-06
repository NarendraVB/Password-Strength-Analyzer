def analyze_password(password):
    report = {
        "length": len(password),
        "has_uppercase": any(char.isupper() for char in password),
        "has_lowercase": any(char.islower() for char in password),
        "has_numbers": any(char.isdigit() for char in password),
        "has_symbols": any(not char.isalnum() for char in password),
    }

    return report